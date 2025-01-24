# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_ismomentregistredzc_39(calendarMoments_t1:List[str]):
    """
     - Name: IsMomentRegistredZC_39 -Version: 001, -Time step: 1
     - Description:
                 * Title: IsMomentRegistredZC_39 model
                 * Authors: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: if FlagLeafLiguleJustVisible is already Registred 
                 * ShortDescription: None
     - inputs:
                 * name: calendarMoments_t1
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
     - outputs:
                 * name: isMomentRegistredZC_39
                               ** description :  if Flag leaf ligule has already appeared 
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
    """

    isMomentRegistredZC_39:int
    isMomentRegistredZC_39 = 1 if "FlagLeafLiguleJustVisible" in calendarMoments_t1 else 0
    return isMomentRegistredZC_39
#%%CyML Model End%%