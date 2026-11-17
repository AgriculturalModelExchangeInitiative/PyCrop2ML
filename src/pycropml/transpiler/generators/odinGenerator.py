# coding: utf8
"""Odin target: generates an Odin package shaped like the cpp2 output.

* one struct per variable category (State, Rate, Auxiliary, Exogenous),
* one struct per ModelUnit holding its parameters, with ``make_``/``destroy_``
  procs and ``_init``/``_calculate_model`` procs reading and writing the
  category structs through pointers,
* one Component struct holding the ModelUnits, driving them in order.

Expressions are rendered to strings (``expr``) rather than written directly,
so that ``int`` operands can be wrapped in ``f64(...)`` where Odin requires an
explicit conversion, and parentheses follow Odin's operator precedence.
"""
import ast
import os
from pathlib import Path

from pycropml.nameconvention import signature2
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.generators.cpp2Generator import Cpp2Trans
from pycropml.transpiler.generators.docGenerator import DocGenerator
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.rules.odinRules import (
    OdinRules, to_snake, to_ada, package_name, string_literal, float_literal,
)

CATEGORIES = ("State", "Rate", "Auxiliary", "Exogenous")
CR_MATH_ENV = "CYML_ODIN_MATH"
STRUCT_VARS = ("m", "s", "s1", "r", "a", "ex")


class OdinNameError(ValueError):
    """Two Crop2ML names map to the same Odin name."""


def categorize(models):
    """Sort the variables of *models* into states, rates, ... (shared with cpp2)."""
    trans = Cpp2Trans(models)
    trans.model_to_node()
    return trans


def composition_of(model):
    """The composition of the package *model* belongs to, or None.

    The domain structs are built from the composition, so a ModelUnit must use
    the composition's category for a variable (a ModelUnit may declare as
    auxiliary what the composition makes a state).
    """
    from pycropml.topology import Topology
    path = Path(model.path)
    cached = Topology.pkgs.get(path.name)
    if cached:
        return cached[1]
    return getattr(Topology(path.name, path), "model", None)


def ptype(node_or_type):
    """Normalised pseudo type: 'int', 'float', 'bool', 'str', or a list."""
    t = getattr(node_or_type, "pseudo_type", node_or_type)
    if isinstance(t, list):
        return t
    t = str(t)
    return "float" if t == "double" else t


def is_sequence_type(t):
    return isinstance(t, list) and t and t[0] in ("list", "array")


def is_constant(node):
    """True for expressions made only of literals; Odin treats them as untyped."""
    if not isinstance(node, Node):
        return False
    if node.type in ("int", "float", "bool"):
        return "value" in node.__dict__
    if node.type == "constant":
        return True
    if node.type == "unary_op":
        return is_constant(node.value)
    if node.type in ("binary_op", "comparison"):
        return is_constant(node.left) and is_constant(node.right)
    return False


def as_list(x):
    if x is None:
        return []
    return x if isinstance(x, list) else [x]


