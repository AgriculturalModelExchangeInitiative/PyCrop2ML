from __future__ import absolute_import
from __future__ import print_function

import os
from os.path import isdir
from path import Path

from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.simplace.simplaceExtraction import SimplaceExtraction
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from pycropml.transpiler.antlr_py.java.java_preprocessing import Declarations, MemberAcess, Custom_call, Local, Assignment
from pycropml.transpiler.antlr_py.java import java_cyml
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.to_specification import extractcomments, createObjectCompo
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml, generate_compositefile, generate_unitfile, create_repo
from pycropml.transpiler.antlr_py.codeExtraction import remove
import itertools


def function_dependency(st, f):
    r = [f]
    z = SimplaceExtraction()
    while True:
        f = f if  isinstance(f, list) else [f]
        print("fffffffff", f)
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



def translate(algo, names):
    
    f = Declarations([], {},names)
    r = f.process(algo)
    
    ass = Assignment()
    r_ass = ass.process(r)
    
    n = Custom_call(f.kvnames)
    m = n.process(r_ass)

    h = Local(f.kvnames)
    v = h.process(m)

    g = MemberAcess()
    s = g.process(v)
    if not s: s = []
    nodes = f.declarations + s

    cd = java_cyml.Java_Cyml_ast(nodes)
    h = cd.transform()
    nd = transform_to_syntax_tree(h)
    zcode = writeCyml(nd)
    return zcode




def translate_f(algo, names):
    f = Declarations([], {},names)
    r = f.process(algo)
    
    ass = Assignment()
    r_ass = ass.process(r)
    
    n = Custom_call(f.kvnames)
    m = n.process(r_ass)

    h = Local(f.kvnames)
    v = h.process(m)

    g = MemberAcess()
    s = g.process(v)
    
    nodes = s

    cd = java_cyml.Java_Cyml_ast(nodes)
    h = cd.transform()
    nd = transform_to_syntax_tree(h)
    zcode = writeCyml(nd)
    return zcode

def run_simplace(components, output):
    compositeStrat = []
    simpleStrat= Path(components).glob('*.java')
    compositeStrats = Path(components).glob('*.xml')
    if compositeStrats: 
        compositeStrat = compositeStrats[0] 
    crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
    if not isdir(crop2ml_rep):
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not isdir(algo_rep):
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not isdir(cyml_rep):
        cyml_rep.mkdir()
    models = []
    p = SimplaceExtraction()
    auxiliary = {}
    func_names = []
    if compositeStrat:
        auxiliary = p.getAuxiliary(compositeStrat)
    for strat in simpleStrat:
        print(strat)
        with open(strat, "r") as f:
            code = f.read()
            
        code = remove(code, "//%%CyML Ignore Begin%%", "//%%CyML Ignore End%%")
        
        com = extractcomments(code, ["//"], ["/*", "*/"])
        #com_meta_info_part = list(extractcomments(code, ["/&&&"], ["/**", "*/"]).values())[0]
        dictasgt = to_dictASG(code,"java", com)
        strAsg = to_CASG(dictasgt)

        mm = SimplaceExtraction()
        mm.modelunit(strAsg, auxiliary)
        mm.model.description

        names = [ j.name for j in mm.model.inputs + mm.model.outputs]   
        algo = mm.getProcess(strAsg)
        init = mm.getInit(strAsg)
        funcs = mm.externFunction(strAsg, [algo] + [init], False) 
         
        algocode = translate(algo.block, names)
        initcode = translate(init.block, names)
        
        if init and init.block:
            dict_init = {}
            name_i = "init."+ mm.model.name
            dict_init["name"] = "init"
            dict_init["filename"] = "algo/pyx/" + name_i + ".pyx"
            mm.model.initialization = [dict_init]
            filename = Path(os.path.join(cyml_rep, "init.%s.pyx"%(mm.model.name)))
            with open(filename, "wb") as tg_file:
                tg_file.write(initcode.encode('utf-8'))    
        
        filename = Path(os.path.join(cyml_rep, "%s.pyx"%(mm.model.name)))
        with open(filename, "wb") as tg_file:
            tg_file.write(algocode.encode('utf-8'))
        funcs = [f for f in funcs if f]
        if funcs:
            for f in funcs:
                if f:
                    r = []
                    # order of function dependency
                    f_dep = function_dependency(strAsg, f)
                    dep_ = list(reversed(f_dep))   
                    dep = []
                    dep_names = [] 
                    print("dep_", dep_)
                    for d in dep_:
                        if d.name not in dep_names:
                            dep.append(d)
                            dep_names.append(d.name)   
                    for ex in dep:  # dep is the list of external function in the order of dependency
                        if ex.name not in func_names:  # to avoid duplicating dependent functions in different auxiliary functions
                            func = mm.externFunction(strAsg, ex, False, ex.name)  
                            extfunc = [p for p in func if p]
                            if extfunc and isinstance(extfunc[0], list):
                                extfunc = list(itertools.chain(*extfunc)) 
                        r.append(ex)
                        func_names.append(ex.name)  
                    cd = java_cyml.Java_Cyml_ast(r)
                    h = cd.transform()
                    nd = transform_to_syntax_tree(h)
                    code = writeCyml(nd) 
                    filename = Path(os.path.join(cyml_rep, "%s.pyx"%(f.name)))
                    with open(filename, "wb") as tg_file:
                        tg_file.write(code.encode('utf-8'))
                    mm.model.function.append(f.name)
                            
                            
        
        models.append(mm.model)
        
                
        
        xml_ = Pl2Crop2ml(mm.model, "Simplace.SoilTemp").run_unit()               
        filename = os.path.join(output,  "crop2ml", "unit.%s.xml"%(mm.model.name)) # "unit.%s.xml"%(strat.basename().split(".")[0])
        with open(filename, "wb") as xml_file:
            r = '<?xml version="1.0" encoding="UTF-8"?>\n'
            r += '<!DOCTYPE ModelUnit PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelUnit.dtd">\n'
            r += xml_.unicode(indent=4)#.encode('utf-8')
            xml_file.write(r.encode())

    op_extr = SimplaceExtraction()
    if compositeStrat: 
        mc = op_extr.modelcomposition(compositeStrat, models)  
        generate_compositefile(output, mc, mc.name)
    else:
        description = {}
        description["name"]=mm.model.name+"_"
        description["version"]=mm.model.version
        description["timestep"]=mm.model.timestep
        description["url"] = ""
        description["Authors"]=mm.model.description.Authors
        description["Reference"]=mm.model.description.Reference
        description["ShortDescription"]=mm.model.description.ShortDescription
        description["ExtendedDescription"]=mm.model.description.ExtendedDescription
        description["Institution"]=mm.model.description.Institution
        mc = createObjectCompo(description,models)
        xml_ = Pl2Crop2ml(mc, "Simplace_").run_compo()
        filename = os.path.join(output, "crop2ml", "composition.%s.xml"%(mm.model.name))
        with open(filename, "wb") as xml_file:
            r = '<?xml version="1.0" encoding="UTF-8"?>\n'
            r += '<!DOCTYPE ModelComposition PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">\n'
            r += xml_.unicode(indent=4)#.encode('utf-8')
            xml_file.write(r.encode())





