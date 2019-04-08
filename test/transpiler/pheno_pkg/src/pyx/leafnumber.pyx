import numpy as np 
from math import *

def leafnumber_(float deltaTT=23.5895677277199,
                float phyllochron=0.0,
                int hasFlagLeafLiguleAppeared=0,
                float leafNumber=0.0,
                float phase=1.0):
    """


    CalculateLeafNumber Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day

    """
    cdef float phyllochron_     
    if (phase >= 1.0 and phase< 4.0):       
        if (hasFlagLeafLiguleAppeared==0):           
            if (phyllochron == 0.0):
                phyllochron_ = 0.0000001
            else: phyllochron_ = phyllochron
            leafNumber = leafNumber + min(deltaTT / phyllochron_, 0.999)
    return  leafNumber
