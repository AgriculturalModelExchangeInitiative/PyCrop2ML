import numpy 
from math import *
def model_soilheatflux(float netRadiationEquivalentEvaporation,
                       float soilEvaporation,
                       float tau):
    """

    SoilHeatFlux model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: The available energy in the soil 
    ShortDescription: None

    """
    cdef float soilHeatFlux
    soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation
    return  soilHeatFlux
