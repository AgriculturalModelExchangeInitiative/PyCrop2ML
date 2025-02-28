# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_stmpsimcalculator(cSoilLayerDepth:'Array[float]',
         cFirstDayMeanTemp:float,
         cAVT:float,
         cABD:float,
         cDampingDepth:float,
         iSoilWaterContent:float,
         iSoilSurfaceTemperature:float,
         SoilTempArray:'Array[float]',
         pSoilLayerDepth:'Array[float]'):
    """
     - Name: STMPsimCalculator -Version: 001, -Time step: 1
     - Description:
                 * Title: STMPsimCalculator model
                 * Authors: Gunther Krauss
                 * Reference: ('http://www.simplace.net/doc/simplace_modules/',)
                 * Institution: INRES Pflanzenbau, Uni Bonn
                 * ExtendedDescription: as given in the documentation
                 * ShortDescription: None
     - inputs:
                 * name: cSoilLayerDepth
                               ** description : Depth of soil layer
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLEARRAY
                               ** len : 
                               ** max : 20.0
                               ** min : 0.03
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
                 * name: cFirstDayMeanTemp
                               ** description : Mean temperature on first day
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : -40.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: cAVT
                               ** description : Constant Temperature of deepest soil layer
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 20.0
                               ** min : -10.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: cABD
                               ** description : Mean bulk density
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 4.0
                               ** min : 1.0
                               ** default : 2.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre
                 * name: cDampingDepth
                               ** description : Initial value for damping depth of soil
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 20.0
                               ** min : 1.5
                               ** default : 6.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
                 * name: iSoilWaterContent
                               ** description : Content of water in Soil
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 20.0
                               ** min : 1.5
                               ** default : 5.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
                 * name: iSoilSurfaceTemperature
                               ** description : Temperature at soil surface
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 20.0
                               ** min : 1.5
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: SoilTempArray
                               ** description : Array of temperature 
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 
                               ** max : 40
                               ** min : -20
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: pSoilLayerDepth
                               ** description : Depth of soil layer plus additional depth
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 
                               ** max : 20.0
                               ** min : 0.03
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
     - outputs:
                 * name: SoilTempArray
                               ** description : Array of temperature 
                               ** datatype : DOUBLEARRAY
                               ** variablecategory : state
                               ** len : 
                               ** max : 40
                               ** min : -20
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    """

    XLAG:float
    XLG1:float
    DP:float
    WC:float
    DD:float
    Z1:float
    i:int
    ZD:float
    RATE:float
    XLAG = .8
    XLG1 = 1 - XLAG
    DP = 1 + (2.5 * cABD / (cABD + exp(6.53 - (5.63 * cABD))))
    WC = 0.001 * iSoilWaterContent / ((.356 - (.144 * cABD)) * cSoilLayerDepth[(len(cSoilLayerDepth) - 1)])
    DD = exp(log(0.5 / DP) * ((1 - WC) / (1 + WC)) * 2) * DP
    Z1 = float(0)
    for i in range(0 , len(SoilTempArray) , 1):
        ZD = 0.5 * (Z1 + pSoilLayerDepth[i]) / DD
        RATE = ZD / (ZD + exp(-.8669 - (2.0775 * ZD))) * (cAVT - iSoilSurfaceTemperature)
        SoilTempArray[i] = XLAG * SoilTempArray[i] + (XLG1 * (RATE + iSoilSurfaceTemperature))
        Z1 = pSoilLayerDepth[i]
    return SoilTempArray
#%%CyML Model End%%

#%%CyML Init Begin%%
def init_stmpsimcalculator(cSoilLayerDepth:'Array[float]',
         cFirstDayMeanTemp:float,
         cAVT:float,
         cABD:float,
         cDampingDepth:float,
         iSoilWaterContent:float,
         iSoilSurfaceTemperature:float):
    SoilTempArray:'array[float]'
    pSoilLayerDepth:'array[float]'
    SoilTempArray = None
    pSoilLayerDepth = None
    tProfileDepth:float
    additionalDepth:float
    firstAdditionalLayerHight:float
    layers:int
    tStmp:'array[float]'
    tz:'array[float]'
    i:int
    depth:float
    tProfileDepth = cSoilLayerDepth[len(cSoilLayerDepth) - 1]
    additionalDepth = cDampingDepth - tProfileDepth
    firstAdditionalLayerHight = additionalDepth - float(floor(additionalDepth))
    layers = int(abs(float(ceil(additionalDepth)))) + len(cSoilLayerDepth)
    tStmp = array("f", [0] * layers)
    tz = array("f", [0] * layers)
    for i in range(0 , len(tStmp) , 1):
        if i < len(cSoilLayerDepth):
            depth = cSoilLayerDepth[i]
        else:
            depth = tProfileDepth + firstAdditionalLayerHight + i - len(cSoilLayerDepth)
        tz[i] = depth
        tStmp[i] = (cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT * depth)) / cDampingDepth
    SoilTempArray = tStmp
    pSoilLayerDepth = tz
    return (SoilTempArray, pSoilLayerDepth)
#%%CyML Init End%%