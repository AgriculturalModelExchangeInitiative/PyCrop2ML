# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_soilevaporation(diffusionLimitedEvaporation:float,
         energyLimitedEvaporation:float):
    """
     - Name: SoilEvaporation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: SoilEvaporation Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference:  https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: Starting from a soil at field capacity, soil evaporation  is assumed to
                     be energy limited during the first phase of evaporation and diffusion limited thereafter.
                     Hence, the soil evaporation model considers these two processes taking the minimum between
                     the energy limited evaporation (PtSoil) and the diffused limited
                     evaporation 
                 * ShortDescription: Starting from a soil at field capacity, soil evaporation  is assumed to
                 be energy limited during the first phase of evaporation and diffusion limited thereafter.
                 Hence, the soil evaporation model considers these two processes taking the minimum between
                 the energy limited evaporation (PtSoil) and the diffused limited
                 evaporation
     - inputs:
                 * name: diffusionLimitedEvaporation
                               ** description : diffusion Limited Evaporation
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** default : 6605.505
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 448.240
                               ** min : 0
                               ** max : 1000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
     - outputs:
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    soilEvaporation:float
    soilEvaporation = min(diffusionLimitedEvaporation, energyLimitedEvaporation)
    return soilEvaporation
#%%CyML Model End%%