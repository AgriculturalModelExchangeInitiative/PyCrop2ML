# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.nameconvention import signature2, signature2_from_name
from pycropml.transpiler.rules.cppRules import CppRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
from pycropml.transpiler.pseudo_tree import Node
import os
from pycropml.transpiler.interface import middleware
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
from pycropml import code2nbk
from pycropml.render_cyml import my_input
from pycropml.composition import ModelComposition
from copy import deepcopy
from itertools import chain

class CppGenerator(CodeGenerator, CppRules):
    """
    This class contains the specific properties of
    C++ language and use the NodeVisitor to generate a cpp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree, model=None, name=None):
        CodeGenerator.__init__(self)
        CppRules.__init__(self)
        self.tree = tree
        self.model = model
        self.indent_with = ' '*4
        self.initialValue = []
        self.z = middleware(self.tree)
        self.z.transform(self.tree)
        self.name = name
        self.cpp_unique_functions = set()
        self.cpp_struct_names = {"s": "s", "s1": "s1", "r": "r", "a": "a", "ex": "ex"}
        if self.model:
            self.doc = DocGenerator(model, '//')
            self.generator = CppTrans([model])
            self.generator.model2Node()
            self.states = [st.name for st in self.model.states]  
            self.rates = [rt.name for rt in self.generator.rates]
            self.auxiliary = [au.name for au in self.generator.auxiliary] 
            self.exogenous = [ex.name for ex in self.generator.exogenous] 
            self.node_param = self.generator.node_param
            self.modparam = [param.name for param in self.node_param]
        self.funcname = ""

    def visit_notAnumber(self, node):
        self.visit(Node(type="local", name="NAN"))
           
    def visit_comparison(self, node):
        #self.write('(')
        self.visit_binary_op(node)
        #self.write(')')
        
    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(op, 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(f" {self.binary_op[op].replace('_', ' ')} ")
        if "type" in dir(node.right):
            if node.right.type == "binary_op" and self.binop_precedence.get(str(node.right.op), 0) >= prec:  # and node.right.op not in ("+","-") :
                self.write("(")
                self.visit(node.right)
                self.write(")")
            else:
                self.visit(node.right)
        else:
            self.visit(node.right)
        self.operator_exit()

    def visit_constant(self, node):
        self.write(self.constant[node.library][node.name])
        
    def visit_unary_op(self, node):
        op = node.operator
        prec = self.unop_precedence[op]
        self.operator_enter(prec)
        self.write(self.unary_op[op])
        self.visit(node.value)
        self.operator_exit()         
        
    def visit_breakstatnode(self, node):
        self.newline(node)
        self.write('break;')    

    def visit_import(self, node):
        pass

    def visit_none(self, node):
        pass
    
    def visit_cond_expr_node(self, node):
        self.visit(node.test)
        self.write(u" ? ")
        self.visit(node.true_val)     
        self.write(u" : ")
        self.visit(node.false_val) 
        
    def visit_if_statement(self, node):
        self.newline(node)
        self.write('if (')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.newline(node)
        self.body(node.block)
        self.newline(node)
        self.write('}')
        while True:
            else_ = node.otherwise
            if len(else_) == 0:
                break
            elif len(else_) == 1 and else_[0].type == 'elseif_statement':
                self.visit(else_[0])
            else:
                self.visit(else_)
                break
            break

    def visit_elseif_statement(self, node):
        self.newline()
        self.write('else if ( ')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.body(node.block)
        self.newline(node)
        self.write('}')        

    def visit_else_statement(self, node):
        self.newline()
        self.write('else')
        self.newline(node)
        self.write('{')        
        self.body(node.block)
        self.newline(node)
        self.write('}') 

    def visit_print(self, node):
        pass

    def visit_ExprStatNode(self, node):
        self.visit(node.expr)

    def visit_float(self, node):
        self.write(node.value)

    def visit_double(self, node):
        self.write(node.value)

    def visit_array(self, node):
        if hasattr(node, "elts"):
            pass
            
        elif isinstance(node.elements, Node):
            self.write(f"new {self.types[node.pseudo_type[1]]}[")
            self.visit(node.elements.left.elements[0])
            self.write("]")
        else:
            self.write("new [] ")        
            self.write(u'{')
            self.comma_separated_list(node.elements)
            self.write(u'}')
                
    def visit_dict(self, node):
        self.write("new ")
        self.visit_decl(node.pseudo_type)
        self.write(u'{')
        self.comma_separated_list(node.pairs)
        self.write(u'}')
    
    def visit_bool(self, node):
        self.write("true") if node.value == True else self.write("false")
   
    def visit_standard_method_call(self, node):
        l = node.receiver.pseudo_type
        if isinstance(l, list):
            l = l[0]
        z = self.methods[l][node.message]        
        if callable(z):
            if node.message == "sum" and node.receiver.type == "sliceindex":
                self.write("std::accumulate(")
                self.visit(node.receiver.receiver)
                self.write(".begin() + ")
                self.visit(node.receiver.args[0])
                self.write(",")
                self.visit(node.receiver.receiver)
                self.write(".begin() + ")
                self.visit(node.receiver.args[1])
                self.write(", 0.0)")
            else: self.visit(z(node))
        else:
            if not node.args:
                self.write(z)
                self.write('(')
                self.visit(node.receiver)
                self.write(')')
            else:
                f"{self.visit(node.receiver)}.{self.write(z)}"
                self.write("(")
                self.comma_separated_list(node.args)
                self.write(")")

    def visit_method_call(self, node):
        "%s.%s"%(self.visit(node.receiver), self.write(node.message))

    def visit_index(self, node):
        self.visit(node.sequence)
        self.write(u"[")
        if isinstance(node.index.type, tuple):
            self.emit_sequence(node.index)
        else:
            self.visit(node.index)
        self.write(u"]")

    def visit_sliceindex(self, node):
        self.visit(node.receiver)
        self.write(u"[")
        if node.message == "sliceindex_from":
            self.visit(node.args)
            self.write(u":")
        if node.message == "sliceindex_to":
            self.write(u":")
            self.visit(node.args)
        if node.message == "sliceindex":
            self.visit(node.args[0])
            self.write(u":")
            self.visit(node.args[1])
        self.write(u"]")
    
    def visit_assignment(self, node):
        if node.value.type == "binary_op" and node.value.left.type == "list":
            self.visit(node.target)
            self.write(".assign(")
            self.visit(node.value.right)
            self.write(", ")
            self.visit(node.value.left.elements[0])
            self.write(");")
            
            
        elif "function" in dir(node.value) and node.value.function.split('_')[0] == "model":
            name = node.value.function.split('model_')[1]
            for m in self.model.model:
                if name == signature2(m):
                    name = signature2(m)
                    break
            self.write(f"_{name}.Calculate_Model(s, s1, r, a);")
            self.newline(node)

        elif node.value.type == "standard_call" and node.value.function == "copy":
            self.newline(node)
            self.write(f"{node.target.name} = {node.value.args.name};")

        elif node.value.type == "standard_call" and node.value.function == "integr":
            target_name = node.target.name
            self.newline(node)
            self.write(f"{target_name} = {node.value.args[0].name};")
            self.newline(node)
            if isinstance(node.value.args[1].pseudo_type, list):
                an = node.value.args[1].name
                self.write(f"{target_name}.reserve({target_name}.size() + distance({an}.begin(), {an}.end()));")
                self.newline(node)
                self.write(f"{target_name}.insert({target_name}.end(), {an}.begin(), {an}.end());")
            else: 
                self.write(f"{target_name}.push_back(")
                self.visit(node.value.args[1])
                self.write(");")

        elif node.value.type == "standard_method_call" and node.value.message in ["keys", "values"]:
            target_name = node.target.name
            self.write(f"{target_name}.reserve({node.value.receiver.name}.size());")
            self.newline(node)
            self.write(f"for(auto const &i : {node.value.receiver.name})")
            self.newline(node)
            self.write("{")
            self.newline(node)
            self.write(f"    {target_name}.push_back(i.first);") if node.value.message == "keys" \
                else self.write(f"    {target_name}.push_back(i.second);")
            self.newline(node)
            self.write("}")
            self.newline(node)
                
        elif node.value.type == "array" and "elements" in dir(node.value):
            if "right" in dir(node.value.elements):
                self.visit(node.target)
                self.write(f" = std::move(std::vector<{self.types[node.value.pseudo_type[1]]}>(")
                self.visit(node.value.elements.right)
                self.write(", ")
                self.visit(node.value.elements.left.elements[0])
                self.write("));")
                self.newline(node)
            else:
                self.visit(node.target)
                self.write(f" = std::move(std::vector<{self.types[node.value.pseudo_type[1]]}>());")

            #self.write("fill(")
            #self.visit(node.target)
            #self.write(".begin(),")
            #self.visit(node.target)
            #self.write(".end(), ")
            #self.visit(node.value.elements.left.elements[0])
            #self.write(");")
            #self.newline(node)
            
        elif node.value.type == "none":
              pass

        else:
            self.newline(node)
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value) 
            self.write(";")
            self.newline(node)

    def visit_continuestatnode(self, node):
        self.newline(node)
        self.write('continue;')

    def transform_return(self, node):
        if self.funcname.startswith("model") or self.funcname.startswith("init"):
            return_values = node.block[-1].value
            if return_values.type == "tuple":
                output_names = [elt.name for elt in return_values.elements]
                output_nodes = [elt for elt in return_values.elements]
            else:
                output_names = [return_values.name]
                output_nodes = [return_values]
        else:
            if len(self.z.returns) == 1:
                return_values = self.z.returns[0].value
                if return_values.type == "tuple":
                    output_names = [elt.name for elt in return_values.elements]
                    output_nodes = [elt for elt in return_values.elements]
                else:
                    if "name" in dir(return_values):
                        output_names = [return_values.name]
                        output_nodes = [return_values]
                    else:                  
                        output_names = []
                        output_nodes = []
            else: 
                output_names = []
                output_nodes = []
        return output_names, output_nodes

    @staticmethod
    def retrieve_params(node):
        return [pa for pa in node.params]
        #parameters = []
        node_params = []
        for pa in node.params:
            #parameters.append(pa.name)
            node_params.append(pa)
        return node.params

    def array_parameter(self, params):
        dict_arrParamSize = {}
        i = 0
        tplte = False
        for pa in params:
            if pa and isinstance(pa.pseudo_type, list) and pa.pseudo_type[0] == "array":
                if len(pa.elts) == 0:
                    tplte = True
                    elt = f"SIZE_{i}"
                    i = i + 1
                    dict_arrParamSize[pa.name] = elt
                elif "name" in dir(pa.elts[0]):
                    tplte = True
                    elt = pa.elts[0].name
                    dict_arrParamSize[pa.name] = elt
        return dict_arrParamSize, tplte
    
    def templateArr(self, node):
        def myfunc(n):
            return f"size_t {n}"
        narr = self.array_parameter(node)
        uniq_val = []
        for k, v in narr[0].items():
            if v not in uniq_val:
                uniq_val.append(v)
        if narr[1]:
            self.write(f"template<{', '.join(map(myfunc, uniq_val))}>")
        self.newline(node)

    @staticmethod
    def internal_declaration(node):
        """create a list of all the internal declaration nodes for a given function node"""
        statements = node.block if isinstance(node.block, list) else [node.block]
        decls = filter(None, map(lambda s: s.decl if s.type == "declaration" else None, statements))
        return list(chain.from_iterable(decls))

    def add_features(self, node):
        internal_decls = self.internal_declaration(node)
        internal_names = [e.name for e in internal_decls]
        for int_decl in internal_decls:
                if 'elements' in dir(int_decl):
                    self.initialValue.append(Node(type="initial", name=int_decl.name, pseudo_type=int_decl.pseudo_type,
                                                  value=int_decl.elements))
        self.params = [p for p in node.params]
        params_name = [p.name for p in node.params]
        output_names, _ = self.transform_return(node)
        variables = self.params + internal_decls
        new_nodes = []
        for var in variables:
            if var not in new_nodes:
                if var.name in params_name and var.name not in output_names:
                    var.feat = "IN"
                    new_nodes.append(var)
                if var.name in params_name and var.name in output_names:
                    var.feat = "INOUT"
                    new_nodes.append(var)
                if var.name in internal_names and var.name in output_names:
                    var.feat = "OUT"
                    new_nodes.append(var)
                if var.name in internal_names and var.name not in output_names:
                    new_nodes.append(var)
        return new_nodes

    def visit_module(self, node):
        #if self.model:
        #    self.write(f'#ifndef _{self.model.name.upper()}_\n')
                   
        self.write('#define _USE_MATH_DEFINES\n'
                   '#include <cmath>\n'
                   '#include <iostream>\n'
                   '#include <vector>\n'
                   '#include <string>\n'
                   '#include <numeric>\n'
                   '#include <algorithm>\n'
                   '#include <array>\n'
                   '#include <map>\n'
                   '#include <tuple>\n')
        if self.model:
            self.write(f'#include "{self.model.name}.h"\n')
        self.write(f"using namespace {Path(self.model.path).name};")

        #self.write("using namespace std;\n")
        self.visit(node.body)
        self.newline(node)
        #self.write('#endif')

    def visit_function_definition(self, node):      
        self.newline(node)
        self.funcname = node.name
        #print(self.funcname)
        z = self.add_features(node)
        if not node.name.startswith("model_") and not node.name.startswith("init_"):
            func_name = f"{self.model.name}::{node.name}" if self.model else f"{node.name}"
            func_signature = (func_name,
                   tuple(map(lambda t: tuple(t) if isinstance(t, list) else t, node.return_type) if isinstance(
                       node.return_type, list) else node.return_type),
                   tuple(map(lambda x: (
                   tuple(x.pseudo_type) if isinstance(x.pseudo_type, list) else x.pseudo_type, x.name), node.params)))
            if func_signature in self.cpp_unique_functions:
                return
            else:
                self.cpp_unique_functions.add(func_signature)
            self.visit_decl(node.return_type) if node.return_type else self.write("void")
            self.write(f" {func_name}(")
            for i, pa in enumerate(node.params):
                #print(pa.name, pa.feat)
                # if pa.name in self.array_parameter(node.params)[0].values(): continue
                # if pa.feat=="IN"  and pa.type in ["list","array"]: self.write("const ")
                self.visit_decl(pa.pseudo_type, pa)
                if i != len(node.params)-1:
                    self.write(', ')
            self.write(')')
            self.newline(node)
            self.write('{') 
            self.newline(node)
        else:
            if not node.name.startswith("init_"):
                self.write(f"{self.model.name}::{self.model.name}() {{}}")
            self.newline(node) 
            if self.node_param and not node.name.startswith("init_"):
                self.getter(self.model.name, self.node_param)
                self.newline(1)
                self.setter(self.model.name, self.node_param)
                self.newline(1)
            param_names = list(map(lambda x: x.name, self.params))
            unique_code_struct_names = False
            while not unique_code_struct_names:
                unique_code_struct_names = True
                for sn, code_sn in self.cpp_struct_names.items():
                    if code_sn in param_names:
                        self.cpp_struct_names[sn] = f"{code_sn}_"
                        unique_code_struct_names = False
            if node.name.startswith("init_"):
                self.write(f"void {self.model.name}::Init(")
            else:
                self.write(f"void {self.model.name}::Calculate_Model(")
            self.write(f"{self.name}State &{self.cpp_struct_names['s']}, {self.name}State &{self.cpp_struct_names['s1']}, "
                       f"{self.name}Rate &{self.cpp_struct_names['r']}, {self.name}Auxiliary &{self.cpp_struct_names['a']}, "
                       f"{self.name}Exogenous &{self.cpp_struct_names['ex']})")
            self.newline(node)
            self.write('{') 
            self.newline(node)
            if not node.name.startswith("init_"):
                self.write(self.doc.header)
                self.newline(node)
                self.write(self.doc.desc)
                self.newline(node)
                self.write(self.doc.inputs_doc)
                self.newline(node)
                self.write(self.doc.outputs_doc)
                self.newline(node)
            self.indentation += 1 
            for arg in z:  # self.add_features(node) :
                if "feat" in dir(arg):
                    if arg.feat in ("IN", "INOUT"):
                        self.newline(node) 
                        if self.model and arg.name not in self.modparam:
                            self.visit_decl(arg.pseudo_type)
                            if arg.pseudo_type[0] in ["list", "array"]:
                                self.write("&")
                            self.write(f" {arg.name}")
                            if node.name.startswith("init_"):
                                if arg.name in self.exogenous:
                                    self.write(f" = {self.cpp_struct_names['ex']}.get{arg.name}()")
                                elif arg.pseudo_type[0] == "list":
                                    self.write(f" = std::vector<{self.types[arg.pseudo_type[1]]}>()")
                                elif arg.pseudo_type[0] == "array":
                                    x = arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name
                                    if not x:
                                        self.write(f" = std::vector<{self.types[arg.pseudo_type[1]]}>()")
                                    else:
                                        self.write(f" = std::vector<{self.types[arg.pseudo_type[1]]}>({x})")
                            else:
                                # make left hand side a reference to the result in case of lists and arrays
                                if arg.name in self.states and not arg.name.endswith("_t1"):
                                    self.write(f" = {self.cpp_struct_names['s']}.get{arg.name}()")
                                elif arg.name.endswith("_t1") and arg.name in self.states:
                                    self.write(f" = {self.cpp_struct_names['s1']}.get{arg.name[:-3]}()")
                                elif arg.name in self.rates:
                                    self.write(f" = {self.cpp_struct_names['r']}.get{arg.name}()")
                                elif arg.name in self.auxiliary:
                                    self.write(f" = {self.cpp_struct_names['a']}.get{arg.name}()")
                                elif arg.name in self.exogenous:
                                    self.write(f" = {self.cpp_struct_names['ex']}.get{arg.name}()")
                            self.write(";")
            self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1 
        self.write('}') 
        self.newline(node)

    def getter(self, m, node):
        for arg in node:
            self.newline(node)
            self.visit_decl(arg.pseudo_type)
            self.write(f" {m}::get{arg.name}()") if not isinstance(arg.pseudo_type, list) \
                else self.write(f"& {m}::get{arg.name}()")
            self.write(f" {{ return this->{arg.name}; }}")

    def setter(self, m, node):
        for arg in node:
            self.newline(node)
            self.write(f"void {m}::set{arg.name}(")
            self.visit_decl(arg.pseudo_type)
            if not isinstance(arg.pseudo_type, list):
                self.write(f" _{arg.name}) {{ this->{arg.name} = _{arg.name}; }}")
            else:
                self.write(f"const &_{arg.name}){{")
                self.newline(1)
                self.indentation += 1
                self.write(f"this->{arg.name} = _{arg.name};")
                self.newline(1)
                self.indentation -= 1
                self.write("}")

    def visit_custom_call(self, node):
        """TODO"""
        self.visit_call(node)
        #self.write(".result")

    def visit_implicit_return(self, node):
        self.newline(node)
        if not self.funcname.startswith("model_") and not self.funcname.startswith("init_"):
            self.newline(node)
            if node.value is None:
                self.write('return')
            else:
                self.write('return ')
                if node.value.type == "tuple":
                    self.write("make_tuple(")
                    self.comma_separated_list(node.value.elements)
                    self.write(")")
                else:
                    self.visit(node.value)
            self.write(";")  
    
    def visit_return(self, node):
        if self.model:
            self.newline(node)
            self.indentation += 1
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("OUT", "INOUT"):
                        self.newline(node) 
                        if arg.name in self.states:
                            self.write(f"{self.cpp_struct_names['s']}.set{arg.name}({arg.name});")
                        if arg.name in self.rates:
                            self.write(f"{self.cpp_struct_names['r']}.set{arg.name}({arg.name});")
                        if arg.name in self.auxiliary:
                            self.write(f"{self.cpp_struct_names['a']}.set{arg.name}({arg.name});")
                        if arg.name in self.exogenous:
                            self.write(f"{self.cpp_struct_names['ex']}.set{arg.name}({arg.name});")
        else:
            self.newline(node)
            self.indentation += 1
    
    def visit_list(self, node): 
        self.visit_decl(node.pseudo_type)
        self.write(u'(')
        self.comma_separated_list(node.elements)
        self.write(u')')
    
    def visit_tuple(self,node):
        self.write("tie(")
        self.comma_separated_list(node.elements)
        self.write(")")

    def visit_datetime(self, node):
        self.write(f"'{node.value[0].value}/{node.value[1].value}/{node.value[0].value}'")
    
    def visit_str(self, node):
        self.safe_double(node)

    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            self.newline(node)
            if 'value' not in dir(n) and not isinstance(n.pseudo_type, list) and n.pseudo_type != "datetime":
                self.write(self.types[n.pseudo_type])
                self.write(f' {n.name};')
            elif 'elements' not in dir(n) and n.type in ("list", "array"):
                if n.type == "list":
                    self.write(f"std::vector<{self.types[n.pseudo_type[1]]}> {n.name};")
                elif n.type == "array":
                    if "elts" not in dir(n) or not n.elts:
                        self.write(f"std::vector<{self.types[n.pseudo_type[1]]}> {n.name};")
                    else:
                        self.write(f"std::vector<{self.types[n.pseudo_type[1]]}> {n.name}")
                        self.write(f"({n.elts[0].name if 'name' in dir(n.elts[0]) else n.elts[0].value});")
            elif 'value' in dir(n) and n.type in ("int", "float", "str", "bool"):
                self.write(f"{self.types[n.type]} {n.name}")
                self.write(" = ")
                if n.type == "local":
                    self.write(n.value)
                else:
                    self.visit(n)
                self.write(";")           
            elif n.type == 'datetime':
                self.newline(node)
                self.write("DateTime ")
                self.write(n.name)
                if "elts" in dir(n):
                    self.write(" = ")
                    self.visit(n.elts)
                self.write(";")            
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                if n.type == "list":
                    self.visit_decl(n.pseudo_type)
                    self.write(n.name)
                    self.write(" = ") 
                    self.write(u'{')
                    self.comma_separated_list(n.elements)
                    self.write(u'};')
                if n.type == 'tuple':
                    pass
            elif 'pairs' in dir(n) and n.type == "dict":
                self.visit_decl(n.pseudo_type)
                self.write(n.name)             
                self.write(u' = {')
                self.comma_separated_list(n.pairs)
                self.write(u'};')

        self.newline(node)
    
    def visit_list_decl(self, node, pa=None):
        if not isinstance(node[1], list):
            self.write(self.types[node[1]])
            self.write('>')
        else:
            node = node[1]
            self.visit_decl(node, pa)
            self.write('>')
        if pa and "name" in dir(pa):
            self.write(f" {pa.name}")
    
    def visit_dict_decl(self, node):  
        self.write(self.types[node[1]])
        self.write(",")        
        if not isinstance(node[2], list):
            self.write(self.types[node[2]])
            self.write('>')
        else:
            node = node[2]
            self.visit_decl(node)
            self.write('>')
    
    def visit_tuple_decl(self, node):
        self.visit_decl(node[0])
        for n in node[1:-1]:
            self.visit_decl(n)
            self.write(",")
        self.visit_decl(node[-1])
        self.write('>')
    
    def visit_float_decl(self, node, pa=None):
        self.write(self.types[node])
        if pa and "name" in dir(pa):
            self.write(f" {pa.name}")

    def visit_datetime_decl(self, node):
        self.write(self.types[node]) 

    def visit_int_decl(self, node, pa=None):
        self.write(self.types[node])
        if pa and "name" in dir(pa):
            self.write(f" {pa.name}")

    def visit_str_decl(self, node, pa=None):
        self.write(self.types[node])
        if pa and "name" in dir(pa):
            self.write(f" {pa.name}")
        
    def visit_bool_decl(self, node, pa=None):
        self.write(self.types[node])
        if pa and "name" in dir(pa):
            self.write(f" {pa.name}")

    def visit_array_decl(self, node, pa=None):
        """if pa: 
            v =self.array_parameter([pa])[0]
            if pa.name in v: size = v[pa.name]
            else: size = pa.elts[0].value
        if not isinstance(node[1], list):
            if pa: 
                self.write("%s>(%s)"%(self.types[node[1]],size))
            self.write('%s> '%self.types[node[1]])
        else:"""
        node = node[1]
        self.visit_decl(node)
        self.write('> ')
        if pa:
            self.write(pa.name)

    def visit_decl(self, node, pa=None):
        if isinstance(node, list):
            if node[0] == "list":
                self.write('std::vector<')
                self.visit_list_decl(node, pa)
            elif node[0] == "dict":
                self.write("std::map<")
                self.visit_dict_decl(node)
            elif node[0] == "tuple":
                self.write('std::tuple<')
                self.visit_tuple_decl(node)
            elif node[0] == "array":
                self.write('std::vector<')
                self.visit_array_decl(node, pa)
        else:
            if node == "float":
                self.visit_float_decl(node, pa)
            elif node == "int":
                self.visit_int_decl(node, pa)
            elif node == "str":
                self.visit_str_decl(node, pa)
            elif node == "bool":
                self.visit_bool_decl(node, pa) 
            elif node in ("DateTime", "datetime"):
                self.visit_datetime_decl(node)                              

    def visit_pair(self, node):
        self.write(u'{')
        self.visit(node.key)
        self.write(u", ")
        self.visit(node.value)
        self.write(u'}')
            
    def visit_call(self, node):
        want_comma = []
        def write_comma():
            if want_comma:
                self.write(', ')
            else:
                want_comma.append(True)
        if "attrib" in dir(node):
             self.write(f"{node.namespace}.{self.visit(node.function)}")
        else:
            if callable(node.function):
                self.visit(node.function(node))
            else: 
                self.write(node.function)
                self.write('(')
                if isinstance(node.args, list):
                    for arg in node.args:
                        write_comma()
                        self.visit(arg)
                else:
                    self.visit(node.args)
                self.write(')')
    
    def visit_standard_call(self, node):     
        node.function = self.functions[node.namespace][node.function]
        self.visit_call(node) 

    def visit_importfrom(self, node):
        pass
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.write("for(")
        if "iterators" in dir(node):
            self.visit(node.iterators) 
        if "sequences" in dir(node):
            self.visit(node.sequences)
            self.write(')')
        self.newline(node)
        self.write('{')   
        if "iterators" in dir(node):
            self.newline(node)
            self.indentation += 1 
            self.write(f"{node.iterators.iterator.name} = {node.iterators.iterator.name}_cyml;")
            self.indentation -= 1
        self.body(node.block)
        self.newline(node)
        self.write('}')   
          
    def visit_for_iterator_with_index(self, node):
        self.visit(node.index)
        self.write(' , ')
        self.visit(node.iterator)        

    def visit_for_sequence_with_index(self, node):     
        """TODO"""
        pass

    def visit_for_iterator(self, node):
        #self.write("%s "%node.iterator.pseudo_type)
        self.write("const auto& ")
        self.visit(node.iterator)
        self.write("_cyml")
        self.write(" : ")
           
    
    def visit_for_range_statement(self, node):
        self.newline(node)
        self.write("for (")
        self.visit(node.index)
        self.write("=")
        self.visit(node.start)
        self.write(' ; ')
        self.visit(node.index)
        self.write("!=")        
        self.visit(node.end)
        self.write(' ; ')
        self.visit(node.index)
        self.write("+=")
        if "value" in dir(node.step) and node.step.value == 1:
            self.write("1")
        else:      
            self.visit(node.step)
        self.write(')')
        self.newline(node)
        self.write('{')        
        self.body(node.block)
        self.newline(node)
        self.write('}')        
        
    def visit_while_statement(self, node):
        self.newline(node)
        self.write('while ( ')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.body_or_else(node)
        self.newline(node)
        self.write('}')        


class CppTrans(CppGenerator):
    """
    This class used to generates states, rates, auxiliary, exogenous classes
    for C++ languages.
    """
    
    def __init__(self, models, tree=None):
        CppGenerator.__init__(self, tree)
        #CppRules.__init__(self)
        self.models = models
        self.states = []
        self.rates = []
        self.auxiliary = []
        self.exogenous = []
        self.extern = []
        self.modparam = []
    DATATYPE = {
        "INT": "int",
        "DOUBLE": "float",
        "STRING": "str",
        "DATEARRAY": ["array", "str"],
        "INTARRAY": ["array", "int"],
        "DOUBLEARRAY": ["array", "float"],
        "STRINGARRAY": ["array", "str"],
        "STRINGLIST": ["list", "str"],
        "DOUBLELIST": ["list", "float"],
        "INTLIST": ["list", "int"],
        "DATELIST": ["list", "str"],
        "BOOLEAN": 'bool',
        "DATE": "str"
    }

    def model2Node(self):
        from copy import copy
        variables = []
        varnames = []
        for m in self.models:
            if "function" in dir(m):
                for f in m.function:
                    self.extern.append(f.name)
            for inp in m.inputs:
                category = inp.variablecategory if "variablecategory" in dir(inp) else inp.parametercategory
                if category+inp.name not in varnames:
                    category = inp.variablecategory if "variablecategory" in dir(inp) else inp.parametercategory
                    variables.append(inp)
                    varnames.append(category+inp.name)
                    if isinstance(m, ModelComposition) and "diff_in" in dir(m):
                        k_ = get_key(m.diff_in, inp.name)
                        if k_:
                            node_ = deepcopy(inp)
                            node_.name = k_
                            variables.append(node_)
                            varnames.append(category+k_)
            for out in m.outputs:
                #print(out)
                #print(out.name)
                category = out.variablecategory if "variablecategory" in dir(out) else out.parametercategory
                if category+out.name not in varnames:
                    variables.append(out)
                    varnames.append(category+out.name)
                    if isinstance(m, ModelComposition) and "diff_out" in dir(m):
                        k_ = get_key(m.diff_out, out.name )
                        if k_:
                            node_ = deepcopy(out)
                            node_.name = k_
                            variables.append(node_)
                            varnames.append(category + k_)
            if "ext" in dir(m):
                for ex in m.ext:
                    category = ex.variablecategory if "variablecategory" in dir(ex) else ex.parametercategory
                    if category+ex.name not in varnames:
                        variables.append(ex)
                        varnames.append(category+ex.name) 
        #print(varnames)
        st = []
        for var in variables:
            if "variablecategory" in dir(var):
                if var.variablecategory=="state" and not var.name.endswith("_t1") and var.name not in st:
                    self.states.append(var)
                    st.append(var.name)
                if var.variablecategory=="state" and var.name.endswith("_t1"):
                    if var.name[:-3] in st:
                        for i, j in enumerate(self.states):
                            if var.name[:-3] in j.name:
                                self.states.remove(j)
                                break
                    z = copy(var)
                    z.name = z.name[:-3]
                    self.states.append(z)
                    st.append(z.name)

                if var.variablecategory=="rate" :
                    self.rates.append(var)
                if var.variablecategory=="auxiliary":
                    self.auxiliary.append(var)
                if var.variablecategory=="exogenous":
                    self.exogenous.append(var)
            if "parametercategory" in dir(var):
                self.modparam.append(var)

        def create(typevar):
            node_typevar = []
            def catvar(var):
                if "variablecategory" in dir(var) and var.variablecategory=="state": return "s"
                if "variablecategory" in dir(var) and var.variablecategory=="rate": return "r"
                if "variablecategory" in dir(var) and var.variablecategory=="auxiliary": return "a"
                if "variablecategory" in dir(var) and var.variablecategory=="exogenous": return "ex"
            for st in typevar:
                if st.datatype in ("INT", "DOUBLE", "BOOLEAN", "STRING", "INTLIST", "DOUBLELIST", "STRINGLIST", "DATE", "DATELIST"):
                    node = Node(type="local", name=st.name, pseudo_type=self.DATATYPE[st.datatype], cat=catvar(st), desc = st.description, unit = st.unit)
                    node_typevar.append(node)
                if st.datatype in ("INTARRAY","DOUBLEARRAY","STRINGARRAY", "DATEARRAY", ):
                    if st.len.isdigit():
                        elts = Node(type='int', value= st.len, pseudo_type= 'int', desc = st.description, unit = st.unit)
                    else:
                        elts = Node(type='name', name= st.len, pseudo_type= 'int', desc = st.description, unit = st.unit)
                    node=Node(type="local", name=st.name, elts=[elts], pseudo_type=self.DATATYPE[st.datatype], cat=catvar(st), desc = st.description, unit = st.unit)
                    node_typevar.append(node)
            return node_typevar
        self.node_states = create(self.states)
        self.node_rates= create(self.rates)
        self.node_auxiliary= create(self.auxiliary) 
        self.node_exogenous= create(self.exogenous) 
        self.node_param=create(self.modparam)       

    def private_hpp(self, node, iscompo=False):
        self.write("private:")
        self.indentation += 1
        for arg in node:
            self.newline(node)
            if (iscompo and arg.name in self.getRealInputs()) or not iscompo:
                self.visit_decl(arg.pseudo_type, arg)
                self.write(" ;")
    
    def public_hpp(self, node, typ, mc=None, h=None, init=False, iscompo=False):
        self.write("public:")
        self.indentation += 1
        self.newline(1)
        self.write(f"{typ}();")
        self.newline(1)
        if iscompo:
            self.write(f"{typ}({typ}& copy);")  # copy constructor
        self.newline(1)
        if mc:  # except domain classes
            #mc = mc
            self.write(f"void Calculate_Model({mc}State &s, {mc}State &s1, {mc}Rate &r, {mc}Auxiliary &a, {mc}Exogenous &ex);")
        
        if init:  # initialization
            self.newline(1)
            #mc = mc
            self.write(f"void Init({mc}State &s, {mc}State &s1, {mc}Rate &r, {mc}Auxiliary &a, {mc}Exogenous &ex);")
        
        if h:  # function externs
            unique_functions = set()
            for fs in h:
                for func_name, (func_return_type, func_params) in fs.items():
                    key = (func_name,
                           tuple(map(lambda t: tuple(t) if isinstance(t, list) else t, func_return_type) if isinstance(
                               func_return_type, list) else func_return_type),
                           tuple(map(lambda x: (
                           tuple(x.pseudo_type) if isinstance(x.pseudo_type, list) else x.pseudo_type, x.name),
                                     func_params)))
                    if key not in unique_functions:
                        unique_functions.add(key)
                        self.newline(1)
                        self.visit_decl(func_return_type)
                        self.write(f" {func_name}(")
                        for i, pa in enumerate(func_params):
                            self.visit_decl(pa.pseudo_type)
                            self.write(f" {pa.name}{', ' if i != len(func_params)-1 else ''}")
                        self.write(");")
        for arg in node:
            self.newline(node)
            if (iscompo and arg.name in self.getRealInputs()) or not iscompo:
                self.visit_decl(arg.pseudo_type)
                self.write(f" get{arg.name}();") if not isinstance(arg.pseudo_type, list) else self.write(f"& get{arg.name}();")
                self.newline(node)
                self.write(f"void set{arg.name}(")
                
                if not isinstance(arg.pseudo_type, list):
                    self.visit_decl(arg.pseudo_type)
                else:
                    self.write("const ")
                    self.visit_decl(arg.pseudo_type)
                    self.write("& ")
                self.write(f" _{arg.name});")  # if not isinstance(arg.pseudo_type, list) else self.write("& _%s);"%arg.name)

    def getRealInputs(self):
        inputs = []
        for inp in self.models[0].inputlink:
            var = inp["source"]
            inputs.append(var)
        return inputs

    def private(self,node):
        for arg in node:
            self.newline(node) 
            self.write('private ')
            self.visit_decl(arg.pseudo_type)
            self.write(" _")
            self.write(arg.name) 
            if arg.pseudo_type[0] == "list":
                self.write("()")
            elif arg.pseudo_type[0] == "array":
                self.write(f" = new {self.types[arg.pseudo_type[1]]}[{arg.elts[0].value if 'value' in dir(arg.elts[0]) else arg.elts[0].name}]")
            self.write(";") 

    def getset(self, node, wrap=False):
        for arg in node:
            self.newline(node)
            self.write("public ")
            if isinstance(arg.pseudo_type, list):
                if arg.pseudo_type[0] in ("list", "array"):
                    self.visit_decl(arg.pseudo_type)
                    self.write(' ' + arg.name)                                                            
            else:
                self.visit_decl(arg.pseudo_type)
                self.write(' ' + arg.name)
            self.write(self.write(self.public_properties_wrap.format(arg.cat,arg.name)
                                  if wrap else self.public_properties.format(arg.name, arg.name)))

    def copyconstructor(self, node):
        for arg in node:
            self.newline(node)
            if isinstance(arg.pseudo_type, list):
                if arg.pseudo_type[0] == "list":
                    self.write("vector<%s> %s;"%(arg.name, self.types[arg.pseudo_type[1]]))
                    self.write(self.copy_constrList%(arg.name,arg.name,arg.name))
                if arg.pseudo_type[0] == "array":
                    t = self.types[arg.pseudo_type[1]]
                    elem_count = arg.elts[0].value if 'value' in dir(arg.elts[0]) else arg.elts[0].name
                    self.write(f"{arg.name} = std::vector<{t}>({elem_count});")
                    self.write(self.copy_constrArray.format(arg.elts[0].value
                                                            if "value" in dir(arg.elts[0]) else arg.elts[0].name,
                                                            arg.name, arg.name))
            else:
                self.write(f"_{arg.name} = toCopy._{arg.name};")

    def generate(self, nodes, typ): 
        self.newline(1)
        self.write(f"{typ}::{typ}() {{}}")
        self.newline(extra=1)
        self.getter(typ, nodes)
        self.newline(extra=1)
        self.setter(typ, nodes)
    
    def generate_hpp(self, node, typ, dc=False, mc=None, h=None, init=False, iscompo=False, ns=None):
        if ns:
            self.write(f"namespace {ns} {{\n")
        self.write(f"class {typ}")
        self.newline(1)
        self.write("{")
        self.newline(node)
        self.indentation += 1        
        self.newline(1)
        self.private_hpp(node, iscompo)
        self.newline(node)
        self.indentation -= 1
        self.public_hpp(node, typ, mc, h, init, iscompo)
        self.newline(extra=1)
        if iscompo:
            self.instanceModels()
        self.newline(extra=1)
        self.indentation -= 2
        self.write("};")
        self.newline(1)
        if ns:
            self.write("}\n")
        #if dc:
        #    self.write("#endif")
    
    def instanceModels(self):
        self.newline(extra = 1)
        for m in self.models[0].model:
            name = m.name
            self.write(f"{name} _{signature2(m)};")
            #self.write(f"{name} _{name};")
            self.newline(1)


def to_struct_cpp(models, rep, name):
    header_cpp(models, rep, name)
    header_mu_cpp(models, rep, name)
    headerCompo(models, rep, name)
    generator = CppTrans(models)
    generator.result = [f'#include "{name}State.h"\n']
    generator.result.append(f"using namespace {rep.name};\n")
    generator.model2Node()
    states = generator.node_states
    generator.generate(states, f"{name}State")
    z = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}State.cpp"))
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))
    rates = generator.node_rates
    generator.result = [f'#include "{name}Rate.h"\n']
    generator.result.append(f"using namespace {rep.name};\n")
    generator.generate(rates, f"{name}Rate")
    z1 = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Rate.cpp"))
    with open(filename, "wb") as tg1_file:
        tg1_file.write(z1.encode('utf-8'))       
    auxiliary = generator.node_auxiliary
    generator.result = [f'#include "{name}Auxiliary.h"\n']
    generator.result.append(f"using namespace {rep.name};\n")
    generator.generate(auxiliary, f"{name}Auxiliary")
    z2 = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Auxiliary.cpp"))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))

    exogenous = generator.node_exogenous
    generator.result = [f'#include "{name}Exogenous.h"\n']
    generator.result.append(f"using namespace {rep.name};\n")
    generator.generate(exogenous, f"{name}Exogenous")
    z2 = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Exogenous.cpp"))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))
    return 0


def header_cpp(models, rep, name):
    generator = CppTrans(models)
    #generator.result=[u"#ifndef _%sState_\n#define _%sState_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name,name)]
    generator.result = [
        f"""\
