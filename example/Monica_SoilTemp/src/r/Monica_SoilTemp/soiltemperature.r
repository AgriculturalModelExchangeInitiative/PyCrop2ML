library(gsubfn)

init_soiltemperature <- function (noOfSoilLayers,
         noOfTempLayers,
         noOfTempLayersPlus1,
         timeStep,
         soilMoistureConst,
         baseTemp,
         initialSurfaceTemp,
         densityAir,
         specificHeatCapacityAir,
         densityHumus,
         specificHeatCapacityHumus,
         densityWater,
         specificHeatCapacityWater,
         quartzRawDensity,
         specificHeatCapacityQuartz,
         nTau,
         layerThickness,
         soilBulkDensity,
         saturation,
         soilOrganicMatter){
    soilSurfaceTemperature <- 0.0
    soilTemperature <- vector(,noOfTempLayers)
    V <- vector(,noOfTempLayers)
    B <- vector(,noOfTempLayers)
    volumeMatrix <- vector(,noOfTempLayers)
    volumeMatrixOld <- vector(,noOfTempLayers)
    matrixPrimaryDiagonal <- vector(,noOfTempLayers)
    matrixSecondaryDiagonal <- vector(,noOfTempLayersPlus1)
    heatConductivity <- vector(,noOfTempLayers)
    heatConductivityMean <- vector(,noOfTempLayers)
    heatCapacity <- vector(,noOfTempLayers)
    solution <- vector(,noOfTempLayers)
    matrixDiagonal <- vector(,noOfTempLayers)
    matrixLowerTriangle <- vector(,noOfTempLayers)
    heatFlow <- vector(,noOfTempLayers)
    soilTemperature <-  rep(0.0,noOfTempLayers)
    V <-  rep(0.0,noOfTempLayers)
    B <-  rep(0.0,noOfTempLayers)
    volumeMatrix <-  rep(0.0,noOfTempLayers)
    volumeMatrixOld <-  rep(0.0,noOfTempLayers)
    matrixPrimaryDiagonal <-  rep(0.0,noOfTempLayers)
    matrixSecondaryDiagonal <-  rep(0.0,noOfTempLayersPlus1)
    heatConductivity <-  rep(0.0,noOfTempLayers)
    heatConductivityMean <-  rep(0.0,noOfTempLayers)
    heatCapacity <-  rep(0.0,noOfTempLayers)
    solution <-  rep(0.0,noOfTempLayers)
    matrixDiagonal <-  rep(0.0,noOfTempLayers)
    matrixLowerTriangle <-  rep(0.0,noOfTempLayers)
    heatFlow <-  rep(0.0,noOfTempLayers)
    for( i in seq(0, noOfSoilLayers-1, 1)){
        soilTemperature[i+1] <- (1.0 - (as.double(i) / noOfSoilLayers)) * initialSurfaceTemp + (as.double(i) / noOfSoilLayers * baseTemp)
    }
    groundLayer <- noOfTempLayers - 2
    bottomLayer <- noOfTempLayers - 1
    layerThickness[groundLayer+1] <- 2.0 * layerThickness[(groundLayer - 1)+1]
    layerThickness[bottomLayer+1] <- 1.0
    soilTemperature[groundLayer+1] <- (soilTemperature[groundLayer - 1+1] + baseTemp) * 0.5
    soilTemperature[bottomLayer+1] <- baseTemp
    V[1] <- layerThickness[1]
    B[1] <- 2.0 / layerThickness[1]
    for( i in seq(1, noOfTempLayers-1, 1)){
        lti_1 <- layerThickness[i - 1+1]
        lti <- layerThickness[i+1]
        B[i+1] <- 2.0 / (lti + lti_1)
        V[i+1] <- lti * nTau
    }
    ts <- timeStep
    dw <- densityWater
    cw <- specificHeatCapacityWater
    dq <- quartzRawDensity
    cq <- specificHeatCapacityQuartz
    da <- densityAir
    ca <- specificHeatCapacityAir
    dh <- densityHumus
    ch <- specificHeatCapacityHumus
    for( i in seq(0, noOfSoilLayers-1, 1)){
        sbdi <- soilBulkDensity[i+1]
        smi <- soilMoistureConst[i+1]
        heatConductivity[i+1] <- (3.0 * (sbdi / 1000.0) - 1.7) * 0.001 / (1.0 + ((11.5 - (5.0 * (sbdi / 1000.0))) * exp(-50.0 * (smi / (sbdi / 1000.0)) ^ 1.5))) * 86400.0 * ts * 100.0 * 4.184
        sati <- saturation[i+1]
        somi <- soilOrganicMatter[i+1] / da * sbdi
        heatCapacity[i+1] <- smi * dw * cw + ((sati - smi) * da * ca) + (somi * dh * ch) + ((1.0 - sati - somi) * dq * cq)
    }
    heatCapacity[groundLayer+1] <- heatCapacity[groundLayer - 1+1]
    heatCapacity[bottomLayer+1] <- heatCapacity[groundLayer+1]
    heatConductivity[groundLayer+1] <- heatConductivity[groundLayer - 1+1]
    heatConductivity[bottomLayer+1] <- heatConductivity[groundLayer+1]
    soilSurfaceTemperature <- initialSurfaceTemp
    heatConductivityMean[1] <- heatConductivity[1]
    for( i in seq(1, noOfTempLayers-1, 1)){
        lti_1 <- layerThickness[i - 1+1]
        lti <- layerThickness[i+1]
        hci_1 <- heatConductivity[i - 1+1]
        hci <- heatConductivity[i+1]
        heatConductivityMean[i+1] <- (lti_1 * hci_1 + (lti * hci)) / (lti + lti_1)
    }
    for( i in seq(0, noOfTempLayers-1, 1)){
        volumeMatrix[i+1] <- V[i+1] * heatCapacity[i+1]
        volumeMatrixOld[i+1] <- volumeMatrix[i+1]
        matrixSecondaryDiagonal[i+1] <- -B[i+1] * heatConductivityMean[i+1]
    }
    matrixSecondaryDiagonal[bottomLayer + 1+1] <- 0.0
    for( i in seq(0, noOfTempLayers-1, 1)){
        matrixPrimaryDiagonal[i+1] <- volumeMatrix[i+1] - matrixSecondaryDiagonal[i+1] - matrixSecondaryDiagonal[i + 1+1]
    }
    return (list ("soilSurfaceTemperature" = soilSurfaceTemperature,"soilTemperature" = soilTemperature,"V" = V,"B" = B,"volumeMatrix" = volumeMatrix,"volumeMatrixOld" = volumeMatrixOld,"matrixPrimaryDiagonal" = matrixPrimaryDiagonal,"matrixSecondaryDiagonal" = matrixSecondaryDiagonal,"heatConductivity" = heatConductivity,"heatConductivityMean" = heatConductivityMean,"heatCapacity" = heatCapacity,"solution" = solution,"matrixDiagonal" = matrixDiagonal,"matrixLowerTriangle" = matrixLowerTriangle,"heatFlow" = heatFlow))
}

