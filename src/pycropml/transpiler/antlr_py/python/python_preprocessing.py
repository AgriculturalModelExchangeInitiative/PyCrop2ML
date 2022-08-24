

from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.api_declarations import Middleware

class RemDeclarations(Middleware):
    
    def __init__(self, localvar=[]):
        self.localvar = localvar
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_declaration(self, tree):
        return

class RemImplicit_return(Middleware):
    
    def __init__(self, localvar=[]):
        self.localvar = localvar
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_implicit_return(self, tree):
        return

class Declarations(Middleware):
    
    def __init__(self, inout):
        self.inout = inout
        self.declarations = []
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_declaration(self, tree):
        res = []
        for decl in tree.decl:
            if decl.name not in self.inout:
                if "value" in dir(decl) and decl.value:
                    self.declarations.append(Node(type="declaration", decl=[Node(type=decl.type, name=decl.name, pseudo_type=decl.pseudo_type)], comments=tree.comments))
                    if not("elements" in dir(decl.value) and decl.value.elements==[]):
                        decl = Node(type ="assignment", target = Node(type="local", name=decl.name, pseudo_type=decl.pseudo_type), op = "=", value = decl.value, comments = tree.comments)
                        res.append(self.transform_default(decl))
                else:self.declarations.append(Node(type="declaration", decl=[decl], comments=tree.comments))
        return res 