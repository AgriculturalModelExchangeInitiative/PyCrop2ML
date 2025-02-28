# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_canopytemperature(minTair:float,
         maxTair:float,
         cropHeatFlux:float,
         conductance:float,
         lambdaV:float,
         rhoDensityAir:float,
         specificHeatCapacityAir:float):
    """
     - Name: CanopyTemperature -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CanopyTemperature Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: It is calculated from the crop heat flux and the boundary layer conductance 
                 * ShortDescription: It is calculated from the crop heat flux and the boundary layer conductance 
     - inputs:
                 * name: minTair
                               ** description : minimum air temperature
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** min : -30
                               ** max : 45
                               ** default : 0.7
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: maxTair
                               ** description : maximum air Temperature
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** min : -30
                               ** max : 45
                               ** default : 7.2
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: cropHeatFlux
                               ** description : Crop heat flux
                               ** variablecategory : rate
                               ** inputtype : variable
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 447.912
                               ** unit : g/m**2/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** variablecategory : state
                               ** inputtype : variable
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 598.685
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ/kg
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.225
                               ** unit : kg/m**3
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.00101
                               ** unit : MJ/kg/degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: minCanopyTemperature
                               ** description : minimal Canopy Temperature  
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: maxCanopyTemperature
                               ** description : maximal Canopy Temperature 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    minCanopyTemperature:float
    maxCanopyTemperature:float
    minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    return (minCanopyTemperature, maxCanopyTemperature)
#%%CyML Model End%%