# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_evapotranspiration(evapoTranspirationPriestlyTaylor,
         evapoTranspirationPenman,
         isWindVpDefined):
    """
     - Name: EvapoTranspiration -Version: 001, -Time step: 1
     - Description:
                 * Title: EvapoTranspiration model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: According to the availability of wind and/or vapor pressure daily data, the            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor            (Priestley and Taylor 1972) method 
                 * ShortDescription: None
     - inputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : g m-2 d-1
                 * name: isWindVpDefined
                               ** description : if wind and vapour pressure are defined
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
     - outputs:
                 * name: evapoTranspiration
                               ** description : evapoTranspiration
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : mm
    """

    if isWindVpDefined == 1:
        evapoTranspiration = evapoTranspirationPenman
    else:
        evapoTranspiration = evapoTranspirationPriestlyTaylor
    return evapoTranspiration