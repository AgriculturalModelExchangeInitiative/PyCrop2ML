# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.main import Main

source = u"""import numpy as np 
from math import *

from fibonacci import fibonacci_ 
def shootnumber_(float canopyShootNumber=288.0,
                 float leafNumber=0.0,
                 int sowingDensity=288,
                 float targetFertileShoot=600.0,
                 list tilleringProfile=[288.0],
                 list leafTillerNumberArray=[1],
                 int tillerNumber=1):

    cdef float averageShootNumberPerPlant
    cdef float oldCanopyShootNumber
    cdef int emergedLeaves, shoots, i
    cdef list a=[15]
    cdef list b=[12]
    oldCanopyShootNumber = canopyShootNumber
    emergedLeaves = int(max(1.0, ceil(leafNumber - 1)))
    shoots = fibonacci_(emergedLeaves)
    canopyShootNumber = min(float(shoots * sowingDensity), targetFertileShoot)
    averageShootNumberPerPlant = canopyShootNumber / sowingDensity       
    if (canopyShootNumber != oldCanopyShootNumber):
        tilleringProfile.append(canopyShootNumber - oldCanopyShootNumber)         
    tillerNumber = len(tilleringProfile)     
    for i in range(len(leafTillerNumberArray),int(ceil(leafNumber)),1):
        leafTillerNumberArray.append(tillerNumber)
    return  averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, tillerNumber
"""
    

test=Main(source, 'f90')
a=test.parse()    
g=test.to_ast(source)  
test.dictAst
code=test.to_source()
print(code)




#!/usr/bin/env python

"""
test code for numpy_test.pyx
"""

import numpy as np

import numpy_test


test_array = np.array( [ (1.2, 3.4),
                         (5.6, 7.8),
                         (9.0, 9.1),
                         ], dtype=np.float64)


def test_init():
    hp = numpy_test.Halo_Positions( test_array )

    print ("type is:", type(hp.x))

    hp.debug()

    assert type(hp.x) is np.ndarray
    assert type(hp.y) is np.ndarray

    assert np.array_equal(hp.x, test_array[:,0])
    assert np.array_equal(hp.y, test_array[:,1])


if __name__ == "__main__":
    test_init()
    print ("if there were no failed assertions, the test passed")