#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include<vector>
#include<string>
"""]
    generator.model2Node()

    states = generator.node_states
    generator.generate_hpp(states, f"{name}State", dc=True, ns=rep.name)
    z = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}State.h"))
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))

    rates = generator.node_rates
    #generator.result=[u"#ifndef _%sRate_\n#define _%sRate_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name,name)]
    generator.result = [f"""\
#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
"""]
    generator.generate_hpp(rates, f"{name}Rate", dc=True, ns=rep.name)
    z1 = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Rate.h"))
    with open(filename, "wb") as tg1_file:
        tg1_file.write(z1.encode('utf-8'))

    auxiliary = generator.node_auxiliary
    #generator.result = [u"#ifndef _%sAuxiliary_\n#define _%sAuxiliary_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name,name)]
    generator.result = [f"""\
#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
"""]
    generator.generate_hpp(auxiliary, f"{name}Auxiliary", dc=True, ns=rep.name)
    z2 = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Auxiliary.h"))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))

    exogenous = generator.node_exogenous
    #generator.result=[u"#ifndef _%sExogenous_\n#define _%sExogenous_\n#define _USE_MATH_DEFINES\n#include <cmath>\n#include <iostream>\n# include<vector>\n# include<string>\nusing namespace std;\n"%(name,name)]
    generator.result = [f"""\
