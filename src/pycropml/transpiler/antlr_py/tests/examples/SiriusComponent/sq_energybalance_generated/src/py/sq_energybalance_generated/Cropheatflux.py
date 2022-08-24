# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_cropheatflux(netRadiationEquivalentEvaporation,
         soilHeatFlux,
         potentialTranspiration):
    """
     - Name: CropHeatFlux -Version: 001, -Time step: 1
     - Description:
                 * Title: CropHeatFlux model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: It is calculated from net Radiation, soil heat flux and potential transpiration 
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
                 * name: soilHeatFlux
                               ** description : soil Heat Flux 
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: potentialTranspiration
                               ** description : potential Transpiration 
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
     - outputs:
                 * name: cropHeatFlux
                               ** description :  crop Heat Flux
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    cropHeatFlux = netRadiationEquivalentEvaporation - soilHeatFlux - potentialTranspiration
    return cropHeatFlux