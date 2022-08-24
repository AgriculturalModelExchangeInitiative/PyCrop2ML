import numpy 
from math import *
def model_netradiation(float minTair,
                       float maxTair,
                       float solarRadiation,
                       float vaporPressure,
                       float extraSolarRadiation,
                       float albedoCoefficient,
                       float stefanBoltzman,
                       float elevation):
    """

    NetRadiation model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short                     and long wavelength radiation 
    ShortDescription: None

    """
    cdef float netRadiation
    cdef float netOutGoingLongWaveRadiation
    cdef float Nsr 
    cdef float clearSkySolarRadiation 
    cdef float averageT 
    cdef float surfaceEmissivity 
    cdef float cloudCoverFactor 
    cdef float Nolr 
    Nsr = (1.0 - albedoCoefficient) * solarRadiation
    clearSkySolarRadiation = (0.75 + (2 * pow(10.0, -5) * elevation)) * extraSolarRadiation
    averageT = (pow(maxTair + 273.16, 4) + pow(minTair + 273.16, 4)) / 2.0
    surfaceEmissivity = 0.34 - (0.14 * sqrt(vaporPressure / 10.0))
    cloudCoverFactor = 1.35 * (solarRadiation / clearSkySolarRadiation) - 0.35
    Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor
    netRadiation = Nsr - Nolr
    netOutGoingLongWaveRadiation = Nolr
    return  netRadiation, netOutGoingLongWaveRadiation
