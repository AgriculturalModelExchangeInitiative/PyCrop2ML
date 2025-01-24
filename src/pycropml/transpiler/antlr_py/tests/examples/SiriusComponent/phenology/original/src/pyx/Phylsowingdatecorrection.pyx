import numpy 
from math import *
def model_phylsowingdatecorrection(float p,
                                   float sDsa_nh,
                                   int sowingDay,
                                   float sDsa_sh,
                                   float latitude,
                                   float rp,
                                   int sDws):
    """

    PhylSowingDateCorrection model
    Author: Loic Manceau
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: Correction of the Phyllochron Varietal parameter according to sowing date 
    ShortDescription: None

    """
    cdef float fixPhyll
    if latitude < 0.0:
        if sowingDay > int(sDsa_sh):
            fixPhyll=p * (1 - (rp * min((sowingDay - sDsa_sh), sDws)))
        else:
            fixPhyll=p
    else:
        if sowingDay < int(sDsa_nh):
            fixPhyll=p * (1 - (rp * min(sowingDay, sDws)))
        else:
            fixPhyll=p
    return  fixPhyll


