
from pycropml.transpiler.generators.csharpGenerator import CsharpGenerator, CsharpCompo
import os


class ApsimGenerator(CsharpGenerator):
    """ This class contains the specific properties of
    Apsim and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        CsharpGenerator.__init__(self, tree, model, name)

    def visit_module(self, node):
        if self.model is not None:
            #self.write("namespace")
            self.write("public class %s: Model"%self.model.name.capitalize())
        else:
            self.write("public class Test")
        self.newline(node)
        self.write("{") 
        self.newline(node)
        self.indentation += 1     
        self.visit(node.body)
        self.newline(node)
        self.indentation -= 1        
        self.newline(node)
        self.write("}")                

    def visit_function_definition(self, node):      
        self.newline(node)
        #self.add_features(node)
        self.funcname = node.name
        if (not node.name.startswith("model_") and not node.name.startswith("init_")) :
            self.write("public static ")
            self.visit_decl(node.return_type) if node.return_type else self.write("void")
            self.write(" Main(") if node.name=="main" else self.write(" %s("%node.name)
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
            if self.node_param and not node.name.startswith("init_") :
                for arg in self.node_param: 
                    self.newline(node) 
                    self.write ('private ') 
                    self.visit_decl(arg.pseudo_type)
                    self.write(" _")
                    self.write(arg.name) 
                    self.write(";")                     
                    #self.generator.private(self.node_param)        
                    self.newline(node)
                    self.write("public ")
                    self.visit_decl(arg.pseudo_type)
                    self.write(' ' +arg.name)
                    self.write(self.public_properties%(arg.name,arg.name))
            self.write(self.constructor%self.model.name.capitalize()) if not node.name.startswith("init_") else ""
            self.newline(node)      
            self.write("public void ")
            self.write(" Calculate_%s("%self.model.name.lower()) if not node.name.startswith("init_") else self.write("Init(")
            self.write('%sState s, %sState s1, %sRate r, %sAuxiliary a)'%(self.name.capitalize(), self.name.capitalize(),self.name.capitalize(), self.name.capitalize()))
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
            for arg in self.add_features(node) :
                if "feat" in dir(arg):
                    if arg.feat in ["IN","INOUT"] :
                        self.newline(node) 
                        if self.model and arg.name not in self.modparam:
                            self.visit_decl(arg.pseudo_type)
                            self.write(" ")
                            self.write(arg.name)
                            if not node.name.startswith("init_"):
                                if arg.name in self.states and not arg.name.endswith("_t1") :
                                    self.write(" = s.%s"%arg.name)
                                if arg.name.endswith("_t1") and arg.name in self.states:
                                    self.write(" = s1.%s"%arg.name[:-3])
                                if arg.name in self.rates:
                                    self.write(" = r.%s"%arg.name)
                                if arg.name in self.auxiliary:
                                    self.write(" = a.%s"%arg.name) 
                            else:
                                if arg.pseudo_type[0] =="list":
                                    self.write(" = new List<%s>()"%(self.types[arg.pseudo_type[1]]))
                                elif arg.pseudo_type[0] =="array":
                                    self.write(" = new %s[%s]"%(self.types[arg.pseudo_type[1]], arg.elts[0].value if "value" in dir(arg.elts[0]) else arg.elts[0].name))
                            self.write(";")                   
            self.indentation -= 1 
        self.body(node.block)
        self.newline(node)
        self.visit_return(node)
        self.newline(node)
        self.indentation -= 1 
        self.write('}') 
        self.newline(node)



class ApsimCompo(CsharpCompo):
    """ This class used to generates states, rates and auxiliary classes
        for C# languages.
    """
    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        CsharpCompo.__init__(self,tree, model, self.name)