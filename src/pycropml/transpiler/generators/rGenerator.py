# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.rRules import RRules, changetyp
from pycropml.transpiler.generators.docGenerator import DocGenerator
import os
from pycropml.render_cyml import signature
from path import Path
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree

class RGenerator(CodeGenerator, RRules):
    """This class contains the specific properties of 
    R language and use the NodeVisitor to generate a R
    code source from a well formed syntax tree.
    """
    def __init__(self, tree, model=None, name = None):
        CodeGenerator.__init__(self)
        RRules.__init__(self)
        self.tree=tree
        self.model=model
        self.name = name
        self.indent_with=' '*4 
        self.imp=True
        self.index=[]
        self.funcname=None
        self.write("library(gsubfn)")
        self.newline(1)
        if self.model: 
            self.doc= DocGenerator(model, "#'")

    def comment(self,doc):
        list_com = [self.indent_with + '#'+x for x in doc.split('\n')]
        com = '\n'.join(list_com)
        return com
    
    def visit_import(self, node):
        pass

    def visit_notAnumber(self, node):
        self.write("NaN")

    def visit_assignment(self, node):
        self.newline(node)
        self.visit(node.target)
        self.write(' <- ')
        self.visit(node.value)

    def visit_constant(self, node):
        self.write(self.constant[node.library][node.name]) 

    def visit_cond_expr_node(self, node):
        self.write(u" if (")
        self.visit(node.test)
        self.write(")")
        self.visit(node.true_val)
        self.write(u" else ")
        self.visit(node.false_val) 
        

    def visit_if_statement(self, node):
        self.newline(node)
        self.write('if (')
        self.visit(node.test)
        self.write(')')
        self.newline(node)
        self.write('{')
        self.body(node.block)
        self.newline(node)
        self.write('}')
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

    def visit_float(self, node):
        self.write(node.value)
        
    def visit_bool(self, node):
        self.write(str(node.value).upper())

    def visit_str(self, node):
        self.emit_string(node)
        #self.write("%s"%str(node.value))
    
    def visit_tuple(self, node):
        self.write("list[")
        for n in node.elements:
            self.write(n.name)
            if n!=node.elements[len(node.elements)-1]:
                self.write(", ")
        self.write("]")  
              
    def visit_pair(self, node):
        self.visit(node.key)
        self.write(u": ")
        self.visit(node.value)         

    def visit_ExprStatNode(self, node):
        self.newline(node)
        self.visit(node.expr)
    
    def visit_list(self, node):
        if len(node.elements)==0: return self.write("vector()")
        self.write("c")
        self.emit_sequence(node.elements, u"()")

    def visit_datetime(self, node):
        self.write("'%s/%s/%s'"%(node.value[0].value,node.value[1].value,node.value[2].value))
    
    def visit_standard_method_call(self, node):
        l = node.receiver.pseudo_type
        if isinstance(l, list):
            l = l[0]
        z = self.methods[l][node.message]        
        if callable(z):
            self.visit(z(node))
        else:
            if not node.args:
                self.write(z)
                self.write('(')
                self.visit(node.receiver)
                self.write(')')
            else:
                "%s.%s"%(self.visit(node.receiver),self.write(z))
                self.write("(")
                self.comma_separated_list(node.args)
                self.write(")")
                
    def visit_standard_call(self, node):
        node.function = self.functions[node.namespace][node.function]
        self.visit_call(node) 


    def visit_index(self, node):
        self.visit(node.sequence)
        self.write(u"[")
        if isinstance(node.index.type, tuple):
            self.emit_sequence(node.index)
            self.write(u"]") 
        else:
                if node.index.type=='standard_method_call':
                    self.visit(node.index)
                    if node.index.message=="index" :
                        self.write(u"]")
                elif node.index.type=="int":
                    z=int(node.index.value)+1
                    if z!=0: self.write(str(z))
                    if int(node.index.value)<0:
                        if z!=0: self.write("%z +")
                        self.write(" SIZE(%s)"%node.sequence.name)
                    self.write(u"]")
                else:
                    self.visit(node.index)
                    self.write("+1]")
        
    
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
        self.visit(node.body)

        
    def visit_comparison(self, node):
        #self.write('(')
        self.visit_binary_op(node)
        #self.write(')')

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
        self.write('%s <- function (' % node.name)
        for i, pa in enumerate(node.params): 
            self.write(pa.name)
            if "value" in dir(pa) or "elements" in dir(pa) or "pairs" in dir(pa) :
                self.write(" = ")
                self.visit(pa)  
            if i!= (len(node.params)-1):
                self.write(',\n         ')
        self.write('){')
        self.newline(node)
        if self.model and  node.name.startswith("model_") and node.name.split("model_")[1]==signature(self.model):
            self.write(self.doc.header)
            self.newline(node)
            self.write(self.doc.desc)
            self.newline(node)
            self.write(self.doc.inputs_doc)
            self.newline(node)
            self.write(self.doc.outputs_doc)
            self.newline(node)
            self.model = None
        self.body(node.block)
        self.newline(node)
        self.write("}")

    def visit_implicit_return(self, node):
        self.newline(node)
        if node.value is None:
            pass
        elif node.value.type=="tuple": 
            self.write("return (list (")
            self.multValreturn(node.value.elements)
            self.write("))")
        else:
            if self.funcname.startswith("model"):
                self.write("return (list('%s' = %s))"%(node.value.name, node.value.name))                
            else:
                self.write('return( ')
                self.visit(node.value)
                self.write(')')

    def multValreturn(self, node):
        for n in node:
            self.write('"%s" = %s'%(n. name, n.name))
            if n!=node[len(node)-1]:
                self.write(",")

    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl  :           
            if 'value' in dir(n) and n.type in ("int", "float"):
                self.newline(node)
                self.write(n.name)
                self.write(" <- ")                 
                self.write(n.value)
            elif 'value' in dir(n) and n.type=="bool":
                self.newline(node)
                self.write(n.name)
                self.write(" <- ") 
                self.write(str(n.value).upper())        
            elif 'value' in dir(n) and n.type=="str":
                self.newline(node)
                self.write(n.name)
                self.write(" <- ") 
                self.emit_string(n) 
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                self.newline(node)
                self.write(n.name)
                self.write(" <- ") 
                if n.type=="list":                
                    self.visit_list(n)
                else: self.visit_tuple(n)
            elif "elts" in dir(n) and n.type=='datetime':
                self.newline(node)
                self.write(n.name)
                self.write(" <- ") 
                self.visit(n.elts)               
            elif n.type=="array" and 'elements' in dir(n):       
                self.visit_array(n)
            elif n.type in ("list", "array"):
                self.newline(node)
                self.write(n.name)
                if n.type=="list": self.write(" <- vector()")   
                if n.type=="array": 
                    typ = n.pseudo_type[-1]
                    newtyp = changetyp(typ)
                    if "elts" in dir(n) and n.elts:
                        self.write(" <- vector(,")   
                        self.visit(n.elts[0])
                        self.write(")")
                    else:
                        
                        self.write("<- vector()")
    
    def visit_empty(self, node):
        pass              


    def visit_array(self,node): 
        if node.elements.type != "list":
            self.write(" rep(")  
            self.visit(node.elements.left.elements[0])
            self.write(",")
            self.visit(node.elements.right) 
            self.write(")")            
        else: 
            self.write("c(")
            self.comma_separated_list(node.elements)
            self.write(")")

    
    
    def visit_none(self, node):
        self.write("NULL") 


    def visit_continuestatnode(self, node):
        self.newline(node)
        self.write('next')
        
    def visit_breakstatnode(self, node):
        self.newline(node)
        self.write('break')              
    
    def visit_importfrom(self, node):
        pass
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.write("for( ")
        if "iterators" in dir(node):
            self.visit(node.iterators) 
        if "sequences" in dir(node):
            self.visit(node.sequences)
            self.write(')')
            self.newline(node)
        self.newline(node)
        self.write('{')
        self.body(node.block)
        self.write('}')

    def visit_for_iterator_with_index(self, node):
        self.visit(node.index)
        self.write(' , ')
        self.visit(node.iterator)        

    def visit_for_sequence_with_index(self, node):
        
        self.write(" in enumerate(")
        self.visit(node.sequence)
        self.write('){')
    
    def visit_for_iterator(self, node):
        self.visit(node.iterator)
        self.write(" in ")
        
    def visit_for_sequence(self, node):
        self.visit(node.sequence)
        self.write(":")
        
    
    def visit_for_range_statement(self, node):
        self.newline(node)
        self.index.append(node.index.name)
        self.write("for( ")
        self.visit(node.index)
        self.write(" in seq(")
        self.visit(node.start)
        self.write(", ")
        self.visit(node.end)
        if node.step.type=='unary_op' and node.step.operator=="-":
            self.write("+1")
        else: self.write("-1") 
        self.write(', ')
        self.visit(node.step)
        self.write(')){')
        self.body(node.block)
        self.newline(node )
        self.write('}')
        
    def visit_while_statement(self, node):
        self.newline(node)
        self.write('while( ')
        self.visit(node.test)
        self.write('){')
        self.body_or_else(node)
        self.write('}')


class RCompo(RGenerator):
    """ This class used to generates states, rates and auxiliary classes
        for C# languages.
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        RGenerator.__init__(self,tree, model, self.name)
        x = os.path.split(self.model.aPath)[0]
        z=x.split('\\')#.pop()
        z.pop()
        sourcePath = "/".join(z)+"/src/r"
        self.write("library (gsubfn) ")
        self.newline()
        self.write("setwd('%s')"%sourcePath)
        self.newline()
        for m in self.model.model:
            self.write("source('%s.r')"%m.name.lower().capitalize())
            self.newline()

    def visit_tuple(self,node):
        self.write("list[")
        for n in node.elements:
            self.write(n.name)
            if n!=node.elements[len(node.elements)-1]:
                self.write(", ")
        self.write("]")           
        
