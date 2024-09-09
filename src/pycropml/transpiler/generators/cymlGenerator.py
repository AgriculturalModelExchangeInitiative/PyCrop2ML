# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.cymlRules import CymlRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
import os
from pycropml.render_cyml import signature
from pycropml.transpiler.pseudo_tree import Node

class CymlGenerator(CodeGenerator, CymlRules):
    """This class contains the specific properties of 
    python language and use the NodeVisitor to generate a python
    code source from a well formed syntax tree.
    """
    def __init__(self, tree, model=None, name = None):
        CodeGenerator.__init__(self)
        CymlRules.__init__(self)
        self.tree=tree
        self.model=model
        self.name = name
        self.indent_with=' '*4 
        self.imp=True
        self.arrVar = {}
        if self.model: 
            self.doc=DocGenerator(self.model, " ")

    def comment(self,doc):
        list_com = [self.indent_with + '#'+x for x in doc.split('\n')]
        com = '\n'.join(list_com)
        return com
    
    def visit_import(self, node):
        if self.imp:
            if isinstance(node.module, list):
                self.write(u"import ")
                for n in node.module:
                    self.write("%s" %n)
                    if n!=node.module[-1]: self.write(",")
            else:  self.write(u"import %s"%node.module)
        self.newline(node)
                
    
    def visit_main(self, node):
        self.write("def main():")
        self.newline(node)
        self.indentation +=1
        self.visit(node.body)
        self.newline(node)

    def visit_notAnumber(self, node):
        self.write("float('nan')")

    def visit_local(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.name,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.name,node.units))
        else: self.write(node.name)

    def visit_int(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.value,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.value,node.units))
        else:self.write(node.value)


    def visit_assignment(self, node):
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
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
            self.write(node.op)
            if isinstance(node.target.pseudo_type, list) and node.value.pseudo_type!="Void" and "elements" in dir(node.value) and "left" in dir(node.value.elements):
                self.write('[')
                self.visit(node.value.elements.left.elements[0])
                self.write(']*(')
                if "right" in dir(node.value.elements) and isinstance(node.value.elements.right[0], Node):
                    self.visit(node.value.elements.right[0])
                else: self.visit(self.arrVar[node.target.name])
                self.write(')')
                self.newline(node)
            else:
                self.visit(node.value)
                self.newline(node)

    def visit_cond_expr_node(self, node):
        self.visit(node.true_val)
        self.write(u" if ")
        self.visit(node.test)
        self.write(u" else ")
        self.visit(node.false_val)  
        
    def visit_constant(self, node):
        self.write(self.constant[node.library][node.name])
    
    def visit_none(self, node):
        self.write("None")

    def visit_if_statement(self, node):
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
        self.newline(node)
        self.write('if ')
        if node.test.right.type=="none" and node.test.op=="==":
            self.visit(node.test.left)
            self.write(" is None")
        else: self.visit(node.test)
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
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
        self.newline(node)
        self.write('elif ')
        self.visit(node.test)
        self.write(':')
        self.body(node.block)

    def visit_else_statement(self, node):
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
        self.newline(node)
        self.write('else:')
        self.body(node.block)
    
    def visit_float(self, node):
        if "units" in dir(node):
            self.write("%s%s"%(node.value,node.units)) if node.units[0]=='/' else self.write("%s*%s"%(node.value,node.units))
        else: self.write(node.value)
        
    def visit_bool(self, node):
        self.write(str(node.value))

    def visit_str(self, node):
        self.safe_double(node)

    def visit_string(self, node):
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
        if "type" in dir(node.elements) and node.elements.type == "binary_op":     
            self.visit(node.elements.left.elements[0])
        else:
            self.emit_sequence(node.elements, u"[]")

    def visit_datetime(self, node):
        self.write("datetime")
        self.emit_sequence(node.value, u"()")

    def visit_standard_method_call(self, node):
        l = node.receiver.pseudo_type
        if isinstance(l, list):
            l = l[0]
        z = self.methods[l][node.message]
        if node.message == "allocate":
            self.arrVar[node.receiver.name] = node.args
        if callable(z):
            self.visit(z(node))
        
        else:
            if len(node.args)==1 and node.args[0] is None: node.args = []
            if not node.args :
                self.write(z)
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
        if "type" in dir(node.index) and isinstance(node.index.type, tuple):
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
        if node.message == "slice_":
            self.write(u":")
        self.write(u"]")


    def visit_module(self, node):
        self.newline(extra=1)
        if node.comments:
            self.translate_com(node.comments)
        self.visit(node.body)
    
    def translate_com(self, comments):
        if isinstance(comments, list):
            for n in comments:
                self.write("#%s"%n[1:])
                self.newline(1)
        else: 
            self.write(f"#{comments[1:]}")
    
    def visit_comments(self, node):
        self.newline(node)
        self.translate_com(node.comments)

    
    def visit_comparison(self, node):
        #self.write('(')
        self.visit_binary_op(node)
        #self.write(')')

    def visit_method_call(self, node):
        "%s.%s"%(self.visit(node.receiver),self.write(node.message))  
              
    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(str(op), 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(u" %s " % self.binary_op[str(op)].replace('_', ' '))
        if "type" in dir(node.right):
            if node.right.type=="binary_op" and  self.binop_precedence.get(str(node.right.op), 0) >= prec : #and node.right.op not in ("+","-") :
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
        prec = self.unop_precedence[str(op)]
        self.operator_enter(prec)
        self.write(u"%s" % self.unary_op[str(op)])
        self.visit(node.value)
        self.operator_exit()

    def visit_function_definition(self, node):
        self.arrVar = {}
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
        self.newline(extra=1)
        self.newline(node)
        self.write('def %s(' % node.name)
        for i, pa in enumerate(node.params):
            if isinstance(pa.pseudo_type, str):
                self.write("%s %s"%(pa.pseudo_type, pa.name))
            elif pa.pseudo_type[0]=="array" and "elts" in dir(pa):
                if isinstance(pa.elts[0], str): self.write("%s %s[]"%(pa.pseudo_type[-1], pa.name))
                else: 
                    x = pa.elts[0].name if "name" in dir(pa.elts[0]) else pa.elts[0].value
                    self.write("%s %s[%s]"%(pa.pseudo_type[-1], pa.name, x))
                    self.arrVar[pa.name] = pa.elts[0]
            else:
                self.write("%s %s"%(pa.pseudo_type[-1]+pa.pseudo_type[0],pa.name))
            if i!= (len(node.params)-1):
                self.write(',\n         ')
        self.write('):')
        self.newline(node)
        if self.model and node.name.split("model_")[1]==signature(self.model):
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
            self.model = None
        self.body(node.block)
        self.arrVar = {}
        
    def visit_implicit_return(self, node):
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
        self.newline(node)
        if node.value is None:
            self.write('return')
        else:
            self.write('return ')
        self.visit(node.value)

    def visit_declaration(self, node):
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)    
        if node.decl[0].type=="list" and ("elements" not in dir(node.decl[0]) or not node.decl[0].elements):
            self.write("cdef %s "%(node.decl[0].pseudo_type[1].lower() + node.decl[0].pseudo_type[0]))
        elif node.decl[0].type == "array"and "elements" not in dir(node.decl[0]):
            if "elts" not in dir(node.decl[0]):
                self.write("cdef %s "%(node.decl[0].pseudo_type[-1])) 
            else:
                self.write("cdef %s "%(node.decl[0].pseudo_type[-1]))
        else:
            self.write("cdef %s "%node.decl[0].type)
            
        for p, n in enumerate(node.decl) :           
            if 'value' in dir(n) and n.type in ("int", "float", "double"):
                self.write("%s = "%(n.name))               
                self.visit(n.value) if isinstance(n.value, Node) else self.write(n.value)
            elif 'value' in dir(n) and n.type=="bool":
                self.write("%s = "%(n.name))
                self.write(str(n.value))        
            elif 'value' in dir(n) and n.type=="str":
                self.write("%s = "%(n.name))
                self.emit_string(n)   
            elif 'value' not in dir(n) and n.type in ("int", "float", "str", "bool"): 
                self.write("%s "%(n.name))           
            elif 'elements' in dir(n) and n.elements and n.type in ("list", "tuple"):
                self.write("%s = "%(n.name)) 
                if n.type=="list":                
                    self.visit_list(n)
                else: self.visit_tuple(n)
            elif 'args' in dir(n) and n.type=='datetime':
                self.write("%s = datetime"%(n.name))
                self.visit_datetime               
            elif 'pairs' in dir(n) and n.type=="dict":
                self.write("%s = "%(n.name))               
                self.visit_dict(n)
            elif n.type=="array" and 'elements' in dir(n):
                if n.dim == 1:
                    self.write("%s "%(n.name))
                    self.write(" = array('%s',"%n.pseudo_type[1][0])
                    self.write("[")
                    self.comma_separated_list(n.elements)
                    self.write("] )")                    
            elif n.type in ("list"):
                self.write(" %s"%(n.name))   
            elif n.type == "array" :
                if "elts" not in dir(n):
                    self.write("%s[]"%( n.name)) 
                else:
                    self.write("%s["%(n.name))
                    self.comma_separated_list(n.elts) if isinstance(n.elts, list) else self.visit(n.elts)
                    self.write("]")
                    if n.elts and len(n.elts)>=1: self.arrVar[n.name] = n.elts[0]   
            else:
                pass
            if p!= len(node.decl)-1:
                self.write(", ")



    def visit_array(self,node): 
        if hasattr(node, "elts"):
            type_ = node.pseudo_type[-1]
            if type_=="int" or type_=="bool": 
                newtype="i"
                self.write("array('%s', [0]*"%newtype)
            if type_=="float": 
                newtype="f"
                self.write("array('%s', [0.0]*"%newtype)
            if type_=="str": 
                newtype="u"
                self.write("array('%s', [None]*"%newtype) # to check
            
            self.visit(node.elts)            #one dimension array
            self.write(")")
            
        elif isinstance(node.elements, Node):
            type_ = node.elements.left.elements[0].type
            if type_=="int" or type_=="bool": newtype="i"
            if type_=="float": newtype="f"
            if type_=="str": newtype="u"
            self.write("array('%s', ["%newtype)
            self.visit(node.elements.left.elements[0])
            self.write(']*')
            self.visit(node.elements.right)
            self.write(")")
        else:
            type_ = node.elements[0].type
            if type_=="int" or type_=="bool": newtype="i"
            if type_=="float": newtype="f"
            if type_=="str": newtype="u"
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
            self.write(node.function)
        self.write('(')
        if node.args:
            if isinstance(node.args, list):
                for arg in node.args:
                    write_comma()
                    self.visit(arg)
            else:
                self.write(node.args)
        self.write(')')
    
    def visit_standard_call(self, node):
        node.function = self.functions[node.namespace][node.function]
        if callable(node.function):
               self.visit(node.function(node)) 
        else: self.visit_call(node)  
        
    def visit_importfrom(self, node):
        if self.imp:
            self.newline(node)
            if node.namespace in ["math", "typing"] :
                self.write("from %s import *"%node.namespace)  
            else:
                self.write('from %s import ' % (node.namespace))
                for idx, item in enumerate(node.name):
                    if idx:
                        self.write(', ')
                    self.write(item)
            self.newline(node)
    
    def visit_for_statement(self, node):
        self.newline(node)
        if node.comments:
            self.translate_com(node.comments)
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
        if node.comments:
            self.translate_com(node.comments)
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
        if node.comments:
            self.translate_com(node.comments)
        self.newline(node)
        self.write('while ')
        self.visit(node.test)
        self.write(':')
        self.body_or_else(node)


class CymlCompo(CymlGenerator):
    """ This class generate the composite module in Cyml
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        CymlGenerator.__init__(self,tree, model, self.name)
            
        
