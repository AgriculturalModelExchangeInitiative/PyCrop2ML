# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_canopytemperature(minTair,
         maxTair,
         cropHeatFlux,
         conductance,
         lambdaV,
         rhoDensityAir,
         specificHeatCapacityAir):
    """
     - Name: CanopyTemperature -Version: 001, -Time step: 1
     - Description:
                 * Title: CanopyTemperature model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: It is calculated from the crop heat flux and the boundary layer conductance 
                 * ShortDescription: None
     - inputs:
                 * name: minTair
                               ** description : minimum air temperature
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 45
                               ** min : -30
                               ** default : 0.7
                               ** unit : Â°C
                 * name: maxTair
                               ** description : maximum air Temperature
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 45
                               ** min : -30
                               ** default : 7.2
                               ** unit : Â°C
                 * name: cropHeatFlux
                               ** description :  crop Heat Flux
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : m/d
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 2.454
                               ** unit : MJ/kg
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1.225
                               ** min : 1.225
                               ** default : 1.225
                               ** unit : kg/m**3
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 0.00101
                               ** min : 0.00101
                               ** default : 0.00101
                               ** unit : MJ/kg/degC
     - outputs:
                 * name: minCanopyTemperature
                               ** description : minimal Canopy Temperature  
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 45
                               ** min : -30
                               ** unit : degC
                 * name: maxCanopyTemperature
                               ** description : maximal Canopy Temperature 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 45
                               ** min : -30
                               ** unit : degC
    """

    minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    return (minCanopyTemperature, maxCanopyTemperature)