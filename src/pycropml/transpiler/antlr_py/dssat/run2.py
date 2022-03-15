from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_dictASG ,to_CASG
from pycropml.transpiler.antlr_py.dssat.dssatExtraction2 import DssatExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py.fortran import f90_cyml


""" Read DSSAT component and infer Crop2ML model

"""

def process_dssat(routines, output):
    compositeStrat= routines.glob('*Component.f90')[0]
    simpleStrat = [f for f in routines.glob('*.f90')  if (f not in compositeStrat and not f.endswith("list_sub.f90"))]
    crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
    if not crop2ml_rep.isdir():
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not algo_rep.isdir():
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not cyml_rep.isdir():
        cyml_rep.mkdir()
    with open(compositeStrat, 'r' ) as fil:
        codecompo = fil.read()
    compodict = to_dictASG(codecompo, 'f90')
    compo = to_CASG(compodict)
    models = []
    for strat in simpleStrat:
        with open(strat, 'r' ) as fil:
            code = fil.read()
        print(strat)
        dictstr =to_dictASG(code,'f90')
        strAsg = to_CASG(dictstr)
        z = DssatExtraction()  
        z.modelunit(strat,strAsg)  
        v = z.model.inputs + z.model.outputs 
        var = [vi.name for vi in v]   
        algo = z.getSubroutine(strAsg)
        if algo :
            for f in algo:
                if f.name.startswith("model"): 
                    cd = f90_cyml.F90_Cyml_ast(f.block, var = var)
                    h = cd.transform()
                    nd = transform_to_syntax_tree(h)
                    code = writeCyml(nd)
                    filename = Path(os.path.join(cyml_rep, "%s.pyx"%(strat.basename().split(".")[0])))
                    with open(filename, "wb") as tg_file:
                        tg_file.write(code.encode('utf-8'))
                    models.append(z.model)
                    xml_ = Pl2Crop2ml(z.model, "Dssat.Pheno_Pkg").run_unit()
                    filename = Path(os.path.join(crop2ml_rep, "unit.%s.xml"%(strat.basename().split(".")[0])))
                    with open(filename, "wb") as xml_file:
                        xml_file.write(xml_.unicode(indent=4).encode('utf-8'))
                
                else:
                    nd = transform_to_syntax_tree(f)
                    code = writeCyml(nd)
                    filename = Path(os.path.join(cyml_rep, "%s.pyx"%(f.name)))
                    with open(filename, "wb") as tg_file:
                        tg_file.write(code.encode('utf-8'))
    z.modelcomposition(compositeStrat, models, compo)
    xml_ = Pl2Crop2ml(z.mc, "Dssat.Pheno_Pkg").run_compo()
    name = z.mc.name[:-9] if z.mc.name.endswith("Component") else z.mc.name
    filename = Path(os.path.join(crop2ml_rep, "composition.%s.xml"%(name)))
    with open(filename, "wb") as xml_file:
        xml_file.write(xml_.unicode(indent=4).encode('utf-8'))
    
    return 0

