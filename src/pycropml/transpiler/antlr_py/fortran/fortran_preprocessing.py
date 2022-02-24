# coding: utf8
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.api_declarations import Middleware
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction


types = ["int", "float", "str", "list", "array", "bool"]


class Declarations(Middleware):
    
    def __init__(self, localvar=[]):
        self.localvar = localvar
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_declaration(self, tree):
        res = []
        if tree.decl[0].type not in types:
            return None
        for decl in tree.decl:
            if decl.name in self.localvar:
                res.append(decl)
        if res:
            tree = Node(type="declaration", decl = res, comments = tree.comments )
        else:
            return None
        return self.transform_default(tree)
        """for decl in tree.decl:
            if decl.type not in types:
                return None
            else:
                res.append(decl)
        if res:
            return Node(type="declaration", decl = res, comments = tree.comments )
        else:
            return None"""

    
class Call_stmt(Middleware):
        
    def __init__(self, trees=None):
        self.trees = trees
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_call_stmt(self, tree):
        from copy import copy
        extr =  DssatExtraction()
        comments = copy(tree.comments)
        name = tree.name
        args = tree.args
        subr = extr.getSubroutine(self.trees, name)
        inputs = [args[n] for n in subr.inputs_pos]
        outputs = [args[n] for n in subr.outputs_pos]
        tree =Node(type="assignment", target = Node(type="tuple", elements=outputs), value = Node(type="custom_call", function=name, args=inputs), comments = comments)
        return self.transform_default(tree)



    
class Assignment(Middleware):
    def __init__(self):
        Middleware.__init__(self)
        self.structfields = dict(list())
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_assignment(self, tree):
        if tree.value.type == "local" and "name" in dir(tree.target) and  tree.target.name == tree.value.name:
            return Node(type="comments", comments = tree.comments)
        else:
            return self.transform_default(tree)

class Attr(Middleware):
    def __init__(self, trees = None, imports=[]):
        Middleware.__init__(self)
        self.decls = []
        self.trees = trees
        self.imports = imports
        self.attrinstance = {}
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_attr(self, tree):
        extr =  DssatExtraction()
        name = str(tree.name)
        pseudo = tree.object.pseudo_type
        comments = tree.comments
        for mod in self.imports:
            modules = extr.getModule(self.trees, mod)
            structs = extr.getStruct(modules, pseudo)
            decls = extr.getDeclaration(structs, name)
            if decls:
                if tree.object.name in self.attrinstance:
                    self.attrinstance[tree.object.name].append(decls.name)
                else:self.attrinstance[tree.object.name]=[decls.name]
                tree = Node(type = "local", name=str(decls.name), pseudo_type = decls.pseudo_type)
                self.decls.append(Node(type="declaration", decl=[decls], comments=comments))
                break
        return self.transform_default(tree)
    

class Implicit_return(Middleware):
    def __init__(self):
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_implicit_return(self, tree):
        pass
    

class ModelUnit(Middleware):
    def __init__(self):
        Middleware.__init__(self)
        self.modelunit = []
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_function_definition(self, tree):
        if tree.comments and tree.comments[-1]=="!%%ModelUnit%%":
            self.modelunit.append(tree)
        return self.transform_default(tree)

class Local(Middleware):
    def __init__(self):
        Middleware.__init__(self)
        self.localvar = set()
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_local(self, tree):
        self.localvar.add(tree.name)
        return self.transform_default(tree)
            
    
    




     
    