# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_netradiationequivalentevaporation(lambdaV:float,
         netRadiation:float):
    """
     - Name: NetRadiationEquivalentEvaporation -Version: 1.0, -Time step: 1
     - Description:
                 * Title: NetRadiationEquivalentEvaporation Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference:  https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription:  It is given by dividing net radiation by latent heat of vaporization of water 
                 * ShortDescription: It is given by dividing net radiation by latent heat of vaporization of water
     - inputs:
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ kg-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: netRadiation
                               ** description : net radiation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 1.566
                               ** min : 0
                               ** max : 5000
                               ** unit : MJ m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
     - outputs:
                 * name: netRadiationEquivalentEvaporation
                               ** variablecategory : auxiliary
                               ** description : net Radiation in Equivalent Evaporation 
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    netRadiationEquivalentEvaporation:float
    netRadiationEquivalentEvaporation = netRadiation / lambdaV * 1000.0
    return netRadiationEquivalentEvaporation
#%%CyML Model End%%