# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_snowcovercalculator(cCarbonContent:float,
         iTempMax:float,
         iTempMin:float,
         iRadiation:float,
         iRAIN:float,
         iCropResidues:float,
         iPotentialSoilEvaporation:float,
         iLeafAreaIndex:float,
         iSoilTempArray:'Array[float]',
         Albedo:float,
         SnowWaterContent:float,
         SoilSurfaceTemperature:float,
         AgeOfSnow:int):
    """
     - Name: SnowCoverCalculator -Version: 001, -Time step: 1
     - Description:
                 * Title: SnowCoverCalculator model
                 * Authors: Gunther Krauss
                 * Reference: ('http://www.simplace.net/doc/simplace_modules/',)
                 * Institution: INRES Pflanzenbau, Uni Bonn
                 * ExtendedDescription: as given in the documentation
                 * ShortDescription: None
     - inputs:
                 * name: cCarbonContent
                               ** description : Carbon content of upper soil layer
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 20.0
                               ** min : 0.0
                               ** default : 0.5
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/percent
                 * name: iTempMax
                               ** description : Daily maximum temperature
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : -40.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: iTempMin
                               ** description : Daily minimum temperature
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : -40.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: iRadiation
                               ** description : Solar radiation
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 2000.0
                               ** min : 0.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/megajoule_per_square_metre
                 * name: iRAIN
                               ** description : Rain amount
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 60.0
                               ** min : 0.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
                 * name: iCropResidues
                               ** description : Crop residues plus above ground biomass
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 20000.0
                               ** min : 0.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/gram_per_square_metre
                 * name: iPotentialSoilEvaporation
                               ** description : Potenial Evaporation
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 12.0
                               ** min : 0.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
                 * name: iLeafAreaIndex
                               ** description : Leaf area index
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 10.0
                               ** min : 0.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/square_metre_per_square_metre
                 * name: iSoilTempArray
                               ** description : Soil Temp array of last day
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLEARRAY
                               ** len : 
                               ** max : 35.0
                               ** min : -15.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: Albedo
                               ** description : Albedo
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1.0
                               ** min : 0.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
                 * name: SnowWaterContent
                               ** description : Snow water content
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1500.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
                 * name: SoilSurfaceTemperature
                               ** description : Soil surface temperature
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 70.0
                               ** min : -40.0
                               ** default : 0.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: AgeOfSnow
                               ** description : Age of snow
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : null
                               ** min : 0
                               ** default : 0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
     - outputs:
                 * name: SnowWaterContent
                               ** description : Snow water content
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 1500.0
                               ** min : 0.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
                 * name: SoilSurfaceTemperature
                               ** description : Soil surface temperature
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 70.0
                               ** min : -40.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: AgeOfSnow
                               ** description : Age of snow
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : null
                               ** min : 0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
                 * name: SnowIsolationIndex
                               ** description : Snow isolation index
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 1.0
                               ** min : 0.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    """

    SnowIsolationIndex:float
    tiCropResidues:float
    tiSoilTempArray:float
    TMEAN:float
    TAMPL:float
    DST:float
    tSoilSurfaceTemperature:float
    tSnowIsolationIndex:float
    SNOWEVAPORATION:float
    SNOWMELT:float
    EAJ:float
    ageOfSnowFactor:float
    SNPKT:float
    tiCropResidues = iCropResidues * 10.0
    tiSoilTempArray = iSoilTempArray[0]
    TMEAN = 0.5 * (iTempMax + iTempMin)
    TAMPL = 0.5 * (iTempMax - iTempMin)
    DST = TMEAN + (TAMPL * (iRadiation * (1 - Albedo) - 14) / 20)
    if iRAIN > float(0) and (tiSoilTempArray < float(1) or (SnowWaterContent > float(3) or SoilSurfaceTemperature < float(0))):
        SnowWaterContent = SnowWaterContent + iRAIN
    tSnowIsolationIndex = 1.0
    if tiCropResidues < float(10):
        tSnowIsolationIndex = tiCropResidues / (tiCropResidues + exp(5.34 - (2.4 * tiCropResidues)))
    if SnowWaterContent < 1E-10:
        tSnowIsolationIndex = tSnowIsolationIndex * 0.85
        tSoilSurfaceTemperature = 0.5 * (DST + ((1 - tSnowIsolationIndex) * DST) + (tSnowIsolationIndex * tiSoilTempArray))
    else:
        tSnowIsolationIndex = max(SnowWaterContent / (SnowWaterContent + exp(0.47 - (0.62 * SnowWaterContent))), tSnowIsolationIndex)
        tSoilSurfaceTemperature = (1 - tSnowIsolationIndex) * DST + (tSnowIsolationIndex * tiSoilTempArray)
    if SnowWaterContent == float(0) and not (iRAIN > float(0) and tiSoilTempArray < float(1)):
        SnowWaterContent = float(0)
    else:
        EAJ = .5
        if SnowWaterContent < float(5):
            EAJ = exp(-max((0.4 * iLeafAreaIndex), (0.1 * (tiCropResidues + 0.1))))
        SNOWEVAPORATION = iPotentialSoilEvaporation * EAJ
        ageOfSnowFactor = AgeOfSnow / (AgeOfSnow + exp(5.34 - (2.395 * AgeOfSnow)))
        SNPKT = .3333 * (2 * min(tSoilSurfaceTemperature, tiSoilTempArray) + iTempMax)
        if TMEAN > float(0):
            SNOWMELT = max(0, sqrt(iTempMax * iRadiation) * (1.52 + (.54 * ageOfSnowFactor * SNPKT)))
        else:
            SNOWMELT = float(0)
        if SNOWMELT + SNOWEVAPORATION > SnowWaterContent:
            SNOWMELT = SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
            SNOWEVAPORATION = SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
        SnowWaterContent = SnowWaterContent - (SNOWMELT + SNOWEVAPORATION)
        if SnowWaterContent < float(0):
            SnowWaterContent = float(0)
        if SnowWaterContent < float(5):
            AgeOfSnow = 0
        else:
            AgeOfSnow = AgeOfSnow + 1
    SnowIsolationIndex = tSnowIsolationIndex
    SoilSurfaceTemperature = tSoilSurfaceTemperature
    return (SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow, SnowIsolationIndex)
#%%CyML Model End%%

#%%CyML Init Begin%%
def init_snowcovercalculator(cCarbonContent:float,
         iTempMax:float,
         iTempMin:float,
         iRadiation:float,
         iRAIN:float,
         iCropResidues:float,
         iPotentialSoilEvaporation:float,
         iLeafAreaIndex:float,
         iSoilTempArray:'Array[float]'):
    Albedo:float
    SnowWaterContent:float = 0.0
    SoilSurfaceTemperature:float = 0.0
    AgeOfSnow:int = 0
    Albedo = 0.0
    Albedo = 0.0226 * log(cCarbonContent, 10) + 0.1502
    return (Albedo, SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow)
#%%CyML Init End%%