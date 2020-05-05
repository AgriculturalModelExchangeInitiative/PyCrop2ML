from pycropml.transpiler.generators.javaGenerator import JavaGenerator


class SimplaceGenerator(JavaGenerator):
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        JavaGenerator.__init__(self, tree, model, self.name)
        self.inputs = [inp.name for inp in self.model.inputs]
        self.outputs = [inp.name for inp in self.model.outputs]
        self.var = self.inputs+self.outputs

    def visit_module(self, node):
        self.visit(node.body)


    def visit_declaration(self, node):
        self.newline(node)
        for n in node.decl:
            if n.name not in self.var:
                self.newline(node)
                if 'value' not in dir(n) and n.type not in ("list", "tuple", "dict", "array"):
                    self.write(self.types[n.pseudo_type])
                    self.write(' %s;'%n.name) 
                    #self.write('%s %s;'%(self.types[n.type],n.name)) 
                if 'elements' not in dir(n) and n.type in ("list","array"):
                    if n.type=="list":
                        self.write("List<%s> %s = new ArrayList<>(Arrays.asList());"%(self.types2[n.pseudo_type[1]],n.name))
                    if n.type=="array":
                        self.write(self.types[n.type]%(self.types2[n.pseudo_type[1]], n.name, self.types2[n.pseudo_type[1]]))
                        #self.write("[%s];"%n.elts[0].value)
                        self.write('[')
                        self.visit(n.elts)
                        self.write('];')
                if 'value' in dir(n) and n.type in ("int", "float", "str", "bool"):
                    self.write("%s %s"%(self.types[n.type], n.name))
                    self.write(" = ")
                    if n.type=="local":
                        self.write(n.value)
                    else: self.visit(n)
                    self.write(";")
                elif 'elements' in dir(n) and n.type in ("list", "tuple"):
                    if n.type=="list":
                        self.visit_decl(n.pseudo_type)
                        self.write(n.name)
                        self.write(" = new ArrayList <>(Arrays.asList") 
                        #self.visit_decl(n.pseudo_type)
                    if n.type=='tuple':
                        pass
                    self.write(u'(')
                    self.comma_separated_list(n.elements)
                    self.write(u'));')           
                elif  n.type=='datetime':
                    self.newline(node)
                    self.write("Date")
                    self.write(n.name)                 
                elif 'pairs' in dir(n) and n.type=="dict":
                    self.visit_decl(n.pseudo_type)
                    self.write(n.name)
                    self.write(" = new ") 
                    self.visit_decl(n.pseudo_type)               
                    self.write(u'{')
                    self.comma_separated_list(n.pairs)
                    self.write(u'};')
                    
            self.newline(node)
   
    def visit_return(self, node):
        if self.model:
            self.newline(node)
            self.indentation += 1
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("OUT", "INOUT"):
                        self.write("%s.setValue(t%s);"%(arg.name,arg.name ))
                        self.newline(node)

    def visit_local(self, node):
        if node.name in self.var:
            return self.write("t%s"%node.name)
        else: self.write(node.name)

    def visit_function_definition(self, node):
        self.newline(node)
        self.funcname = node.name
        self.newline(node)
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            if node.name=="main":
                self.write("public static void main(String[] args)") 
            else:
                self.write("public static ")
                self.visit_decl(node.return_type) if node.return_type else self.write("void")
                self.write(" %s("%node.name)
                for i, pa in enumerate(node.params):
                    self.visit_decl(pa.pseudo_type)
                    self.write(" %s"%pa.name)
                    if i!= (len(node.params)-1):
                        self.write(', ')
                self.write(')')
            self.newline(node)
            self.write('{') 
            self.newline(node)
        else:
            self.write("public void Process()")
            self.newline(node)
            self.write('{')
            self.newline(node)
            self.indentation += 1
            for arg in self.add_features(node):
                if "feat" in dir(arg):
                    if arg.feat in ("IN", "OUT", "INOUT"):
                        self.newline(1)
                        if self.model :
                            self.visit_decl(arg.pseudo_type)
                            self.write(" t")
                            self.write(arg.name)
                            self.write(" = %s.getValue();" % arg.name)
        self.indentation -= 1
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1
        self.write('}')
        self.newline(node)

    def visit_import(self, node):
        return

class SimplaceCompo(JavaGenerator):
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        JavaGenerator.__init__(self, tree, model, self.name)
