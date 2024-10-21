# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
import os
from os.path import isdir
from path import Path
from copy import deepcopy
from typing import *

from collections import defaultdict

from pycropml.transpiler.antlr_py.to_CASG import to_dictASG, to_CASG
from pycropml.transpiler.antlr_py.bioma.biomaExtraction import BiomaExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.csharp import cs_cyml
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py import repowalk

from pycropml.transpiler.antlr_py.csharp.csharp_preprocessing import ExprStatNode, TransformLocal, CheckingInOut, Custom_call, Declarations,Assignment, Member_access, Binary_op, Index, Local

""" Read BioMA component and extract metadata

"""

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

pseudo_type_={
    "DOUBLE":"double",
    "INT":"int",
    "STRING":"string",
    "DATE":"date",
    "DOUBLELIST":["List", "double"],
    "INTLIST":["List", "int"],
     "STRINGLIST":["List", "string"],
     "DATELIST":["List", "date"],
    "BOOLEAN":"bool",
    "DOUBLEARRAY":["array", "double"],
    "INTARRAY":["array", "int"]}
    
    
    

def create_package(output):
    crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
    if not isdir(crop2ml_rep):
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not isdir(algo_rep):
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not isdir(cyml_rep):
        cyml_rep.mkdir()
    return crop2ml_rep, cyml_rep    
                




def redefine_params(m:Node, var_:Tuple, member_category, inputs, outputs)->List[Node]:
    """It allows to change all parameters which are instance of domain class with the explicit attributes required

    Args:
        m (Node): Auxiliary function ASG
        var_ (Tuple): Metadata from strategy classes and varinfo files: (inputs, parameters, outputs) 
        member_category (_type_): _description_
        inputs (List[str]): Parameter names of the auxiliary function. It can be an instance of domain class

    Returns:
        List[Node]: New parameters nodes
    """
    name = m.name
    inputs_p_node = []
    outputs_p_node = []
    for p in m.params:
        if p.pseudo_type not in list(pseudo_type_.values()) :
            # find the inputs whose instance is p.name
            inputs_p = [key for key, val in member_category[name].items() if val==p.name]
                        # find its datatype
            for p_ in set(inputs):
                if p_ in inputs_p:
                    vn = p_[:-3] if (len(p_)>3 and p_.endswith("_t1")) else p_
                    for m_inp in var_[0] + var_[2]:
                        if m_inp["Name"].decode("utf-8") == vn:
                            inputs_p_node.append(Node(type=type_[m_inp['ValueType']], name=p_, pseudo_type=pseudo_type_[m_inp['ValueType']]))
                            
            for p_ in set(outputs):
                if p_ in inputs_p:
                    vn = p_[:-3] if (len(p_)>3 and p_.endswith("_t1")) else p_
                    for m_inp in var_[0] + var_[2]:
                        if m_inp["Name"].decode("utf-8") == vn:
                            outputs_p_node.append(Node(type= "local", name=p_, pseudo_type=pseudo_type_[m_inp['ValueType']]))
        else:
            inputs_p_node.append(p) 
    return  inputs_p_node, outputs_p_node






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




def translate(total_tree, varinfo, algo, not_declared,  res_inout={}, member_category={}, instance_dclass={}):
    """Transform specific nodes based on class of subnodes of node. It also allows to extract some usefull information. At finish
    the  modified node contains only the constructs of CyML and converted in CyML after applying translate_simple function.

    Args:
        total_tree (Node): ASG of all the component
        varinfo (Node): ASG of the Var info files

    Returns:
        ASG: transform algo
    """
    z = BiomaExtraction()
    funcs = z.externFunction(total_tree, algo)  
    funcs = [f for f in funcs if f]
    
    rr1 = Member_access(total_tree, varinfo)
    vv1 = rr1.process(algo)

    ri2 = Index()
    vi2= ri2.process(vv1)

    rr2 = Binary_op()
    vv2= rr2.process(vi2)

    rr3 = Assignment()
    vv3 = rr3.process(vv2)

    rr = Declarations()
    vv = rr.process(vv3)

    rr4 = Custom_call(total_tree, funcs, not_declared,  res_inout, member_category, instance_dclass)
    vv4 = rr4.process(vv)
    
    expr = ExprStatNode(funcs,  res_inout)
    expr_ = expr.process(vv4)
    
    return  rr, expr_


