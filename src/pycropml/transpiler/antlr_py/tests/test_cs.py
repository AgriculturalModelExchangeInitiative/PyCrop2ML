
from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG


cwd = Path(__file__).dirname()
data = cwd/'examples'/'cs'

simpleStrat = [f for f in data.glob('*.cs')]

strat = simpleStrat[0]
print(strat)


with open(strat, "r") as f:
    code = f.read()
strAsg = to_CASG(code,'cs')