import numpy 
from math import *
def model_ismomentregistredzc_39(stringlist calendarMoments_t1):
    """

    IsMomentRegistredZC_39 model
    Author: Pierre Martre
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: if FlagLeafLiguleJustVisible is already Registred 
    ShortDescription: None

    """
    cdef int isMomentRegistredZC_39
    isMomentRegistredZC_39=1 if "FlagLeafLiguleJustVisible" in calendarMoments_t1 else 0
    return  isMomentRegistredZC_39


