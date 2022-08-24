# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_ismomentregistredzc_39(calendarMoments_t1):
    """
     - Name: IsMomentRegistredZC_39 -Version: 001, -Time step: 1
     - Description:
                 * Title: IsMomentRegistredZC_39 model
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
     - outputs:
                 * name: isMomentRegistredZC_39
                               ** datatype : INT
                               ** description :  if Flag leaf ligule has already appeared 
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
    """

    isMomentRegistredZC_39 = 1 if "FlagLeafLiguleJustVisible" in calendarMoments_t1 else 0
    return isMomentRegistredZC_39