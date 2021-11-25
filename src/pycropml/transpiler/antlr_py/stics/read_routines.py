from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG

def read_unit(file):
    filename = Path(file)
    with open(filename, 'r',  encoding='utf-8') as f:
        all_text = f.read()
    routines = all_text.split("!@routine")
    return routines


def main():
    file = "C:/Users/midingoy/Documents/phosphorus-modules/phosphorus/src/uptake_P/uptake_P_routines.f90"
    return (read_unit(file))

mod1 = Path("C:/Users/midingoy/Documents/Restore/Users/midingoy/Documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/tests/examples/DssatComponent/phenology/Vernalizationprogress.f90")


from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.fortran import f90_cyml
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
mod1 = Path("C:/Users/midingoy/Documents/Restore/Users/midingoy/Documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/tests/examples/DssatComponent/phenology/Vernalizationprogress.f90")
file = "C:/Users/midingoy/Documents/phosphorus-modules/phosphorus/src/uptake_P/uptake_P_routines.f90"
file = Path("C:/Users/midingoy/Documents/projet/Shootnumber.f90")

file = "C:/Users/midingoy/Documents/phosphorus-modules/phosphorus/src/uptake_P/test.f90"
from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.fortran import f90_cyml
from pycropml.transpiler.antlr_py.dssat.dssatExtraction import DssatExtraction
from pycropml.transpiler.antlr_py.createXml import Pl2Crop2ml
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
file = "C:/Users/midingoy/Documents/phosphorus-modules/phosphorus/src/uptake_P/test.f90"
with open(file, "r") as fil:
    code = fil.read()
asg = to_CASG(code,'f90')
z = DssatExtraction()
#z.modelunit(file, asg)
algo = z.getSubroutine(asg)
f = algo[5]
cd = f90_cyml.F90_Cyml_ast(f.block)#, var=var)
h = cd.transform()
nd = transform_to_syntax_tree(h)
code = writeCyml(nd)


v = z.model.inputs + z.model.outputs
var = [vi.name for vi in v]
algo = z.getSubroutine(asg)
f = algo[1]
cd = f90_cyml.F90_Cyml_ast(f.block)#, var=var)
h = cd.transform()
nd = transform_to_syntax_tree(h)
code = writeCyml(nd)
xml_ = Pl2Crop2ml(z.model, "Dssat.Pheno_Pkg").run_unit()