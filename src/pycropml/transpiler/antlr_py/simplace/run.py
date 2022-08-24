from __future__ import absolute_import
from __future__ import print_function

from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.simplace.simplaceExtraction import SimplaceExtraction
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from pycropml.transpiler.antlr_py.java.java_preprocessing import Declarations, MemberAcess, Custom_call, Local, Assignment
from pycropml.transpiler.antlr_py.java import java_cyml
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.to_specification import extractcomments
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml, generate_compositefile, generate_unitfile, create_repo
from pycropml.transpiler.antlr_py.codeExtraction import remove






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
    
    nodes = f.declarations + s

    cd = java_cyml.Java_Cyml_ast(nodes)
    h = cd.transform()
    
    print(h)
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
    simpleStrat= Path(components).glob('*.java')
    compositeStrat = Path(components).glob('*.xml')[0]
    crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
    if not crop2ml_rep.isdir():
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not algo_rep.isdir():
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not cyml_rep.isdir():
        cyml_rep.mkdir()

    for strat in simpleStrat:
        print(strat)
        with open(strat, "r") as f:
            code = f.read()
            
        code = remove(code, "//%%CyML Ignore Begin%%", "//%%CyML Ignore End%%")
        
        com = extractcomments(code, ["//"], ["/*", "*/"])
        dictasgt = to_dictASG(code,"java", com)
        strAsg = to_CASG(dictasgt)

        mm = SimplaceExtraction()
        mm.modelunit(strAsg)
        mm.model.description

        names = [ j.name for j in mm.model.inputs + mm.model.outputs]   
        algo = mm.getProcess(strAsg)
        init = mm.getInit(strAsg)
         
        algocode = translate(algo.block, names)
        initcode = translate(init.block, names)
        
        if init and init.block:
            dict_init = {}
            name_i = "init."+ mm.model.name
            dict_init["name"] = "init"
            dict_init["filename"] = "algo/pyx/" + name_i + ".pyx"
            mm.model.initialization = [dict_init] 
        
        filename = Path(os.path.join(cyml_rep, "%s.pyx"%(mm.model.name)))
        with open(filename, "wb") as tg_file:
            tg_file.write(algocode.encode('utf-8'))

        filename = Path(os.path.join(cyml_rep, "init.%s.pyx"%(mm.model.name)))
        with open(filename, "wb") as tg_file:
            tg_file.write(initcode.encode('utf-8'))          
        
        funcs = mm.externFunction(strAsg, algo)
        if funcs:
            for m in funcs:
                if m:
                    mm.model.function.append(m.name)
                    code = translate_f(m, [])
                    filename = Path(os.path.join(cyml_rep, "%s.pyx"%(m.name)))
                    with open(filename, "wb") as tg_file:
                        tg_file.write(code.encode('utf-8'))
        
       
        xml_ = Pl2Crop2ml(mm.model, "Simplace.SoilTemp").run_unit()               
        filename = os.path.join(output,  "crop2ml", "unit.%s.xml"%(mm.model.name)) # "unit.%s.xml"%(strat.basename().split(".")[0])
        with open(filename, "wb") as xml_file:
            r = '<?xml version="1.0" encoding="UTF-8"?>\n'
            r += '<!DOCTYPE ModelUnit PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelUnit.dtd">\n'
            r += xml_.unicode(indent=4)#.encode('utf-8')
            xml_file.write(r.encode())

    op_extr = SimplaceExtraction() 
    mc = op_extr.modelcomposition(compositeStrat)  
    generate_compositefile(output, mc, mc.name)





