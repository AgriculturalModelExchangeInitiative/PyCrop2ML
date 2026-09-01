# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Init Begin%%
def init_soiltemperature(noOfTempLayers:int,
         noOfSoilLayers:int,
         timeStep:float,
         soilMoistureConst:float,
         baseTemp:float,
         initialSurfaceTemp:float,
         densityAir:float,
         specificHeatCapacityAir:float,
         densityHumus:float,
         specificHeatCapacityHumus:float,
         densityWater:float,
         specificHeatCapacityWater:float,
         quartzRawDensity:float,
         specificHeatCapacityQuartz:float,
         nTau:float,
         layerThickness:'Array[float]',
         soilBulkDensity:'Array[float]',
         saturation:'Array[float]',
         soilOrganicMatter:'Array[float]'):
    soilSurfaceTemperature:float = 0.0
    soilTemperature:'array[float]' = array('f',[0.0]*22)
    V:'array[float]' = array('f',[0.0]*22)
    B:'array[float]' = array('f',[0.0]*22)
    volumeMatrix:'array[float]' = array('f',[0.0]*22)
    volumeMatrixOld:'array[float]' = array('f',[0.0]*22)
    matrixPrimaryDiagonal:'array[float]' = array('f',[0.0]*22)
    matrixSecondaryDiagonal:'array[float]' = array('f',[0.0]*23)
    heatConductivity:'array[float]' = array('f',[0.0]*22)
    heatConductivityMean:'array[float]' = array('f',[0.0]*22)
    heatCapacity:'array[float]' = array('f',[0.0]*22)
    solution:'array[float]' = array('f',[0.0]*22)
    matrixDiagonal:'array[float]' = array('f',[0.0]*22)
    matrixLowerTriangle:'array[float]' = array('f',[0.0]*22)
    heatFlow:'array[float]' = array('f',[0.0]*22)
    soilTemperature = array('f', [0.0]*22)
    V = array('f', [0.0]*22)
    B = array('f', [0.0]*22)
    volumeMatrix = array('f', [0.0]*22)
    volumeMatrixOld = array('f', [0.0]*22)
    matrixPrimaryDiagonal = array('f', [0.0]*22)
    matrixSecondaryDiagonal = array('f', [0.0]*23)
    heatConductivity = array('f', [0.0]*22)
    heatConductivityMean = array('f', [0.0]*22)
    heatCapacity = array('f', [0.0]*22)
    solution = array('f', [0.0]*22)
    matrixDiagonal = array('f', [0.0]*22)
    matrixLowerTriangle = array('f', [0.0]*22)
    heatFlow = array('f', [0.0]*22)
    groundLayer:int
    bottomLayer:int
    lti_1:float
    lti:float
    ts:float
    dw:float
    cw:float
    dq:float
    cq:float
    da:float
    ca:float
    dh:float
    ch:float
    sbdi:float
    smi:float
    sati:float
    somi:float
    hci_1:float
    hci:float
    i:int
    for i in range(0 , noOfSoilLayers , 1):
        soilTemperature[i] = (1.0 - (float(i) / noOfSoilLayers)) * initialSurfaceTemp + (float(i) / noOfSoilLayers * baseTemp)
    groundLayer = noOfTempLayers - 2
    bottomLayer = noOfTempLayers - 1
    layerThickness[groundLayer] = 2.0 * layerThickness[(groundLayer - 1)]
    layerThickness[bottomLayer] = 1.0
    soilTemperature[groundLayer] = (soilTemperature[groundLayer - 1] + baseTemp) * 0.5
    soilTemperature[bottomLayer] = baseTemp
    V[0] = layerThickness[0]
    B[0] = 2.0 / layerThickness[0]
    for i in range(1 , noOfTempLayers , 1):
        lti_1 = layerThickness[i - 1]
        lti = layerThickness[i]
        B[i] = 2.0 / (lti + lti_1)
        V[i] = lti * nTau
    ts = timeStep
    dw = densityWater
    cw = specificHeatCapacityWater
    dq = quartzRawDensity
    cq = specificHeatCapacityQuartz
    da = densityAir
    ca = specificHeatCapacityAir
    dh = densityHumus
    ch = specificHeatCapacityHumus
    for i in range(0 , noOfSoilLayers , 1):
        sbdi = soilBulkDensity[i]
        smi = soilMoistureConst
        heatConductivity[i] = (3.0 * (sbdi / 1000.0) - 1.7) * 0.001 / (1.0 + ((11.5 - (5.0 * (sbdi / 1000.0))) * exp(-50.0 * pow(smi / (sbdi / 1000.0), 1.5)))) * 86400.0 * ts * 100.0 * 4.184
        sati = saturation[i]
        somi = soilOrganicMatter[i] / da * sbdi
        heatCapacity[i] = smi * dw * cw + ((sati - smi) * da * ca) + (somi * dh * ch) + ((1.0 - sati - somi) * dq * cq)
    heatCapacity[groundLayer] = heatCapacity[groundLayer - 1]
    heatCapacity[bottomLayer] = heatCapacity[groundLayer]
    heatConductivity[groundLayer] = heatConductivity[groundLayer - 1]
    heatConductivity[bottomLayer] = heatConductivity[groundLayer]
    soilSurfaceTemperature = initialSurfaceTemp
    heatConductivityMean[0] = heatConductivity[0]
    for i in range(1 , noOfTempLayers , 1):
        lti_1 = layerThickness[i - 1]
        lti = layerThickness[i]
        hci_1 = heatConductivity[i - 1]
        hci = heatConductivity[i]
        heatConductivityMean[i] = (lti_1 * hci_1 + (lti * hci)) / (lti + lti_1)
    for i in range(0 , noOfTempLayers , 1):
        volumeMatrix[i] = V[i] * heatCapacity[i]
        volumeMatrixOld[i] = volumeMatrix[i]
        matrixSecondaryDiagonal[i] = -B[i] * heatConductivityMean[i]
    matrixSecondaryDiagonal[bottomLayer + 1] = 0.0
    for i in range(0 , noOfTempLayers , 1):
        matrixPrimaryDiagonal[i] = volumeMatrix[i] - matrixSecondaryDiagonal[i] - matrixSecondaryDiagonal[i + 1]
    return (soilSurfaceTemperature, soilTemperature, V, B, volumeMatrix, volumeMatrixOld, matrixPrimaryDiagonal, matrixSecondaryDiagonal, heatConductivity, heatConductivityMean, heatCapacity, solution, matrixDiagonal, matrixLowerTriangle, heatFlow)