class OdinGenerator(CodeGenerator, OdinRules):
    """Translate one ModelUnit (or a function library) into an Odin file."""

    def __init__(self, tree, model=None, name=None):
        CodeGenerator.__init__(self)
        OdinRules.__init__(self)
        self.indent_with = "\t"
        self.tree = tree
        self.model = model
        self.name = name
        self.imports = set()
        # import path of MONICA's support/cr_math, as seen from the generated package
        self.cr_math = os.environ.get(CR_MATH_ENV) or None
        self.funcname = ""
        self.in_model_proc = False
        self.local_types = {}
        self.param_types = {}
        self.returned = set()
        self.struct_vars = {v: v for v in STRUCT_VARS}
        self.functions = {}
        if tree is not None and isinstance(getattr(tree, "body", None), list):
            for f in tree.body:
                if isinstance(f, Node) and f.type == "function_definition":
                    self.functions[f.name] = f
        self.state_names, self.rate_names = [], []
        self.auxiliary_names, self.exogenous_names = [], []
        self.param_names, self.node_param = [], []
        self.unit_categories = None
        if model is not None:
            self.doc = DocGenerator(model, "// ", indent_with="")
            unit = categorize([model])
            composition = composition_of(model)
            if composition is not None:
                self.set_categories(categorize([composition]))
                self.unit_categories = unit
            else:
                self.set_categories(unit)
            self.node_param = unit.node_param
            self.param_names = [p.name for p in unit.node_param]

    # ------------------------------------------------------------------ names

    def set_categories(self, trans):
        self.state_names = [v.name for v in trans.states]
        self.rate_names = [v.name for v in trans.rates]
        self.auxiliary_names = [v.name for v in trans.auxiliary]
        self.exogenous_names = [v.name for v in trans.exogenous]
        self.node_param = trans.node_param
        self.param_names = [p.name for p in trans.node_param]

    def domain_type(self, category):
        return to_ada(f"{self.name}{category}")

    def struct_for(self, name):
        """(struct variable, field name) holding Crop2ML variable *name* in a model proc."""
        if not self.in_model_proc:
            return None
        if name in self.local_types and name not in self.struct_fields:
            return None
        if name in self.param_names:
            return self.struct_vars["m"], name
        if name in self.state_names:
            return self.struct_vars["s"], name
        if name.endswith("_t1") and name[:-3] in self.state_names:
            return self.struct_vars["s1"], name[:-3]
        if name in self.rate_names:
            return self.struct_vars["r"], name
        if name in self.auxiliary_names:
            return self.struct_vars["a"], name
        if name in self.exogenous_names:
            return self.struct_vars["ex"], name
        if self.unit_categories is not None:
            for names, var in ((self.unit_categories.states, "s"), (self.unit_categories.rates, "r"),
                               (self.unit_categories.auxiliary, "a"), (self.unit_categories.exogenous, "ex")):
                if name in (v.name for v in names):
                    return self.struct_vars[var], name
        return None

    @property
    def struct_fields(self):
        names = set(self.param_names + self.state_names + self.rate_names
                    + self.auxiliary_names + self.exogenous_names
                    + [n + "_t1" for n in self.state_names])
        if self.unit_categories is not None:
            u = self.unit_categories
            names.update(v.name for v in u.states + u.rates + u.auxiliary + u.exogenous)
        return names

    def var(self, name):
        sf = self.struct_for(name)
        if sf:
            return f"{sf[0]}.{to_snake(sf[1])}"
        return to_snake(name)

    def check_names(self, names, where):
        seen = {}
        for n in names:
            snake = to_snake(n)
            if snake in seen and seen[snake] != n:
                raise OdinNameError(
                    f"{where}: '{seen[snake]}' and '{n}' both become '{snake}' in Odin")
            seen[snake] = n

    def pick_struct_vars(self, names, model_var="m"):
        """Rename the struct pointer parameters if a variable uses the same name."""
        taken = {to_snake(n) for n in names}
        self.struct_vars = {}
        for v in STRUCT_VARS:
            name = model_var if v == "m" else v
            while name in taken:
                name += "_"
            self.struct_vars[v] = name

    # ------------------------------------------------------------------ types

    def type_str(self, t, param=False):
        t = ptype(t)
        if isinstance(t, list):
            kind = t[0]
            if kind in ("list", "array"):
                elem = self.type_str(t[1])
                if param and kind == "array":
                    return f"[]{elem}"
                return f"[dynamic]{elem}"
            if kind == "dict":
                return f"map[{self.type_str(t[1])}]{self.type_str(t[2])}"
            if kind == "tuple":
                return "(" + ", ".join(self.type_str(x) for x in t[1:]) + ")"
            raise NotImplementedError(f"Odin: unsupported type {t}")
        if t in self.types:
            return self.types[t]
        raise NotImplementedError(f"Odin: unsupported type {t}")

    def return_str(self, return_type):
        if not return_type or return_type == "Void":
            return ""
        t = ptype(return_type)
        if isinstance(t, list) and t[0] == "tuple":
            return " -> (" + ", ".join(self.result_type_str(x) for x in t[1:]) + ")"
        return " -> " + self.result_type_str(t)

    def result_type_str(self, t):
        """Helpers return lists and arrays as slices; the caller copies them."""
        t = ptype(t)
        if is_sequence_type(t):
            return f"[]{self.type_str(t[1])}"
        return self.type_str(t)

    # ------------------------------------------------------------ expressions

    def expr(self, node, want=None):
        code, _ = self.expr_prec(node, want)
        return code

    def expr_prec(self, node, want=None):
        method = getattr(self, f"expr_{node.type}", None)
        if method is None:
            raise NotImplementedError(f"Odin: no expression rule for node type '{node.type}'")
        code, prec = method(node)
        return self.cast(code, prec, node, want)

    def cast(self, code, prec, node, want):
        have = ptype(node)
        if want == "float" and have == "int" and not is_constant(node):
            return f"f64({code})", self.odin_atom_precedence
        if want == "int" and have == "float":
            return f"int({code})", self.odin_atom_precedence
        return code, prec

    def paren(self, node, min_prec, want=None):
        code, prec = self.expr_prec(node, want)
        return f"({code})" if prec < min_prec else code

    def condition(self, node, min_prec=0):
        """*node* where Odin needs a bool: a number is true if not 0, as in Python."""
        if ptype(node) in ("int", "float"):
            prec = self.odin_binop_precedence["!="]
            code = f"{self.paren(node, prec + 1)} != 0"
            return f"({code})" if prec < min_prec else code
        return self.paren(node, min_prec)

    def expr_local(self, node):
        return self.var(node.name), self.odin_atom_precedence

    def expr_int(self, node):
        if "value" not in node.__dict__:
            return self.var(node.name), self.odin_atom_precedence
        return str(node.value), self.odin_atom_precedence

    def expr_float(self, node):
        if "value" not in node.__dict__:
            return self.var(node.name), self.odin_atom_precedence
        return float_literal(node.value), self.odin_atom_precedence

    expr_double = expr_float

    def expr_bool(self, node):
        if "value" not in node.__dict__:
            return self.var(node.name), self.odin_atom_precedence
        return ("true" if str(node.value).lower() in ("true", "1") else "false"), self.odin_atom_precedence

    def expr_str(self, node):
        if "value" not in node.__dict__:
            return self.var(node.name), self.odin_atom_precedence
        return string_literal(node.value), self.odin_atom_precedence

    def expr_none(self, node):
        return "nil", self.odin_atom_precedence

    def expr_notAnumber(self, node):
        self.imports.add('"core:math"')
        return "math.nan_f64()", self.odin_atom_precedence

    def expr_constant(self, node):
        self.imports.add('"core:math"')
        return self.constants[node.library][node.name], self.odin_atom_precedence

    def expr_datetime(self, node):
        return string_literal("/".join(str(v.value) for v in node.value)), self.odin_atom_precedence

    def expr_binary_op(self, node):
        op = str(node.op)
        lt, rt = ptype(node.left), ptype(node.right)
        if op in ("in", "not_in", "not in"):
            code = self.contains(node.right, node.left)
            return (code if op == "in" else f"!{code}"), self.odin_unary_precedence
        if op in ("is", "is_not") or (node.right.type == "none" and op in ("==", "!=")):
            # lists and arrays are values; None is mapped to empty (see visit_assignment)
            negate = op in ("is_not", "!=")
            if is_sequence_type(lt):
                return f"len({self.expr(node.left)}) {'!=' if negate else '=='} 0", self.odin_binop_precedence["=="]
            return f"{self.expr(node.left)} {'!=' if negate else '=='} nil", self.odin_binop_precedence["=="]
        if op == "**":
            return self.math_call("math.pow", [node.left, node.right]), self.odin_atom_precedence
        want = "float" if "float" in (lt, rt) and op not in ("and", "or") else None
        if op == "%" and want == "float":
            return self.math_call("math.mod", [node.left, node.right]), self.odin_atom_precedence
        if op == "//":
            op = "/"
        prec = self.odin_binop_precedence[op]
        if op in ("and", "or"):
            left, right = self.condition(node.left, prec), self.condition(node.right, prec + 1)
            return f"{left} {self.binary_op[op]} {right}", prec
        left = self.paren(node.left, prec, want)
        if op in ("<<", ">>") and not is_constant(node.right):
            right = f"uint({self.expr(node.right)})"  # Odin requires an unsigned shift count
        else:
            right = self.paren(node.right, prec + 1, want)
        return f"{left} {self.binary_op[op]} {right}", prec

    expr_comparison = expr_binary_op

    def expr_unary_op(self, node):
        op = str(node.operator)
        if op == "not":
            return f"!{self.condition(node.value, self.odin_unary_precedence + 1)}", self.odin_unary_precedence
        operand = self.paren(node.value, self.odin_unary_precedence + 1)
        return f"{self.unary_op[op]}{operand}", self.odin_unary_precedence

    def expr_cond_expr_node(self, node):
        want = ptype(node)
        want = want if want in ("int", "float") else None
        test = self.condition(node.test, 1)
        return f"{test} ? {self.paren(node.true_val, 1, want)} : {self.paren(node.false_val, 1, want)}", 0

    def expr_index(self, node):
        seq = self.paren(node.sequence, self.odin_atom_precedence)
        if isinstance(node.index, list):
            return seq + "".join(f"[{self.expr(i, 'int')}]" for i in node.index), self.odin_atom_precedence
        return f"{seq}[{self.expr(node.index, 'int')}]", self.odin_atom_precedence

    def slice_bounds(self, node):
        args = as_list(node.args)
        msg = node.message
        if msg == "sliceindex_from":
            return self.expr(args[0], "int"), ""
        if msg == "sliceindex_to":
            return "", self.expr(args[0], "int")
        if msg == "sliceindex":
            return self.expr(args[0], "int"), self.expr(args[1], "int")
        return "", ""

    def expr_sliceindex(self, node):
        lo, hi = self.slice_bounds(node)
        return f"{self.paren(node.receiver, self.odin_atom_precedence)}[{lo}:{hi}]", self.odin_atom_precedence

    def expr_list(self, node):
        elem = self.type_str(ptype(node)[1]) if is_sequence_type(ptype(node)) else "f64"
        items = ", ".join(self.expr(e) for e in as_list(getattr(node, "elements", [])))
        return f"[]{elem}{{{items}}}", self.odin_atom_precedence

    def expr_tuple(self, node):
        return ", ".join(self.expr(e) for e in node.elements), 0

    def slice_of(self, node):
        """Expression *node* (a list/array) as an Odin slice."""
        if node.type in ("sliceindex", "list"):
            return self.expr(node)
        return f"{self.paren(node, self.odin_atom_precedence)}[:]"

    def contains(self, seq, item):
        self.imports.add('"core:slice"')
        return f"slice.contains({self.slice_of(seq)}, {self.expr(item)})"

    def math_call(self, fn, args):
        """Call ``math.<name>``; transcendental functions go through cr_math if configured.

        core:math procs are proc groups: every argument must be typed f64.
        """
        rendered = []
        for a in args:
            code = self.expr(a, "float")
            if is_constant(a):
                code = f"f64({code})"
            rendered.append(code)
        name = fn.split(".", 1)[1]
        if self.cr_math and name in self.cr_math_functions:
            self.imports.add(f'cr_math "{self.cr_math}"')
            if name == "log":  # log(x, base); cr_math.log is the natural logarithm
                return f"(cr_math.log({rendered[0]}) / cr_math.log({rendered[1]}))"
            return f"cr_math.{self.cr_math_functions[name]}({', '.join(rendered)})"
        self.imports.add('"core:math"')
        return f"{fn}({', '.join(rendered)})"

    def expr_standard_call(self, node):
        ns, fn = str(node.namespace), str(node.function)
        args = as_list(node.args)
        result_type = ptype(node)
        if fn == "log":
            if len(args) == 1:
                code = self.math_call("math.ln", args)
            else:
                code = self.math_call("math.log", args)
        elif fn in self.math_functions and (ns == "math" or fn in ("pow", "round")):
            code = self.math_call(self.math_functions[fn], args)
            if fn == "isnan":
                return code, self.odin_atom_precedence
        elif fn in ("min", "max"):
            if len(args) == 1:
                self.imports.add('"core:slice"')
                return f"slice.{fn}({self.slice_of(args[0])})", self.odin_atom_precedence
            want = result_type if result_type in ("int", "float") else None
            return f"{fn}({', '.join(self.expr(a, want) for a in args)})", self.odin_atom_precedence
        elif fn == "abs":
            return f"abs({self.expr(args[0])})", self.odin_atom_precedence
        elif fn == "copy":
            return self.expr(args[0]), self.odin_atom_precedence
        elif fn == "datetime":
            return string_literal("/".join(str(getattr(a, "value", "")) for a in args)), self.odin_atom_precedence
        else:
            raise NotImplementedError(f"Odin: no rule for function {ns}.{fn}")
        if result_type == "int":
            return f"int({code})", self.odin_atom_precedence
        return code, self.odin_atom_precedence

    def expr_standard_method_call(self, node):
        recv = node.receiver
        rt = ptype(recv)
        kind = rt[0] if isinstance(rt, list) else rt
        msg = str(node.message)
        args = as_list(node.args)
        if kind in ("int", "float", "bool") and msg in ("float", "int"):
            target = "f64" if msg == "float" else "int"
            if kind == msg:
                return self.expr_prec(recv)
            return f"{target}({self.expr(recv)})", self.odin_atom_precedence
        if msg == "len":
            return f"len({self.expr(recv)})", self.odin_atom_precedence
        if kind in ("list", "array"):
            r = self.expr(recv)
            if msg == "append":
                return f"append(&{r}, {self.expr(args[0], ptype(rt[1]))})", self.odin_atom_precedence
            if msg == "extend":
                return f"append(&{r}, ..{self.slice_of(args[0])})", self.odin_atom_precedence
            if msg == "sum":
                self.imports.add('"core:math"')
                return f"math.sum({self.slice_of(recv)})", self.odin_atom_precedence
            if msg == "pop":
                if args:
                    return f"ordered_remove(&{r}, {self.expr(args[0], 'int')})", self.odin_atom_precedence
                return f"pop(&{r})", self.odin_atom_precedence
            if msg == "insert_at":
                return f"inject_at(&{r}, {self.expr(args[0], 'int')}, {self.expr(args[1], ptype(rt[1]))})", self.odin_atom_precedence
            if msg == "contains?":
                return self.contains(recv, args[0]), self.odin_atom_precedence
            if msg == "not contains?":
                return f"!{self.contains(recv, args[0])}", self.odin_unary_precedence
            if msg == "index":
                # Python's list.index raises if the value is missing; -1 (as
                # C#'s IndexOf, Java's indexOf) makes the indexing that
                # usually follows fail Odin's bounds check instead.
                self.imports.add('"core:slice"')
                return (f"(slice.linear_search({self.slice_of(recv)}, {self.expr(args[0], ptype(rt[1]))}) or_else -1)",
                        self.odin_atom_precedence)
            if msg == "allocate":
                return f"resize(&{r}, {self.expr(args[0], 'int')})", self.odin_atom_precedence
        if kind == "dict":
            r = self.expr(recv)
            if msg == "get":
                return f"{r}[{self.expr(args[0])}]", self.odin_atom_precedence
            if msg == "contains?":
                return f"{self.expr(args[0])} in {r}", self.odin_binop_precedence["=="]
        if kind == "str" and msg == "find":
            self.imports.add('"core:strings"')
            return f"strings.index({self.expr(recv)}, {self.expr(args[0])})", self.odin_atom_precedence
        raise NotImplementedError(f"Odin: no rule for method {kind}.{msg}")

    def expr_call(self, node):
        fn = str(node.function)
        callee = self.functions.get(fn)
        params = callee.params if callee is not None else []
        rendered = []
        for i, a in enumerate(as_list(node.args)):
            pt = ptype(params[i]) if i < len(params) else None
            if is_sequence_type(pt) and pt[0] == "array":
                rendered.append(self.slice_of(a))
            else:
                rendered.append(self.expr(a, pt if pt in ("int", "float") else None))
        return f"{to_snake(fn)}({', '.join(rendered)})", self.odin_atom_precedence

    expr_custom_call = expr_call

    # ------------------------------------------------------------- statements

    def line(self, code):
        self.newline()
        self.write(code)

    def block(self, statements):
        self.indentation += 1
        for st in as_list(statements):
            self.visit(st)
        self.indentation -= 1

    def visit_import(self, node):
        pass

    def visit_importfrom(self, node):
        pass

    def visit_print(self, node):
        pass

    def visit_ExprStatNode(self, node):
        if node.expr.type == "standard_call" and str(node.expr.function) == "print":
            return
        self.line(self.expr(node.expr))

    def visit_breakstatnode(self, node):
        self.line("break")

    def visit_continuestatnode(self, node):
        self.line("continue")

    def visit_if_statement(self, node):
        self.line(f"if {self.condition(node.test)} {{")
        self.block(node.block)
        for other in as_list(getattr(node, "otherwise", [])):
            if other.type == "elseif_statement":
                self.line(f"}} else if {self.condition(other.test)} {{")
            else:
                self.line("} else {")
            self.block(other.block)
        self.line("}")

    def visit_while_statement(self, node):
        self.line(f"for {self.condition(node.test)} {{")
        self.block(node.block)
        self.line("}")

    def visit_for_range_statement(self, node):
        idx = self.expr(node.index)
        step = node.step
        negative = (step.type == "unary_op" and str(step.operator) == "-") or \
            (step.type == "int" and str(getattr(step, "value", "")).startswith("-"))
        cmp = ">" if negative else "<"
        start, end = self.expr(node.start, "int"), self.expr(node.end, "int")
        self.line(f"for {idx} = {start}; {idx} {cmp} {end}; {idx} += {self.expr(step, 'int')} {{")
        self.block(node.block)
        self.line("}")

    def visit_for_statement(self, node):
        it, seq = node.iterators, node.sequences
        sequence = self.expr(seq.sequence)
        if it.type == "for_iterator":
            name = self.expr(it.iterator)
            item = f"{to_snake(it.iterator.name)}_it"
            self.line(f"for {item} in {sequence} {{")
            self.indentation += 1
            self.line(f"{name} = {item}")
            self.indentation -= 1
        elif it.type == "for_iterator_with_index":
            name, index = self.expr(it.iterator), self.expr(it.index)
            item, idx = f"{to_snake(it.iterator.name)}_it", f"{to_snake(it.index.name)}_it"
            self.line(f"for {item}, {idx} in {sequence} {{")
            self.indentation += 1
            self.line(f"{name} = {item}")
            self.line(f"{index} = {idx}")
            self.indentation -= 1
        elif it.type == "for_iterator_with_items":
            key, value = self.expr(it.key), self.expr(it.value)
            k, v = f"{to_snake(it.key.name)}_it", f"{to_snake(it.value.name)}_it"
            self.line(f"for {k}, {v} in {sequence} {{")
            self.indentation += 1
            self.line(f"{key} = {k}")
            self.line(f"{value} = {v}")
            self.indentation -= 1
        else:
            raise NotImplementedError(f"Odin: unsupported loop {it.type}")
        self.block(node.block)
        self.line("}")

    def visit_implicit_return(self, node):
        if self.in_model_proc:
            return
        if node.value is None:
            self.line("return")
            return
        rt = ptype(self.current_return)
        if node.value.type == "tuple":
            types = rt[1:] if isinstance(rt, list) and rt[0] == "tuple" else []
            elements = as_list(node.value.elements)
        else:
            types, elements = [rt], [node.value]
        vals = []
        for i, e in enumerate(elements):
            t = ptype(types[i]) if i < len(types) else None
            if is_sequence_type(t) or is_sequence_type(ptype(e)):
                vals.append(self.slice_of(e) if not self.is_slice_param(e) else self.expr(e))
            else:
                vals.append(self.expr(e, t if t in ("int", "float") else None))
        self.line("return " + ", ".join(vals))

    def is_slice_param(self, node):
        """Array parameters of helpers are already slices."""
        t = self.param_types.get(getattr(node, "name", None))
        return node.type == "local" and is_sequence_type(t) and t[0] == "array"

    # declarations ---------------------------------------------------------

    def visit_declaration(self, node):
        for n in node.decl:
            if self.struct_for(n.name):
                self.declare_field(n)
            else:
                self.declare_local(n)

    def size_of(self, n):
        elts = as_list(getattr(n, "elts", None))
        if not elts:
            return None
        e = elts[0]
        if isinstance(e, Node):
            return self.expr(e, "int")
        return str(e)

    def declared_value(self, n):
        v = n.value
        if isinstance(v, Node):
            return self.expr(v, ptype(n))
        t = ptype(n)
        if t == "float":
            return float_literal(v)
        if t == "bool":
            return "true" if str(v).lower() in ("true", "1") else "false"
        if t in ("str", "datetime"):
            return string_literal(v)
        return str(v)

    def declare_field(self, n):
        """A declared variable that lives in a struct: initialise the field."""
        target = self.var(n.name)
        t = ptype(n)
        if is_sequence_type(t):
            size = self.size_of(n)
            elements = as_list(getattr(n, "elements", None))
            if size is not None:
                self.line(f"resize(&{target}, {size})")
            elif elements:
                self.line(f"clear(&{target})")
                self.line(f"append(&{target}, {', '.join(self.expr(e, ptype(t[1])) for e in elements)})")
            elif n.type == "list":
                self.line(f"clear(&{target})")
        elif "value" in n.__dict__:
            self.line(f"{target} = {self.declared_value(n)}")

    def declare_local(self, n):
        name = to_snake(n.name)
        t = ptype(n)
        self.local_types[n.name] = t
        if is_sequence_type(t):
            size = self.size_of(n)
            elements = as_list(getattr(n, "elements", None))
            if size is not None:
                self.line(f"{name} := make({self.type_str(t)}, {size})")
            else:
                self.line(f"{name}: {self.type_str(t)}")
                if elements:
                    self.line(f"append(&{name}, {', '.join(self.expr(e, ptype(t[1])) for e in elements)})")
            if n.name not in self.returned:
                self.line(f"defer delete({name})")
        elif isinstance(t, list) and t[0] == "dict":
            self.line(f"{name}: {self.type_str(t)}")
            for pair in as_list(getattr(n, "pairs", None)):
                self.line(f"{name}[{self.expr(pair.key)}] = {self.expr(pair.value, ptype(t[2]))}")
            if n.name not in self.returned:
                self.line(f"defer delete({name})")
        elif "value" in n.__dict__ and n.value is not None:
            self.line(f"{name}: {self.type_str(t)} = {self.declared_value(n)}")
        else:
            self.line(f"{name}: {self.type_str(t)}")

    # assignments ----------------------------------------------------------

    def visit_assignment(self, node):
        target, value = node.target, node.value
        if value.type == "none":
            if is_sequence_type(ptype(target)):
                self.line(f"clear(&{self.expr(target)})")
            return
        if value.type in ("call", "custom_call") and self.returns_sequence(value):
            self.assign_from_call(target, value)
            return
        if target.type == "tuple":
            self.line(f"{self.expr(target)} = {self.expr(value)}")
            return
        tt = ptype(target)
        if target.type == "sliceindex":
            self.line(f"copy({self.expr(target)}, {self.slice_of(value)})")
            return
        if is_sequence_type(tt):
            self.assign_sequence(target, value, tt)
            return
        self.line(f"{self.expr(target)} = {self.expr(value, tt if tt in ('int', 'float') else None)}")

    @staticmethod
    def result_types(call):
        t = ptype(call)
        if isinstance(t, list) and t[0] == "tuple":
            return [ptype(x) for x in t[1:]]
        return [t]

    def returns_sequence(self, call):
        return any(is_sequence_type(t) for t in self.result_types(call))

    def fresh_results(self, call):
        """Per result: True if the callee allocated it (the caller must free it)."""
        n = len(self.result_types(call))
        callee = self.functions.get(str(call.function))
        if callee is None:
            return [False] * n
        params = {p.name for p in callee.params} - self.copied_params(callee)
        fresh = [True] * n
        returns = []

        def walk(x):
            if isinstance(x, list):
                for y in x:
                    walk(y)
            elif isinstance(x, Node):
                if x.type == "implicit_return":
                    returns.append(x)
                for k, v in x.__dict__.items():
                    if k != "type" and isinstance(v, (Node, list)):
                        walk(v)

        walk(callee.block)
        if not returns:
            return [False] * n
        for r in returns:
            elements = as_list(r.value.elements) if r.value is not None and r.value.type == "tuple" else [r.value]
            for i in range(n):
                e = elements[i] if i < len(elements) else None
                if not (isinstance(e, Node) and e.type == "local" and e.name not in params
                        and is_sequence_type(ptype(e))):
                    fresh[i] = False
        return fresh

    def assign_from_call(self, target, call):
        """``a, xs = f(...)`` with list/array results: copy into the targets, free fresh results."""
        targets = as_list(target.elements) if target.type == "tuple" else [target]
        types = self.result_types(call)
        fresh = self.fresh_results(call)
        temps = [f"_r{i}" for i in range(len(targets))]
        self.line("{")
        self.indentation += 1
        self.line(f"{', '.join(temps)} := {self.expr(call)}")
        for t, tmp, ty in zip(targets, temps, types):
            dest = self.expr(t)
            if t.type == "sliceindex":
                self.line(f"copy({dest}, {tmp})")
            elif is_sequence_type(ty):
                self.line(f"resize(&{dest}, len({tmp}))")
                self.line(f"copy({dest}[:], {tmp})")
            elif ptype(t) == "float" and ty == "int":
                self.line(f"{dest} = f64({tmp})")
            else:
                self.line(f"{dest} = {tmp}")
        for tmp, is_fresh in zip(temps, fresh):
            if is_fresh:
                self.line(f"delete({tmp})")
        self.indentation -= 1
        self.line("}")

    def repeat_parts(self, value):
        """(fill value, count) for ``[v] * n`` and ``array('f', [v] * n)``, else None."""
        if value.type == "array" and isinstance(getattr(value, "elements", None), Node):
            value = value.elements
        if value.type == "binary_op" and str(value.op) == "*" and value.left.type == "list":
            return as_list(value.left.elements)[0], value.right
        return None

    def assign_sequence(self, target, value, tt):
        t = self.expr(target)
        elem = ptype(tt[1])
        rep = self.repeat_parts(value)
        if rep is not None:
            fill, count = rep
            self.imports.add('"core:slice"')
            self.line(f"resize(&{t}, {self.expr(count, 'int')})")
            self.line(f"slice.fill({t}[:], {self.expr(fill, elem)})")
        elif value.type in ("list", "array") and not as_list(getattr(value, "elements", None)) \
                and not as_list(getattr(value, "elts", None)):
            self.line(f"clear(&{t})")
        elif value.type == "list":
            self.line(f"clear(&{t})")
            self.line(f"append(&{t}, {', '.join(self.expr(e, elem) for e in as_list(value.elements))})")
        elif value.type in ("local", "sliceindex", "index") or \
                (value.type == "standard_call" and str(value.function) == "copy"):
            src = value if value.type != "standard_call" else as_list(value.args)[0]
            s = self.slice_of(src)
            self.line(f"resize(&{t}, len({s}))")
            self.line(f"copy({t}[:], {s})")
        elif value.type == "standard_call" and str(value.function) == "integr":
            first, second = as_list(value.args)
            s = self.slice_of(first)
            self.line(f"resize(&{t}, len({s}))")
            self.line(f"copy({t}[:], {s})")
            if is_sequence_type(ptype(second)):
                self.line(f"append(&{t}, ..{self.slice_of(second)})")
            else:
                self.line(f"append(&{t}, {self.expr(second, elem)})")
        else:
            self.line(f"{t} = {self.expr(value)}")

    # functions ------------------------------------------------------------

    @staticmethod
    def assigned_names(statements, whole_only=False):
        """Names assigned in *statements*; with *whole_only*, only names rebound as a
        whole (``xs = ...``, ``xs.append(...)``), not element writes (``xs[i] = ...``)."""
        names = set()

        def walk(n):
            if isinstance(n, list):
                for x in n:
                    walk(x)
                return
            if not isinstance(n, Node):
                return
            if n.type == "assignment":
                t = n.target
                for x in (as_list(t.elements) if t.type == "tuple" else [t]):
                    if not whole_only:
                        while x.type in ("index", "sliceindex"):
                            x = x.sequence if x.type == "index" else x.receiver
                    if x.type == "local":
                        names.add(x.name)
            if n.type == "standard_method_call" and str(n.message) in (
                    "append", "extend", "pop", "insert_at", "allocate"):
                if n.receiver.type == "local":
                    names.add(n.receiver.name)
            if n.type in ("for_range_statement",):
                names.add(n.index.name)
            for k, v in n.__dict__.items():
                if k != "type" and isinstance(v, (Node, list)):
                    walk(v)

        walk(statements)
        return names

    def copied_params(self, function):
        """List/array parameters a helper rebinds or resizes: it works on a local copy."""
        rebound = self.assigned_names(function.block, whole_only=True)
        return {p.name for p in function.params if p.name in rebound and is_sequence_type(ptype(p))}

    @staticmethod
    def declared_names(statements):
        names = []

        def walk(n):
            if isinstance(n, list):
                for x in n:
                    walk(x)
                return
            if not isinstance(n, Node):
                return
            if n.type == "declaration":
                names.extend(d.name for d in n.decl)
            for k, v in n.__dict__.items():
                if k != "type" and isinstance(v, (Node, list)):
                    walk(v)

        walk(statements)
        return names

    @staticmethod
    def returned_names(statements):
        names = set()

        def walk(n):
            if isinstance(n, list):
                for x in n:
                    walk(x)
                return
            if not isinstance(n, Node):
                return
            if n.type == "implicit_return" and n.value is not None:
                for e in (as_list(n.value.elements) if n.value.type == "tuple" else [n.value]):
                    if getattr(e, "type", None) == "local":
                        names.add(e.name)
            for k, v in n.__dict__.items():
                if k != "type" and isinstance(v, (Node, list)):
                    walk(v)

        walk(statements)
        return names

    def model_proc_signature(self):
        sv = self.struct_vars
        return (f"{sv['m']}: ^{to_ada(self.model.name)}, "
                f"{sv['s']}: ^{self.domain_type('State')}, {sv['s1']}: ^{self.domain_type('State')}, "
                f"{sv['r']}: ^{self.domain_type('Rate')}, {sv['a']}: ^{self.domain_type('Auxiliary')}, "
                f"{sv['ex']}: ^{self.domain_type('Exogenous')}")

    def visit_function_definition(self, node):
        name = str(node.name)
        is_init, is_model = name.startswith("init_"), name.startswith("model_")
        self.funcname = name
        self.current_return = node.return_type
        params = list(node.params)
        declared = self.declared_names(node.block)
        self.check_names([p.name for p in params] + declared, f"{self.model.name if self.model else ''}.{name}")
        self.returned = self.returned_names(node.block)
        self.local_types = {}
        self.param_types = {} if (is_init or is_model) and self.model is not None else {p.name: ptype(p) for p in params}
        self.in_model_proc = (is_init or is_model) and self.model is not None
        self.newline(extra=1)
        if self.in_model_proc:
            self.pick_struct_vars([p.name for p in params] + declared)
            proc = "init" if is_init else "calculate_model"
            if is_model:
                for doc in (self.doc.inputs_doc, self.doc.outputs_doc):
                    for doc_line in doc.split("\n"):
                        self.line(doc_line.rstrip())
            self.line(f"{to_snake(self.model.name)}_{proc} :: proc({self.model_proc_signature()}, allocator := context.allocator) {{")
            self.indentation += 1
            self.line("context.allocator = allocator")
            self.indentation -= 1
        else:
            for p in params:
                self.local_types[p.name] = ptype(p)
            if self.model is not None:
                self.line('@(private="file")')
            sig = ", ".join(f"{to_snake(p.name)}: {self.type_str(p.pseudo_type, param=True)}" for p in params)
            self.line(f"{to_snake(name)} :: proc({sig}){self.return_str(node.return_type)} {{")
            assigned = self.assigned_names(node.block)
            copied = self.copied_params(node)
            self.indentation += 1
            for p in params:
                pname = to_snake(p.name)
                if p.name in copied:
                    self.imports.add('"core:slice"')
                    source = pname if ptype(p)[0] == "array" else f"{pname}[:]"
                    self.line(f"{pname} := slice.clone_to_dynamic({source})")
                    if p.name not in self.returned:
                        self.line(f"defer delete({pname})")
                    self.param_types[p.name] = ["list", ptype(p)[1]]
                elif p.name in assigned and not is_sequence_type(ptype(p)):
                    self.line(f"{pname} := {pname}")
            self.indentation -= 1
        self.block(node.block)
        self.line("}")
        self.in_model_proc = False
        self.struct_vars = {v: v for v in STRUCT_VARS}

    # model unit file ------------------------------------------------------

    def default_value(self, p):
        default = getattr(p, "default_val", None)
        if default is None or str(default).strip() == "":
            return None
        t = ptype(p)
        if is_sequence_type(t):
            try:
                values = ast.literal_eval(str(default))
            except (ValueError, SyntaxError):
                return None
            if not isinstance(values, (list, tuple)) or not values:
                return None
            elem = ptype(t[1])
            if elem == "float":
                return [float_literal(repr(float(v))) for v in values]
            if elem == "int":
                return [str(int(v)) for v in values]
            if elem == "bool":
                return ["true" if v else "false" for v in values]
            return [string_literal(v) for v in values]
        if t == "float":
            return float_literal(default)
        if t == "bool":
            return "true" if str(default).lower() in ("true", "1") else "false"
        if t in ("str", "datetime"):
            return string_literal(default)
        return str(default)

    def write_unit_struct(self):
        model_type = to_ada(self.model.name)
        snake = to_snake(self.model.name)
        for doc in (self.doc.header, self.doc.desc):
            for doc_line in doc.split("\n"):
                self.line(doc_line.rstrip())
        self.line(f"{model_type} :: struct {{")
        self.indentation += 1
        for p in self.node_param:
            self.line(f"{to_snake(p.name)}: {self.type_str(p.pseudo_type)}{unit_tag(p)},{field_comment(p)}")
        self.indentation -= 1
        self.line("}")
        self.newline(extra=1)
        self.line(f"make_{snake} :: proc(allocator := context.allocator) -> (m: {model_type}) {{")
        self.indentation += 1
        self.line("context.allocator = allocator")
        for p in self.node_param:
            value = self.default_value(p)
            if value is None:
                continue
            if isinstance(value, list):
                self.line(f"append(&m.{to_snake(p.name)}, {', '.join(value)})")
            else:
                self.line(f"m.{to_snake(p.name)} = {value}")
        self.line("return")
        self.indentation -= 1
        self.line("}")
        self.newline(extra=1)
        self.write_destroy(f"destroy_{snake}", "m", model_type, self.node_param)

    def write_destroy(self, proc_name, var, type_name, fields):
        self.line(f"{proc_name} :: proc({var}: ^{type_name}) {{")
        self.indentation += 1
        for f in fields:
            if isinstance(ptype(f.pseudo_type), list):
                self.line(f"delete({var}.{to_snake(f.name)})")
        self.indentation -= 1
        self.line("}")

    def header(self):
        pkg = package_name(Path(self.model.path).name) if self.model is not None else "main"
        text = f"package {pkg}\n"
        if self.imports:
            text += "\n" + "".join(f"import {imp}\n" for imp in sorted(self.imports))
        return text

    def visit_module(self, node):
        if self.model is not None:
            self.write_unit_struct()
        body = as_list(node.body)
        # Python lets a later definition replace an earlier one with the same name
        last = {str(f.name): i for i, f in enumerate(body)
                if isinstance(f, Node) and f.type == "function_definition"}
        for i, f in enumerate(body):
            if isinstance(f, Node) and f.type == "function_definition" and last[str(f.name)] != i:
                continue
            self.visit(f)
        self.newline()
        body = "".join(self.result).lstrip("\n")
        self.result = [self.header(), "\n", body]


