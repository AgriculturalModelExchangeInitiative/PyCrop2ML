from datetime import datetime
from math import *
from SoilTemp.Snowcovercalculator import model_snowcovercalculator
from SoilTemp.Stmpsimcalculator import model_stmpsimcalculator
def model_soiltemperature(float cCarbonContent,
      float iAirTemperatureMax,
      float iAirTemperatureMin,
      float iGlobalSolarRadiation,
      float iRAIN,
      float iCropResidues,
      float iPotentialSoilEvaporation,
      float iLeafAreaIndex,
      float SoilTempArray[],
      float cSoilLayerDepth[],
      float cFirstDayMeanTemp,
      float cAverageGroundTemperature,
      float cAverageBulkDensity,
      float cDampingDepth,
      float iSoilWaterContent):
    cdef float iTempMax
    cdef float iTempMin
    cdef float iRadiation
    cdef float iSoilTempArray[]
    cdef float Albedo
    cdef float SnowWaterContent
    cdef float SoilSurfaceTemperature
    cdef int AgeOfSnow
    cdef float SnowIsolationIndex
    cdef float cAVT
    cdef float cABD
    cdef float iSoilSurfaceTemperature
    cdef float pSoilLayerDepth[]
    iTempMax = iAirTemperatureMax 
    iTempMin = iAirTemperatureMin 
    iRadiation = iGlobalSolarRadiation 
    iSoilTempArray = SoilTempArray 
    cAVT = cAverageGroundTemperature 
    cABD = cAverageBulkDensity 
    SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow, SnowIsolationIndex = model_snowcovercalculator( cCarbonContent,iTempMax,iTempMin,iRadiation,iRAIN,iCropResidues,iPotentialSoilEvaporation,iLeafAreaIndex,iSoilTempArray,Albedo,SnowWaterContent,SoilSurfaceTemperature,AgeOfSnow)
    iSoilSurfaceTemperature = SoilSurfaceTemperature
    SoilTempArray = model_stmpsimcalculator( cSoilLayerDepth,cFirstDayMeanTemp,cAVT,cABD,cDampingDepth,iSoilWaterContent,iSoilSurfaceTemperature,SoilTempArray,pSoilLayerDepth)
    return SoilSurfaceTemperature, SnowIsolationIndex, SnowWaterContent, SoilTempArray