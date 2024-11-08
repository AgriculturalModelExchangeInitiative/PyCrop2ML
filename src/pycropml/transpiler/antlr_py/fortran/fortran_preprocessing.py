# coding: utf8
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.api_declarations import Middleware
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction


types = ["int", "float", "str", "list", "array", "bool"]


class Retrive_from_Comparison(Middleware):
    
    def __init__(self, localvar=[]):
        self.localvar = localvar
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_comparison(self, tree):
        if tree.left.type == "local" and isinstance(tree.left.pseudo_type, list):
            self.var = tree.left
        return tree
            
                                
                                
                                
class TransformLocal(Middleware):
    
    def __init__(self, localvar=[]):
        self.localvar = localvar
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_local(self, tree):
        if isinstance(tree.pseudo_type, list):
            if tree.pseudo_type[0]=="array":
                res = Node(type = 'index',
                sequence = Node(type = 'local',
                name = tree.name,
                pseudo_type = tree.pseudo_type),
                index = Node(type = 'local',
                name = 'i_cyml',
                pseudo_type = 'int'),
                pseudo_type = tree.pseudo_type[-1])
                tree = res
        return tree
        
        
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
        otherparams = []
        if subr.notdeclared:
            imports = subr.imports
            res = extr.getDecl(self.trees, imports, subr.notdeclared)
            for j in res.values():
                j.type="local"
                otherparams.append(j) 
        inputs = [args[n] for n in subr.inputs_pos]
        if otherparams: inputs = otherparams + inputs
        outputs = [args[n] for n in subr.outputs_pos]
        if len(outputs)==1: tree =Node(type="assignment", op="=", target = Node(type="local", name=outputs[0].name, pseudo_type=outputs[0].pseudo_type), value = Node(type="custom_call", function=name, args=inputs), comments = comments)
        else: tree =Node(type="assignment", op="=",target = Node(type="tuple", elements=outputs), value = Node(type="custom_call", function=name, args=inputs), comments = comments)
        return self.transform_default(tree)



    
class Assignment(Middleware):
    def __init__(self):
        Middleware.__init__(self)
        self.structfields = dict(list())
        self.targets = []
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_assignment(self, tree):
        if tree.target.type == "local":
            self.targets.append(tree.target.name)
        else:
            self.targets.append(tree.target.sequence.name)
        if tree.value.type == "local" and "name" in dir(tree.target) and  tree.target.name == tree.value.name:
            return Node(type="comments", comments = tree.comments)
        else:
            return self.transform_default(tree)

class Attr(Middleware):
    def __init__(self, trees = None, imports=[]):
        Middleware.__init__(self)
        self.decls = []
        self.trees = trees if trees else None
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
            
    
    




     
    