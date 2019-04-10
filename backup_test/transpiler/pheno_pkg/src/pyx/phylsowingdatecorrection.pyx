import numpy as np 
from math import *

def phylsowingdatecorrection_(int sowingDay=1,
                              float latitude=0.0,
                              int sDsa_sh=1,
                              float rp=0.0,
                              int sDws=1,
                              int sDsa_nh=1,
                              float p=120.0):
    """


    PhylSowingDateCorrection Model
    Author: Loic Manceau
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 

    """
    cdef float fixPhyll
    if (latitude < 0.0):
        if (sowingDay > sDsa_sh):
            fixPhyll = p * (1 - rp * min(sowingDay - sDsa_sh, sDws))
        else: fixPhyll = p
    else:
        if (sowingDay < sDsa_nh):
            fixPhyll = p * (1 - rp * min(sowingDay, sDws))
        else: fixPhyll = p
    return  fixPhyll
