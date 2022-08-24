import numpy 
from math import *
def model_soilevaporation(float diffusionLimitedEvaporation,
                          float energyLimitedEvaporation):
    """

    SoilEvaporation model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: Starting from a soil at field capacity, soil evaporation  is assumed to                be energy limited during the first phase of evaporation and diffusion limited thereafter.                Hence, the soil evaporation model considers these two processes taking the minimum between                the energy limited evaporation (PtSoil) and the diffused limited                evaporation 
    ShortDescription: None

    """
    cdef float soilEvaporation
    soilEvaporation = min(diffusionLimitedEvaporation, energyLimitedEvaporation)
    return  soilEvaporation