#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
"""]
    generator.generate_hpp(exogenous, f"{name}Exogenous", dc=True, ns=rep.name)
    z2 = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Exogenous.h"))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z2.encode('utf-8'))

    return 0


def header_mu_cpp(models, rep, name):
    mc = models[0].name 
    h = [] 
    init = False
    for m in models[0].model:
        if m.function:
            for mf in m.function:
                file_func = mf.filename
                path_func = Path(os.path.join(m.path, "crop2ml", file_func))
                func_tree=parser(Path(path_func))  
                newtree = AstTransformer(func_tree, path_func)
                #print(newtree)
                dict_ast = newtree.transformer()
                node_ast= transform_to_syntax_tree(dict_ast)
                z = {}
                for f in filter(lambda x: x.type == "function_definition", node_ast.body):
                    z[f.name] = [f.return_type, f.params]
                h.append(z) 
        if m.initialization:
            init = True
        generator = CppTrans([m])
        generator.result = [f'''
#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include "{name}State.h"
#include "{name}Rate.h"
#include "{name}Auxiliary.h"
#include "{name}Exogenous.h"
''']
        generator.model2Node()
        param = generator.node_param
        generator.generate_hpp(param, f"{m.name}", mc=mc, h=h, init=init, ns=rep.name)
        z = ''.join(generator.result)
        filename = Path(os.path.join(rep, f"{m.name}.h"))
        with open(filename, "wb") as tg_file:
            tg_file.write(z.encode('utf-8'))
        h = []


def headerCompo(models, rep, name):
    """ Header file of model composite"""
    mc = models[0].name 
    h = [] 
    models_incl = [f'#include "{m.name}.h"' for m in models[0].model]
    #domclass_inc = ['#include "%sState.h"'%name,'#include "%sRate.h"'%name,'#include "%sAuxiliary.h"'%name]   
    includes = '\n'.join(models_incl)
    generator = CppTrans(models)
    generator.result = [includes + "\n\n"]
    generator.model2Node()
    param = generator.node_param
    generator.generate_hpp(param, f"{mc}Component", mc=mc, h=h, init=True, iscompo=True, ns=rep.name)
    z = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{mc}Component.h"))
    with open(filename, "wb") as tg_file:
        tg_file.write(z.encode('utf-8'))


class CppCompo(CppTrans):
    """ This class generate the C++ composite class."""

    def __init__(self, tree=None, modelt=None, name=None):
        CppTrans.__init__(self, [modelt])
        self.modelt = modelt
        self.tree = tree
        self.name = modelt.name
        self.init = False
        self.write(f'#include "{self.name}Component.h"\n')
        self.write(f"using namespace {modelt.path.name};\n")
        self.modeltparams = [pa.name for pa in self.modelt.inputs if "parametercategory" in dir(pa)]
        self.model2Node()
        self.statesName = [st.name for st in self.states]
        self.ratesName = [rt.name for rt in self.rates]
        self.auxiliaryName = [au.name for au in self.auxiliary]
        self.exogenousName = [ex.name for ex in self.exogenous]
        self.aux = [link["source"].split(".")[1] for link in self.modelt.internallink]
        self.realinp = []  # determine the real inputs of the composite
        for node in self.node_auxiliary + self.node_exogenous:
            if node.name not in self.realinp and node.name not in self.aux:
                self.realinp.append(node)

    def visit_module(self, node):        
        self.visit(node.body)
        self.newline(node)
        if "function" in dir(self.modelt) and self.modelt.function:
            func_name = os.path.split(self.modelt.function[0].filename)[1]
            func_path = os.path.join(self.modelt.path, "src", "pyx", func_name)
            func_tree = parser(Path(func_path))
            newtree = AstTransformer(func_tree, func_path)
            dictAst = newtree.transformer()
            nodeAst = transform_to_syntax_tree(dictAst)
            self.modelt = None
            self.visit(nodeAst.body)
        self.indentation -= 1        
        self.newline(node)              

    def visit_function_definition(self, node):      
        self.add_features(node)
        self.funcname = node.name
        if node.name.startswith("init_"):
            self.write("")
        else:
            self.write(self.constructor%(f"{self.modelt.name}Component", f"{self.modelt.name}Component"))
        self.newline(extra=1)          

        n = self.name
        if self.node_param and not node.name.startswith("init_"):
            self.getter(f"{n}Component", self.node_param)
            self.newline(extra=1)
            self.setter(f"{n}Component", self.node_param)
            self.newline(node)      

        if node.name.startswith("init_"):
            self.write(f"void {n}Component::Init(")
            self.init = True
        else:
            self.write(f"void {n}Component::Calculate_Model(")

        self.write(f"{n}State &s, {n}State &s1, {n}Rate &r, {n}Auxiliary &a, {n}Exogenous &ex)")
        self.newline(node)
        self.write('{') 
        self.newline(node)
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        # self.indentation -= 1
        self.write('}') 
        self.newline(node)
        typ = self.modelt.name+"Component"
        if node.name.startswith("init_"):
            self.write("")  # copy constructor
        else:
            self.write(f"{typ}::{typ}({typ}& toCopy)")
            self.newline(1)
            self.write("{")
            self.copyconstructor(self.node_param)
            self.newline(node)
            self.write('}')  
        self.newline(1)

    def visit_assignment(self, node):
        if "function" in dir(node.value) and node.value.function.split('_')[0] == "model":
            name = node.value.function.split('model_')[1]
            for m in self.modelt.model:
                if name.lower() == signature2(m).lower():
                    name = signature2(m)
                    break
            self.write(f"_{name}.Calculate_Model(s, s1, r, a, ex);")
            self.newline(node)
        else:
            self.newline(node)
            if node.value.name not in self.modeltparams:
                if node.target.name in self.statesName:
                    self.write("s.set")
                elif node.target.name in self.ratesName:
                    self.write("r.set")
                elif node.target.name in self.auxiliaryName:
                    self.write("a.set")
                elif node.target.name in self.exogenousName:
                    self.write("ex.set")
                self.visit(node.target)
                self.write('(')
                if node.value.name in self.statesName:
                    self.write("s.get")
                elif node.value.name in self.ratesName:
                    self.write("r.get")
                elif node.value.name in self.auxiliaryName:
                    self.write("a.get")
                elif node.value.name in self.exogenousName:
                    self.write("ex.get")
                self.visit(node.value) 
                self.write("());")
            else:
                #x = self.getmo(node.target.name)
                pass
            self.newline(node)

    def visit_declaration(self, node):
        if self.init:
            return CppGenerator(self.tree).visit_declaration(node)
        else: 
            pass

    def assignParam(self):
        h = 'from datetime import datetime\n'
        for m in self.model.inputs:
            if "parametercategory" in dir(m):
                if "len" in dir(m):
                    m.len = "100"
                h += "cdef " + my_input(m) + "\n"
        return h
    
    def tranAssignParam(self):
        from pycropml.transpiler.main import Main
        snip = Main(self.assignParam(), "cpp")
        a = snip.parse()
        g = snip.to_ast(self.assignParam())
        snip.dictAst
        return snip.to_source()
    
    def format(self):
        code = self.tranAssignParam()
        lines = code.split("\n")
        lines = lines[5:-1]
        code = "\n".join(lines)
        return code

    def visit_local(self, node):
        self.write(node.name)

    """def visit_declaration(self, node):
        pass"""
    
    def visit_return(self, node):
        self.newline(node)

    def getter(self, m, node):
        for arg in node:
            self.newline(node)
            if arg.name in self.getRealInputs():
                self.visit_decl(arg.pseudo_type)
                if isinstance(arg.pseudo_type, list):
                    self.write(f"& {m}::get{arg.name}()")
                else:
                    self.write(f" {m}::get{arg.name}()")
                #mo = self.get_mo(arg.name)
                #for mi in mo:
                #    self.write(f"{{ return _{list(mi.keys())[0]}.get{list(mi.values())[0]}(); }}")
                #    self.newline(1)
                self.write(f"{{ return this->{arg.name}; }}")
                
    def setter(self, m, node):
        for arg in node:
            self.newline(node)
            argname = arg.name
            if argname in self.getRealInputs():
                if not isinstance(arg.pseudo_type, list):
                    self.write(f"void {m}::set{arg.name}(")
                    self.visit_decl(arg.pseudo_type)
                    self.write(f" _{arg.name})")
                else:
                    self.write(f"void {m}::set{arg.name}(const ")
                    self.visit_decl(arg.pseudo_type)
                    self.write(f"& _{arg.name})")
                self.newline(1)
                self.write("{")
                self.newline(1)
                self.indentation += 1
                mo = self.get_mo(arg.name)
                for mi in mo:
                    self.write(f"_{signature2_from_name(mi[0])}.set{mi[1]}(_{arg.name});")
                    self.newline(1)
                self.newline(1)
                self.indentation -= 1
                self.write("}")

    def getRealInputs(self):
        inputs = []
        for inp in self.modelt.inputlink:
            var = inp["source"]
            inputs.append(var)
        return inputs

    def get_mo(self, varname):
        listmo = []
        for inp in self.modelt.inputlink:
            var = inp["source"]
            mod = inp["target"].split(".")[0]
            modvar = inp["target"].split(".")[1]
            if var == varname:
                listmo.append((mod, modvar))
        return listmo

    def copyconstructor(self,node):
        for arg in node:
            self.newline(node)
            if arg.name in self.getRealInputs():
                if isinstance(arg.pseudo_type, list):
                    if arg.pseudo_type[0] == "list":
                        self.write(f"    {self.copy_constrList%(arg.name,arg.name,arg.name)}")
                    if arg.pseudo_type[0] =="array":
                        #self.write("    %s"%self.copy_constrArray%(arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name,arg.name,arg.name))
                        length = arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name 
                        if not length:
                            length = f"toCopy.get{arg.name}().size()"
                        self.write(f"    {self.copy_constrArray%(length,arg.name,arg.name)}")
                else:
                    self.write("    %s = toCopy.get%s();"%(arg.name, arg.name)) 

    def initCompo(self):            
        pass
    
    def wrapper(self):           
        self.write(f"class {self.modelt.name}Wrapper")
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.privateWrap()
        self.constrWrap()
        self.newline(extra=1)
        self.write(self.format())
        self.newline(extra=1)
        self.outputWrap()
        self.newline(extra=1)
        self.copyconstrWrap()
        self.newline(extra=1)
        self.initWrap()
        self.newline(extra=1)
        self.loadParamWrap()
        self.newline(extra=1)
        self.estimateWrap()
        self.newline(extra=1)
        self.indentation -= 1
        self.write("}")
        self.newline(extra=1)

    def privateWrap(self) :
        name = self.modelt.name
        self.write(f"private {name}State s;")
        self.newline(1)
        self.write(f"private {name}Rate r;")
        self.newline(1)
        self.write(f"private {name}Auxiliary a;")
        self.newline(1)
        self.write(f"private {name}Exogenous ex;")
        self.newline(1)
        self.write(f"private {name}Component {name.lower()}Component;")
        self.newline(extra=1)
    
    def constrWrap(self):
        name = self.modelt.name
        self.write(f"public {name}Wrapper()")
        self.newline(1)
        self.write("{") 
        self.newline(1)
        self.indentation += 1
        self.write(f"s = new {name}State();")
        self.newline(1)
        self.write(f"r = new {name}Rate();")
        self.newline(1)
        self.write(f"a = new {name}Auxiliary();")
        self.newline(1)
        self.write(f"ex = new {name}Exogenous();")
        self.newline(1)
        self.write(f"{name.lower()}Component = new {name}Component();")
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")
    
    def outputWrap(self):
        out = [out.name for out in self.modelt.outputs]
        tabout = []
        nodes = self.node_states + self.node_rates + self.node_auxiliary + self.node_exogenous
        for node in nodes :
            if node.name in out and node.name not in tabout:
                self.getset([node], True)
                tabout.append(node.name)

    def copyconstrWrap(self):
        n = self.modelt.name
        self.write(f"public {n}Wrapper({n}Wrapper toCopy, bool copyAll) : this()")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        self.write(f"s = (toCopy.s != null) ? new {n}State(toCopy.s, copyAll) : null;")
        self.newline(1)
        self.newline(1)
        self.write(f"r = (toCopy.r != null) ? new {n}Rate(toCopy.r, copyAll) : null;")
        self.newline(1)
        self.write(f"a = (toCopy.a != null) ? new {n}Auxiliary(toCopy.a, copyAll) : null;")
        self.newline(1)
        self.write(f"ex = (toCopy.ex != null) ? new {n}Exogenous(toCopy.ex, copyAll) : null;")
        self.newline(1)
        self.write("if (copyAll)")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        nl = n.lower()
        self.write(f"{nl}Component = (toCopy.{n}Component != null) ? new {n}Component(toCopy.{nl}Component) : null;")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")
        self.newline(1)
        self.indentation -= 1        
        self.write("}")

    def initWrap(self):
        self.write("public void Init()")
        self.write("{")
        self.newline(1)
        self.indentation += 1 
        self.write(f"{self.modelt.name.lower()}Component.Init(s, r, a);")
        self.newline(1)
        self.write("loadParameters();")
        self.newline(1)
        self.indentation -= 1
        self.write("}")
    
    def loadParamWrap(self):
        self.write("private void loadParameters()")  
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1
        tab = []
        for node in self.modparam :
            if node.name not in tab:
                self.write(f"{self.model.name.lower()}Component.{node.name} = {node.name};")
                tab.append(node.name)
                self.newline(1)
        self.indentation -= 1 
        self.write("}")
    
    def estimateWrap(self):
        modelt_name = self.modelt.name
        self.write(f"public void Estimate{modelt_name}(")
        for node in self.realinp:
                self.visit_decl(node.pseudo_type)
                self.write(" ")
                self.write(node.name)
                self.write(", ") if node != self.realinp[len(self.realinp)-1] else ''
        self.write(")")
        self.newline(1)
        self.write("{")
        self.newline(1)
        self.indentation += 1 
        for node in self.realinp:
            self.write(f"a.{node.name} = {node.name};")
            self.newline(1)
        n = modelt_name.lower()
        self.write(f"{n}Component.Calculate_{n}(s, s1, r, a);")
        self.newline(1)
        self.indentation -= 1 
        self.write("}")


def to_wrapper_cpp(models, rep, name):
    generator = CppCompo(modelt=models)
    generator.result = [
        "#define _USE_MATH_DEFINES\n"
        "#include <cmath>\n"
        "#include <iostream>\n"
        "#include <vector>\n"
        "#include <string>\n"
        #"using namespace std;\n"
    ]
    generator.model2Node()
    generator.wrapper()
    z = ''.join(generator.result)
    filename = Path(os.path.join(rep, f"{name}Wrapper.cpp"))
    with open(filename, "wb") as tg2_file:
        tg2_file.write(z.encode('utf-8'))
    return 0

def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key
    return None