#%%CyML Init End%%

#%%CyML Model Begin%%
def model_soiltemperature(noOfTempLayers:int,
         noOfSoilLayers:int,
         soilSurfaceTemperature:float,
         timeStep:float,
         soilMoistureConst:float,
         baseTemp:float,
         initialSurfaceTemp:float,
         densityAir:float,
         specificHeatCapacityAir:float,
         densityHumus:float,
         specificHeatCapacityHumus:float,
         densityWater:float,
         specificHeatCapacityWater:float,
         quartzRawDensity:float,
         specificHeatCapacityQuartz:float,
         nTau:float,
         layerThickness:'Array[float]',
         soilBulkDensity:'Array[float]',
         saturation:'Array[float]',
         soilOrganicMatter:'Array[float]',
         soilTemperature:'Array[float]',
         V:'Array[float]',
         B:'Array[float]',
         volumeMatrix:'Array[float]',
         volumeMatrixOld:'Array[float]',
         matrixPrimaryDiagonal:'Array[float]',
         matrixSecondaryDiagonal:'Array[float]',
         heatConductivity:'Array[float]',
         heatConductivityMean:'Array[float]',
         heatCapacity:'Array[float]',
         solution:'Array[float]',
         matrixDiagonal:'Array[float]',
         matrixLowerTriangle:'Array[float]',
         heatFlow:'Array[float]'):
    """
     - Name: SoilTemperature -Version: 1, -Time step: 1
     - Description:
                 * Title: Model of soil temperature
                 * Authors: Michael Berg-Mohnicke
                 * Reference: None
                 * Institution: ZALF e.V.
                 * ExtendedDescription: None
                 * ShortDescription: Calculates the soil temperature at all soil layers
     - inputs:
                 * name: noOfTempLayers
                               ** description : noOfTempLayers=noOfSoilLayers+2
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 
                               ** min : 
                               ** default : 22
                               ** unit : dimensionless
                 * name: noOfSoilLayers
                               ** description : noOfSoilLayers
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 
                               ** min : 
                               ** default : 20.0
                               ** unit : dimensionless
                 * name: soilSurfaceTemperature
                               ** description : current soilSurfaceTemperature
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 80.0
                               ** min : -50.0
                               ** default : 0.0
                               ** unit : °C
                 * name: timeStep
                               ** description : timeStep
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 1.0
                               ** unit : dimensionless
                 * name: soilMoistureConst
                               ** description : initial soilmoisture
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 0.25
                               ** unit : m**3/m**3
                 * name: baseTemp
                               ** description : baseTemperature
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 9.5
                               ** unit : °C
                 * name: initialSurfaceTemp
                               ** description : initialSurfaceTemperature
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 10.0
                               ** unit : °C
                 * name: densityAir
                               ** description : DensityAir
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 1.25
                               ** unit : kg/m**3
                 * name: specificHeatCapacityAir
                               ** description : SpecificHeatCapacityAir
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 1005.0
                               ** unit : J/kg/K
                 * name: densityHumus
                               ** description : DensityHumus
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 1300.0
                               ** unit : kg/m**3
                 * name: specificHeatCapacityHumus
                               ** description : SpecificHeatCapacityHumus
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 1920.0
                               ** unit : J/kg/K
                 * name: densityWater
                               ** description : DensityWater
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 1000.0
                               ** unit : kg/m**3
                 * name: specificHeatCapacityWater
                               ** description : SpecificHeatCapacityWater
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 4192.0
                               ** unit : J/kg/K
                 * name: quartzRawDensity
                               ** description : QuartzRawDensity
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 2650.0
                               ** unit : kg/m**3
                 * name: specificHeatCapacityQuartz
                               ** description : SpecificHeatCapacityQuartz
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 750.0
                               ** unit : J/kg/K
                 * name: nTau
                               ** description : NTau
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 
                               ** min : 
                               ** default : 0.65
                               ** unit : ?
                 * name: layerThickness
                               ** description : layerThickness
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : m
                 * name: soilBulkDensity
                               ** description : bulkDensity
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLEARRAY
                               ** len : 20
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : kg/m**3
                 * name: saturation
                               ** description : saturation
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLEARRAY
                               ** len : 20
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : m**3/m**3
                 * name: soilOrganicMatter
                               ** description : soilOrganicMatter
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLEARRAY
                               ** len : 20
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : m**3/m**3
                 * name: soilTemperature
                               ** description : soilTemperature
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: V
                               ** description : V
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: B
                               ** description : B
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: volumeMatrix
                               ** description : volumeMatrix
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: volumeMatrixOld
                               ** description : volumeMatrixOld
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: matrixPrimaryDiagonal
                               ** description : matrixPrimaryDiagonal
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: matrixSecondaryDiagonal
                               ** description : matrixSecondaryDiagonal
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 23
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: heatConductivity
                               ** description : heatConductivity
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: heatConductivityMean
                               ** description : heatConductivityMean
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: heatCapacity
                               ** description : heatCapacity
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: solution
                               ** description : solution
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: matrixDiagonal
                               ** description : matrixDiagonal
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: matrixLowerTriangle
                               ** description : matrixLowerTriangle
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
                 * name: heatFlow
                               ** description : heatFlow
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : °C
     - outputs:
                 * name: soilTemperature
                               ** description : soilTemperature next day
                               ** variablecategory : state
                               ** datatype : DOUBLEARRAY
                               ** len : 22
                               ** max : 
                               ** min : 
                               ** unit : °C
    """

    groundLayer:int
    bottomLayer:int
    i:int
    j:int
    j_1:int
    groundLayer = noOfTempLayers - 2
    bottomLayer = noOfTempLayers - 1
    heatFlow[0] = soilSurfaceTemperature * B[0] * heatConductivityMean[0]
    for i in range(0 , noOfTempLayers , 1):
        solution[i] = (volumeMatrixOld[i] + ((volumeMatrix[i] - volumeMatrixOld[i]) / layerThickness[i])) * soilTemperature[i] + heatFlow[i]
    matrixDiagonal[0] = matrixPrimaryDiagonal[0]
    for i in range(1 , noOfTempLayers , 1):
        matrixLowerTriangle[i] = matrixSecondaryDiagonal[i] / matrixDiagonal[(i - 1)]
        matrixDiagonal[i] = matrixPrimaryDiagonal[i] - (matrixLowerTriangle[i] * matrixSecondaryDiagonal[i])
    for i in range(1 , noOfTempLayers , 1):
        solution[i] = solution[i] - (matrixLowerTriangle[i] * solution[(i - 1)])
    solution[bottomLayer] = solution[bottomLayer] / matrixDiagonal[bottomLayer]
    for i in range(0 , bottomLayer , 1):
        j = bottomLayer - 1 - i
        j_1 = j + 1
        solution[j] = solution[j] / matrixDiagonal[j] - (matrixLowerTriangle[j_1] * solution[j_1])
    for i in range(0 , noOfTempLayers , 1):
        soilTemperature[i] = solution[i]
    for i in range(0 , noOfSoilLayers , 1):
        volumeMatrixOld[i] = volumeMatrix[i]
    volumeMatrixOld[groundLayer] = volumeMatrix[groundLayer]
    volumeMatrixOld[bottomLayer] = volumeMatrix[bottomLayer]
    return soilTemperature
#%%CyML Model End%%