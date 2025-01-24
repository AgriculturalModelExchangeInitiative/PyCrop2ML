# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_dictASG, to_CASG
from pycropml.transpiler.antlr_py.apsim.apsimExtraction import ApsimExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.csharp import cs_cyml
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py import repowalk
from pycropml.transpiler.antlr_py.to_specification import createObjectCompo

from copy import deepcopy, copy
from typing import *
import networkx as nx
import itertools
import xml.etree.ElementTree as xml

from pycropml.transpiler.antlr_py.csharp.csharp_preprocessing import *
from pycropml.transpiler.antlr_py.codeExtraction import extraction
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import extract
from pycropml.transpiler.antlr_py.api_declarations import Middleware

from pycropml.transpiler import lib
from pycropml.pparse import ModelParser

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
    "STRINGARRAY":"array",
    "INTARRAY":"array"}

pseudo_={
    "DOUBLE":"double",
    "INT":"int",
    "STRING":"string",
    "DATE":"date",
    "DOUBLELIST":["List", "double"],
    "INTLIST":["List", "int"],
     "STRINGLIST":["List", 'string'],
     "DATELIST":["List", "date"],
    "BOOLEAN":"bool",
    "DOUBLEARRAY":["array", "double"],
    "INTARRAY":["array", "int"],
    "STRINGARRAY":["array", "string"],}




def redefine_params(m:Node, var_:Dict, member_category, inputs, outputs, extfunc, instance_dclass)->List[Node]:
    """It allows to change all parameters which are instance of domain class with the explicit attributes required

    Args:
        m (Node): Auxiliary function ASG
        var_ (dict): Metadata from strategy classes and varinfo files: (inputs, parameters, outputs) 
        member_category (_type_): _description_
        inputs (List[str]): Parameter names of the auxiliary function. It can be an instance of domain class

    Returns:
        List[Node]: New parameters nodes
    """
    res = []
    name = m.name
    inputs_p_node = []
    outputs_p_node = []
    inps = list(set(inputs))
    pseudo_name = []
    pos = 0
    reso = []
    inpnames = {p.name:p.pseudo_type for p in m.params}
    for p in m.params:
        pos = pos + 1
        if p.pseudo_type not in list(pseudo_.values()) :
            pseudo = p.pseudo_type.pseudo_type if isinstance(p.pseudo_type, Node) else p.pseudo_type
            pseudo_name.append(pseudo)
            # find the inputs whose instance is p.name
            inputs_p = [key for key, val in member_category[name].items() if val==p.name]
            #inputs_p = inps
                        # find its datatype
            for p_ in inps:
                if p_ in inputs_p:
                    vn = p_[:-3] if (len(p_)>3 and p_.endswith("_t1")) else p_
                    for k, m_inp in var_.items():
                        if k == vn or (k == p_):
                            inputs_p_node.append(Node(type=type_[m_inp['ValueType']], name=p_, pseudo_type=pseudo_[m_inp['ValueType']], position_args = pos))
                            res.append(name)
                            break
                else:
                    indice = 1 if pseudo_name.count(pseudo)>1 else 0
                    for f in extfunc:
                        test = False
                        dclass = deepcopy(instance_dclass[f.name])
                        meth_member_category = member_category[f.name]
                        if meth_member_category:
                            var = dclass[pseudo][indice]
                            inputs_names = [key for key, val in meth_member_category.items() if val==var]
                            if p_ in inputs_names:
                                vn = p_[:-3] if (len(p_)>3 and p_.endswith("_t1")) else p_
                                for k, m_inp in var_.items():
                                    if k == vn or (k == p_):
                                        test = True
                                        res.append(name)
                                        inputs_p_node.append(Node(type=type_[m_inp['ValueType']], name=p_, pseudo_type=pseudo_[m_inp['ValueType']], position_args = pos))
                                        break
                        if test: break
        else:
            if p.name not in res and p.name in inputs:
                inputs_p_node.append(p) 
                res.append(p.name)
            if isinstance(p.pseudo_type, list) and p.pseudo_type[0] in ("array", "List", "list") and p.name in outputs and p.name not in reso:
                outputs_p_node.append(Node(type= "local", name=p.name, pseudo_type=p.pseudo_type))
                reso.append(p.name) # This case because in C# an input with datatype list or array is passed by reference
            

    outs = list(set(outputs))
    for p_ in outs:
        vn = p_[:-3] if (len(p_)>3 and p_.endswith("_t1")) else p_
        for k, m_inp in var_.items():
            if (k == vn or (k == p_)) and p_ not in reso:
                outputs_p_node.append(Node(type= "local", name=p_, pseudo_type=pseudo_[m_inp]))
                reso.append(p_)
                break
        if p_ not in reso and p_ in inpnames:
            outputs_p_node.append(Node(type= "local", name=p_, pseudo_type=inpnames[p_]))
            reso.append(p_)
    return  inputs_p_node, outputs_p_node

