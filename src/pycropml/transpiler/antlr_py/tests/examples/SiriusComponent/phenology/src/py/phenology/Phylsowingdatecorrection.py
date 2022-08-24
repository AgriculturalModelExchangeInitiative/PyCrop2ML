# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_phylsowingdatecorrection(sowingDay,
         latitude,
         sDsa_sh,
         rp,
         sDws,
         sDsa_nh,
         p):
    """
     - Name: PhylSowingDateCorrection -Version: 001, -Time step: 1
     - Description:
                 * Title: PhylSowingDateCorrection model
                 * Author: Loic Manceau
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: sowingDay
                               ** datatype : INT
                               ** default : 1
                               ** description : Day of Year at sowing
                               ** inputtype : parameter
                               ** max : 365
                               ** min : 1
                               ** parametercategory : constant
                               ** unit : d
                 * name: latitude
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Latitude
                               ** inputtype : parameter
                               ** max : 90
                               ** min : -90
                               ** parametercategory : constant
                               ** unit : Â°
                 * name: sDsa_sh
                               ** datatype : DOUBLE
                               ** default : 1.0
                               ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
                               ** inputtype : parameter
                               ** max : 365
                               ** min : 1
                               ** parametercategory : constant
                               ** unit : d
                 * name: rp
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Rate of change of Phyllochrone with sowing date
                               ** inputtype : parameter
                               ** max : 365
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : d-1
                 * name: sDws
                               ** datatype : INT
                               ** default : 1
                               ** description : Sowing date at which Phyllochrone is minimum
                               ** inputtype : parameter
                               ** max : 365
                               ** min : 1
                               ** parametercategory : constant
                               ** unit : d
                 * name: sDsa_nh
                               ** datatype : DOUBLE
                               ** default : 1.0
                               ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
                               ** inputtype : parameter
                               ** max : 365
                               ** min : 1
                               ** parametercategory : constant
                               ** unit : d
                 * name: p
                               ** datatype : DOUBLE
                               ** default : 120
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** max : 1000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d leaf-1
     - outputs:
                 * name: fixPhyll
                               ** datatype : DOUBLE
                               ** description :  Phyllochron Varietal parameter 
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                               ** variablecategory : auxiliary
    """

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