def field_comment(var):
    desc = str(getattr(var, "desc", "") or "").strip().replace("\n", " ")
    return f" // {desc}" if desc else ""


def unit_tag(var):
    """The variable's unit as a struct tag, `unit:"..."`, as the package declares it.

    A tag rather than a comment so that it can be read at run time
    (core:reflect's struct_tag_lookup), e.g. to label outputs. No tag if the
    variable declares no unit at all.
    """
    unit = getattr(var, "unit", None)
    if unit is None:
        return ""
    # a tag is a raw string in backticks with a quoted value
    unit = " ".join(str(unit).split()).replace("\\", "/").replace('"', "'").replace("`", "'")
    return f' `unit:"{unit}"`'


def to_struct_odin(models, rep, name):
    """Domain-class factory: one file per variable category struct."""
    rep = Path(rep)
    trans = categorize(models)
    nodes = {
        "State": trans.node_states,
        "Rate": trans.node_rates,
        "Auxiliary": trans.node_auxiliary,
        "Exogenous": trans.node_exogenous,
    }
    for category in CATEGORIES:
        gen = OdinGenerator(None)
        type_name = to_ada(f"{name}{category}")
        gen.line(f"{type_name} :: struct {{")
        gen.indentation += 1
        gen.check_names([v.name for v in nodes[category]], type_name)
        for v in nodes[category]:
            gen.line(f"{to_snake(v.name)}: {gen.type_str(v.pseudo_type)}{unit_tag(v)},{field_comment(v)}")
        gen.indentation -= 1
        gen.line("}")
        gen.newline(extra=1)
        gen.write_destroy(f"destroy_{to_snake(name + category)}", "x", type_name, nodes[category])
        gen.newline()
        code = f"package {package_name(rep.name)}\n\n" + "".join(gen.result).lstrip("\n")
        (rep / f"{name}{category}.odin").write_text(code, encoding="utf-8")
    return 0


