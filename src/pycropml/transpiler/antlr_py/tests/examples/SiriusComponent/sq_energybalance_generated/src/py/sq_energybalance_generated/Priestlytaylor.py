# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_priestlytaylor(netRadiationEquivalentEvaporation,
         hslope,
         psychrometricConstant,
         Alpha):
    """
     - Name: PriestlyTaylor -Version: 001, -Time step: 1
     - Description:
                 * Title: PriestlyTaylor model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: Calculate Energy Balance 
                 * ShortDescription: None
     - inputs:
                 * name: netRadiationEquivalentEvaporation
                               ** description : net Radiation in Equivalent Evaporation 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0.584
                               ** unit : hPa Â°C-1
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.66
                               ** unit : 
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 1.5
                               ** unit : 
     - outputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    evapoTranspirationPriestlyTaylor = max(Alpha * hslope * netRadiationEquivalentEvaporation / (hslope + psychrometricConstant), 0.0)
    return evapoTranspirationPriestlyTaylor