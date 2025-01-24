import numpy 
from math import *
def model_leafnumber(float deltaTT,
                     float phyllochron_t1,
                     int hasFlagLeafLiguleAppeared,
                     float leafNumber_t1,
                     float phase):
    """

    LeafNumber model
    Author: Pierre MARTRE
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: calculate leaf number. LeafNumber increase is caped at one more leaf per day
    ShortDescription: None

    """
    cdef float leafNumber
    cdef float phyllochron_ 
    leafNumber=leafNumber_t1
    if phase >= 1.0 and phase < 4.0:
        if hasFlagLeafLiguleAppeared == 0:
            if phyllochron_t1 == 0.0:
                phyllochron_=0.0000001
            else:
                phyllochron_=phyllochron_t1
            leafNumber=leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
    return  leafNumber


