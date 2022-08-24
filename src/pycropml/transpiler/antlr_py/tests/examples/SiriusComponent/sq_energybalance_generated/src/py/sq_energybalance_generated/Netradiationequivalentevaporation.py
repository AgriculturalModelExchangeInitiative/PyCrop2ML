# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_netradiationequivalentevaporation(netRadiation,
         lambdaV):
    """
     - Name: NetRadiationEquivalentEvaporation -Version: 001, -Time step: 1
     - Description:
                 * Title: NetRadiationEquivalentEvaporation model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription:  It is given by dividing net radiation by latent heat of vaporization of water 
                 * ShortDescription: None
     - inputs:
                 * name: netRadiation
                               ** description :  net radiation 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : MJ m-2 d-1
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 2.454
                               ** unit : MJ kg-1
     - outputs:
                 * name: netRadiationEquivalentEvaporation
                               ** description : net Radiation in Equivalent Evaporation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    netRadiationEquivalentEvaporation = netRadiation / lambdaV * 1000.0
    return netRadiationEquivalentEvaporation