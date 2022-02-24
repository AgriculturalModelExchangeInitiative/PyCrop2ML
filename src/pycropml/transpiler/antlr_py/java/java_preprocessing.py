# coding: utf8
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.api_declarations import Middleware




class Declarations(Middleware):
    
    def __init__(self, declarations=[], kvnames={}, all_decl={}):
        self.declarations = declarations
        self.kvnames = kvnames
        self.all_decl = all_decl
        self.declnames = []
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_declaration(self, tree):
        res = []
        for decl in tree.decl:
            test  =False
            if "value" in dir(decl) and decl.value.type == "custom_call" and decl.value.function == "getValue" and decl.value.instance.name in self.all_decl:
                self.kvnames[decl.name] = decl.value.instance.name
            elif "value" not in dir(decl):
                newdecl = decl
                if decl.type == "array":
                    for el in decl.elements:
                        if el.name in self.declnames:
                            test = True
                        break
                if test:
                    newdecl = Node(type = "array", name=decl.name, dim= len(decl.elements), elements = [], pseudo_type=decl.pseudo_type) 
                    tree = Node(type = 'ExprStatNode',
                        expr = Node(type = 'standard_method_call',
                        receiver = Node(type = 'local',
                        name = newdecl.name,
                        pseudo_type = newdecl.pseudo_type,
                        ),
                        message = 'allocate',
                        args = decl.elements,
                        pseudo_type = "Void"),
                        comments = tree.comments)                   
                    
                    res.append(self.transform_default(tree))
                    #del decl.value
                self.declarations.append(Node(type="declaration", decl=[newdecl], comments=tree.comments))
                self.declnames.append(decl.name)
            else: 
                tree = Node(type ="assignment", target = Node(type="local", name=decl.name, pseudo_type=decl.pseudo_type), op = "=", value = decl.value, comments = tree.comments)
                del decl.value
                self.declarations.append(Node(type="declaration", decl=[decl], comments = [])) 
                self.declnames.append(decl.name)               
                res.append(self.transform_default(tree))
        return res
    
class Custom_call(Middleware):
        
    def __init__(self, kvnames):
        self.kvnames = kvnames
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_custom_call(self, tree):
        if tree.function != "setDefaultValue":
            if tree.function == "getValue":
                tree = tree.instance
                tree.pseudo_type = tree.pseudo_type[-1]
            elif tree.function == "setValue":
                if "name" in dir(tree.args[0]) and tree.args[0].name in self.kvnames and self.kvnames[tree.args[0].name] == tree.instance.name:
                    return None
                else: 
                    tree = Node(type="assignment", op="=", target=tree.instance, value=tree.args[0], comments = tree.comments)
            elif tree.function == "setArrayValue":
                tree = Node(type="assignment", 
                            op="=", 
                            target = Node(type ='index', 
                                          sequence = tree.instance,
                                          index = [tree.args[0]], 
                                          pseudo_type = tree.instance.pseudo_type[-1]),
                            value = tree.args[1],
                            comments = tree.comments
                            )
            return self.transform_default(tree)
        else:
            pass

class Local(Middleware):
    def __init__(self, kvnames):
        self.kvnames = kvnames
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_local(self, tree):
        tree = tree.name if isinstance(tree.name, Node) else tree
        if tree.name in self.kvnames.keys():
            tree = Node(type="local", name=self.kvnames[tree.name], pseudo_type = tree.pseudo_type, comments=tree.comments)
        return self.transform_default(tree)

class MemberAcess(Middleware):
    def __init__(self):
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_member_access(self, tree):
        if isinstance(tree.name, Node):
            name = tree.name
            if isinstance(tree.member, list) and len(tree.member)==1 and tree.member[0]=="length":
                tree = Node(type="standard_method_call",receiver = name, message="len",  args = [], pseudo_type="int", comments=tree.comments )
        return self.transform_default(tree)
    
class Assignment(Middleware):
    def __init__(self):
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_assignment(self, tree):
        if tree.value.type == "RefTypeCasting" \
        and tree.value.message[0]=="FWSimVariable" \
        and tree.value.receiver.type== "custom_call" \
        and tree.value.receiver.function == "getVariable":
            pass
        else:
            return self.transform_default(tree)
    


    
    




     
    