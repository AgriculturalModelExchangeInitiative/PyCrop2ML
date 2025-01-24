# coding: utf8
from pycropml.transpiler.antlr_py.bioma.biomaExtraction import BiomaExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.api_declarations import Middleware
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction
from pycropml.transpiler.antlr_py.csharp.builtin_typed_api import *
from pycropml.transpiler.antlr_py.csharp.api_transform import *
from pycropml.transpiler.helpers import *
from pycropml.transpiler.errors import *
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.env import Env
from copy import deepcopy
from collections import defaultdict

types = ["int", "float", "str", "list", "array", "bool"]

type_={
    "DOUBLE":"double",
    "INT":"int",
    "STRING":"string",
    "DATE":"date",
    "DOUBLELIST":"List",
    "INTLIST":"List",
     "STRINGLIST":"List",
     "DATELIST":"List",
    "BOOLEAN":"bool",
    "DOUBLEARRAY":"array",
    "INTARRAY":"array"}

def inst_dclass(meth):
    params = meth.params
    lst = []
    for p in params:
        if isinstance(p.pseudo_type, Node) and "typename" in dir(p.pseudo_type):
            pname = str(p.name)
            lst.append((p.pseudo_type.pseudo_type, pname))
        elif isinstance(p.pseudo_type, str):
            lst.append((p.pseudo_type, str(p.name)))    
        else:
            lst.append((p.pseudo_type[1].upper() + p.pseudo_type[0].upper(), str(p.name))) 
    
    orDict = defaultdict(list)
    # iterating over list of tuples
    for key, val in lst:
        orDict[key].append(val)      
    dclassdict = dict(orDict)
    return dclassdict


class CheckingInOut(Middleware):
    
    """_summary_
    This code defines a middleware class called "CheckingInOut" 
    that checks the inputs and outputs of a given code block. 
    It does this by keeping track of the current scope and environment, 
    and adding any new variables to the environment. 
    It also keeps track of the inputs and outputs of the code block 
    by checking if a variable is already in the current scope or not. 
    The middleware class has methods for different types of statements 
    and expressions, such as assignment, if statements, for loops, and function calls. 
    The purpose of this middleware is to ensure that the inputs and outputs 
    of a code block are well-defined and can be used by other parts of a program.
    """
    
    def __init__(self, env_init=None, isAlgo=False):
        if env_init is None:
            self.env_init = {}
        self.env_init = env_init 
        self.env = [self.env_init]
        self.current_scope = {}
        self.if_scope = None
        self.isAlgo = isAlgo
        self.inputs = []
        self.outputs = []
        Middleware.__init__(self)
              
    def process(self, tree):
        self.current_scope = self.current()
        return self.transform(tree,in_block=False)
    
    def current(self):
        return {k: v for d in self.env for k, v in d.items()}
    
    def workflow(self, tree):
        self.env.append({})
        r = self.transform_default(tree)
        self.env.pop()
        self.current_scope = self.current()
        return r
            
    def action_assignment(self, tree):
        self.transform(tree.value)
        if tree.target.type == "local":
            t_name = tree.target.name
            type_ = tree.target.pseudo_type
            if t_name not in self.current_scope and not self.isAlgo: # self.env[-1]
                self.inputs.append(t_name) 
            
            self.env[-1][t_name] = type_
            self.outputs.append(t_name)
            
        elif "sequence" in dir(tree.target):
            t_name = tree.target.sequence.name
            type_ = tree.target.sequence.pseudo_type
            if t_name not in self.current_scope and not(isinstance(type_, list) and type_[0]=="array"):
                self.inputs.append(t_name)
            self.env[-1][t_name] = type_
            self.outputs.append(t_name)
            
        else:
            for elem in tree.target.elements:
                t_name = elem.name
                type_ = elem.pseudo_type
                self.outputs.append(t_name)
                self.env[-1][t_name] = type_
                
        
        if "op" in dir(tree) and tree.op != "=":
            if t_name not in self.current_scope:
                self.inputs.append(t_name)   
        
        self.current_scope = self.current()
        return tree
    
    def action_standard_method_call(self, tree):
        if isinstance(tree.receiver.pseudo_type, list) and tree.message in ["append", "sum", "remove", "extend", "insert"]:
            t_name = tree.receiver.name
            if t_name not in self.current_scope:
                self.inputs.append(t_name)
            self.env[-1][t_name] = tree.receiver.pseudo_type
            self.outputs.append(t_name)
            self.current_scope = self.current()
        self.transform_default(tree)
        return tree
    
    def action_declaration(self, tree):
        for d in tree.decl:
            if "value" in dir(d):
                self.transform_default(d.value)
            self.env[-1][d.name] = d.type
            self.current_scope = self.current()
        return tree
            
    
    def action_local(self, tree):
        
        if tree.name not in self.current_scope:# and tree.name  not in self.outputs:
            self.inputs.append(tree.name)
            self.env[-1][tree.name] = tree.type 
            self.current_scope = self.current()      
        return tree
    
    def action_if_statement(self, tree):
        self.env.append({})
        self.transform(tree.test)
        self.transform(tree.block)
        m1 = self.env[-1]
        self.env.pop()
        self.current_scope = self.current()
        
        if tree.otherwise:
            self.env.append({})
            self.transform(tree.otherwise)
            m2 = self.env[-1]
            self.env.pop()
            common_keys = m1.keys( ) & m2.keys()
            common_dict = {k:m1[k] for k in common_keys}
            self.env[-1].update(common_dict)
            self.current_scope = self.current()   
        return tree
    
    #def action_elseif_statement(self, tree):
        #print("oooooooooooooooo")
        #return self.workflow(tree)

    #def action_else_statement(self, tree):
        #return self.workflow(tree)
    
    def action_for_statement(self, tree):
        return self.workflow(tree)

    def action_for_range_statement(self, tree):
        return self.workflow(tree)
    
    def action_while_statement(self, tree):
        return self.workflow(tree)
    
    def action_custom_call(self, tree):
        for arg in tree.args:
            self.transform(arg)
        return tree

    def action_standard_call(self, tree):
        for arg in tree.args:
            self.transform(arg)
        return tree
        
    
    
    


