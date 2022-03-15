
from __future__ import absolute_import
from __future__ import print_function
from functools import total_ordering
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG


cwd = Path(__file__).dirname()
data = cwd/'examples'/'cs'

simpleStrat = [f for f in data.glob('*.cs')]

strat = simpleStrat[0]
print(strat)


with open(strat, "r") as f:
    code = f.read()

strdict = to_dictASG(code,'cs')
strAsg = to_CASG(strdict)