from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.csharpRules import types, csharpOP

class CsharpGenerator(CodeGenerator):
    """ This class contains the specific properties of
    Csharp language and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
    """
    
    def __init__(self):
        super().__init__(indent_with=' '*4)
        self.write(u"using System;\nusing System.Collections.Generic;\n")
         
    def visit_import(self, node):
        pass
        
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

    def visit_elseif_statement(self, node):
        self.newline()
        self.write('elseif ( ')
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
        self.write("d")
   
    def visit_standard_method_call(self, node):
        if not node.args:
            self.write(node.message)
            self.write('(')
            self.visit(node.receiver)
            self.write(')')
        else:
            pass
                         
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

    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(op, 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(u" %s " % csharpOP[op].replace('_', ' '))
        self.visit(node.right)
        self.operator_exit()
    
    def visit_assignment(self, node):
        self.newline(node)
        self.visit(node.target)
        self.write(' = ')
        self.visit(node.value) 
        self.write(";")
         
    def visit_function_definition(self, node):
        self.write("public class Program")
        self.newline(node)
        self.write("{")
        self.indentation += 1        
        self.newline(node)
        self.body("")        
        self.write('static %s %s(' %(node.return_type, node.name))
        for i, pa in enumerate(node.params):
            self.write('%s '%pa.pseudo_type)
            self.visit(pa)
            if i!= (len(node.params)-1):
                self.write(',')
        self.write(')')
        self.newline(node)
        self.write('{')            
        self.body(node.block)
        self.newline(node)
        self.write('}') 
        self.newline(node)
        self.indentation -= 1 
        self.write('}')         
        
    def visit_implicit_return(self, node):
        self.newline(node)
        if node.value is None:
            self.write('return')
        else:
            self.write('return ')
        self.visit(node.value)
        self.write(";")
    
    def sequence_visit(left, right):
        def visit(self, node):
            self.write(left)
            for idx, item in enumerate(node.elements):
                if idx:
                    self.write(', ')
                self.visit(item)
            self.write(right)
        return visit

    visit_list = sequence_visit('[', ']')
    del sequence_visit

    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            self.newline(node)
            if 'value' not in dir(n) and n.type not in ("list", "tuple"):
                self.write('%s %s;'%(types[n.type],n.name)) 
            if 'elements' not in dir(n) and n.type=="list":
                self.write("var %s = new List()"%n.name)
            if 'value' in dir(n) and n.type in ("int", "float"):
                self.write('%s %s'%("double" if n.type=="float" else "int",n.name))
                self.write(" = ")
                self.write(n.value if n.type=="int" else "%sd"%n.value)
                self.write(";")
            elif 'value' in dir(n) and n.type=="str": 
                self.write('%s %s'%("String",n.name))
                self.write(n.name)
                self.write(" = ")
                self.emit_string(n) 
                self.write(";")
            elif 'elements' in dir(n) and n.type=="list":
                self.write('%s<%s> %s= new %s<%s>'%(types[n.type], n.pseudo_type[1],n.name, types[n.type], n.pseudo_type[1] ))
                self.write(u'{')
                self.comma_separated_list(n.elements)
                self.write(u'};')
             
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
        self.visit_call(node)  
        
    def visit_importfrom(self, node):
        pass
    
    def visit_for_statement(self, node):
        self.newline(node)
        self.write("foreach(")
        if "iterators" in dir(node):
            self.visit(node.iterators) 
        if "sequences" in dir(node):
            self.visit(node.sequences)
            self.write(')')
        self.newline(node)
        self.write('{')   
        self.body(node.block)
        self.newline(node)
        self.write('}')  
          
    def visit_for_iterator_with_index(self, node):
        self.visit(node.index)
        self.write(' , ')
        self.visit(node.iterator)        

    def visit_for_sequence_with_index(self, node):     
        
        """self.write(" in enumerate(")
        self.visit(node.sequence)
        self.write('))')"""

    
    def visit_for_iterator(self, node):
        self.write("%s "%node.iterator.pseudo_type)
        self.visit(node.iterator)
        self.write(" in ")
           
    
    def visit_for_range_statement(self, node):
        self.newline(node)
        self.write("for (")
        self.visit(node.index)
        self.write("=")
        self.visit(node.start)
        self.write(' , ')
        self.visit(node.index)
        self.write("<")        
        self.visit(node.end)
        self.write(' , ')
        self.visit(node.index)
        self.write("+=")         
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

  
        
