# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.main import Main

source = u"""import numpy as np 
from math import *
def initshootnumber_(float sowingDensity=288.0):
    cdef float x
    x=23*(4/5*2.0)
    return  x
"""

test=Main(source, 'f90')
a=test.parse()    
g=test.to_ast(source)  
test.dictAst
code=test.to_source()
print(code)



