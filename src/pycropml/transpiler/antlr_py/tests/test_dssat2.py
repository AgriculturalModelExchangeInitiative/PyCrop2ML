
from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.csharp import cs_cyml
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.antlr_py import parse, simplifyAntlrTree
from pycropml.transpiler.antlr_py.to_CASG import GENERATORS

""" Read BioMA component and extract metadata

"""

cwd = Path(__file__).dirname()
data = cwd/'examples'/'DssatComponent'/'phenology'

composite= data.glob('*Component.cs')[0]
simple = [f for f in data.glob('*.cs')  if f not in composite]

output = cwd/'examples'/'DssatComponent'/'phenology'
crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
if not crop2ml_rep.isdir():
    crop2ml_rep.mkdir()
algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
if not algo_rep.isdir():
    algo_rep.mkdir()
cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
if not cyml_rep.isdir():
    cyml_rep.mkdir()


from path import Path
mod1 = Path("C:/Users/midingoy/Documents/Restore/Users/midingoy/Documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/tests/examples/DssatComponent/phenology/Vernalizationprogress.f90")
from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.fortran import f90_cyml
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
asg = to_CASG(mod1, 'f90')
z = DssatExtraction() 
z.modelunit(mod1)
v = z.model.inputs + z.model.outputs
var = [vi.name for vi in v]
algo = z.getSubroutine(asg)
f = algo[0]
cd = f90_cyml.F90_Cyml_ast(f.block, var=var)
h = cd.transform()
nd = transform_to_syntax_tree(h)
code = writeCyml(nd)

xml_ = Pl2Crop2ml(z.model, "Dssat.Pheno_Pkg").run_unit()


