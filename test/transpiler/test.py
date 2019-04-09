# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.main import Main

source = u"""from math import *
def evapo(float MSALB,float SRAD,
                 float TMAX,
                 float TMIN,
                 float XHLAI):
    cdef float ALBEDO
    cdef float SLANG
    cdef float EEQ
    cdef float eo
    cdef float TD
    cdef float EO
    TD = 0.60*TMAX + 0.40*TMIN
    if (XHLAI <= 0.0):
        ALBEDO = MSALB
    else:
        ALBEDO = 0.23 - (0.23-MSALB)*exp(-0.75*XHLAI)
    SLANG = SRAD * 23.923
    EEQ = SLANG * (2.04E-4 - 1.83E-4 * ALBEDO)*(TD+29.0)
    eo = EEQ*1.1
    if (TMAX < 35.0):
        eo = EEQ*((TMAX-35.0)*0.05+1.1)
    else:
        eo = EEQ*0.01*exp(0.18*(TMAX+20.0))
    EO = max(eo, 0.0001)
    return EO """
    
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


