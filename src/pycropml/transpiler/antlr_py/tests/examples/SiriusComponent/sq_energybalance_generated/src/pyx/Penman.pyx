import numpy 
from math import *
def model_penman(float evapoTranspirationPriestlyTaylor,
                 float hslope,
                 float VPDair,
                 float conductance,
                 float psychrometricConstant,
                 float Alpha,
                 float lambdaV,
                 float rhoDensityAir,
                 float specificHeatCapacityAir):
    """

    Penman model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: It uses Penmann-Monteith method vase on the availability of wind and vapor pressure daily data
    ShortDescription: None

    """
    cdef float evapoTranspirationPenman
    evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + (1000.0 * (rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / (lambdaV * (hslope + psychrometricConstant))))
    return  evapoTranspirationPenman
