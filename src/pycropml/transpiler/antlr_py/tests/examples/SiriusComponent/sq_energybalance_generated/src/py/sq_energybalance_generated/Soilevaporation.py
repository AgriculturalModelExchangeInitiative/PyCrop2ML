# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_soilevaporation(diffusionLimitedEvaporation,
         energyLimitedEvaporation):
    """
     - Name: SoilEvaporation -Version: 001, -Time step: 1
     - Description:
                 * Title: SoilEvaporation model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: Starting from a soil at field capacity, soil evaporation  is assumed to                be energy limited during the first phase of evaporation and diffusion limited thereafter.                Hence, the soil evaporation model considers these two processes taking the minimum between                the energy limited evaporation (PtSoil) and the diffused limited                evaporation 
                 * ShortDescription: None
     - inputs:
                 * name: diffusionLimitedEvaporation
                               ** description : the evaporation from the diffusion limited soil 
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
     - outputs:
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    soilEvaporation = min(diffusionLimitedEvaporation, energyLimitedEvaporation)
    return soilEvaporation