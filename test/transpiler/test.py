# coding: utf-8
from pycropml.transpiler.main import Main, formater
from pycropml.pparse import model_parser

source = u"""import numpy as np 
from math import *
def conductance_(float vonKarman=0.42,
                 float heightWeatherMeasurements=2.0,
                 float zm=0.13,
                 float zh=0.013,
                 float d=0.67,
                 float plantHeight=0.0,
                 float wind=124000.0):
    cdef float conductance
    cdef float h
    h = max(10, plantHeight) / 100.0
    conductance = (wind * pow(vonKarman, 2)) / (log((heightWeatherMeasurements - d * h) / (zm * h)) * log((heightWeatherMeasurements - d * h) / (zh * h)))
    return  conductance"""

test=Main(source, "f90")
a=test.parse()    
g=test.to_ast(source)  
test.dictAst
code=test.to_source()
print(code)
