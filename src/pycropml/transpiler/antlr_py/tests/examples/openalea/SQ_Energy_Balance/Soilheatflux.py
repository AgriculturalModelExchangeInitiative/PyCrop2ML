# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_soilheatflux(netRadiationEquivalentEvaporation:float,
         tau:float,
         soilEvaporation:float):
    """
     - Name: SoilHeatFlux -Version: 1.0, -Time step: 1
     - Description:
                 * Title: SoilHeatFlux Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference:  https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: The available energy in the soil 
                 * ShortDescription: The available energy in the soil
     - inputs:
                 * name: netRadiationEquivalentEvaporation
                               ** variablecategory : auxiliary
                               ** description : net Radiation Equivalent Evaporation
                               ** datatype : DOUBLE
                               ** default : 638.142
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: tau
                               ** description : plant cover factor
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** default : 0.9983
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 448.240
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
     - outputs:
                 * name: soilHeatFlux
                               ** description : soil Heat Flux 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    soilHeatFlux:float
    soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation
    return soilHeatFlux
#%%CyML Model End%%