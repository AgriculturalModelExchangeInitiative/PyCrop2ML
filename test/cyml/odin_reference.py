"""Run a package's generated Odin code against its generated Python code.

Both are generated from the same Crop2ML package and fed the same
deterministic inputs, built from the composition metadata (defaults, min/max).
After ``init`` and after each of *days* steps, every composition output and
state is recorded on both sides (floats as their bit patterns) and compared.

The Python target differs from the struct-based targets (cpp2, Odin) in a few
ways that are bugs or limitations of that target, not semantics of the model.
The reference corrects them so that only the translation is compared:

* arrays are ``array('f')`` (single precision): loaded as ``array('d')``;
* declared but unassigned locals are unbound: zero-initialised, as in Odin;
* the composition function re-declares states as fresh locals on every call
  and uses states it does not receive: its body is executed statement by
  statement in one persistent namespace, declarations only initialise once;
* the composition's init does not apply renamed InputLinks: applied up front;
* ModelUnit parameters the composition does not expose: their defaults;
* math functions raise outside their domain: they return NaN, as in C and Odin.
"""
import ast
import math
import os
import re
import struct
import subprocess
import sys
import types
from array import array
from dataclasses import dataclass, field
from pathlib import Path

from pycropml.topology import Topology
from pycropml.transpiler.generators.odinGenerator import categorize
from pycropml.transpiler.rules.odinRules import to_ada, to_snake

TOLERANCE = 1e-12


@dataclass
class Comparison:
    package: str
    identical: int = 0
    close: int = 0
    differences: list = field(default_factory=list)  # (relative error, "step name", python, odin)
    one_sided: list = field(default_factory=list)
    python_error: str = None

    def summary(self):
        text = (f"{self.package}: {self.identical} identical, {self.close} within {TOLERANCE}, "
                f"{len(self.differences)} differ, {len(self.one_sided)} only on one side")
        if self.python_error:
            text += f"; Python reference failed: {self.python_error}"
        for d in sorted(self.differences, key=lambda d: step_key(d[1]))[:8]:
            text += f"\n    {d}"
        return text


def nan_on_domain_error(fn):
    """math functions return NaN outside their domain, as in C and Odin, instead of raising."""
    def wrapped(*args):
        try:
            return fn(*args)
        except (ValueError, OverflowError):
            return math.nan
    return wrapped


def step_key(key):
    step, name = key.split(" ", 1)
    return int(step), name


def num(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def bits(x):
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float):
        return "%016x" % struct.unpack("<Q", struct.pack("<d", x))[0]
    return str(x)


def from_bits(h):
    return struct.unpack("<d", struct.pack("<Q", int(h, 16)))[0]