model_soiltemperature <- function (noOfSoilLayers,
         noOfTempLayers,
         noOfTempLayersPlus1,
         soilSurfaceTemperature,
         timeStep,
         soilMoistureConst,
         baseTemp,
         initialSurfaceTemp,
         densityAir,
         specificHeatCapacityAir,
         densityHumus,
         specificHeatCapacityHumus,
         densityWater,
         specificHeatCapacityWater,
         quartzRawDensity,
         specificHeatCapacityQuartz,
         nTau,
         layerThickness,
         soilBulkDensity,
         saturation,
         soilOrganicMatter,
         soilTemperature,
         V,
         B,
         volumeMatrix,
         volumeMatrixOld,
         matrixPrimaryDiagonal,
         matrixSecondaryDiagonal,
         heatConductivity,
         heatConductivityMean,
         heatCapacity,
         solution,
         matrixDiagonal,
         matrixLowerTriangle,
         heatFlow){
    #'- Name: SoilTemperature -Version: 1, -Time step: 1
    #'- Description:
    #'            * Title: Model of soil temperature
    #'            * Authors: Michael Berg-Mohnicke
    #'            * Reference: None
    #'            * Institution: ZALF e.V.
    #'            * ExtendedDescription: None
    #'            * ShortDescription: Calculates the soil temperature at all soil layers
    #'- inputs:
    #'            * name: noOfSoilLayers
    #'                          ** description : noOfSoilLayers
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 20
    #'                          ** unit : dimensionless
    #'            * name: noOfTempLayers
    #'                          ** description : noOfTempLayers=noOfSoilLayers+2
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 22
    #'                          ** unit : dimensionless
    #'            * name: noOfTempLayersPlus1
    #'                          ** description : for matrixSecondaryDiagonal
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 23
    #'                          ** unit : dimensionless
    #'            * name: soilSurfaceTemperature
    #'                          ** description : current soilSurfaceTemperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** max : 80.0
    #'                          ** min : -50.0
    #'                          ** default : 0.0
    #'                          ** unit : °C
    #'            * name: timeStep
    #'                          ** description : timeStep
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 1.0
    #'                          ** unit : dimensionless
    #'            * name: soilMoistureConst
    #'                          ** description : constant soilmoisture during the model run
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfSoilLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : m**3/m**3
    #'            * name: baseTemp
    #'                          ** description : baseTemperature
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 9.5
    #'                          ** unit : °C
    #'            * name: initialSurfaceTemp
    #'                          ** description : initialSurfaceTemperature
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 10.0
    #'                          ** unit : °C
    #'            * name: densityAir
    #'                          ** description : DensityAir
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 1.25
    #'                          ** unit : kg/m**3
    #'            * name: specificHeatCapacityAir
    #'                          ** description : SpecificHeatCapacityAir
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 1005.0
    #'                          ** unit : J/kg/K
    #'            * name: densityHumus
    #'                          ** description : DensityHumus
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 1300.0
    #'                          ** unit : kg/m**3
    #'            * name: specificHeatCapacityHumus
    #'                          ** description : SpecificHeatCapacityHumus
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 1920.0
    #'                          ** unit : J/kg/K
    #'            * name: densityWater
    #'                          ** description : DensityWater
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 1000.0
    #'                          ** unit : kg/m**3
    #'            * name: specificHeatCapacityWater
    #'                          ** description : SpecificHeatCapacityWater
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 4192.0
    #'                          ** unit : J/kg/K
    #'            * name: quartzRawDensity
    #'                          ** description : QuartzRawDensity
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 2650.0
    #'                          ** unit : kg/m**3
    #'            * name: specificHeatCapacityQuartz
    #'                          ** description : SpecificHeatCapacityQuartz
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 750.0
    #'                          ** unit : J/kg/K
    #'            * name: nTau
    #'                          ** description : NTau
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 0.65
    #'                          ** unit : ?
    #'            * name: layerThickness
    #'                          ** description : layerThickness
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : m
    #'            * name: soilBulkDensity
    #'                          ** description : bulkDensity
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfSoilLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : kg/m**3
    #'            * name: saturation
    #'                          ** description : saturation
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfSoilLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : m**3/m**3
    #'            * name: soilOrganicMatter
    #'                          ** description : soilOrganicMatter
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfSoilLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : m**3/m**3
    #'            * name: soilTemperature
    #'                          ** description : soilTemperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: V
    #'                          ** description : V
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: B
    #'                          ** description : B
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: volumeMatrix
    #'                          ** description : volumeMatrix
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: volumeMatrixOld
    #'                          ** description : volumeMatrixOld
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: matrixPrimaryDiagonal
    #'                          ** description : matrixPrimaryDiagonal
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: matrixSecondaryDiagonal
    #'                          ** description : matrixSecondaryDiagonal
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayersPlus1
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: heatConductivity
    #'                          ** description : heatConductivity
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: heatConductivityMean
    #'                          ** description : heatConductivityMean
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: heatCapacity
    #'                          ** description : heatCapacity
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: solution
    #'                          ** description : solution
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: matrixDiagonal
    #'                          ** description : matrixDiagonal
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: matrixLowerTriangle
    #'                          ** description : matrixLowerTriangle
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'            * name: heatFlow
    #'                          ** description : heatFlow
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : noOfTempLayers
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : °C
    #'- outputs:
    #'            * name: soilTemperature
    #'                          ** description : soilTemperature next day
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : 22
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : °C
    groundLayer <- noOfTempLayers - 2
    bottomLayer <- noOfTempLayers - 1
    heatFlow[1] <- soilSurfaceTemperature * B[1] * heatConductivityMean[1]
    for( i in seq(0, noOfTempLayers-1, 1)){
        solution[i+1] <- (volumeMatrixOld[i+1] + ((volumeMatrix[i+1] - volumeMatrixOld[i+1]) / layerThickness[i+1])) * soilTemperature[i+1] + heatFlow[i+1]
    }
    matrixDiagonal[1] <- matrixPrimaryDiagonal[1]
    for( i in seq(1, noOfTempLayers-1, 1)){
        matrixLowerTriangle[i+1] <- matrixSecondaryDiagonal[i+1] / matrixDiagonal[(i - 1)+1]
        matrixDiagonal[i+1] <- matrixPrimaryDiagonal[i+1] - (matrixLowerTriangle[i+1] * matrixSecondaryDiagonal[i+1])
    }
    for( i in seq(1, noOfTempLayers-1, 1)){
        solution[i+1] <- solution[i+1] - (matrixLowerTriangle[i+1] * solution[(i - 1)+1])
    }
    solution[bottomLayer+1] <- solution[bottomLayer+1] / matrixDiagonal[bottomLayer+1]
    for( i in seq(0, bottomLayer-1, 1)){
        j <- bottomLayer - 1 - i
        j_1 <- j + 1
        solution[j+1] <- solution[j+1] / matrixDiagonal[j+1] - (matrixLowerTriangle[j_1+1] * solution[j_1+1])
    }
    for( i in seq(0, noOfTempLayers-1, 1)){
        soilTemperature[i+1] <- solution[i+1]
    }
    for( i in seq(0, noOfSoilLayers-1, 1)){
        volumeMatrixOld[i+1] <- volumeMatrix[i+1]
    }
    volumeMatrixOld[groundLayer+1] <- volumeMatrix[groundLayer+1]
    volumeMatrixOld[bottomLayer+1] <- volumeMatrix[bottomLayer+1]
    return (list('soilTemperature' = soilTemperature))
}