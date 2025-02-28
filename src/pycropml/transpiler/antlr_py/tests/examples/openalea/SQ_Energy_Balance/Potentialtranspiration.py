# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_potentialtranspiration(evapoTranspiration:float,
         tau:float):
    """
     - Name: PotentialTranspiration -Version: 1.0, -Time step: 1
     - Description:
                 * Title: PotentialTranspiration Model
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference:  https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
             
                 * ExtendedDescription: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict
                         transpiration as soil moisture is depleted 
                 * ShortDescription: It uses the availability of water from the soil reservoir as a method to restrict
                 transpiration as soil moisture is depleted
     - inputs:
                 * name: evapoTranspiration
                               ** description : evapoTranspiration
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** default : 830.958
                               ** min : 0
                               ** max : 10000
                               ** unit : mm
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: tau
                               ** description : plant cover factor
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** default : 0.9983
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: potentialTranspiration
                               ** description : potential Transpiration 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    potentialTranspiration:float
    potentialTranspiration = evapoTranspiration * (1.0 - tau)
    return potentialTranspiration
#%%CyML Model End%%