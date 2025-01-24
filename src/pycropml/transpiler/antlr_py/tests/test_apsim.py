from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
from pycropml.transpiler.antlr_py.apsim.apsimExtraction import ApsimExtraction
from pycropml.transpiler.antlr_py.apsim.run import run_apsim

cwd = os.path.join(Path(__file__).parent, "examples")
print("iii", cwd)
data = cwd/'apsimComponent/Toy1'
print(data)

simpleStrat = [f for f in data.glob('*.cs')]

strat = simpleStrat[0]


component = cwd/'apsimComponent/Toy1'
output = cwd/'apsimComponent/Toy1'
run_apsim(component, output)