# extract inputs and outputs name and datatype from the xml file

def extract_io(xfile):
    """Extract inputs and outputs name and datatype from the xml file

    Args:
        xfile (_type_): xml file path

    Returns:
        Tuple: inputs, outputs
    """
    # read the xml file and extract the inputs and outputs by each tag "Input" and "Output"
    doc = xml.parse(xfile)
    root = doc.getroot()
    res = {}
    for el in list(root):
        for l in list(el):
            if l.tag=="Input" or l.tag=="Output":
                attr = l.attrib
                name = attr.get("name")
                dtype = attr.get("datatype")
                res[name] = dtype
    return res

# transform each inputs into Node type with type provided by res dictionary
def transform_io(inputs, res, out=False):
    ret = []
    for i in inputs:
        pseudo_type = res.get(i)
        if pseudo_type in type_: 
            dtype = type_[pseudo_type]
            pseudo_type = pseudo_[pseudo_type]
        else: dtype = pseudo_type
        if isinstance(dtype, list): dtype = dtype[0]
        if dtype is not None and pseudo_type is not None:
            if out: dtype="local"      
            ret.append(Node(type=dtype, name=i, pseudo_type=pseudo_type))
    return ret
        
        
class Custom_call2(Middleware):
    
    def __init__(self, vars, extfunc = [], not_declared={},  ext_func_inout={}, member_category={}):
        self.vars = vars
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
                    if  "message" in tree and  tree["message"] not in ("contains?", "index", "copyto"):
                        tree = transform_to_syntax_tree({"type": 'ExprStatNode', 'expr': tree})
                    else: 
                        return tree
                if not api:
                        raise translation_error('CyMLT doesn\' t support %s %s ' % (receiver_type, method),
                                                suggestions='CyMLT supports those %s functions\n  %s' % (
                          name, prepare_table(TYPED_API[receiver_type], ORIGINAL_METHODS.get(receiver_type)).strip()))
        if self.extfunc:
            for f in self.extfunc:
                if f.name == method:
                    trees = copy(tree)
                    args = []
                    z = ApsimExtraction()
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

                    if len(trees.args) != len(inps):
                        trees.args.extend(inps[len(trees.args):])
                    """if f.name == "Divide": 
                        print("Divideeeeeeee", [t.y for t in inps])
                        print("Divide", [t.y for t in trees.args])"""
                    for num1, ar1 in enumerate(trees.args):
                        for num2, ar2 in enumerate(inps):
                            if num1 == num2:
                                if ((ar1.type == "int" ) or (ar1.type=="local" and ar1.pseudo_type=="int")) and ar2.pseudo_type in ["float", "double"] :
                                    trees.args[num1] = Node(type="standard_method_call", receiver=trees.args[num1], args=[], message="float", pseudo_type="float")   

                    outs = deepcopy(self.ext_func_inout[f.name]["outputs"])
                    if outs:
                        if outs.type=="local" and "pos" in dir(outs):
                            reso = copy(outs)
                            reso.name = trees.args[outs.pos].name
                            res =  transform_to_syntax_tree({"type": 'assignment', "target":reso,'op':"=", 'value': trees})
                            return res
                        else:
                            if outs.type == "Tuple":
                                reso = deepcopy(outs)
                                for j, o in enumerate(reso.elements):
                                    if "pos" in dir(o):
                                        reso.elements[j].name = copy(trees.args)[o.pos].name
                                return transform_to_syntax_tree({"type": 'assignment', "target":reso,'op':"=", 'value': trees})
                            else:
                                return transform_to_syntax_tree({"type": 'assignment', "target":outs,'op':"=", 'value': trees})
                    z.getTypeNode(f, "implicit_return")
                    if not z.getTree:
                        print("TODODODODODODO")
                        return transform_to_syntax_tree({"type": 'ExprStatNode', 'expr': trees})
        return self.transform_default(tree)      
    

