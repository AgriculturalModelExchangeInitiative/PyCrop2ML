import numpy
from math import *

def model_withsnowsoilsurfacetemperature(float noSnowSoilSurfaceTemperature,
                                         float soilSurfaceTemperatureBelowSnow,
                                         bool hasSnowCover):
    """
    Soil surface temperature with potential snow cover
    Author: Michael Berg-Mohnicke
    Reference: None
    Institution: ZALF e.V.
    ExtendedDescription: None
    ShortDescription: It calculates the soil surface temperature taking a potential snow cover into account
        
    """

    cdef float soilSurfaceTemperature
    if hasSnowCover:
        soilSurfaceTemperature = soilSurfaceTemperatureBelowSnow
    else:
        soilSurfaceTemperature = noSnowSoilSurfaceTemperature
    return  soilSurfaceTemperature



