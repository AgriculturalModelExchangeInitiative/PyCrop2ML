import numpy 
from math import *
def model_potentialtranspiration(float evapoTranspiration,
                                 float tau):
    """

    PotentialTranspiration model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict                    transpiration as soil moisture is depleted 
    ShortDescription: None

    """
    cdef float potentialTranspiration
    potentialTranspiration = evapoTranspiration * (1.0 - tau)
    return  potentialTranspiration