class OdinCompo(OdinGenerator):
    """Generate the Component that holds and drives the ModelUnits."""

    def __init__(self, tree=None, modelt=None, name=None):
        OdinGenerator.__init__(self, tree)
        self.modelt = modelt
        self.name = modelt.name
        self.doc = DocGenerator(modelt, "// ", indent_with="")
        self.set_categories(categorize([modelt]))
        self.component_type = to_ada(f"{self.name}Component")
        self.prefix = to_snake(f"{self.name}Component")

    def unit_for(self, call_name, prefix):
        short = call_name[len(prefix):]
        for m in self.modelt.model:
            if short.lower() == signature2(m).lower() or short.lower() == m.name.lower():
                return m
        raise ValueError(f"Odin: composition calls unknown model '{call_name}'")

    def struct_for(self, name):
        if not self.in_model_proc:
            return None
        sf = OdinGenerator.struct_for(self, name)
        if sf and sf[0] == self.struct_vars["m"]:
            return None
        return sf

    def composite_inputs(self):
        """Composition parameters and the ModelUnit fields they are linked to."""
        params = {p.name: p for p in self.node_param}
        links = {}
        for link in self.modelt.inputlink:
            source = link["source"]
            if source not in params:
                continue
            unit, var = link["target"].split(".")
            links.setdefault(source, []).append((unit, var))
        return [(params[s], targets) for s, targets in links.items()]

    def unit_field(self, unit_name):
        for m in self.modelt.model:
            if m.name == unit_name or signature2(m) == unit_name:
                return to_snake(m.name)
        return to_snake(unit_name)

    def model_proc_signature(self):
        sv = self.struct_vars
        return (f"{sv['m']}: ^{self.component_type}, "
                f"{sv['s']}: ^{self.domain_type('State')}, {sv['s1']}: ^{self.domain_type('State')}, "
                f"{sv['r']}: ^{self.domain_type('Rate')}, {sv['a']}: ^{self.domain_type('Auxiliary')}, "
                f"{sv['ex']}: ^{self.domain_type('Exogenous')}")

    def call_args(self):
        sv = self.struct_vars
        return f"{sv['s']}, {sv['s1']}, {sv['r']}, {sv['a']}, {sv['ex']}"

    def write_component(self):
        for doc in (self.doc.header, self.doc.desc):
            for doc_line in doc.split("\n"):
                self.line(doc_line.rstrip())
        self.line(f"{self.component_type} :: struct {{")
        self.indentation += 1
        for m in self.modelt.model:
            self.line(f"{to_snake(m.name)}: {to_ada(m.name)},")
        self.indentation -= 1
        self.line("}")
        self.newline(extra=1)
        self.line(f"make_{self.prefix} :: proc(allocator := context.allocator) -> (c: {self.component_type}) {{")
        self.indentation += 1
        self.line("context.allocator = allocator")
        for m in self.modelt.model:
            self.line(f"c.{to_snake(m.name)} = make_{to_snake(m.name)}()")
        self.line("return")
        self.indentation -= 1
        self.line("}")
        self.newline(extra=1)
        self.line(f"destroy_{self.prefix} :: proc(c: ^{self.component_type}) {{")
        self.indentation += 1
        for m in self.modelt.model:
            self.line(f"destroy_{to_snake(m.name)}(&c.{to_snake(m.name)})")
        self.indentation -= 1
        self.line("}")
        for p, targets in self.composite_inputs():
            t = ptype(p.pseudo_type)
            self.newline(extra=1)
            alloc = ", allocator := context.allocator" if is_sequence_type(t) else ""
            self.line(f"{self.prefix}_set_{to_snake(p.name)} :: proc(c: ^{self.component_type}, "
                      f"value: {self.type_str(t, param=True)}{alloc}) {{")
            self.indentation += 1
            if alloc:
                self.line("context.allocator = allocator")
            for unit, var in targets:
                field = f"c.{self.unit_field(unit)}.{to_snake(var)}"
                if is_sequence_type(t):
                    self.line(f"resize(&{field}, len(value))")
                    self.line(f"copy({field}[:], value)")
                else:
                    self.line(f"{field} = value")
            self.indentation -= 1
            self.line("}")

    def visit_module(self, node):
        self.write_component()
        for f in as_list(node.body):
            if isinstance(f, Node) and f.type == "function_definition" and \
                    (str(f.name).startswith("model_") or str(f.name).startswith("init_")):
                self.visit(f)
        self.newline()
        body = "".join(self.result).lstrip("\n")
        pkg = package_name(Path(self.modelt.path).name)
        text = f"package {pkg}\n"
        if self.imports:
            text += "\n" + "".join(f"import {imp}\n" for imp in sorted(self.imports))
        self.result = [text, "\n", body]

    def visit_function_definition(self, node):
        name = str(node.name)
        is_init = name.startswith("init_")
        self.funcname = name
        self.current_return = node.return_type
        params = list(node.params)
        self.local_types = {}
        self.returned = set()
        self.in_model_proc = True
        self.pick_struct_vars([p.name for p in params] + self.declared_names(node.block), model_var="c")
        proc = "init" if is_init else "calculate_model"
        self.newline(extra=1)
        self.line(f"{self.prefix}_{proc} :: proc({self.model_proc_signature()}, allocator := context.allocator) {{")
        self.indentation += 1
        self.line("context.allocator = allocator")
        if is_init:
            self.renamed_input_links()
        self.indentation -= 1
        self.block(node.block)
        self.line("}")
        self.in_model_proc = False

    def renamed_input_links(self):
        """Copy composition inputs to the differently named ModelUnit inputs they feed.

        The composition's model function does this itself; its init function does
        not, so the ModelUnit inits would otherwise read unset fields.
        """
        trans = categorize([self.modelt])
        types = {v.name: v.pseudo_type for v in
                 trans.node_states + trans.node_rates + trans.node_auxiliary + trans.node_exogenous}
        done = set()
        for link in self.modelt.inputlink:
            source, target = link["source"], link["target"].split(".")[1]
            if source == target or source in self.param_names or target in done:
                continue
            if self.struct_for(source) and self.struct_for(target):
                if is_sequence_type(ptype(types.get(target))):
                    self.line(f"resize(&{self.var(target)}, len({self.var(source)}))")
                    self.line(f"copy({self.var(target)}[:], {self.var(source)}[:])")
                else:
                    self.line(f"{self.var(target)} = {self.var(source)}")
                done.add(target)

    def visit_declaration(self, node):
        pass

    def visit_implicit_return(self, node):
        pass

    def visit_assignment(self, node):
        value = node.value
        fn = str(getattr(value, "function", "")) if value.type in ("call", "custom_call") else ""
        if fn.startswith("model_") or fn.startswith("init_"):
            prefix = "model_" if fn.startswith("model_") else "init_"
            unit = self.unit_for(fn, prefix)
            proc = "calculate_model" if prefix == "model_" else "init"
            self.line(f"{to_snake(unit.name)}_{proc}(&{self.struct_vars['m']}.{to_snake(unit.name)}, {self.call_args()})")
            return
        if getattr(value, "name", None) in self.param_names:
            return
        OdinGenerator.visit_assignment(self, node)
