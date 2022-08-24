# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_netradiation(minTair,
         maxTair,
         solarRadiation,
         vaporPressure,
         extraSolarRadiation,
         albedoCoefficient,
         stefanBoltzman,
         elevation):
    """
     - Name: NetRadiation -Version: 001, -Time step: 1
     - Description:
                 * Title: NetRadiation model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short                     and long wavelength radiation 
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
                 * name: solarRadiation
                               ** description : solar Radiation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 3
                               ** unit : MJ m-2 d-1
                 * name: vaporPressure
                               ** description : vapor Pressure
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 6.1
                               ** unit : hPa
                 * name: extraSolarRadiation
                               ** description : extra Solar Radiation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 11.7
                               ** unit : MJ m2 d-1
                 * name: albedoCoefficient
                               ** description : albedo Coefficient
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.23
                               ** unit : 
                 * name: stefanBoltzman
                               ** description : stefan Boltzman constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 4.903E-09
                               ** unit : 
                 * name: elevation
                               ** description : elevation
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : -500
                               ** default : 0
                               ** unit : m
     - outputs:
                 * name: netRadiation
                               ** description :  net radiation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : MJ m-2 d-1
                 * name: netOutGoingLongWaveRadiation
                               ** description : net OutGoing Long Wave Radiation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    Nsr = (1.0 - albedoCoefficient) * solarRadiation
    clearSkySolarRadiation = (0.75 + (2 * pow(10.0, -5) * elevation)) * extraSolarRadiation
    averageT = (pow(maxTair + 273.16, 4) + pow(minTair + 273.16, 4)) / 2.0
    surfaceEmissivity = 0.34 - (0.14 * sqrt(vaporPressure / 10.0))
    cloudCoverFactor = 1.35 * (solarRadiation / clearSkySolarRadiation) - 0.35
    Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor
    netRadiation = Nsr - Nolr
    netOutGoingLongWaveRadiation = Nolr
    return (netRadiation, netOutGoingLongWaveRadiation)