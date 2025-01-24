# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_phylsowingdatecorrection(p:float,
         sDsa_nh:float,
         sowingDay:int,
         sDsa_sh:float,
         latitude:float,
         rp:float,
         sDws:int):
    """
     - Name: PhylSowingDateCorrection -Version: 001, -Time step: 1
     - Description:
                 * Title: PhylSowingDateCorrection model
                 * Authors: Loic Manceau
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: Correction of the Phyllochron Varietal parameter according to sowing date 
                 * ShortDescription: None
     - inputs:
                 * name: p
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 120
                               ** unit : Â°C d leaf-1
                 * name: sDsa_nh
                               ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 365
                               ** min : 1
                               ** default : 1.0
                               ** unit : d
                 * name: sowingDay
                               ** description : Day of Year at sowing
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 365
                               ** min : 1
                               ** default : 1
                               ** unit : d
                 * name: sDsa_sh
                               ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 365
                               ** min : 1
                               ** default : 1.0
                               ** unit : d
                 * name: latitude
                               ** description : Latitude
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 90
                               ** min : -90
                               ** default : 0.0
                               ** unit : Â°
                 * name: rp
                               ** description : Rate of change of Phyllochrone with sowing date
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 365
                               ** min : 0
                               ** default : 0
                               ** unit : d-1
                 * name: sDws
                               ** description : Sowing date at which Phyllochrone is minimum
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 365
                               ** min : 1
                               ** default : 1
                               ** unit : d
     - outputs:
                 * name: fixPhyll
                               ** description :  Phyllochron Varietal parameter 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
    """

    fixPhyll:float
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
    return fixPhyll
#%%CyML Model End%%