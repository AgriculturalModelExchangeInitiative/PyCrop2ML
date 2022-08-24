import numpy 
from math import *
def model_priestlytaylor(float netRadiationEquivalentEvaporation,
                         float hslope,
                         float psychrometricConstant,
                         float Alpha):
    """

    PriestlyTaylor model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: Calculate Energy Balance 
    ShortDescription: None

    """
    cdef float evapoTranspirationPriestlyTaylor
    evapoTranspirationPriestlyTaylor = max(Alpha * hslope * netRadiationEquivalentEvaporation / (hslope + psychrometricConstant), 0.0)
    return  evapoTranspirationPriestlyTaylor