class CheckingInOut2(Middleware):
    
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
        self.newdecl = []
        Middleware.__init__(self)
              
    def process(self, tree):
        self.current_scope = self.current()
        self.name = tree.name
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
                #self.inputs.append(t_name) 
                
                self.newdecl.append({t_name:type_})
            
            self.env[-1][t_name] = type_
            self.outputs.append(t_name)
            
        elif "sequence" in dir(tree.target):
            t_name = tree.target.sequence.name
            type_ = tree.target.sequence.pseudo_type
            if t_name not in self.current_scope and not(isinstance(type_, list) and type_[0]=="array"):
                self.inputs.append(t_name)
            self.env[-1][t_name] = type_
            self.outputs.append(t_name)
        elif tree.target.type == "sliceindex":
            t_name = tree.target.receiver.name
            type_ = tree.target.receiver.pseudo_type
            if t_name not in self.current_scope:
                self.inputs.append(t_name)
            self.env[-1][t_name] = type_
            self.outputs.append(t_name)
        else:
            for elem in tree.target.elements:
                t_name = elem.name if "name" in dir(elem) else elem.sequence.name
                type_ = elem.pseudo_type
                self.outputs.append(t_name)
                self.env[-1][t_name] = type_
                
        
        if "op" in dir(tree) and tree.op != "=":
            if t_name not in self.current_scope:
                self.inputs.append(t_name)   
        
        self.current_scope = self.current()
        return tree
    
    def action_member_access(self, tree):
        newvar = tree.name + "_" + tree.member
        tree = Node(type="local", name=newvar, pseudo_type=tree.pseudo_type)
        if tree.name not in self.current_scope:# and tree.name  not in self.outputs:
            self.inputs.append(tree.name)
            self.env[-1][tree.name] = tree.type 
            self.current_scope = self.current()  
        return tree
    
    def action_custom_call(self, tree):
        if "namespace" in dir(tree):
            self.transform(tree.namespace)
        for arg in tree.args:
            self.transform(arg)
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
    
    def action_implicit_return(self, tree): 
        self.transform(tree.value)
        return tree
    
    def action_binary_op(self, tree):
        self.transform(tree.left)
        self.transform(tree.right)
        return tree
    
    #def action_elseif_statement(self, tree):
        #print("oooooooooooooooo")
        #return self.workflow(tree)

    #def action_else_statement(self, tree):
        #return self.workflow(tree)
        """type': 'for_statement', 
        'sequences': {'type': 'for_sequence', 
        'sequence': {'type': 'local', 'name': 'Values', 'pseudo_type': ['array', 'double']}}, 
        'iterators': {'type': 'for_iterator', 'iterator': {'type': 'local', 'name': 'Value', 'pseudo_type': 'double'
        """
    def action_for_iterator(self, tree):
        iterator = tree.iterator.name
        if iterator not in self.current_scope:
            self.env[-1][iterator] = tree.iterator.pseudo_type
            self.current_scope = self.current()
        return tree
    
    def action_for_statement(self, tree):
        return self.workflow(tree)

    def action_for_range_statement(self, tree):
        return self.workflow(tree)
    
    def action_while_statement(self, tree):
        return self.workflow(tree)

    def action_standard_call(self, tree):
        for arg in tree.args:
            self.transform(arg)
        return tree
        

class Local2(Middleware):
    
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
            pseudo_type = self.params[tree.name]
            tree.pseudo_type = pseudo_type
        return tree  

class Member_access2(Middleware):
    
    def __init__(self, totaltree, all_var):
        self.totaltree = totaltree
        self.all_var = all_var
        self.members = []
        self.m_cat = {}
        Middleware.__init__(self)
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_member_access(self, tree):
        if "." in tree.member and tree.name + "_" + tree.member.split(".")[0] in self.all_var :
            propert = tree.member.split(".")[-1]
            name = tree.name + "_" + tree.member.split(".")[0]
            type_ = pseudo_[self.all_var[name]]
            if isinstance(type_, list):
                type_ = type_[0]
            pseudo_type = self.all_var[name]
            if type_ in PROPERTY_API:
                rec = {"type":"local", "name": name, "pseudo_type":pseudo_type}
                api = PROPERTY_API[type_].get(propert)      
                if not api:
                    raise PseudoCythonTypeCheckError("Not implemented property , %s"%propert)  

                elif not isinstance(api, dict):
                    z = api.expand([rec])
                    return transform_to_syntax_tree(z)
        member = tree.member.replace(".", "_")
        name = tree.name + "_" + member
        pseudo = tree.pseudo_type
        tree.name = name
        self.members.append(tree)
        # retrieve the class name
        # retrieve the corresponding node in the totaltree
        # dtype: retrieve the datatype wwith the variable name
        # return {"type":"local", "name":name, "pseudo_type":dtype}
        if pseudo is None:
            return Node(type="local", name= name)
        else:
            return Node(type = "local", name =name, pseudo_type = pseudo_[self.all_var[name]])
        
