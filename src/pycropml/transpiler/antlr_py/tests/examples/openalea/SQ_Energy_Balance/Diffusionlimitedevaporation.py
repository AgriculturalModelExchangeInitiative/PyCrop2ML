# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_diffusionlimitedevaporation(deficitOnTopLayers:float,
         soilDiffusionConstant:float):
    """
     - Name: DiffusionLimitedEvaporation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: DiffusionLimitedEvaporation Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference:  https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: the evaporation from the diffusion limited soil 
                 * ShortDescription: It calculates the diffusion limited evaropration
             
     - inputs:
                 * name: deficitOnTopLayers
                               ** description : deficit On TopLayers
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 5341
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: soilDiffusionConstant
                               ** description : soil Diffusion Constant
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** default : 4.2
                               ** min : 0
                               ** max : 10
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: diffusionLimitedEvaporation
                               ** description : the evaporation from the diffusion limited soil 
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    diffusionLimitedEvaporation:float
    if deficitOnTopLayers / 1000.0 <= 0.0:
        diffusionLimitedEvaporation = 8.3 * 1000.0
    else:
        if deficitOnTopLayers / 1000.0 < 25.0:
            diffusionLimitedEvaporation = 2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0) * 1000.0
        else:
            diffusionLimitedEvaporation = 0.0
    return diffusionLimitedEvaporation
#%%CyML Model End%%