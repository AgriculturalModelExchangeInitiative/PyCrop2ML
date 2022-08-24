# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_penman(evapoTranspirationPriestlyTaylor,
         hslope,
         VPDair,
         conductance,
         psychrometricConstant,
         Alpha,
         lambdaV,
         rhoDensityAir,
         specificHeatCapacityAir):
    """
     - Name: Penman -Version: 001, -Time step: 1
     - Description:
                 * Title: Penman model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: It uses Penmann-Monteith method vase on the availability of wind and vapor pressure daily data
                 * ShortDescription: None
     - inputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0.584
                               ** unit : hPa Â°C-1
                 * name: VPDair
                               ** description :  vapour pressure density
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 2.19
                               ** unit : hPa
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : m/d
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.66
                               ** unit : 
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 1.5
                               ** unit : 
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 2.454
                               ** unit : 
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1.225
                               ** min : 1.225
                               ** default : 1.225
                               ** unit : 
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.00101
                               ** unit : 
     - outputs:
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + (1000.0 * (rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / (lambdaV * (hslope + psychrometricConstant))))
    return evapoTranspirationPenman