class Member_access(Middleware):
    
    def __init__(self, totaltree, prec_cur=[]):
        self.totaltree = totaltree
        self.members = []
        self.prec_cur = prec_cur
        self.m_cat = {}
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_member_access(self, tree):
        name = tree.member
        if "." in name: name = name.split('.')[0]
        pseudo = tree.pseudo_type
        self.members.append(tree)
        # retrieve the class name
        # retrieve the corresponding node in the totaltree
        # dtype: retrieve the datatype wwith the variable name
        # return {"type":"local", "name":name, "pseudo_type":dtype}
        if pseudo is None:
            return Node(type="local", name= tree.member.split(".")[-1])
        classname = pseudo.pseudo_type if isinstance(pseudo, Node) else pseudo
        z = BiomaExtraction()
        z.getTypeNode(self.totaltree, "classDef")
        classNode = [m for m in z.getTree if m.name == classname]
        z.getTypeNode(classNode[0], "propertyDef")
        propNode = [m for m in z.getTree if m.name == name]
        
        if not propNode: return Node(type = "local", name =name, pseudo_type = pseudo)
        
        pseudo_prop = propNode[0].pseudo_type
        if isinstance(pseudo_prop, Node):
            pseudo_type = pseudo_prop.pseudo_type
        else:
            pseudo_type = pseudo_prop
        if isinstance(pseudo_type, list):
            type_ = pseudo_type[0]
        else: type_ = pseudo_type       
        
        if "." in tree.member: 
            v = tree.member.split('.')
            propert = v[1]
            name = from_attr_to_var(tree.name, v[0], self.prec_cur)
            self.m_cat[name] = tree.name
            if type_ in PROPERTY_API:
                rec = {"type":"local", "name": name, "pseudo_type":pseudo_type}
                api = PROPERTY_API[type_].get(propert)      
                if not api:
                    raise PseudoCythonTypeCheckError("Not implemented property , %s"%propert)  

                elif not isinstance(api, dict):
                    z = api.expand([rec])
                    return transform_to_syntax_tree(z)
        else:
            if self.prec_cur:
                name = from_attr_to_var(tree.name, tree.member, self.prec_cur)
                self.m_cat[name] = tree.name
            else: name = tree.member 
            return Node(type = "local", name =name, pseudo_type = pseudo_type)
        
        return tree

