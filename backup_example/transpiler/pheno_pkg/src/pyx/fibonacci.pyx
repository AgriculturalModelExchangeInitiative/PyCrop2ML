import numpy as np 
from math import *

def fibonacci_(int n):
    """


    fibonacci function
    Author: Pierre Martre
    Reference:  to write in package
    Institution: INRA Montpellier
    Abstract: see documentation

    """
    cdef int result
    cdef int b, temp, i
    result = 0
    b = 1
    for i in range(0,n,1):
        temp = result
        result = b
        b = temp + b
    return  result
