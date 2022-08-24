# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_leafnumber(hasFlagLeafLiguleAppeared,
         phase,
         leafNumber_t1,
         phyllochron_t1,
         deltaTT):
    """
     - Name: LeafNumber -Version: 001, -Time step: 1
     - Description:
                 * Title: LeafNumber model
                 * Author: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: hasFlagLeafLiguleAppeared
                               ** datatype : INT
                               ** default : 1
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** inputtype : variable
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: phase
                               ** datatype : DOUBLE
                               ** default : 1
                               ** description :  the name of the phase
                               ** inputtype : variable
                               ** max : 7
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: leafNumber_t1
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: phyllochron_t1
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : phyllochron
                               ** inputtype : variable
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                               ** variablecategory : state
                 * name: deltaTT
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** max : 100.0
                               ** min : 0.0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
     - outputs:
                 * name: leafNumber
                               ** datatype : DOUBLE
                               ** description : Actual number of phytomers
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
    """

    leafNumber = leafNumber_t1
    if phase >= 1.0 and phase < 4.0:
        if hasFlagLeafLiguleAppeared == 0:
            if phyllochron_t1 == 0.0:
                phyllochron_ = 0.0000001
            else:
                phyllochron_ = phyllochron_t1
            leafNumber = leafNumber_t1 + min(deltaTT / phyllochron_, 0.999)
    return leafNumber