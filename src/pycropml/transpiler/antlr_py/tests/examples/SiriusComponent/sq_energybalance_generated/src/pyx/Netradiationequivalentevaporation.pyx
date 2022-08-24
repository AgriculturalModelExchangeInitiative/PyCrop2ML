import numpy 
from math import *
def model_netradiationequivalentevaporation(float netRadiation,
                                            float lambdaV):
    """

    NetRadiationEquivalentEvaporation model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription:  It is given by dividing net radiation by latent heat of vaporization of water 
    ShortDescription: None

    """
    cdef float netRadiationEquivalentEvaporation
    netRadiationEquivalentEvaporation = netRadiation / lambdaV * 1000.0
    return  netRadiationEquivalentEvaporation
