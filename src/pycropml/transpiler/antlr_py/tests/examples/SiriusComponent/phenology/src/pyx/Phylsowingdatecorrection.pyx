import numpy 
from math import *
def model_phylsowingdatecorrection(int sowingDay,
                                   float latitude,
                                   float sDsa_sh,
                                   float rp,
                                   int sDws,
                                   float sDsa_nh,
                                   float p):
    """

    PhylSowingDateCorrection model
    Author: Loic Manceau
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: 
    ShortDescription: 

    """
    cdef float fixPhyll
    if latitude < 0.0:
        if sowingDay > int(sDsa_sh):
            fixPhyll = p * (1 - (rp * min((sowingDay - sDsa_sh), sDws)))
        else:
            fixPhyll = p
    else:
        if sowingDay < int(sDsa_nh):
            fixPhyll = p * (1 - (rp * min(sowingDay, sDws)))
        else:
            fixPhyll = p
    return  fixPhyll
