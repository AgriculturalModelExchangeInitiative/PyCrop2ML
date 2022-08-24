import numpy 
from math import *
def model_conductance(float plantHeight,
                      float wind,
                      float vonKarman,
                      float heightWeatherMeasurements,
                      float zm,
                      float zh,
                      float d):
    """

    Conductance model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: The boundary layer conductance is expressed as the wind speed profile above the            canopy and the canopy structure. The approach does not take into account buoyancy            effects.         
    ShortDescription: None

    """
    cdef float conductance
    cdef float h 
    h = max(10.0, plantHeight) / 100.0
    conductance = wind * pow(vonKarman, 2) / (log((heightWeatherMeasurements - (d * h)) / (zm * h)) * log((heightWeatherMeasurements - (d * h)) / (zh * h)))
    return  conductance
