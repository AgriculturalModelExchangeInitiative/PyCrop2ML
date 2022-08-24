# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_soilheatflux(netRadiationEquivalentEvaporation,
         soilEvaporation,
         tau):
    """
     - Name: SoilHeatFlux -Version: 001, -Time step: 1
     - Description:
                 * Title: SoilHeatFlux model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: The available energy in the soil 
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
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: tau
                               ** description : plant cover factor
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 0.9983
                               ** unit : 
     - outputs:
                 * name: soilHeatFlux
                               ** description : soil Heat Flux 
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation
    return soilHeatFlux