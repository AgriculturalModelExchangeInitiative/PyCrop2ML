# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_potentialtranspiration(evapoTranspiration,
         tau):
    """
     - Name: PotentialTranspiration -Version: 001, -Time step: 1
     - Description:
                 * Title: PotentialTranspiration model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict                    transpiration as soil moisture is depleted 
                 * ShortDescription: None
     - inputs:
                 * name: evapoTranspiration
                               ** description : evapoTranspiration
                               ** inputtype : variable
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 
                               ** unit : mm
                 * name: tau
                               ** description : plant cover factor
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.9983
                               ** unit : 
     - outputs:
                 * name: potentialTranspiration
                               ** description : potential Transpiration 
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
    """

    potentialTranspiration = evapoTranspiration * (1.0 - tau)
    return potentialTranspiration