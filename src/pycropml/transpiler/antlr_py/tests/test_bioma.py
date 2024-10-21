
from __future__ import absolute_import
from __future__ import print_function
import os
from os.path import isdir
from path import Path
from pycropml.transpiler.antlr_py.to_CASG import to_dictASG, to_CASG
from pycropml.transpiler.antlr_py.bioma.biomaExtraction import BiomaExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.csharp import cs_cyml
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml

""" Read BioMA component and extract metadata

"""

cwd = Path(__file__).dirname()
data = cwd/'examples'/'SiriusComponent'/'phenology'/'Strategies'

compositeStrat= data.glob('*Component.cs')[0]
simpleStrat = [f for f in data.glob('*.cs')  if f not in compositeStrat]

data = cwd/'examples'/'SiriusComponent'/'phenology'/'DomainClass'
varInfo = data.glob('*VarInfo.cs')

output = cwd/'examples'/'SiriusComponent'/'phenology'
crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
if not isdir(crop2ml_rep):
    crop2ml_rep.mkdir()
algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
if not isdir(algo_rep):
    algo_rep.mkdir()
cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
if not isdir(cyml_rep):
    cyml_rep.mkdir()


vinfoAsg = []
for vi in varInfo:
    with open(vi, "r") as f:
        v = f.read()
    dictasg = to_dictASG(v, 'cs')
    asg = to_CASG(dictasg)
    vinfoAsg.append(asg)

with open(compositeStrat, "r") as f:
    strat = f.read()
dictcompo = to_dictASG(strat, 'cs')
compo = to_CASG(dictcompo)

models = []
for fil in simpleStrat:
    print(fil)
    with open(fil, "r") as f:
        strat = f.read()
    dictstrat = to_dictASG(strat,'cs')
    strAsg = to_CASG(dictstrat)
    z = BiomaExtraction()
    p2 = z.prec_cur_states(strAsg)
    algo = z.getAlgo(strAsg)
    funcs = z.externFunction(strAsg, algo)
    var =  z.totalvar(strAsg)
    cd = cs_cyml.Cs_Cyml_ast(algo.block, var = var)
    h = cd.transform()
    nd = transform_to_syntax_tree(h)
    code = writeCyml(nd)
    filename = Path(os.path.join(cyml_rep, "%s.pyx"%(fil.basename().split(".")[0])))
    with open(filename, "wb") as tg_file:
        tg_file.write(code.encode('utf-8'))
    
    if funcs:
        for m in funcs:
            cd = cs_cyml.Cs_Cyml_ast(m)
            h = cd.transform()
            nd = transform_to_syntax_tree(h)
            code = writeCyml(nd)
            filename = Path(os.path.join(cyml_rep, "%s.pyx"%(m.name)))
            with open(filename, "wb") as tg_file:
                tg_file.write(code.encode('utf-8'))
    
    z.modelunit(strAsg,vinfoAsg)
    models.append(z.model)
    xml_ = Pl2Crop2ml(z.model, "SQ.Pheno_Pkg").run_unit()
    filename = Path(os.path.join(crop2ml_rep, "unit.%s.xml"%(fil.basename().split(".")[0])))
    with open(filename, "wb") as xml_file:
        xml_file.write(xml_.unicode(indent=4).encode('utf-8'))

z.modelcomposition(models,compo)
xml_ = Pl2Crop2ml(z.mc, "SQ.Pheno_Pkg").run_compo()
name = z.mc.name[:-9] if z.mc.name.endswith("Component") else z.mc.name
filename = Path(os.path.join(crop2ml_rep, "composition.%s.xml"%(name)))
with open(filename, "wb") as xml_file:
    xml_file.write(xml_.unicode(indent=4).encode('utf-8'))


