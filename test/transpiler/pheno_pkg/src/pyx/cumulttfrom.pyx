import numpy as np 
from math import *

def cumulttfrom_(list calendarMoments=['Sowing'],
                 list calendarCumuls=[0.0],
                 float cumulTT=8.0):
    """


    CumulTTFrom Model
    Author: Pierre Martre
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: Calculate CumulTT 

    """
    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_39
    cdef float cumulTTFromZC_91
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0     
    if "Anthesis" in calendarMoments:
        cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.index("Anthesis")]    
    if "FlagLeafLiguleJustVisible" in calendarMoments:
        cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]  
    if "EndGrainFilling"in calendarMoments:
        cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.index("EndGrainFilling")]
    return  cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91
