MODULE Soiltemperaturecompmod
    USE Soiltemperaturemod
    USE Nosnowsoilsurfacetemperaturemod
    USE Withsnowsoilsurfacetemperaturemod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_soiltemperaturecomp(tmin, &
        tmax, &
        globrad, &
        dampingFactor, &
        soilCoverage, &
        soilSurfaceTemperatureBelowSnow, &
        hasSnowCover, &
        timeStep, &
        soilMoistureConst, &
        baseTemp, &
        initialSurfaceTemp, &
        densityAir, &
        specificHeatCapacityAir, &
        densityHumus, &
        specificHeatCapacityHumus, &
        densityWater, &
        specificHeatCapacityWater, &
        quartzRawDensity, &
        specificHeatCapacityQuartz, &
        nTau, &
        noOfTempLayers, &
        noOfTempLayersPlus1, &
        noOfSoilLayers, &
        layerThickness, &
        soilBulkDensity, &
        saturation, &
        soilOrganicMatter, &
        V, &
        B, &
        volumeMatrix, &
        volumeMatrixOld, &
        matrixPrimaryDiagonal, &
        matrixSecondaryDiagonal, &
        heatConductivity, &
        heatConductivityMean, &
        heatCapacity, &
        solution, &
        matrixDiagonal, &
        matrixLowerTriangle, &
        heatFlow, &
        soilSurfaceTemperature, &
        soilTemperature)
        IMPLICIT NONE
        INTEGER:: i_cyml_r
        REAL, INTENT(IN) :: tmin
        REAL, INTENT(IN) :: tmax
        REAL, INTENT(IN) :: globrad
        REAL, INTENT(IN) :: dampingFactor
        REAL, INTENT(IN) :: soilCoverage
        REAL, INTENT(IN) :: soilSurfaceTemperatureBelowSnow
        LOGICAL, INTENT(IN) :: hasSnowCover
        REAL, INTENT(IN) :: timeStep
        REAL , DIMENSION(noOfSoilLayers ), INTENT(IN) :: soilMoistureConst
        REAL, INTENT(IN) :: baseTemp
        REAL, INTENT(IN) :: initialSurfaceTemp
        REAL, INTENT(IN) :: densityAir
        REAL, INTENT(IN) :: specificHeatCapacityAir
        REAL, INTENT(IN) :: densityHumus
        REAL, INTENT(IN) :: specificHeatCapacityHumus
        REAL, INTENT(IN) :: densityWater
        REAL, INTENT(IN) :: specificHeatCapacityWater
        REAL, INTENT(IN) :: quartzRawDensity
        REAL, INTENT(IN) :: specificHeatCapacityQuartz
        REAL, INTENT(IN) :: nTau
        INTEGER, INTENT(IN) :: noOfTempLayers
        INTEGER, INTENT(IN) :: noOfTempLayersPlus1
        INTEGER, INTENT(IN) :: noOfSoilLayers
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: layerThickness
        REAL , DIMENSION(noOfSoilLayers ), INTENT(IN) :: soilBulkDensity
        REAL , DIMENSION(noOfSoilLayers ), INTENT(IN) :: saturation
        REAL , DIMENSION(noOfSoilLayers ), INTENT(IN) :: soilOrganicMatter
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: V
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: B
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: volumeMatrix
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: volumeMatrixOld
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: matrixPrimaryDiagonal
        REAL , DIMENSION(noOfTempLayersPlus1 ), INTENT(IN) ::  &
                matrixSecondaryDiagonal
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: heatConductivity
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: heatConductivityMean
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: heatCapacity
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: solution
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: matrixDiagonal
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: matrixLowerTriangle
        REAL , DIMENSION(noOfTempLayers ), INTENT(IN) :: heatFlow
        REAL, INTENT(OUT) :: soilSurfaceTemperature
        REAL , DIMENSION(noOfTempLayers ), ALLOCATABLE , INTENT(OUT) ::  &
                soilTemperature
        REAL:: noSnowSoilSurfaceTemperature
        !- Name: SoilTemperatureComp -Version: 1, -Time step: 1
        !- Description:
    !            * Title: SoilTemperature model
    !            * Authors: Michael Berg-Mohnicke
    !            * Reference: None
    !            * Institution: ZALF e.V.
    !            * ExtendedDescription: None
    !            * ShortDescription: Calculates the soil temperature in all layers and soil surface temperature
        !- inputs:
    !            * name: tmin
    !                          ** description : the days min air temperature
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 70.0
    !                          ** min : -50.0
    !                          ** default : 
    !                          ** unit : °C
    !            * name: tmax
    !                          ** description : the days max air temperature
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 70.0
    !                          ** min : -50.0
    !                          ** default : 
    !                          ** unit : °C
    !            * name: globrad
    !                          ** description : the days global radiation
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 30.0
    !                          ** min : 0.0
    !                          ** default : 0.0
    !                          ** unit : MJ/m**2/d
    !            * name: dampingFactor
    !                          ** description : dampingFactor
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 0.8
    !                          ** unit : dimensionless
    !            * name: soilCoverage
    !                          ** description : soilCoverage
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 0.0
    !                          ** default : 0.0
    !                          ** unit : dimensionless
    !            * name: soilSurfaceTemperatureBelowSnow
    !                          ** description : soilSurfaceTemperature below snow cover
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 0.0
    !                          ** unit : °C
    !            * name: hasSnowCover
    !                          ** description : is soil covered by snow
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : BOOLEAN
    !                          ** max : 
    !                          ** min : 
    !                          ** default : false
    !                          ** unit : dimensionless
    !            * name: timeStep
    !                          ** description : timeStep
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 1.0
    !                          ** unit : dimensionless
    !            * name: soilMoistureConst
    !                          ** description : constant soilmoisture during the model run
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfSoilLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : m**3/m**3
    !            * name: baseTemp
    !                          ** description : baseTemperature
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 9.5
    !                          ** unit : °C
    !            * name: initialSurfaceTemp
    !                          ** description : initialSurfaceTemperature
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 10.0
    !                          ** unit : °C
    !            * name: densityAir
    !                          ** description : DensityAir
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 1.25
    !                          ** unit : kg/m**3
    !            * name: specificHeatCapacityAir
    !                          ** description : SpecificHeatCapacityAir
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 1005.0
    !                          ** unit : J/kg/K
    !            * name: densityHumus
    !                          ** description : DensityHumus
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 1300.0
    !                          ** unit : kg/m**3
    !            * name: specificHeatCapacityHumus
    !                          ** description : SpecificHeatCapacityHumus
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 1920.0
    !                          ** unit : J/kg/K
    !            * name: densityWater
    !                          ** description : DensityWater
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 1000.0
    !                          ** unit : kg/m**3
    !            * name: specificHeatCapacityWater
    !                          ** description : SpecificHeatCapacityWater
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 4192.0
    !                          ** unit : J/kg/K
    !            * name: quartzRawDensity
    !                          ** description : QuartzRawDensity
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 2650.0
    !                          ** unit : kg/m**3
    !            * name: specificHeatCapacityQuartz
    !                          ** description : SpecificHeatCapacityQuartz
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 750.0
    !                          ** unit : J/kg/K
    !            * name: nTau
    !                          ** description : NTau
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 0.65
    !                          ** unit : ?
    !            * name: noOfTempLayers
    !                          ** description : noOfTempLayers=noOfSoilLayers+2
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : INT
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 22
    !                          ** unit : dimensionless
    !            * name: noOfTempLayersPlus1
    !                          ** description : for matrixSecondaryDiagonal
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : INT
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 23
    !                          ** unit : dimensionless
    !            * name: noOfSoilLayers
    !                          ** description : noOfSoilLayers
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : INT
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 20
    !                          ** unit : dimensionless
    !            * name: layerThickness
    !                          ** description : layerThickness
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : m
    !            * name: soilBulkDensity
    !                          ** description : bulkDensity
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfSoilLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : kg/m**3
    !            * name: saturation
    !                          ** description : saturation
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfSoilLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : m**3/m**3
    !            * name: soilOrganicMatter
    !                          ** description : soilOrganicMatter
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfSoilLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : m**3/m**3
    !            * name: V
    !                          ** description : V
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: B
    !                          ** description : B
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: volumeMatrix
    !                          ** description : volumeMatrix
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: volumeMatrixOld
    !                          ** description : volumeMatrixOld
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: matrixPrimaryDiagonal
    !                          ** description : matrixPrimaryDiagonal
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: matrixSecondaryDiagonal
    !                          ** description : matrixSecondaryDiagonal
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayersPlus1
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: heatConductivity
    !                          ** description : heatConductivity
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: heatConductivityMean
    !                          ** description : heatConductivityMean
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: heatCapacity
    !                          ** description : heatCapacity
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: solution
    !                          ** description : solution
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: matrixDiagonal
    !                          ** description : matrixDiagonal
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: matrixLowerTriangle
    !                          ** description : matrixLowerTriangle
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
    !            * name: heatFlow
    !                          ** description : heatFlow
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : noOfTempLayers
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 
    !                          ** unit : °C
        !- outputs:
    !            * name: soilSurfaceTemperature
    !                          ** description : soilSurfaceTemperature
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** unit : °C
    !            * name: soilTemperature
    !                          ** description : soilTemperature next day
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : 22
    !                          ** max : 
    !                          ** min : 
    !                          ** unit : °C
        call model_nosnowsoilsurfacetemperature(tmin, tmax, globrad,  &
                soilCoverage, dampingFactor, soilSurfaceTemperature)
        noSnowSoilSurfaceTemperature = soilSurfaceTemperature
        call  &
                model_withsnowsoilsurfacetemperature(noSnowSoilSurfaceTemperature,  &
                soilSurfaceTemperatureBelowSnow, hasSnowCover,soilSurfaceTemperature)
        call model_soiltemperature(noOfSoilLayers, noOfTempLayers,  &
                noOfTempLayersPlus1, soilSurfaceTemperature, timeStep,  &
                soilMoistureConst, baseTemp, initialSurfaceTemp, densityAir,  &
                specificHeatCapacityAir, densityHumus, specificHeatCapacityHumus,  &
                densityWater, specificHeatCapacityWater, quartzRawDensity,  &
                specificHeatCapacityQuartz, nTau, layerThickness, soilBulkDensity,  &
                saturation, soilOrganicMatter, soilTemperature, V, B, volumeMatrix,  &
                volumeMatrixOld, matrixPrimaryDiagonal, matrixSecondaryDiagonal,  &
                heatConductivity, heatConductivityMean, heatCapacity, solution,  &
                matrixDiagonal, matrixLowerTriangle, heatFlow)
    END SUBROUTINE model_soiltemperaturecomp

END MODULE