class Index(Middleware):
    
    def __init__(self):
        Middleware.__init__(self)
        self.indexes = []
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_index(self, tree):
        if isinstance(tree.pseudo_type, Node):
            pseudo_type = tree.sequence.pseudo_type
            tree.pseudo_type = pseudo_type[-1]
        return tree

class Binary_op(Middleware):
    
    def __init__(self):
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_binary_op(self, tree):
        left = tree.left
        right = tree.right
        
        if left.type == "binary_op" and left.pseudo_type=="unknown":
            left = self.transform(left)
            left.pseudo_type = TYPED_API['operators'][left.op](
            left.left.pseudo_type, left.right.pseudo_type)[-1]
        
        if right.type == "binary_op" and right.pseudo_type=="unknown":
            right = self.transform(right)
            right.pseudo_type = TYPED_API['operators'][right.op](
            right.left.pseudo_type, right.right.pseudo_type)[-1]
            
        tree.pseudo_type = TYPED_API['operators'][tree.op](
            left.pseudo_type, right.pseudo_type)[-1]
        
        return tree

class Assignment(Middleware):
    
    def __init__(self):

        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_assignment(self, tree):
        if tree.target.pseudo_type == "unknown":
            tree.target.pseudo_type = tree.value.pseudo_type
        if "name" in dir(tree.value) and "name" in dir(tree.target) and tree.target.name == tree.value.name: return
        return tree


class Custom_call(Middleware):
    
    def __init__(self, totaltree, extfunc = [], not_declared={},  ext_func_inout={}, member_category={}):
        self.totaltree = totaltree
        self.extfunc = extfunc
        self.not_declared = not_declared
        self.ext_func_inout = ext_func_inout
        self.member_category = member_category
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_custom_call(self, tree):
        method = tree.function
        if "namespace" in dir(tree):
            namespace = tree.namespace
            name = namespace.name
            args = tree.args
            receiver_type = namespace.pseudo_type
            rec = {"type":"local", "name":name, "pseudo_type":receiver_type}
            receiver_type = receiver_type[0] if isinstance(receiver_type, list) else receiver_type
            if receiver_type in METHOD_API:
                api = METHOD_API.get(receiver_type,{}).get(method)
                if api:
                    tree = api.expand([rec]+ args)
                    if  tree["message"] not in ("contains?", "index"):
                        tree = transform_to_syntax_tree({"type": 'ExprStatNode', 'expr': tree})
                    else: return tree
                if not api:
                        raise translation_error('CyMLT doesn\' t support %s %s ' % (receiver_type, method),
                                                suggestions='CyMLT supports those %s functions\n  %s' % (
                          name, prepare_table(TYPED_API[receiver_type], ORIGINAL_METHODS.get(receiver_type)).strip()))
        if self.extfunc:
            for f in self.extfunc:
                if f.name == method:
                    args = []
                    tree.args = tree.args + self.not_declared[method]
                    z = BiomaExtraction()
                    inps = self.ext_func_inout[f.name]["inputs"]
                    if not isinstance(inps, list): inps = [inps]
                    meth_member_category = self.member_category[f.name]
                    if meth_member_category:
                        for num, arg in enumerate(tree.args):
                            if isinstance(arg.pseudo_type, Node) :
                                restricted_inputs = [ins for ins in inps if ("position_args" in dir(ins) and ins.position_args == num+1)]
                                for k in restricted_inputs:
                                    k.type = "local"
                                    args.append(k)
                            else:
                                args.append(arg)
                    if args: tree.args = args
                    if self.ext_func_inout[f.name]["outputs"]:
                        return transform_to_syntax_tree({"type": 'assignment', "target":self.ext_func_inout[f.name]["outputs"],'op':"=", 'value': tree})
                    z.getTypeNode(f, "implicit_return")
                    if not z.getTree:
                        return transform_to_syntax_tree({"type": 'ExprStatNode', 'expr': tree})
        return self.transform_default(tree)

