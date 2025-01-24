# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_ptsoil(evapoTranspirationPriestlyTaylor:float,
         Alpha:float,
         tau:float,
         tauAlpha:float):
    """
     - Name: PtSoil -Version: 1.0, -Time step: 1
     - Description:
                 * Title: PtSoil EnergyLimitedEvaporation Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: Evaporation from the soil in the energy-limited stage 
                 * ShortDescription: Evaporation from the soil in the energy-limited stage
     - inputs:
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration Priestly Taylor
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** default : 120
                               ** min : 0
                               ** max : 1000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.5
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: tau
                               ** description : plant cover factor
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** default : 0.9983
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: tauAlpha
                               ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** default : 0.3
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    energyLimitedEvaporation:float
    AlphaE:float
    if tau < tauAlpha:
        AlphaE = 1.0
    else:
        AlphaE = Alpha - ((Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha))
    energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau
    return energyLimitedEvaporation
#%%CyML Model End%%