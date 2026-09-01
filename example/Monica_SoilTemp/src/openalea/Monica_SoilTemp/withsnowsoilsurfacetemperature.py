# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_withsnowsoilsurfacetemperature(noSnowSoilSurfaceTemperature:float,
         soilSurfaceTemperatureBelowSnow:float,
         hasSnowCover:bool):
    """
     - Name: WithSnowSoilSurfaceTemperature -Version: 1, -Time step: 1
     - Description:
                 * Title: Soil surface temperature with potential snow cover
                 * Authors: Michael Berg-Mohnicke
                 * Reference: None
                 * Institution: ZALF e.V.
                 * ExtendedDescription: None
                 * ShortDescription: It calculates the soil surface temperature taking a potential snow cover into account
             
     - inputs:
                 * name: noSnowSoilSurfaceTemperature
                               ** description : soilSurfaceTemperature without snow
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 0.0
                               ** unit : °C
                 * name: soilSurfaceTemperatureBelowSnow
                               ** description : soilSurfaceTemperature below snow cover
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 0.0
                               ** unit : °C
                 * name: hasSnowCover
                               ** description : is soil covered by snow
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : BOOLEAN
                               ** max : 
                               ** min : 
                               ** default : false
                               ** unit : dimensionless
     - outputs:
                 * name: soilSurfaceTemperature
                               ** description : soilSurfaceTemperature
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** unit : °C
    """

    soilSurfaceTemperature:float
    if hasSnowCover:
        soilSurfaceTemperature = soilSurfaceTemperatureBelowSnow
    else:
        soilSurfaceTemperature = noSnowSoilSurfaceTemperature
    return soilSurfaceTemperature
#%%CyML Model End%%