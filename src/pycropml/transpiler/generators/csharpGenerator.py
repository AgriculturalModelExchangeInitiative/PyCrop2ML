# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.rules.csharpRules import CsharpRules
from pycropml.transpiler.generators.docGenerator import DocGenerator

class CsharpGenerator(CodeGenerator,CsharpRules):
    """ This class contains the specific properties of
    Csharp language and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree, model=None):
        CodeGenerator.__init__(self)
        CsharpRules.__init__(self)
        self.tree = tree
        self.model=model
        self.indent_with=' '*4
        self.write(u"using System;\nusing System.Collections.Generic;\n")
        if self.model: self.doc= DocGenerator(model, '//')  
        
    

         
    def visit_import(self, node):
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
        self.write("d")

    def visit_array(self, node):
        self.write("new []")        
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
        self.write("true") if node.value==True else self.write("false")
   
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

            
    
    def visit_method_call(self, node):
        "%s.%s"%(self.visit(node.receiver),self.write(node.message))
        
                                
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
    
    def visit_assignment(self, node):
        self.newline(node)
        self.visit(node.target)
        self.write(' = ')
        self.visit(node.value) 
        self.write(";")
         
    def visit_function_definition(self, node):
        self.write("public class %s"%node.name.capitalize())
        self.newline(node)
        self.write("{")
        self.indentation += 1        
        self.newline(node)
        self.body("")        
        self.write("public static ")
        self.visit_decl(node.return_type)
        self.write(" %s("%node.name)
        for i, pa in enumerate(node.params):
            self.visit_decl(pa.pseudo_type)
            self.write(" ")
            self.visit(pa)
            if i!= (len(node.params)-1):
                self.write(',')
        self.write(')')
        self.newline(node)
        self.write('{') 
        self.newline(node)
        if self.model:
            self.write(self.doc.desc)
            self.newline(node)
            self.write(self.doc.inputs_doc)
            self.newline(node)
            self.write(self.doc.outputs_doc)
            self.newline(node) 
        self.body(node.block)
        self.newline(node)
        self.write('}') 
        self.newline(node)
        self.indentation -= 1 
        self.write('}')  
    
    def visit_custom_call(self, node):
        "TODO"
        self.visit_call(node)
        self.write(".result")
        
        
    def visit_implicit_return(self, node):
        self.newline(node)
        if node.value is None:
            self.write('return')
        else:
            self.write('return ')
        self.visit(node.value)
        self.write(";")
    
    def visit_list(self, node):
        self.write("new ")
        self.visit_decl(node.pseudo_type)
        self.write(u'{')
        self.comma_separated_list(node.elements)
        self.write(u'}')
    
    def visit_tuple(self,node):
        self.write("Tuple.Create(")
        self.comma_separated_list(node.elements)
        self.write(")")
    
    def visit_str(self, node):
        self.safe_double(node)


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            self.newline(node)
            if 'value' not in dir(n) and n.type not in ("list", "tuple", "dict"):
                self.write('%s %s;'%(self.types[n.type],n.name)) 
            if 'elements' not in dir(n) and n.type=="list":
                self.write("var %s = new List()"%n.name)
            if 'value' in dir(n) and n.type in ("int", "float", "str", "bool"):
                self.write("%s %s"%(self.types[n.type], n.name))
                self.write(" = ")
                self.visit(n)
                self.write(";")
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                if n.type=="list":
                    self.visit_decl(n.pseudo_type)
                    self.write(n.name)
                    self.write(" = new ") 
                    self.visit_decl(n.pseudo_type)
                if n.type=='tuple':
                    pass
                self.write(u'{')
                self.comma_separated_list(n.elements)
                self.write(u'};')
            elif 'pairs' in dir(n) and n.type=="dict":
                self.visit_decl(n.pseudo_type)
                self.write(n.name)
                self.write(" = new ") 
                self.visit_decl(n.pseudo_type)               
                self.write(u'{')
                self.comma_separated_list(n.pairs)
                self.write(u'};')
                
        self.newline(node)
    
    def visit_list_decl(self, node):        
        if not isinstance(node[1], list):
            self.write(self.types[node[1]])
            self.write('>')
        else:
            node = node[1]
            self.visit_decl(node)
            self.write('>')
    
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
        self.write('> ')
    
    def visit_float_decl(self, node):
        self.write(self.types[node])
        
    def visit_int_decl(self, node):
        self.write(self.types[node])

    def visit_str_decl(self, node):
        self.write(self.types[node])
        
    def visit_bool_decl(self, node):
        self.write(self.types[node])        

    def visit_array_decl(self, node):
        self.visit_decl(node[1])
        self.write("[]")
        
    def visit_decl(self, node):
        if isinstance(node, list):
            if node[0]=="list":
                self.write('List<')
                self.visit_list_decl(node)
            if node[0] == "dict":
                self.write("Dictionary<")
                self.visit_dict_decl(node)
            if node[0]=="tuple":
                self.write('Tuple<')
                self.visit_tuple_decl(node)
            if node[0]=="array":
                self.visit_array_decl(node)
        else:
            if node=="float":
                self.visit_float_decl(node)
            if node =="int":
                self.visit_int_decl(node)
            if node =="str":
                self.visit_str_decl(node)
            if node =="bool":
                self.visit_bool_decl(node)                

            
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
        pass

    
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
        self.write(' ; ')
        self.visit(node.index)
        self.write("<")        
        self.visit(node.end)
        self.write(' ; ')
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

        
