# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.main import Main

source = u"""import numpy as np 
from math import *

def cumulttfrom_(list calendarMoments=['Sowing'],
                 list calendarCumuls=[0.0],
                 int switchMaize=0,
                 float cumulTT=8.0):

    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_39
    cdef float cumulTTFromZC_91
    
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0     
    if "Anthesis" in calendarMoments:
        if (switchMaize == 0): cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.index("Anthesis")]    
    if "FlagLeafLiguleJustVisible" in calendarMoments:
        if (switchMaize == 0): cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]  
    if "EndGrainFilling"in calendarMoments:
        if (switchMaize == 0): cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.index("EndGrainFilling")]
    return  cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91"""

test=Main(source, "f90")
a=test.parse()    
g=test.to_ast(source)  
test.dictAst
code=test.to_source()
print(code)
