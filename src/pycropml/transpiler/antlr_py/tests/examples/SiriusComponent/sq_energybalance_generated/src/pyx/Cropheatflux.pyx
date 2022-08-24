import numpy 
from math import *
def model_cropheatflux(float netRadiationEquivalentEvaporation,
                       float soilHeatFlux,
                       float potentialTranspiration):
    """

    CropHeatFlux model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: It is calculated from net Radiation, soil heat flux and potential transpiration 
    ShortDescription: None

    """
    cdef float cropHeatFlux
    cropHeatFlux = netRadiationEquivalentEvaporation - soilHeatFlux - potentialTranspiration
    return  cropHeatFlux
