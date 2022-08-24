import numpy 
from math import *
def model_evapotranspiration(float evapoTranspirationPriestlyTaylor,
                             float evapoTranspirationPenman,
                             int isWindVpDefined):
    """

    EvapoTranspiration model
    Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
    Reference: None
    Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
    ExtendedDescription: According to the availability of wind and/or vapor pressure daily data, the            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor            (Priestley and Taylor 1972) method 
    ShortDescription: None

    """
    cdef float evapoTranspiration
    if isWindVpDefined == 1:
        evapoTranspiration = evapoTranspirationPenman
    else:
        evapoTranspiration = evapoTranspirationPriestlyTaylor
    return  evapoTranspiration
