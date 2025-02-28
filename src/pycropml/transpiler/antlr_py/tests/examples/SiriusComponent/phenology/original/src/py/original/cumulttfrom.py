# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_cumulttfrom(cumulTT:float,
         calendarMoments_t1:List[str],
         calendarCumuls_t1:List[float]):
    """
     - Name: CumulTTFrom -Version: 001, -Time step: 1
     - Description:
                 * Title: CumulTTFrom model
                 * Authors: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: Calculate CumulTT 
                 * ShortDescription: None
     - inputs:
                 * name: cumulTT
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : -200
                               ** default : 112.330110409888
                               ** unit : Â°C d
                 * name: calendarMoments_t1
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: calendarCumuls_t1
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
     - outputs:
                 * name: cumulTTFromZC_65
                               ** description :  cumul TT from Anthesis to current date 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : -5000
                               ** min : 0
                               ** unit : Â°C d
                 * name: cumulTTFromZC_91
                               ** description :  cumul TT from EndGrainFilling to current date 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 4000
                               ** min : 0
                               ** unit : Â°C d
                 * name: cumulTTFromZC_39
                               ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : Â°C d
    """

    cumulTTFromZC_65:float
    cumulTTFromZC_91:float
    cumulTTFromZC_39:float
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0
    if "Anthesis" in calendarMoments_t1:
        cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("Anthesis")]
    if "FlagLeafLiguleJustVisible" in calendarMoments_t1:
        cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("FlagLeafLiguleJustVisible")]
    if "EndGrainFilling" in calendarMoments_t1:
        cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("EndGrainFilling")]
    return (cumulTTFromZC_65, cumulTTFromZC_91, cumulTTFromZC_39)
#%%CyML Model End%%