import numpy 
from math import *
def model_leafnumber(int hasFlagLeafLiguleAppeared,
                     float phase,
                     float leafNumber_t1,
                     float phyllochron_t1,
                     float deltaTT):
    """

    LeafNumber model
    Author: Pierre MARTRE
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: 
    ShortDescription: 

    """
    cdef float leafNumber
    leafNumber = leafNumber_t1
    cdef float phyllochron_ 
    if phase >= 1.0 and phase < 4.0:
        if hasFlagLeafLiguleAppeared == 0:
            if phyllochron_t1 == 0.0:
                phyllochron_ = 0.0000001
            else:
                phyllochron_ = phyllochron_t1
            leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
    return  leafNumber
