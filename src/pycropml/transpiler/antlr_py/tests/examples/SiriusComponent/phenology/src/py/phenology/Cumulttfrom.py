# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_cumulttfrom(calendarMoments_t1,
         calendarCumuls_t1,
         cumulTT):
    """
     - Name: CumulTTFrom -Version: 001, -Time step: 1
     - Description:
                 * Title: CumulTTFrom model
                 * Author: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: calendarMoments_t1
                               ** datatype : STRINGLIST
                               ** default : 
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarCumuls_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: cumulTT
                               ** datatype : DOUBLE
                               ** default : 112.330110409888
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** max : 10000
                               ** min : -200
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
     - outputs:
                 * name: cumulTTFromZC_65
                               ** datatype : DOUBLE
                               ** description :  cumul TT from Anthesis to current date 
                               ** max : -5000D
                               ** min : 0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: cumulTTFromZC_39
                               ** datatype : DOUBLE
                               ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
                               ** max : 5000
                               ** min : 0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: cumulTTFromZC_91
                               ** datatype : DOUBLE
                               ** description :  cumul TT from EndGrainFilling to current date 
                               ** max : 4000D
                               ** min : 0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
    """

    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0
    if "Anthesis" in calendarMoments_t1:
        cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("Anthesis")]
    if "FlagLeafLiguleJustVisible" in calendarMoments_t1:
        cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("FlagLeafLiguleJustVisible")]
    if "EndGrainFilling" in calendarMoments_t1:
        cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("EndGrainFilling")]
    return (cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91)