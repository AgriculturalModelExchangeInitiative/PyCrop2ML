import numpy 
from math import *
def model_ptsoil(float evapoTranspirationPriestlyTaylor,
                 float Alpha,
                 float tau,
                 float tauAlpha):
    """

    PtSoil model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: Evaporation from the soil in the energy-limited stage 
    ShortDescription: None

    """
    cdef float energyLimitedEvaporation
    cdef float AlphaE 
    if tau < tauAlpha:
        AlphaE = 1.0
    else:
        AlphaE = Alpha - ((Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha))
    energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau
    return  energyLimitedEvaporation