class For_statement2(Middleware):
    
    def __init__(self):
        Middleware.__init__(self)
        self.declared = []
              
    def process(self, tree):
        return self.transform(tree,in_block=False)
    
    def action_for_statement(self, tree):
        """_summary_

        {'type': 'for_sequence', 
        'sequence': {'type': 'local', 'name': 'soilConstituentNames', 'pseudo_type': ['array', 'string']}}, 
        'iterators': {'type': 'for_iterator', 
        'iterator': {'type': 'local', 'name': 'constituentName', 'pseudo_type': 'var'}}
        """
        if tree.sequences.sequence.type == "ExprStatNode":
            if tree.sequences.sequence.expr.type == "standard_method_call" and tree.sequences.sequence.expr.message == "except":
                tree = Node(type="for_statement", 
                    sequences=Node(type='for_sequence',
                                    sequence = tree.sequences.sequence.expr.receiver), 
                    iterators=tree.iterators, 
                    block=Node(type ='if_statement',
                                test = Node(type ='standard_method_call',
                                            receiver = Node(type = "List",
                                                            pseudo_type =  ["List",tree.sequences.sequence.expr.args[0].pseudo_type[-1]],
                                                            elements = [r.init.value[0] for r in tree.sequences.sequence.expr.args]),
                                            message ='not contains?',
                                            args =[tree.iterators.iterator],
                                            pseudo_type = 'Boolean'), 
                                block = tree.block,
                                otherwise = []))
            
        
        iterator_pseudo_type = tree.iterators.iterator.pseudo_type
        if iterator_pseudo_type == "var":
            tree.iterators.iterator.pseudo_type = tree.sequences.sequence.pseudo_type[-1]
        self.declared.append(tree.iterators.iterator.name)
        return tree

dir_lib = Path(os.path.dirname(lib.__file__))
modelpath = ""
f_src=dir_lib/"apsim"
# get all csharp files in f_src directory
files = repowalk.walk(f_src, "cs" )
pkg = "" 
f_dest = os.path.join(modelpath,"src","f90",pkg,"list_sub.f90") 



def create_package(output):
    crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
    if not crop2ml_rep.isdir():
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not algo_rep.isdir():
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not cyml_rep.isdir():
        cyml_rep.mkdir()
    return crop2ml_rep, cyml_rep    
                



def function_dependency(st, f):
    r = [f]
    z = ApsimExtraction()
    while True:
        f = f if  isinstance(f, list) else [f]
        f_exts = [z.externFunction(st, n, False, n.name) for n in f]
        exts = list(itertools.chain(*f_exts))
        exs = [i for i in exts if i ]
        if exs:
            for ex in exs: 
                r.append(ex)
            f = exs
        else:
            break
    return r 


def translate(total_tree, varinfo, algo, not_declared,  res_inout={}, member_category={}, pa={}):
    """Transform specific nodes based on class of subnodes of node. It also allows to extract some usefull information. At finish
    the  modified node contains only the constructs of CyML and converted in CyML after applying translate_simple function.

    Args:
        total_tree (Node): ASG of all the component
        varinfo (Node): ASG of the Var info files

    Returns:
        ASG: transform algo
    """
    z = ApsimExtraction()
    funcs = z.externFunction(total_tree, algo)  
    funcs = [f for f in funcs if f]
    

    rr1 = Member_access2(total_tree, varinfo)
    vv1 = rr1.process(algo)
    
    rr1_ = Local2(params=pa)
    vv1_ = rr1_.process(vv1)

    ri2 = Index()
    vi2= ri2.process(vv1_)

    rr2 = Binary_op()
    vv2= rr2.process(vi2)

    rr3 = Assignment()
    vv3 = rr3.process(vv2)
    
    rr = Declarations()
    vv = rr.process(vv3)

    """rr = rr3 #Declarations()
    vv = vv3 #rr.process(vv3)"""

    rr4 = Custom_call2(total_tree, funcs, not_declared,  res_inout, member_category)
    vv4 = rr4.process(vv)
    
    expr = ExprStatNode(funcs,  res_inout)
    expr_ = expr.process(vv4)
    
    return  rr, expr_


