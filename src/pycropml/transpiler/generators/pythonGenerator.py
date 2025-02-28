# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.pythonRules import PythonRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
import os
from pycropml.render_cyml import signature
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
from pycropml.transpiler.pseudo_tree import Node




def initVal(type_):
    if type_=="f": return 0.0
    if type_=="i": return 0
    

class PythonGenerator(CodeGenerator, PythonRules):
    """This class contains the specific properties of 
    python language and use the NodeVisitor to generate a python
    code source from a well formed syntax tree.
    """
    def __init__(self, tree, model=None, name = None):
        CodeGenerator.__init__(self)
        PythonRules.__init__(self)
        self.tree=tree
        self.model=model
        self.name = name
        self.indent_with=' '*4 
        self.imp=True
        if self.model: 
            self.doc=DocGenerator(self.model, " ")

    def comment(self,doc):
        list_com = [self.indent_with + '#'+x for x in doc.split('\n')]
        com = '\n'.join(list_com)
        return com
    
    def visit_import(self, node):
        if self.imp:
            self.write(u"import %s" % node.module)

    def visit_notAnumber(self, node):
        self.write("float('nan')")

    def visit_local(self, node):
        if "unit" in dir(node):
            self.write("%s%s"%(node.name,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.name,node.units))
        else: self.write(node.name)

    def visit_int(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.value,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.value,node.units))
        else:self.write(node.value)


    def visit_assignment(self, node):
        self.newline(node)
        if node.value.type == "standard_call" and node.value.function=="integr":
            self.write("%s = copy(%s)"%(node.target.name, node.value.args[0].name))
            self.newline(node)
            if isinstance(node.value.args[1].pseudo_type, list):
                self.write("%s.extend("%node.target.name)
            else: self.write("%s.append("%node.target.name)
            self.visit( node.value.args[1])
            self.write(")")
        
        else:
            self.visit(node.target)
            self.write(' = ')
            self.visit(node.value)
    
    def visit_none(self, node):
        self.write("None")

    def visit_cond_expr_node(self, node):
        self.visit(node.true_val)
        self.write(u" if ")
        self.visit(node.test)
        self.write(u" else ")
        self.visit(node.false_val)  
        
    def visit_constant(self, node):
        self.write(self.constant[node.library][node.name])

    def visit_if_statement(self, node):
        self.newline(node)
        self.write('if ')
        self.visit(node.test)
        self.write(':')
        self.body(node.block)
        while True:
            else_ = node.otherwise
            if len(else_) == 0:
                break
            elif len(else_) == 1 and else_[0].type=='elseif_statement':
                self.visit(else_[0])
            else:
                self.visit(else_)
                break
            break
    
    def visit_elseif_statement(self, node):
        self.newline()
        self.write('elif ')
        self.visit(node.test)
        self.write(':')
        self.body(node.block)

    def visit_else_statement(self, node):
        self.newline()
        self.write('else:')
        self.body(node.block)
    
    def visit_float(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.value,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.value,node.units))
        else: self.write(node.value)
        
    def visit_bool(self, node):
        self.write(str(node.value).capitalize())

    def visit_str(self, node):
        self.safe_double(node)
    
    def visit_tuple(self, node):
        self.emit_sequence(node.elements, u"()")
        
    def visit_dict(self, node):
        self.emit_sequence(node.pairs, u"{}")
        
    def visit_pair(self, node):
        self.visit(node.key)
        self.write(u": ")
        self.visit(node.value)         

    def visit_ExprStatNode(self, node):
        self.newline(node)
        self.visit(node.expr)
    
    def visit_list(self, node):
        self.emit_sequence(node.elements, u"[]")

    def visit_datetime(self, node):
        self.write("datetime")
        self.emit_sequence(node.value, u"()")

    def visit_standard_method_call(self, node):
        l = node.receiver.pseudo_type
        if isinstance(l, list):
            l = l[0]
        z = self.methods[l][node.message]
        if callable(z):
            self.visit(z(node))
        
        else:
            if not node.args:
                self.write(node.message)
                self.write('(')
                self.visit(node.receiver)
                self.write(')')
            else:
                "%s.%s"%(self.visit(node.receiver),self.write(z))
                self.write("(")
                self.comma_separated_list(node.args)
                self.write(")")

    def visit_custom_call(self, node):
        self.visit_call(node)


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
        if node.message=="sliceindex_from":
            self.visit(node.args)
            self.write(u":")
        if node.message=="sliceindex_to":
            self.write(u":")
            self.visit(node.args)
        if node.message=="sliceindex":
            self.visit(node.args[0])
            self.write(u":")
            self.visit(node.args[1])
        self.write(u"]")


    def visit_module(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.write("# coding: utf8")
        self.newline(node)
        #self.write("from pycropml.units import u")
        #self.newline(node)
        self.write("from copy import copy\nfrom array import array\nfrom math import *\nfrom typing import *\nfrom datetime import datetime\n")
        self.newline(node)
        self.visit(node.body)

        
    def visit_comparison(self, node):
        if node.op == "is":
            if node.right.type == "none":
                self.visit(node.left)
                self.write(" is None")
        else:
            self.visit_binary_op(node)

    def visit_method_call(self, node):
        "%s.%s"%(self.visit(node.receiver),self.write(node.message))  
              
    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(op, 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(u" %s " % self.binary_op[op].replace('_', ' '))
        if "type" in dir(node.right):
            if node.right.type=="binary_op" and  self.binop_precedence.get(str(node.right.op), 0) >= prec: # and node.right.op not in ("+","-") :
                self.write("(")
                self.visit(node.right)
                self.write(")")
            else:
                self.visit(node.right)
        else:
            self.visit(node.right)
        self.operator_exit()
    
    def visit_unary_op(self, node):
        op = node.operator
        prec = self.unop_precedence[op]
        self.operator_enter(prec)
        self.write(u"%s" % self.unary_op[op])
        self.visit(node.value)
        self.operator_exit()

    def visit_function_definition(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.funcname = node.name
        if self.model and self.funcname.startswith("model_") and self.funcname.split("model_")[1]==signature(self.model):
            self.write("#%%CyML Model Begin%%")
            self.newline(node)
        if  self.funcname.startswith("init_"):
            self.write("#%%CyML Init Begin%%")
            self.newline(node)
        self.write('def %s(' % node.name)
        for i, pa in enumerate(node.params):
            #if pa.type == "local": 
            if not isinstance(pa.pseudo_type, list):
                self.write("%s:%s"%(pa.name,pa.pseudo_type))
            elif isinstance(pa.pseudo_type, list):
                if pa.pseudo_type[0] not in ["dict", "array"] :
                    self.write("%s:%s[%s]"%(pa.name, pa.pseudo_type[0].capitalize(),  pa.pseudo_type[1]))
                elif pa.pseudo_type[0] == "dict": self.write("%s:%s[%s, %s]"%(pa.name, pa.pseudo_type[0].capitalize(),  pa.pseudo_type[1], pa.pseudo_type[2]))
                else: self.write("%s:'%s[%s]'"%(pa.name, pa.pseudo_type[0].capitalize(),  pa.pseudo_type[1]))
                
            if "value" in dir(pa) or "elements" in dir(pa) or "pairs" in dir(pa) :
                #self.write(pa.name)
                self.write(" = ")
                self.visit(pa)  
            if i!= (len(node.params)-1):
                self.write(',\n         ')
        self.write('):')
        self.newline(node)
        if self.model and node.name.startswith("model_") and node.name.split("model_")[1]==signature(self.model):
            self.write('    """\n')
            self.write(self.doc.header)
            self.newline(node)
            self.write(self.doc.desc)
            self.newline(node)
            self.write(self.doc.inputs_doc)
            self.newline(node)
            self.write(self.doc.outputs_doc)
            self.newline(node)
            self.write('    """\n')
            self.newline(node)
        self.body(node.block)
        if self.model and self.funcname.startswith("model_") and self.funcname.split("model_")[1]==signature(self.model):
            self.newline(node)
            self.write("#%%CyML Model End%%")
            self.newline(node)
        if self.funcname.startswith("init_"):
            self.newline(node)
            self.write("#%%CyML Init End%%")
            self.newline(node)
        #self.model = None
        
    def visit_implicit_return(self, node):
        self.newline(node)
        if node.value is None:
            self.write('return')
        else:
            self.write('return ')
        self.visit(node.value)


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl  : 
            if n.type in ("int", "float", "bool", "str") and "value" not in dir(n):
                self.newline(node)
                self.write("%s:%s"%(n.name, n.pseudo_type))       
            elif n.type in ("int", "float") and "value" in dir(n):
                self.newline(node)
                self.write("%s:%s"%(n.name, n.pseudo_type))
                self.write(" = ")                 
                self.visit(n.value) if isinstance(n.value, Node) else self.write(n.value)
            elif n.type=="bool" and "value" in dir(n):
                self.newline(node)
                self.write("%s:%s"%(n.name, n.pseudo_type))
                self.write(" = ") 
                self.visit(n.value) if isinstance(n.value, Node) else self.write(n.value.capitalize())      
            elif  n.type=="str" and "value" in dir(n):
                self.newline(node)
                self.write("%s:%s"%(n.name, n.pseudo_type))
                self.write(" = ") 
                #self.emit_string(n)   
                self.visit(n.value) if isinstance(n.value, Node) else self.emit_string(n)           
            elif n.type in ("list", "tuple"):
                self.newline(node)
                self.write("%s:%s[%s]"%(n.name, n.pseudo_type[0].capitalize(),  n.pseudo_type[1]))
                self.write(" = ") 
                if n.type=="list":                
                    self.visit_list(n) if "elements" in dir(n) else self.write("[]")
                else: self.visit_tuple(n)
                self.newline(node)
            elif 'args' in dir(n) and n.type=='datetime':
                self.newline(node)
                self.write("%s:%s"%(n.name, n.pseudo_type))
                self.write(" = datetime") 
                self.visit_datetime(n)               
            elif 'pairs' in dir(n) and n.type=="dict":
                self.newline(node)
                self.write("%s:%s[%s, %s]"%(n.name, n.pseudo_type[0].capitalize(),  n.pseudo_type[1], n.pseudo_type[2]))
                self.write(" = ")                 
                self.visit_dict(n)
            elif n.type=="array" and 'elements' in dir(n):
                    self.write("%s:'%s[%s]'"%(n.name, n.pseudo_type[0],  n.pseudo_type[1]))
                    self.write(" = array('%s',"%n.pseudo_type[1][0])
                    self.write("[")
                    self.comma_separated_list(n.elements)
                    self.write("] )") 
            elif n.type=="array" and 'elements' not in dir(n):
                if "elts" in dir(n) and n.elts:
                    c = n.pseudo_type[1][0]
                    self.write("%s:'%s[%s]'"%(n.name, n.pseudo_type[0],  n.pseudo_type[1]))
                    self.write(" = array('%s',"%n.pseudo_type[1][0])
                    self.write("[%s]*("%initVal(c))
                    self.visit(n.elts[0]) if isinstance(n.elts, list) else self.visit(n.elts)
                    self.write("))")   
                else:
                    self.write("%s:'%s[%s]'"%(n.name, n.pseudo_type[0],  n.pseudo_type[1]))           
                self.newline(node)
            elif n.type in ("list"):
                self.newline(node)
                self.write("%s:%s[%s]"%(n.name, n.pseudo_type[0].capitalize(),  n.pseudo_type[1]))
                self.write(" = []") 
                self.newline(node)

    def visit_array(self,node): 
        if hasattr(node, "elts"):
            type_ = node.pseudo_type[-1]
            newtype= newtype_func(type_)
            self.write("array('%s', [None]*"%newtype)
            self.visit(node.elts)            #one dimension array
            self.write(")")
            
            
        elif isinstance(node.elements, Node):
            if node.elements.type == "standard_call" and node.elements.function=="range":
                self.write("array('%s', range"%newtype_func(node.elements.args[0].pseudo_type))
                self.write("(")
                self.comma_separated_list(node.elements.args)
                self.write("))")
                
            else:
                type_ = node.elements.left.elements[0].type
                newtype= newtype_func(type_)
                self.write("array('%s', ["%newtype)
                self.visit(node.elements.left.elements[0])
                self.write(']*(')
                self.visit(node.elements.right)
                self.write("))")
        else:
            type_ = node.elements[0].type
            newtype= newtype_func(type_)
            self.write("array('%s',"%newtype)
            self.write("[")
            self.comma_separated_list(node.elements)
            self.write("])")

    def visit_continuestatnode(self, node):
        self.newline(node)
        self.write('continue')
        
    def visit_breakstatnode(self, node):
        self.newline(node)
        self.write('break')              
        
    def visit_call(self, node):
        want_comma = []
        def write_comma():
            if want_comma:
                self.write(', ')
            else:
                want_comma.append(True)
        if "attrib" in dir(node):
             self.write(u"%s.%s"%(node.namespace,self.visit(node.function)))
        else:
            self.write(self.visit(node.function))
        self.write('(')
        for arg in node.args:
            write_comma()
            self.visit(arg)
        self.write(')')
    
    def visit_standard_call(self, node):
        node.function = self.functions[node.namespace][node.function]
        if callable(node.function):
               self.visit(node.function(node)) 
        else: self.visit_call(node)  
        
    def visit_importfrom(self, node):
        if self.imp:
            self.newline(node)
            if node.namespace not in ["math", "array", "typing", "datetime"]:
                self.write('from %s import ' % (node.namespace))
                for idx, item in enumerate(node.name):
                    if idx:
                        self.write(', ')
                    self.write(item)
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.write("for ")
        if "iterators" in dir(node):
            self.visit(node.iterators) 
        if "sequences" in dir(node):
            self.visit(node.sequences)
        self.body(node.block)

    
    def visit_for_iterator_with_index(self, node):
        self.visit(node.index)
        self.write(' , ')
        self.visit(node.iterator)        

    def visit_for_sequence_with_index(self, node):
        
        self.write(" in enumerate(")
        self.visit(node.sequence)
        self.write('):')
    
    def visit_for_iterator(self, node):
        self.visit(node.iterator)
        self.write(" in ")
        
    def visit_for_sequence(self, node):
        self.visit(node.sequence)
        self.write(":")
        
        
    
    def visit_for_range_statement(self, node):
        self.newline(node)
        self.write("for ")
        self.visit(node.index)
        self.write(" in range(")
        self.visit(node.start)
        self.write(' , ')
        self.visit(node.end)
        self.write(' , ')
        self.visit(node.step)
        self.write('):')
        self.body(node.block)
        
    def visit_while_statement(self, node):
        self.newline(node)
        self.write('while ')
        self.visit(node.test)
        self.write(':')
        self.body_or_else(node)


class PythonCompo(PythonGenerator):
    """ This class generate the composite module in Python
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        PythonGenerator.__init__(self,tree, model, self.name)

class PythonSimulation(CodeGenerator):
    """[summary]

    Args:
        PythonCompo ([type]): [description]
    """

    def __init__(self, modelcomposite, package_name=''):
        """[summary]

        Args:
            modelcomposite (ModelComposite): [description]
        """
        self.modelcomposite = modelcomposite
        self.package_name = package_name if package_name else self.modelcomposite.name
        self.params = []
        self.variables = []
        self.stateInit = []
        self.outputs = []
        self.inputs = []
        for inp in self.modelcomposite.inputs:
            self.inputs.append(inp.name)
            if "parametercategory" in dir(inp):
                self.params.append(inp.name)
            if "variablecategory" in  dir(inp) and not inp.name.endswith("_t1"):
                self.variables.append(inp.name)
            if "variablecategory" in  dir(inp) and inp.name.endswith("_t1"):
                self.stateInit.append(inp.name)
        for out in self.modelcomposite.outputs:
            self.outputs.append(out.name)
        CodeGenerator.__init__(self)
    
    def generate(self):
        self.write("from . import %sComponent"%self.modelcomposite.name)
        self.newline(1)
        self.write("import pandas as pd")
        self.newline(1)
        self.write("import os")
        self.newline(extra=1)
        self.write("def simulation(datafile, vardata, params, init):")
        self.newline(1)
        self.indentation += 1
        self.write("rep = os.path.dirname(datafile)")
        self.newline(1)
        self.write("out = os.path.join(rep, 'output.csv')")
        self.newline(1)
        self.write('df = pd.read_csv(datafile, sep = ";")')


        self.newline(extra=1)
        self.write("# inputs values")
        for inp in self.variables:
            self.newline(1)
            self.write('t_%s = df[vardata.loc[vardata["Variables"]=="%s","Data columns"].iloc[0]].to_list()'%(inp, inp))
            
        
        self.newline(extra=1)
        self.write("#parameters")
        for pa in self.params:
            self.newline(1)
            self.write('%s = params.loc[params["name"]=="%s", "value"].iloc[0]'%(pa, pa))

        self.newline(extra=1)
        self.write("#initialization")
        for ini in self.stateInit:
            self.newline(1)
            self.write('%s = init.loc[init["name"]=="%s", "value"].iloc[0]'%(ini, ini))
        
        self.newline(extra=1)
        self.write("#outputs")   
        self.newline(1)
        self.write("output_names = [") 
        for out in self.outputs:
            self.write('"%s"'%out)
            if out!=self.outputs[-1]:
                self.write(",")
        self.write("]")
        self.newline(extra=1)

        self.write("df_out = pd.DataFrame(columns = output_names)")
        self.newline(1)
        self.write("for i in range(0,len(df.index)-1):")
        self.newline(1)
        self.indentation +=1
        for inp in self.variables:
            self.write("%s = t_%s[i]"%(inp, inp))
            self.newline(1)
        
        self.newline(1)
        for out in self.outputs:
            self.write(out)
            if out!=self.outputs[-1]:
                self.write(",")
        self.write("= %sComponent.model_%s("%(self.modelcomposite.name,self.modelcomposite.name.lower() ))
        
        for inp in self.inputs:
            self.write(inp)
            if inp!=self.inputs[-1]:
                self.write(",")
        self.write(")")
        self.newline(extra=1)

        for inp in self.stateInit:
            self.write("%s = %s"%(inp, inp.split("_t1")[0]))
            self.newline(1)
        
        self.newline(1)
        self.write("df_out.loc[i] = [")
        for out in self.outputs:
            self.write(out)
            if out!=self.outputs[-1]:
                self.write(",")
        self.write("]")

        self.newline(1)
        self.indentation -=1

        self.write("df_out.insert(0, 'date', pd.to_datetime(df.year*10000 + df.month*100 + df.day, format='%Y%m%d'), True)")
        self.newline(1)
        self.write('df_out.set_index("date", inplace=True)')
        self.newline(1)
        self.write('df_out.to_csv(out, sep=";")')
        self.newline(1)
        self.write("return df_out")
    
    def generate_setup(self):
        self.write("import setuptools")
        self.newline(1)
        self.write("setuptools.setup(name='%s',"%self.package_name)
        self.newline(1)
        self.write("version='0.1',")
        self.newline(1)
        self.write("description='%s',"%self.modelcomposite.description.Abstract)
        self.newline(1)
        self.write("url='#',")
        self.newline(1)
        self.write("author='%s',"%self.modelcomposite.description.Authors)
        self.newline(1)
        self.write("install_requires=['opencv-python'],")
        self.newline(1)
        self.write("author_email='',")
        self.newline(1)
        self.write("packages=setuptools.find_packages(),")
        self.newline(1)
        self.write("zip_safe=False)")
        self.newline(1)

    def generate_pyproject(self):
        # use setuptools
        self.write('[build-system]')
        self.newline(1)
        self.write('requires = ["setuptools>=61", "setuptools_scm[toml]>=7"]')
        self.newline(1)
        self.write('build-backend = "setuptools.build_meta"')
        self.newline(1)

        # project metainformation
        self.write('[project]')
        self.newline(1)
        self.write(f'name = "{self.package_name}"')
        self.newline(1)
        self.write('authors = [{name = "%s"}]'%(self.modelcomposite.description.Authors))
        self.newline(1)
        self.write(f'description="{self.modelcomposite.description.Abstract}"')
        self.newline(1)
        self.write('version="0.1"')
        self.newline(1)

        # project dependencies
        self.write('dependencies = ["pandas","numpy"]')
        self.newline(1)


def newtype_func(type_):
    if type_=="int" or type_=="bool": newtype="i"
    elif type_=="float": newtype="f"
    elif type_=="str": newtype="u"
    return newtype
        











            
        
