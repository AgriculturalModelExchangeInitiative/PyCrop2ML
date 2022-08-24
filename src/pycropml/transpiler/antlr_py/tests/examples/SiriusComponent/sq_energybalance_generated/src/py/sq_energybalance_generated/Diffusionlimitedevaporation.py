# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_diffusionlimitedevaporation(deficitOnTopLayers,
         soilDiffusionConstant):
    """
     - Name: DiffusionLimitedEvaporation -Version: 001, -Time step: 1
     - Description:
                 * Title: DiffusionLimitedEvaporation model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: the evaporation from the diffusion limited soil 
                 * ShortDescription: None
     - inputs:
                 * name: deficitOnTopLayers
                               ** description : deficit On TopLayers
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 5341
                               ** unit : g m-2 d-1
                 * name: soilDiffusionConstant
                               ** description : soil Diffusion Constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 4.2
                               ** unit : 
     - outputs:
                 * name: diffusionLimitedEvaporation
                               ** description : the evaporation from the diffusion limited soil 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    if deficitOnTopLayers / 1000.0 <= 0.0:
        diffusionLimitedEvaporation = 8.3 * 1000.0
    else:
        if deficitOnTopLayers / 1000.0 < 25.0:
            diffusionLimitedEvaporation = 2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0) * 1000.0
        else:
            diffusionLimitedEvaporation = 0.0
    return diffusionLimitedEvaporation