from collections import defaultdict

def inst_dclass(meth):
    params = meth.params
    lst = []
    if params:
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

def run_apsim(component, output):
    """Transform an APSIM component in Crop2ML

    Args:
        component (_type_): Apsim component path
        output (_type_): Crop2ML package path
    """
    crop2ml_rep, cyml_rep = create_package(output)
    
    pkg = os.path.split(component)[-1].replace('-', '_')
    
    files = repowalk.walk(component, "cs" )
    xfiles = repowalk.walk(component, "xml" )
    modelp = ModelParser()
    mp = modelp.parse(component)
    res = {}
    stra = {}
    straNames = []
    varinfo = {}
    dclass = []
    domclass = []
    compo = {}
    source_codes=[]
    print(xfiles)
    for  k, v in files.items():
        print(v, "pmmmmmm")
        with open(v, 'r') as f:
            code = f.read()
        if code : # and k=="WheatLAIState.cs":
            if code.startswith("ï»¿"): code = code[3:]
            splitcode = code.split('\n')
            zz = map(lambda x: x.lstrip(), splitcode)
            codelist = [n  for n in zz if not n.startswith("#") ]
            code = "\n".join(codelist)
            dictasgt = to_dictASG(code,"cs")
            strAsg = to_CASG(dictasgt)
            res[k] = strAsg
            #print(dictasgt)
            m = ApsimExtraction()
            m.getTypeNode(strAsg, "classDef")
            g= m.getTree
            n = m.getmethod( g, "OnProcess")
            if g and g[0].base and  m.getmethod( g[0], "OnProcess"):
                if m.getmethod( g[0],"EstimateOfAssociatedClasses"):
                    compo[k] = strAsg
                else: 
                    stra[k]=strAsg
                    straNames.append(g[0].name)
                    source_codes.append(code)
                    print("strat", straNames)
            else:
                m.getTypeNode(strAsg, "interface")
                varinfo[k] = strAsg


    total_tree = list(res.values())
    vinfo = list(varinfo.values())
    strats = list(stra.values())
    compos = list(compo.values())
    models = []
    func_names = []
    kk = ApsimExtraction()
    #all_var = kk.getAllVar(vinfo)
    all_var = extract_io(list(xfiles.values())[0])
    #print("all", all_var)
    for k, st in enumerate(strats):
        print(k, st)
        mod = source_codes[k]
        #st_ = deepcopy(st)
        z = ApsimExtraction() 
        algo = z.getAlgo(st)
        init_ = z.getInit(st)
        funcs = z.externFunction(st, algo.block + init_.block, False) 
        funcs = [f for f in funcs if f]
        params_not_declared = {}
        params_not_declared_ = {}
        decl = {}
        member_category = {}   # member_category[func1] = {member1:instance1, member2: instance1, ...}
        
        res_inout = {}
        instance_dclass = {}  
                 
        if funcs:
            for f in funcs:
                r = []
                # order of function dependency
                f_dep = function_dependency(st, f)
                dep_ = list(reversed(f_dep))   
                dep = []
                dep_names = [] 
                for d in dep_:
                    if d.name not in dep_names:
                        dep.append(d)
                        dep_names.append(d.name)   
                for ex in dep:  # dep is the list of external function in the order of dependency
                    if ex.name not in func_names:  # to avoid duplicating dependent functions in different auxiliary functions
                        func = z.externFunction(total_tree, ex, False, ex.name)  
                        extfunc = [p for p in func if p]
                        if extfunc and isinstance(extfunc[0], list):
                            extfunc = list(itertools.chain(*extfunc)) 
                        for rr in extfunc:
                            if ex.class_!= rr.class_:
                                rr.name = "_" + rr.class_ + "__" + rr.name +"_" 
                                params_not_declared[rr.name]   = []     
                        res = []
                        res_ = []
                        res_inout[ex.name] = {"inputs":None, "outputs":None}
                        dclassdict = inst_dclass(ex)
                        #print("dclassdict", dclassdict)
                        f_rr1 = Member_access2(total_tree, all_var)
                        f1 = f_rr1.process(ex)
                        member_category[ex.name] = f_rr1.m_cat
                        #print("member_category", member_category)
                        ri2 = Index()
                        vi2= ri2.process(f1)
                        dr = Declarations()
                        dv = dr.process(vi2)
                        lr = Local2(dr.declnames)
                        lv = lr.process(dv)
                        
                        lr1 = For_statement2()
                        lv1 = lr1.process(lv)
                        params = [] if lv1.params is None  else lv1.params
                        args = dr.declnames + [p.name for p in params] if params else dr.declnames
                        not_declared = list(set(lr.not_declared) - set(args) - set(lr1.declared)) 
                        for n in not_declared:
                            if n in all_var:
                                tt = Node(type=type_[all_var[n]], name=n, pseudo_type=pseudo_[all_var[n]])
                                res.append(tt)
                                tt.type = "local"
                                res_.append(tt)
                        
                        params_names_not_declared = [p.name for p in res]
                        for fc in extfunc:
                             params_t = params_not_declared[fc.name]
                             for p in params_t:
                                 if p.name not in params_names_not_declared:
                                     res.append(p)
                                     res_.append(p)
                        #print("mmmmmmmmmmmmmmmmmmm",lv1.name,[r.name for r in res] )


                        params_not_declared[lv1.name] = res 
                        params_not_declared_[lv1.name] = res_ 
                        decl[lv1.name] = dr.declarations
                                  
                        name = lv1.name
                        instance_dclass[name]  = inst_dclass(lv1)  # before changing the signature

                        lv1.params =  params_not_declared[name] if lv1.params is None else lv1.params + params_not_declared[name]
                        if isinstance(lv1.block, Node): 
                            lv1.block = [decl[name], lv1.block]
                        else: lv1.block.insert(0,decl[name])
                        
                        trans_local = TransformLocal(params_not_declared[name])
                        r_trans_local = trans_local.process(lv1)
                        rr2 = Binary_op()
                        vv2= rr2.process(r_trans_local)
                        
                        rr4 = Custom_call2(total_tree, extfunc, params_not_declared_,  res_inout, member_category)
                        #rr4 = Custom_call(total_tree, extfunc, params_not_declared_,  res_inout, member_category)
                        p_cust = rr4.process(vv2)
                        
                        env = {xx.name:xx.pseudo_type for j in decl[name] for xx in j.decl}
                        zz = CheckingInOut2( env,isAlgo = False)
                        rch = zz.process(p_cust)
                                   
                        inputs_p_node, outputs_p_node = redefine_params(p_cust,all_var,member_category,zz.inputs, zz.outputs,extfunc, instance_dclass)
                        
                        p_cust.params = inputs_p_node# p_cust.params #+ transform_io(zz.inputs, all_var) if p_cust.params else transform_io(zz.inputs, all_var)
                        res_inout[name]["inputs"] = inputs_p_node 
                        
                        #name = rch.name
                        params = {p.name:p.pseudo_type for p in p_cust.params}
                        
                        lr = Local2(declnames=[], params=params)
                        lv = lr.process(p_cust)
                        #print("p_cust", lv.name, [p.name for p in lv.params])

                        outputs_node = outputs_p_node # transform_io(zz.outputs, all_var, True)
                        newinps = {p.name:i for i,p in enumerate(inputs_p_node)}
                        if lv.return_type == "Void":
                            if len(outputs_node) == 1:
                                lv.return_type = outputs_node[0].pseudo_type
                                return_ = Node(type = "implicit_return", value = Node(type = "local", pseudo_type = p_cust.return_type, name = outputs_node[0].name))    
                                if outputs_node[0].name in newinps.keys():
                                    return_ = Node(type = "implicit_return", value = Node(type = "local", pseudo_type = p_cust.return_type, name = outputs_node[0].name, pos = newinps[outputs_node[0].name]))
                            else:
                                lv.return_type = ["Tuple"] + [n.pseudo_type for n in outputs_node]     
                                return_ = Node(type = "implicit_return", value = Node(type = "Tuple", pseudo_type = p_cust.return_type, elements = outputs_node))
                            lv.block.append(return_)
                            res_inout[name]["outputs"] = return_.value
                        else:
                            if "modifiers" in dir(lv.block[-1]):
                                return_ = lv.block[-1].value
                                #print(lv.block[-1].y)
                                if return_.type == "local" and return_.name in newinps.keys():
                                    elts = []
                                    elts.append(Node(type = "local", pseudo_type = lv.return_type, name = return_.name, pos = newinps[return_.name]))
                                    #print("ggggggggggggggggggggggggggggggggggggggM", lv.name, newinps[return_.name], return_.name)
                                    for o in outputs_node:
                                        if o.name in newinps.keys() and o.name != return_.name and o.name in all_var and o.name not in dr.declnames:
                                            elts.append(Node(type = "local", pseudo_type = o.pseudo_type, name = o.name, pos = newinps[o.name]))
                                            #print("gggggggggggggggggggggggggggggggggggggg", lv.name, newinps[o.name], o.name)
                                        elif o.name != return_.name and o.name in all_var and o.name not in dr.declnames:
                                            elts.append(o)
                                    if len(elts) == 1:
                                        return_ = elts[0]
                                    else:
                                        return_ = Node(type = "Tuple", pseudo_type = ["Tuple"]+[e.pseudo_type for e in elts], elements = elts)
                                    lv.block[-1] = Node(type = "implicit_return", value = return_)
                                    #print("################################", o.name, lv.block[-1].y)
                                else:
                                    elts = []
                                    r_outs = [o.name for o in return_.elements]
                                    for o in outputs_node:
                                        if o.name in r_outs and o.name in newinps.keys():
                                            elts.append(Node(type = "local", pseudo_type = o.pseudo_type, name = o.name, pos = newinps[o.name]))
                                        elif o.name in r_outs:
                                            elts.append(Node(type = "local", pseudo_type = o.pseudo_type, name = o.name))
                                        elif o.name not in r_outs:
                                            elts.append(o)
                                    return_ = Node(type = "Tuple", pseudo_type = lv.return_type, elements = elts)
                                    lv.block[-1] = Node(type = "implicit_return", value = return_)
                                    lv.return_type = ["Tuple"] + [n.pseudo_type for n in outputs_node]                                    
                                res_inout[name]["outputs"] = return_
                        """else:
                            res_inout[name]["outputs"] = outputs_node"""
                            
                                     
                        r.append(lv)
                        func_names.append(p_cust.name)
                        

                cd = cs_cyml.Cs_Cyml_ast(r)
                h = cd.transform()
                nd = transform_to_syntax_tree(h)
                code = writeCyml(nd) 
                filename = Path(os.path.join(cyml_rep, "%s.pyx"%(name)))
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))

        rr, vv = translate(total_tree, all_var, algo.block, params_not_declared_, res_inout, member_category)
              
        cd = cs_cyml.Cs_Cyml_ast(vv)
        h = cd.transform()
        nd = transform_to_syntax_tree(h)
        code = writeCyml(nd)
        filename = Path(os.path.join(cyml_rep, "%s.pyx"%(straNames[k])))
        with open(filename, "wb") as tg_file:
            tg_file.write(code.encode('utf-8'))

        if init_:
            rr_, init_pseudo = translate(total_tree, z.dclassdict, init_.block, params_not_declared_, res_inout, member_category)
            dict_init = {}
            name_i = "init."+straNames[k]
            dict_init["name"] = "init"
            dict_init["filename"] = "algo/pyx/" + name_i + ".pyx"
            #z.model.initialization = [dict_init]
            cd = cs_cyml.Cs_Cyml_ast(rr_.declarations + init_pseudo,  var =all_var)
            h = cd.transform()
            nd = transform_to_syntax_tree(h)
            initcode = writeCyml(nd)
            filename = Path(os.path.join(cyml_rep, "init_%s.pyx"%(straNames[k])))
            with open(filename, "wb") as tg_file:
                tg_file.write(initcode.encode('utf-8'))
        
    description = {"Title":"model of soil", "Authors":"Cyrille", "Institution":"INRAE" } 
    description["name"]= "Soiltemp"
    description["version"]="2.0"
    description["timestep"]="1.0"
    description["url"] = ""
    description["ExtendedDescription"]="Soil Temperature"
    description["ShortDescription"]="Soil Temperature"
    mc = createObjectCompo(description,mp)

    xml_ = Pl2Crop2ml(mc, "APSIM_").run_compo()
    filename = os.path.join(pkg, "crop2ml", "composition.%s.xml"%(mp[0].name))
    with open(filename, "wb") as xml_file:
        r = '<?xml version="1.0" encoding="UTF-8"?>\n'
        r += '<!DOCTYPE ModelComposition PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">\n'
        r += xml_.unicode(indent=4)#.encode('utf-8')
        xml_file.write(r.encode())