# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_penman(evapoTranspirationPriestlyTaylor:float,
         hslope:float,
         VPDair:float,
         psychrometricConstant:float,
         Alpha:float,
         lambdaV:float,
         rhoDensityAir:float,
         specificHeatCapacityAir:float,
         conductance:float):
    """
     - Name: Penman -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Penman Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference:  https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: It uses Penmann-Monteith method vase on the availability of wind and vapor pressure daily data
                 * ShortDescription: It uses Penmann-Monteith method vase on the availability of wind and vapor pressure daily data
     - inputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** default : 449.367
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.584
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa °C-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: VPDair
                               ** description :  vapour pressure density
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 2.19
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.66
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.5
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.225
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.00101
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: conductance
                               ** description : conductance
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 598.685
                               ** unit : m d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
     - outputs:
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    evapoTranspirationPenman:float
    evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + (1000.0 * (rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / (lambdaV * (hslope + psychrometricConstant))))
    return evapoTranspirationPenman
#%%CyML Model End%%