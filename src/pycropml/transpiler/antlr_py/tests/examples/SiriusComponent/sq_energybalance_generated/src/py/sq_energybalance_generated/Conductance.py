# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_conductance(plantHeight,
         wind,
         vonKarman,
         heightWeatherMeasurements,
         zm,
         zh,
         d):
    """
     - Name: Conductance -Version: 001, -Time step: 1
     - Description:
                 * Title: Conductance model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: The boundary layer conductance is expressed as the wind speed profile above the            canopy and the canopy structure. The approach does not take into account buoyancy            effects.         
                 * ShortDescription: None
     - inputs:
                 * name: plantHeight
                               ** description : plant Height
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0
                               ** unit : mm
                 * name: wind
                               ** description : wind
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000000
                               ** min : 0
                               ** default : 124000
                               ** unit : m/d
                 * name: vonKarman
                               ** description : von Karman constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.42
                               ** unit : dimensionless
                 * name: heightWeatherMeasurements
                               ** description : reference height of wind and humidity measurements
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 2
                               ** unit : m
                 * name: zm
                               ** description : roughness length governing momentum transfer, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.13
                               ** unit : m
                 * name: zh
                               ** description : roughness length governing transfer of heat and vapour, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.013
                               ** unit : m
                 * name: d
                               ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.67
                               ** unit : dimensionless
     - outputs:
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : m/d
    """

    h = max(10.0, plantHeight) / 100.0
    conductance = wind * pow(vonKarman, 2) / (log((heightWeatherMeasurements - (d * h)) / (zm * h)) * log((heightWeatherMeasurements - (d * h)) / (zh * h)))
    return conductance