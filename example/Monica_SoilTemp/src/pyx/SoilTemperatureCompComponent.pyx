from datetime import datetime
from math import *
from Monica_SoilTemp.soiltemperature import model_soiltemperature
from Monica_SoilTemp.nosnowsoilsurfacetemperature import model_nosnowsoilsurfacetemperature
from Monica_SoilTemp.withsnowsoilsurfacetemperature import model_withsnowsoilsurfacetemperature
def model_soiltemperaturecomp(float tmin,
      float tmax,
      float globrad,
      float dampingFactor,
      float soilCoverage,
      float soilSurfaceTemperatureBelowSnow,
      bool hasSnowCover,
      float timeStep,
      float soilMoistureConst[noOfSoilLayers],
      float baseTemp,
      float initialSurfaceTemp,
      float densityAir,
      float specificHeatCapacityAir,
      float densityHumus,
      float specificHeatCapacityHumus,
      float densityWater,
      float specificHeatCapacityWater,
      float quartzRawDensity,
      float specificHeatCapacityQuartz,
      float nTau,
      int noOfTempLayers,
      int noOfTempLayersPlus1,
      int noOfSoilLayers,
      float layerThickness[noOfTempLayers],
      float soilBulkDensity[noOfSoilLayers],
      float saturation[noOfSoilLayers],
      float soilOrganicMatter[noOfSoilLayers],
      float V[noOfTempLayers],
      float B[noOfTempLayers],
      float volumeMatrix[noOfTempLayers],
      float volumeMatrixOld[noOfTempLayers],
      float matrixPrimaryDiagonal[noOfTempLayers],
      float matrixSecondaryDiagonal[noOfTempLayersPlus1],
      float heatConductivity[noOfTempLayers],
      float heatConductivityMean[noOfTempLayers],
      float heatCapacity[noOfTempLayers],
      float solution[noOfTempLayers],
      float matrixDiagonal[noOfTempLayers],
      float matrixLowerTriangle[noOfTempLayers],
      float heatFlow[noOfTempLayers]):
    cdef float soilSurfaceTemperature
    cdef float soilTemperature[noOfTempLayers]
    cdef float noSnowSoilSurfaceTemperature
    soilSurfaceTemperature = model_nosnowsoilsurfacetemperature(tmin,tmax,globrad,soilCoverage,dampingFactor,soilSurfaceTemperature)
    noSnowSoilSurfaceTemperature = soilSurfaceTemperature
    soilSurfaceTemperature = model_withsnowsoilsurfacetemperature(noSnowSoilSurfaceTemperature,soilSurfaceTemperatureBelowSnow,hasSnowCover)
    soilTemperature = model_soiltemperature(noOfSoilLayers,noOfTempLayers,noOfTempLayersPlus1,soilSurfaceTemperature,timeStep,soilMoistureConst,baseTemp,initialSurfaceTemp,densityAir,specificHeatCapacityAir,densityHumus,specificHeatCapacityHumus,densityWater,specificHeatCapacityWater,quartzRawDensity,specificHeatCapacityQuartz,nTau,layerThickness,soilBulkDensity,saturation,soilOrganicMatter,soilTemperature,V,B,volumeMatrix,volumeMatrixOld,matrixPrimaryDiagonal,matrixSecondaryDiagonal,heatConductivity,heatConductivityMean,heatCapacity,solution,matrixDiagonal,matrixLowerTriangle,heatFlow)

    return soilSurfaceTemperature, soilTemperature