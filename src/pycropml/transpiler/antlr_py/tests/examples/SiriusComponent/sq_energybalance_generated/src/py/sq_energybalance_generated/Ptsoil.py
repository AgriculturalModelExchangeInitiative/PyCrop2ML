# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_ptsoil(evapoTranspirationPriestlyTaylor,
         Alpha,
         tau,
         tauAlpha):
    """
     - Name: PtSoil -Version: 001, -Time step: 1
     - Description:
                 * Title: PtSoil model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: Evaporation from the soil in the energy-limited stage 
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
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 1.5
                               ** unit : 
                 * name: tau
                               ** description : plant cover factor
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 0.9983
                               ** unit : 
                 * name: tauAlpha
                               ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.3
                               ** unit : 
     - outputs:
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    if tau < tauAlpha:
        AlphaE = 1.0
    else:
        AlphaE = Alpha - ((Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha))
    energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau
    return energyLimitedEvaporation