class Inputs:
    """Deterministic input values for every composition input."""

    def __init__(self, comp):
        self.inputs = {v.name: v for v in comp.inputs}
        self.params = {n: v for n, v in self.inputs.items() if hasattr(v, "parametercategory")}
        self.length_vars = {str(getattr(v, "len", "")) for v in list(comp.inputs) + list(comp.outputs)}
        # parameters first: they size the arrays
        self.ordered = sorted(self.inputs.values(), key=lambda v: (v.name not in self.params, v.name))
        self.salts = {v.name: i for i, v in enumerate(self.ordered)}
        self.values = {}
        for v in self.ordered:
            self.values[v.name] = self.value(v, 0)

    def scalar(self, var, step, salt):
        dt = var.datatype
        lo, hi = num(getattr(var, "min", None)), num(getattr(var, "max", None))
        d = num(getattr(var, "default", None))
        is_param = var.name in self.params
        if dt == "BOOLEAN":
            if is_param:
                return str(getattr(var, "default", "False")).lower() == "true"
            return (step + salt) % 3 == 0
        if dt == "INT":
            if is_param or d is not None:
                return int(d) if d is not None else 1
            return step % 365 + 1
        if dt in ("STRING", "DATE"):
            return str(getattr(var, "default", "") or "")
        if is_param and d is not None:
            return d
        if d is not None:
            mid, amp = d, abs(d) * 0.2 or 0.2
            if lo is not None and hi is not None:
                amp = max(0.0, min(amp, hi - d, d - lo))
                if amp == 0.0 and hi > lo and not is_param:
                    mid, amp = (lo + hi) / 2, (hi - lo) / 4
        elif lo is not None and hi is not None:
            mid, amp = (lo + hi) / 2, (hi - lo) / 4
        else:
            mid, amp = 1.0, 0.2
        if is_param:
            return mid
        if var.name in self.length_vars:
            return int(round(mid))
        return mid + amp * math.sin(0.3 * step + salt)

    def length(self, var):
        ln = str(getattr(var, "len", "") or "")
        if ln.isdigit():
            return int(ln)
        if ln in self.values:
            return int(self.values[ln])
        if ln in self.params:
            return int(num(self.params[ln].default, 1))
        return 5

    def value(self, var, step):
        salt = self.salts.get(var.name, 0)
        dt = var.datatype
        if dt.endswith("ARRAY") or dt.endswith("LIST"):
            base = dt.replace("ARRAY", "").replace("LIST", "")
            elem = types.SimpleNamespace(**{**var.__dict__, "datatype": base})
            default = str(getattr(var, "default", "") or "")
            n = self.length(var) if dt.endswith("ARRAY") else None
            try:
                vals = ast.literal_eval(default) if default.strip() else None
            except (ValueError, SyntaxError):
                vals = None
            if isinstance(vals, (list, tuple)) and vals and (n is None or len(vals) == n):
                vals = [float(x) if base == "DOUBLE" else x for x in vals]
            else:
                vals = [self.scalar(elem, step + i, salt + i) for i in range(n if n is not None else 5)]
            if dt.endswith("ARRAY") and base in ("DOUBLE", "INT"):
                return array("d" if base == "DOUBLE" else "i", vals)
            return vals
        return self.scalar(var, step, salt)


class PythonReference:
    """The generated Python ModelUnits, driven with struct semantics."""

    def __init__(self, package, comp, inputs, report_names):
        self.comp, self.inputs, self.report_names = comp, inputs, report_names
        self.env = dict(inputs.values)
        src = package / "src" / "py" / package.name
        self.modules = [package.name]
        root = types.ModuleType(package.name)
        root.__path__ = [str(src)]
        sys.modules[package.name] = root
        for f in sorted(src.glob("*.py")):
            if f.stem not in ("__init__", "simulation") and not f.stem.endswith("Component"):
                self.load(f, f"{package.name}.{f.stem}")
        compo_file = next(src.glob("*Component.py"))
        self.compo = self.load(compo_file, f"{package.name}.{compo_file.stem}")
        # declarations in the composition are handled by run_body, not zero-initialised
        tree = ast.parse(self.patch(compo_file.read_text(encoding="utf-8"), zero_init=False))
        bodies = {f.name: f.body for f in tree.body if isinstance(f, ast.FunctionDef)}
        self.model_body = bodies[f"model_{comp.name.lower()}"]
        self.init_body = bodies.get(f"init_{comp.name.lower()}")
        self.unit_defaults = {}
        for m in comp.model:
            for inp in m.inputs:
                if hasattr(inp, "parametercategory") and str(getattr(inp, "default", "") or "").strip():
                    self.unit_defaults[inp.name] = inputs.value(inp, 0)
        for link in comp.inputlink:
            target = link["target"].split(".")[1]
            if target != link["source"] and link["source"] in self.env and target not in self.env:
                self.env[target] = self.env[link["source"]]

    @staticmethod
    def patch(code, zero_init=True):
        code = re.sub(r"array\((['\"])f\1", "array('d'", code)
        if not zero_init:
            return code
        for t, zero in (("float", "0.0"), ("int", "0"), ("bool", "False"), ("str", '""')):
            code = re.sub(rf"^(\s+\w+:{t})\s*$", rf"\1 = {zero}", code, flags=re.M)
        return code

    def load(self, path, name):
        module = types.ModuleType(name)
        module.__file__ = str(path)
        sys.modules[name] = module
        self.modules.append(name)
        exec(compile(self.patch(path.read_text(encoding="utf-8")), str(path), "exec"), module.__dict__)
        for fn in ("sqrt", "log", "log10", "acos", "asin", "pow", "exp"):
            if module.__dict__.get(fn) is getattr(math, fn):
                module.__dict__[fn] = nan_on_domain_error(getattr(math, fn))
        return module

    def unload(self):
        for name in self.modules:
            sys.modules.pop(name, None)

    def run_body(self, body):
        env = self.env
        for stmt in body:
            if isinstance(stmt, ast.Return):
                continue
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
                continue
            if isinstance(stmt, ast.AnnAssign):
                name = stmt.target.id
                if name in env:
                    continue
                if stmt.value is None:
                    if name in self.unit_defaults:
                        env[name] = self.unit_defaults[name]
                    else:
                        ann = ast.unparse(stmt.annotation).lower()
                        env[name] = ([] if ("array" in ann or "list" in ann) else 0.0 if "float" in ann
                                     else 0 if "int" in ann else False if "bool" in ann else "")
                    continue
                try:
                    self.exec(stmt)
                except TypeError:
                    env[name] = []
                continue
            self.exec(stmt)

    def exec(self, stmt):
        code = compile(ast.fix_missing_locations(ast.Module([stmt], [])), "composition", "exec")
        exec(code, self.compo.__dict__, self.env)

    def dump(self, step, out):
        for n in self.report_names:
            v = self.env.get(n)
            if v is None:
                continue
            if isinstance(v, (list, tuple)) or hasattr(v, "typecode"):
                for i, x in enumerate(v):
                    out[f"{step} {n}[{i}]"] = bits(x)
            else:
                out[f"{step} {n}"] = bits(v)

    def run(self, days, exogenous):
        out = {}
        if self.init_body is not None:
            self.run_body(self.init_body)
        self.dump(-1, out)
        for step in range(days):
            for v in self.inputs.ordered:
                if v.name in exogenous:
                    self.env[v.name] = self.inputs.value(v, step + 1)
            self.run_body(self.model_body)
            self.dump(step, out)
        return out