def translate_(f, pa):
    res = []
    res_ = []
    dr = Declarations()
    dv = dr.process(f)
    lr = Local(dr.declnames)
    lv = lr.process(dv)
    params = [str(p.name) for p in f.params]
    args = params + dr.declnames
    not_declared = list(set(lr.not_declared) - set(args))
    for n in not_declared:
        for m in pa:
            if m["Name"].decode("utf-8") == n:
                r = Node(type=type_[m['ValueType']], name=n, pseudo_type=pseudo_type_[m['ValueType']])
                res.append(r)
                r.type = "local"
                res_.append(r)
                break
    return lv, dr.declarations, res_

def run_bioma(component, output):
    """Transform a BioMA component in Crop2ML

    Args:
        component (_type_): bioma component path
        output (_type_): Crop2ML package path
    """
    crop2ml_rep, cyml_rep = create_package(output)
    
    pkg = os.path.split(component)[-1].replace('-', '_')
    
    files = repowalk.walk(component, "cs" )
    res = {}
    stra = {}
    straNames = []
    varinfo = {}
    dclass = []
    domclass = []
    compo = ""
    for  k, v in files.items():
        #print(v)
        with open(v, 'r') as f:
            code = f.read()
        if code : # and k=="WheatLAIState.cs":
            if code.startswith("ï»¿"): code = code[3:]
            splitcode = code.split('\n')
            zz = map(lambda x: x.lstrip(), splitcode)
            codelist = [n  for n in zz if not n.startswith("#") ]
            code = "\n".join(codelist)
            print(k)
            dictasgt = to_dictASG(code,"cs")
            strAsg = to_CASG(dictasgt)
            res[k] = strAsg
            
            m = BiomaExtraction()
            m.getTypeNode(strAsg, "classDef")
            g= m.getTree
            n = m.getmethod( g, "Estimate")
            if g and g[0].base and  m.getmethod( g[0], "Estimate"):
                if m.getmethod( g[0],"EstimateOfAssociatedClasses"):
                    compo = strAsg
                else: 
                    stra[k] = strAsg
                    straNames.append(g[0].name)

            elif g and g[0].base and g[0].base[0].type=="IVarInfoClass":
                varinfo[k] = strAsg
            
            elif g and g[0].base and len(g[0].base) ==2  and g[0].base[1]=="IDomainClass" :
                dclass.append(strAsg)
                
    total_tree = list(res.values())
    vinfo = list(varinfo.values())
    strats = list(stra.values())
    models = []
    func_names = []
    kk = BiomaExtraction()
    all_var = kk.getAllVar(vinfo, dclass)
    for k, st in enumerate(strats):
        print(k, st)
        #st_ = deepcopy(st)
        z = BiomaExtraction() 
        description = z.description(st)  
        var_ = z.getFromVarInfo(st,vinfo, dclass)
        past_cur = z.instancePastCurrent(st) 
        
        pc = z.prec_cur_states(st, past_cur)

        var =  z.totalvar(st)
        algo = z.getAlgo(st)
        funcs = z.externFunction(st, algo.block)  
        funcs = [f for f in funcs if f]
        strat_var = z.getStrategyVar(st)
        pa = strat_var[0]
        dict_pa = {f["Name"].decode("utf-8"):f for f in pa}
        
        all_var_pa = {**dict_pa, **all_var}   # all the variable from all varinfo files and parameters of the specific strategy.
        params_not_declared = {}
        params_not_declared_ = {}
        decl = {}
        member_category = {}   # member_category[func1] = {member1:instance1, member2: instance1, ...}
        
        res_inout = {}
        instance_dclass = {}
        if funcs:
            for f in funcs:
                res = []
                res_ = []
                f_rr1 = Member_access(total_tree, inst_dclass(f))
                f_vv1 = f_rr1.process(f)
                member_category[f.name] = f_rr1.m_cat
                ri2 = Index()
                vi2= ri2.process(f_vv1)
                dr = Declarations()
                dv = dr.process(vi2)
                lr = Local(dr.declnames)
                lv = lr.process(dv)
                params = [str(p.name) for p in lv.params]
                args = params + dr.declnames
                not_declared = list(set(lr.not_declared) - set(args))
                for n in not_declared:
                    for m in pa:
                        if m["Name"].decode("utf-8") == n:
                            r = Node(type=type_[m['ValueType']], name=n, pseudo_type=pseudo_type_[m['ValueType']])
                            res.append(r)
                            r.type = "local"
                            res_.append(r)
                            break
                params_not_declared[lv.name] = res
                params_not_declared_[lv.name] = res_
                decl[lv.name] = dr.declarations
    
                name = lv.name
                instance_dclass[name]  = inst_dclass(lv)  # before changing the signature
                res_inout[name] = {"inputs":None, "outputs":None}
                #z.model.function.append(name)
                lv.params = lv.params + params_not_declared[name]
                lv.block.insert(0,decl[name])
                trans_local = TransformLocal(params_not_declared[name])
                r_trans_local = trans_local.process(lv)
                rr2 = Binary_op()
                vv2= rr2.process(r_trans_local)
                cust = Custom_call(total_tree, not_declared=params_not_declared[name])
                p_cust = cust.process(vv2)
                
                env = {xx.name:xx.pseudo_type for j in decl[name] for xx in j.decl}
                zz = CheckingInOut(env)
                r_ch = zz.process(p_cust)
                
                inputs_p_node, outputs_p_node = redefine_params(p_cust,var_, member_category,zz.inputs, zz.outputs)
                p_cust.params = inputs_p_node  
                res_inout[name]["inputs"] = inputs_p_node 
                #print("************", name, member_category)
                if p_cust.return_type == "Void":
                    if len(outputs_p_node) == 1:
                        p_cust.return_type = outputs_p_node[0].pseudo_type
                        return_ = Node(type = "implicit_return", value = Node(type = "local", pseudo_type = p_cust.return_type, name = outputs_p_node[0].name))    
                    else:
                        p_cust.return_type = ["Tuple"] + [n.pseudo_type for n in outputs_p_node]     
                        return_ = Node(type = "implicit_return", value = Node(type = "Tuple", pseudo_type = p_cust.return_type, elements = outputs_p_node))
                    p_cust.block.append(return_)
                    res_inout[name]["outputs"] = return_.value
                
                r = [p_cust]
                
                while True:
                    func = f
                    f = f if  isinstance(f, list) else [f]
                    exts = [z.externFunction(st, n, False, n.name) for n in f][0]
                    exs = [i for i in exts if i ]
                    if exs:
                        for ex in exs:
                            if ex.name not in func_names:  # to avoid duplicating dependant functions in different auxiliary functions
                                res = []
                                res_ = []
                                res_inout[ex.name] = {"inputs":None, "outputs":None}
                                
                                dclassdict = inst_dclass(ex)
                                f_rr1 = Member_access(total_tree, dclassdict)
                                f_vv1 = f_rr1.process(ex)
                                ri2 = Index()
                                vi2= ri2.process(f_vv1)
                                dr = Declarations()
                                dv = dr.process(vi2)
                                lr = Local(dr.declnames)
                                lv = lr.process(dv)
                                                              
                                params = [str(p.name) for p in lv.params]
                                               
                                args = params + dr.declnames
                                not_declared = list(set(lr.not_declared) - set(args))
                                for n in not_declared:
                                    for mm in pa:
                                        if mm["Name"].decode("utf-8") == n:
                                            tt = Node(type=type_[mm['ValueType']], name=n, pseudo_type=pseudo_type_[mm['ValueType']])
                                            res.append(tt)
                                            tt.type = "local"
                                            res_.append(tt)
                                            break
                                params_not_declared[lv.name] = res
                                params_not_declared_[lv.name] = res_

                                trans_local = TransformLocal(params_not_declared[lv.name])
                                r_trans_local = trans_local.process(lv)
                                rr2 = Binary_op()
                                vv2= rr2.process(r_trans_local)
                                cust = Custom_call(total_tree, not_declared=params_not_declared[lv.name])
                                p_cust = cust.process(vv2)

                                env = {xx.name:xx.pseudo_type for j in dr.declarations for xx in j.decl}
                                zz = CheckingInOut(env)
                                r_ch = zz.process(p_cust)
                                member_category[p_cust.name] = f_rr1.m_cat

                                inputs_p_node, outputs_p_node = redefine_params(p_cust,var_, member_category,zz.inputs, zz.outputs)
                                p_cust.params = inputs_p_node 
                                res_inout[p_cust.name]["inputs"] = inputs_p_node   

                                if p_cust.return_type == "Void":
                                    if len(outputs_p_node) == 1:
                                        p_cust.return_type = outputs_p_node[0].pseudo_type
                                        return_ = Node(type = "implicit_return", value = Node(type = "local", pseudo_type = p_cust.return_type, name = outputs_p_node[0].name))    
                                    else:
                                        lv.return_type = ["Tuple"] + [n.pseudo_type for n in outputs_p_node]     
                                        return_ = Node(type = "implicit_return", value = Node(type = "Tuple", pseudo_type = p_cust.return_type, elements = outputs_p_node))
                                    p_cust.block.append(return_)
                                    res_inout[p_cust.name]["outputs"] = return_.value
                                    
                                p_cust.params = p_cust.params + res
                                p_cust.block.insert(0,dr.declarations)
                                r.append(p_cust)
                                func_names.append(p_cust.name)   # to avoid duplicating dependant functions in different auxiliary functions
                         
                        f = exs
                    else:
                        break
                
                #print(z.dclassdict)
                #rr1 = Member_access(total_tree, z.dclassdict)
                #vv1 = rr1.process(r)
                
                cd = cs_cyml.Cs_Cyml_ast(r)
                h = cd.transform()
                nd = transform_to_syntax_tree(h)
                code = writeCyml(nd) 
                filename = Path(os.path.join(cyml_rep, "%s.pyx"%(name)))
                with open(filename, "wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))

        rr, vv = translate(total_tree, z.dclassdict, algo.block, params_not_declared_, res_inout, member_category, instance_dclass)
        

        env = {m.name:m.pseudo_type for j in rr.declarations for m in j.decl}
        zz = CheckingInOut(env)
        r_ch = zz.process(vv)
       
    
        z.modelunit(description, var_, all_var_pa,var,  list(set(zz.inputs)), list(set(zz.outputs)))
        #print(z.model.name, list(set(mod_inputs)))
        z.model.function = [n.name for n in funcs if f]
        models.append(z.model)
        
        #print(z.model.name,set(zz.inputs) )
     
        cd = cs_cyml.Cs_Cyml_ast(rr.declarations + vv,  var =var)
        h = cd.transform()
        nd = transform_to_syntax_tree(h)
        code = writeCyml(nd)
         
        filename = Path(os.path.join(cyml_rep, "%s.pyx"%(straNames[k])))
        with open(filename, "wb") as tg_file:
            tg_file.write(code.encode('utf-8'))
        
        xml_ = Pl2Crop2ml(z.model, "Crop2ML."+pkg).run_unit() 
        filename = Path(os.path.join(crop2ml_rep, "unit.%s.xml"%(straNames[k])))
        with open(filename, "wb") as xml_file:
            #xml_file.write(xml_.unicode(indent=4).encode('utf-8'))
            r = '<?xml version="1.0" encoding="UTF-8"?>\n'
            r += '<!DOCTYPE ModelUnit PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelUnit.dtd">\n'
            r += xml_.unicode(indent=4)#.encode('utf-8')
            xml_file.write(r.encode())
           
    z.modelcomposition(models,compo)
    xml_ = Pl2Crop2ml(z.mc, "Crop2ML."+pkg).run_compo()
    name = z.mc.name[:-9] if z.mc.name.endswith("Component") else z.mc.name
    filename = Path(os.path.join(crop2ml_rep, "composition.%s.xml"%(name)))
    with open(filename, "wb") as xml_file:
        #xml_file.write(xml_.unicode(indent=4).encode('utf-8'))
        r = '<?xml version="1.0" encoding="UTF-8"?>\n'
        r += '<!DOCTYPE ModelComposition PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">\n'
        r += xml_.unicode(indent=4)#.encode('utf-8')
        xml_file.write(r.encode())
        
        
        

        
                    
                
            
                

