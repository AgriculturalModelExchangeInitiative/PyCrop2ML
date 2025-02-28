# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

from Simplace_SoilTemperature.Snowcovercalculator import model_snowcovercalculator
from Simplace_SoilTemperature.Stmpsimcalculator import model_stmpsimcalculator

#%%CyML Model Begin%%
def model_soiltemperature(cCarbonContent:float,
         iAirTemperatureMax:float,
         iAirTemperatureMin:float,
         iGlobalSolarRadiation:float,
         iRAIN:float,
         iCropResidues:float,
         iPotentialSoilEvaporation:float,
         iLeafAreaIndex:float,
         SoilTempArray:'Array[float]',
         cSoilLayerDepth:'Array[float]',
         cFirstDayMeanTemp:float,
         cAverageGroundTemperature:float,
         cAverageBulkDensity:float,
         cDampingDepth:float,
         iSoilWaterContent:float,
         Albedo:float,
         SnowWaterContent:float,
         SoilSurfaceTemperature:float,
         AgeOfSnow:int,
         pSoilLayerDepth:'Array[float]'):
    """
     - Name: SoilTemperature -Version: 001, -Time step: 1
     - Description:
                 * Title: SoilTemperature model
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
                 * name: iAirTemperatureMax
                               ** description : Daily maximum temperature
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : -40.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: iAirTemperatureMin
                               ** description : Daily minimum temperature
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : -40.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: iGlobalSolarRadiation
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
                 * name: SoilTempArray
                               ** description : Soil Temp array of last day
                               ** inputtype : variable
                               ** variablecategory : exogenous
                               ** datatype : DOUBLEARRAY
                               ** len : 
                               ** max : 35.0
                               ** min : -15.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
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
                 * name: cAverageGroundTemperature
                               ** description : Constant Temperature of deepest soil layer
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 20.0
                               ** min : -10.0
                               ** default : 
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: cAverageBulkDensity
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
                 * name: SoilSurfaceTemperature
                               ** description : Soil surface temperature
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 70.0
                               ** min : -40.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: SnowIsolationIndex
                               ** description : Snow isolation index
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 1.0
                               ** min : 0.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
                 * name: SnowWaterContent
                               ** description : Snow water content
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 1500.0
                               ** min : 0.0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
                 * name: SoilTempArray
                               ** description : Array of temperature 
                               ** datatype : DOUBLEARRAY
                               ** variablecategory : state
                               ** len : 
                               ** max : 40
                               ** min : -20
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
                 * name: AgeOfSnow
                               ** description : Age of snow
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : null
                               ** min : 0
                               ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    """

    iTempMax:float
    iTempMin:float
    iRadiation:float
    iSoilTempArray:'array[float]'
    SnowIsolationIndex:float
    cAVT:float
    cABD:float
    iSoilSurfaceTemperature:float
    iTempMax = iAirTemperatureMax
    iTempMin = iAirTemperatureMin
    iRadiation = iGlobalSolarRadiation
    iSoilTempArray = SoilTempArray
    cAVT = cAverageGroundTemperature
    cABD = cAverageBulkDensity
    (SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow, SnowIsolationIndex) = model_snowcovercalculator(cCarbonContent, iTempMax, iTempMin, iRadiation, iRAIN, iCropResidues, iPotentialSoilEvaporation, iLeafAreaIndex, iSoilTempArray, Albedo, SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow)
    iSoilSurfaceTemperature = SoilSurfaceTemperature
    SoilTempArray = model_stmpsimcalculator(cSoilLayerDepth, cFirstDayMeanTemp, cAVT, cABD, cDampingDepth, iSoilWaterContent, iSoilSurfaceTemperature, SoilTempArray, pSoilLayerDepth)
    return (SoilSurfaceTemperature, SnowIsolationIndex, SnowWaterContent, SoilTempArray, AgeOfSnow)
#%%CyML Model End%%