class OdinDriver:
    """An Odin main that drives the generated Component with the same inputs."""

    def __init__(self, package, comp, inputs, report_names, trans):
        self.comp, self.inputs, self.report_names = comp, inputs, report_names
        self.generated = package / "src" / "odin" / package.name.replace("-", "_")
        self.code = "\n".join(p.read_text(encoding="utf-8") for p in self.generated.glob("*.odin"))
        self.prefix = to_snake(f"{comp.name}Component")
        self.structs = ((trans.states, "s"), (trans.rates, "r"), (trans.auxiliary, "a"), (trans.exogenous, "ex"))
        self.types = {v.name: v.datatype for v in list(comp.inputs) + list(comp.outputs)}

    def struct_of(self, name):
        for variables, var in self.structs:
            if name in (v.name for v in variables):
                return var
        return None

    def literal(self, datatype, v):
        if isinstance(v, (list, array)):
            base = datatype.replace("ARRAY", "").replace("LIST", "")
            t = {"DOUBLE": "f64", "INT": "int", "BOOLEAN": "bool"}.get(base, "string")
            return f"[]{t}{{{', '.join(self.literal(base, x) for x in v)}}}"
        if datatype == "BOOLEAN":
            return "true" if v else "false"
        if datatype == "INT":
            return str(int(v))
        if datatype in ("STRING", "DATE"):
            return '"' + str(v) + '"'
        return f"transmute(f64)u64(0x{bits(float(v))})"

    def assign(self, var, v):
        if var.name in self.inputs.params:
            setter = f"{self.prefix}_set_{to_snake(var.name)}"
            if re.search(rf"^{setter} ::", self.code, re.M):
                return f"\tpkg.{setter}(&c, {self.literal(var.datatype, v)})"
            return f"\t// no setter for parameter {var.name}"
        sv = self.struct_of(var.name)
        if sv is None:
            return f"\t// {var.name}: not in a struct"
        target = f"{sv}.{to_snake(var.name)}"
        if isinstance(v, (list, array)):
            return f"\tresize(&{target}, {len(v)}); copy({target}[:], {self.literal(var.datatype, v)})"
        return f"\t{target} = {self.literal(var.datatype, v)}"

    def dump(self):
        lines = []
        for n in self.report_names:
            sv = self.struct_of(n)
            if sv is None:
                continue
            target = f"{sv}.{to_snake(n)}"
            dt = self.types.get(n, "DOUBLE")
            if dt.endswith("ARRAY") or dt.endswith("LIST"):
                double = dt.replace("ARRAY", "").replace("LIST", "") == "DOUBLE"
                item, spec = ("transmute(u64)x", "%016x") if double else ("x", "%v")
                lines.append(f'\tfor x, i in {target} {{ fmt.printf("%d {n}[%d] {spec}\\n", step, i, {item}) }}')
            elif dt == "DOUBLE":
                lines.append(f'\tfmt.printf("%d {n} %016x\\n", step, transmute(u64){target})')
            else:
                lines.append(f'\tfmt.printf("%d {n} %v\\n", step, {target})')
        return lines

    def write(self, directory, days, exogenous):
        name = self.comp.name
        main = [
            "package main", "", 'import "core:fmt"',
            f'import pkg "{Path(os.path.relpath(self.generated, directory)).as_posix()}"', "",
            "main :: proc() {",
            f"\tc := pkg.make_{self.prefix}()",
            f"\ts, s1: pkg.{to_ada(name + 'State')}",
            f"\tr: pkg.{to_ada(name + 'Rate')}",
            f"\ta: pkg.{to_ada(name + 'Auxiliary')}",
            f"\tex: pkg.{to_ada(name + 'Exogenous')}",
            "\tstep: int",
        ]
        main += [self.assign(v, self.inputs.value(v, 0)) for v in self.inputs.ordered]
        if re.search(rf"^{self.prefix}_init ::", self.code, re.M):
            main.append(f"\tpkg.{self.prefix}_init(&c, &s, &s1, &r, &a, &ex)")
        main.append("\tstep = -1")
        main += self.dump()
        for step in range(days):
            main.append(f"\tstep = {step}")
            main += [self.assign(v, self.inputs.value(v, step + 1))
                     for v in self.inputs.ordered if v.name in exogenous]
            main.append(f"\tpkg.{self.prefix}_calculate_model(&c, &s, &s1, &r, &a, &ex)")
            main += self.dump()
        main.append("}")
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "main.odin").write_text("\n".join(main) + "\n", encoding="utf-8")

    def run(self, odin, directory, days, exogenous):
        self.write(directory, days, exogenous)
        result = subprocess.run([odin, "run", str(directory), f"-out:{directory / 'driver'}"],
                                capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Odin driver failed:\n{result.stdout[-3000:]}{result.stderr[-3000:]}")
        out = {}
        for line in result.stdout.strip().split("\n"):
            step, name, value = (line.split(" ", 2) + [""])[:3]  # a string value may be empty or contain spaces
            out[f"{step} {name}"] = value
        return out


def compare(package, days, odin, work_dir):
    """Compare the generated Odin and Python code of a transpiled *package*."""
    package = Path(package).resolve()
    comp = Topology(package.name, package).model
    trans = categorize([comp])
    inputs = Inputs(comp)
    exogenous = {v.name for v in trans.exogenous}
    report_names = list(dict.fromkeys([o.name for o in comp.outputs] + [v.name for v in trans.states]))

    result = Comparison(package.name)
    reference = PythonReference(package, comp, inputs, report_names)
    try:
        python = reference.run(days, exogenous)
    except Exception as e:  # still run the Odin side, report both
        python = {}
        result.python_error = f"{type(e).__name__}: {e}"
    finally:
        reference.unload()
    odin_out = OdinDriver(package, comp, inputs, report_names, trans).run(odin, Path(work_dir), days, exogenous)

    result.one_sided = sorted(set(python) ^ set(odin_out))
    for key in python.keys() & odin_out.keys():
        a, b = python[key], odin_out[key]
        if a == b:
            result.identical += 1
            continue
        try:
            fa, fb = from_bits(a), from_bits(b)
        except ValueError:
            result.differences.append((math.inf, key, a, b))
            continue
        if math.isnan(fa) and math.isnan(fb):
            result.identical += 1
            continue
        rel = abs(fa - fb) / max(abs(fa), abs(fb), 1e-300)
        if rel <= TOLERANCE:
            result.close += 1
        else:
            result.differences.append((rel, key, fa, fb))
    return result
