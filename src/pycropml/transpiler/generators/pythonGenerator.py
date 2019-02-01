from pycropml.transpiler.codeGenerator import CodeGenerator

class PythonGenerator(CodeGenerator):
    """This class contains the specific properties of 
    python language and use the NodeVisitor to generate a python
    code source from a well formed syntax tree.
    """
    def __init__(self):
        super().__init__(indent_with=' '*4)        
    
    def visit_import(self, node):
        self.write(u"import %s" % node.module)

    def visit_assignment(self, node):
        self.newline(node)
        self.visit(node.target)
        self.write(' = ')
        self.visit(node.value)

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

    def visit_comparison(self, node):
        self.visit_binary_op(node)
    
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
        self.write(node.value)
    
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
        self.write(u" %s " % op.replace('_', ' '))
        self.visit(node.right)
        self.operator_exit()
          
    def visit_function_definition(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.write('def %s(' % node.name)
        for i, pa in enumerate(node.params):
            self.visit(pa)
            if i!= (len(node.params)-1):
                self.write(',')
        self.write('):')
        self.body(node.block)
        
    def visit_implicit_return(self, node):
        self.newline(node)
        if node.value is None:
            self.write('return')
        else:
            self.write('return ')
        self.visit(node.value)
    
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
            if 'value' in dir(n) and n.type in ("int", "float"):
                self.write(n.name)
                self.write(" = ")
                self.write(n.value)
            elif 'value' in dir(n) and n.type=="str":                
                self.write(n.name)
                self.write(" = ")
                self.emit_string(n)                
            elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                self.write(n.name)
                self.write(" = ")
                self.write(u'[')
                self.comma_separated_list(n.elements)
                self.write(u']')          
     
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
        self.newline(node)
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



            
        
