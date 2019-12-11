# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.pythonRules import PythonRules
from pycropml.transpiler.generators.docGenerator import DocGenerator
import os
from pycropml.render_cyml import signature
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree

class CheckGenerator(CodeGenerator, PythonRules):
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
        #self.indent_with=' '*4 
        self.imp=True
        if self.model: 
            self.doc=DocGenerator(self.model, " ")
    
    def visit_import(self, node):
        pass

    def visit_local(self, node):
        if 'unit' in dir(node):
            self.write(node.unit)
        else: self.write(node.name)

    def visit_notAnumber(self, node):
        pass

    def visit_assignment(self, node):
        if "value" not in dir(node.value):
            self.newline(node)
            self.visit(node.target)
            self.write(' == ')
            self.visit(node.value)

    def visit_cond_expr_node(self, node):
        self.visit(node.true_val)
        self.visit(node.test)
        self.visit(node.false_val)  
        

    def visit_if_statement(self, node):
        self.newline(node)
        self.visit(node.test)
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
        self.visit(node.test)
        self.body(node.block)

    def visit_else_statement(self, node):
        self.newline()
        self.body(node.block)
    
    def visit_float(self, node):
        self.write(node.value)
        
    def visit_bool(self, node):
        self.write(node.value)

    def visit_str(self, node):
        self.write(node.value)
    
    def visit_tuple(self, node):
        pass
        
    def visit_dict(self, node):
        pass
        
    def visit_pair(self, node):
        pass        

    def visit_ExprStatNode(self, node):
        self.newline(node)
        self.visit(node.expr)
    
    def visit_list(self, node):
        pass

    def visit_datetime(self, node):
        pass

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
        pass
    
    def visit_sliceindex(self, node):
        pass


    def visit_module(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.write("# coding: utf8")
        self.newline(node)
        self.visit(node.body)

        
    def visit_comparison(self, node):
        if "value" not in dir(node.right):
            #self.write('(')
            self.visit_binary_op(node)
            #self.write(')')

    def visit_method_call(self, node):
        pass 
              
    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(op, 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(u" %s " % self.binary_op[op].replace('_', ' '))
        if "type" in dir(node.right):
            if node.right.type=="binary_op" and node.right.op not in ("+","-") :
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
        self.body(node.block)
        
    def visit_implicit_return(self, node):
        pass

    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl  :           
            if 'value' in dir(n) and n.type in ("int", "float"):
                self.newline(node)
                self.write(n.name)
                self.write(" = ")                 
                self.write(n.value)
            elif 'value' in dir(n) and n.type=="bool":
                self.newline(node)
                self.write(n.name)
                self.write(" = ") 
                self.write(str(n.value))        
            elif 'value' in dir(n) and n.type=="str":
                self.newline(node)
                self.write(n.name)
                self.write(" = ") 
                self.emit_string(n)                
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                self.newline(node)
                self.write(n.name)
                self.write(" = ") 
                if n.type=="list":                
                    self.visit_list(n)
                else: self.visit_tuple(n)
            elif 'args' in dir(n) and n.type=='datetime':
                self.newline(node)
                self.write(n.name)
                self.write(" = datetime") 
                self.visit_datetime               
            elif 'pairs' in dir(n) and n.type=="dict":
                self.newline(node)
                self.write(n.name)
                self.write(" = ")                 
                self.visit_dict(n)
            elif n.type=="array" and 'elements' in dir(n):       
                self.visit_array(n)
            elif n.type in ("list", "array"):
                self.newline(node)
                self.write(n.name)
                self.write(" = []")                  


    def visit_array(self,node): 
        self.write(node.name)


    def visit_continuestatnode(self, node):
        pass
        
    def visit_breakstatnode(self, node):
        pass              
        
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
        self.visit_call(node) 
        
    def visit_importfrom(self, node):
        pass
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.body(node.block)

    
    def visit_for_iterator_with_index(self, node):
        pass       

    def visit_for_sequence_with_index(self, node):
        pass
    
    def visit_for_iterator(self, node):
        pass
        
    def visit_for_sequence(self, node):
        pass
        
        
    
    def visit_for_range_statement(self, node):
        pass
        
    def visit_while_statement(self, node):
        self.visit(node.test)
        self.body_or_else(node)


class CheckCompo(CheckGenerator):
    """ This class used to generates states, rates and auxiliary classes
        for C# languages.
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        CheckGenerator.__init__(self,tree, model, self.name)
            
        