class ExprStatNode(Middleware):
    
    def __init__(self, extfunc = [],  ext_func_inout={}):
        self.extfunc = extfunc
        self.ext_func_inout = ext_func_inout
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_ExprStatNode(self, tree):
        if tree.expr.type == "custom_call":
            for f in self.extfunc:
                if tree.expr.function == f.name:
                    return transform_to_syntax_tree({"type": 'assignment', "target":self.ext_func_inout[f.name]["outputs"],'op':"=", 'value': tree.expr})
        return tree
                    
class Declarations(Middleware):
    
    def __init__(self):
        self.declarations = []
        self.declnames=[]
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_declaration(self, tree):
        res = []
        for decl in tree.decl:
            if "value" not in dir(decl):
                newdecl = decl
                if decl.name not in self.declnames:
                    self.declnames.append(decl.name)
                    self.declarations.append(Node(type="declaration", decl=[newdecl], comments=tree.comments))
            else:
                 
                if decl.type=="array" and "init" in dir(decl.value):
                    if decl.value.init.value is None:
                        r = Node(name = decl.name, type="array", dim=1, elts=decl.value.elts, pseudo_type=decl.pseudo_type)
                        self.declarations.append(Node(type="declaration", decl=[r], comments = [])) 
                        self.declnames.append(decl.name)
                    else:
                        r = Node(name = decl.name, type="array", dim=1, elts=decl.value.elts, pseudo_type=decl.pseudo_type)
                        self.declarations.append(Node(type="declaration", decl=[r], comments = [])) 
                        self.declnames.append(decl.name)
                        tree = Node(type ="assignment", target = Node(type="local", name=decl.name, pseudo_type=decl.pseudo_type), op = "=", value = Node(type="array", init= decl.value.init), comments = tree.comments)
                        res.append(self.transform_default(tree))
                elif decl.type=="array" and "elts" in dir(decl.value):
                    r = Node(name = decl.name, type="array", dim=1, elts=decl.value.elts, pseudo_type=decl.pseudo_type)
                    self.declarations.append(Node(type="declaration", decl=[r], comments = [])) 
                    self.declnames.append(decl.name)
                else:
                    if "type" in dir(decl.value) and decl.value.type=="List" and "args" in dir(decl.value) and len(decl.value.args)==1 and decl.value.args[0].name==decl.name: return
                    if isinstance(decl.pseudo_type, Node):
                        r = decl.value.pseudo_type
                        decl.type = r[0] if  isinstance(r, list)   else r
                        decl.pseudo_type = r
                    
                    if "name" in dir(decl.value) and decl.name== decl.value.name: return
                    tree = Node(type ="assignment", target = Node(type="local", name=decl.name, pseudo_type=decl.pseudo_type), op = "=", value = decl.value, comments = tree.comments)
                   
                    if decl.type == "unknown" or decl.type == "var":
                        x = decl.value.pseudo_type
                        if isinstance(x, list):
                            decl.type = x[0]
                            decl.pseudo_type = x[1:]
                        else:
                            decl.type = x
                            decl.pseudo_type = x
                    del decl.value
                    if decl.name not in self.declnames:
                        self.declarations.append(Node(type="declaration", decl=[decl], comments = [])) 
                        self.declnames.append(decl.name)               
                    res.append(self.transform_default(tree))
        return res


class Local(Middleware):
    
    def __init__(self, declnames=[], params={}):
        self.declnames = declnames
        self.not_declared=[]
        self.params = params
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_local(self, tree):
        if tree.name not in self.declnames:
            self.not_declared.append(str(tree.name))
        if tree.name in  self.params:
            pseudo_type = type_[self.params[tree.name]["ValueType"]]
            tree.pseudo_type = pseudo_type
        return tree

class TransformLocal(Middleware):
    
    def __init__(self, notdeclared):
        self.notdeclared= notdeclared
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_local(self, tree):
        for f in self.notdeclared:
            if f.name == tree.name:
                tree = f
                break
        return tree


def from_attr_to_var(instance, attr, d):
    pos = None
    for i, j in d.items():
        for l, k in enumerate(j):
            if k == instance:
                pos = l
                break
        if pos:
            break
    if pos == 0:
        return attr
    else: return attr + "_t%s"%pos
    

     
    