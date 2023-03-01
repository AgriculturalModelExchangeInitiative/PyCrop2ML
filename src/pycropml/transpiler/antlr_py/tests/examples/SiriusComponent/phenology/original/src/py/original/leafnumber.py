# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_leafnumber(deltaTT:float,
         phyllochron_t1:float,
         hasFlagLeafLiguleAppeared:int,
         leafNumber_t1:float,
         phase:float):
    """
     - Name: LeafNumber -Version: 001, -Time step: 1
     - Description:
                 * Title: LeafNumber model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: calculate leaf number. LeafNumber increase is caped at one more leaf per day
                 * ShortDescription: None
     - inputs:
                 * name: deltaTT
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 100.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d
                 * name: phyllochron_t1
                               ** description : phyllochron
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0
                               ** unit : Â°C d leaf-1
                 * name: hasFlagLeafLiguleAppeared
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: leafNumber_t1
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: phase
                               ** description :  the name of the phase
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 7
                               ** min : 0
                               ** default : 1
                               ** unit : 
     - outputs:
                 * name: leafNumber
                               ** description : Actual number of phytomers
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
    """

    leafNumber:float
    phyllochron_:float
    leafNumber = leafNumber_t1
    if phase >= 1.0 and phase < 4.0:
        if hasFlagLeafLiguleAppeared == 0:
            if phyllochron_t1 == 0.0:
                phyllochron_ = 0.0000001
            else:
                phyllochron_ = phyllochron_t1
            leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
    return leafNumber
#%%CyML Model End%%