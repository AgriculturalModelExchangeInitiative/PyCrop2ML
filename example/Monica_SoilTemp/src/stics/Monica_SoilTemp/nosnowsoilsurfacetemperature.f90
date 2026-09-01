MODULE Nosnowsoilsurfacetemperaturemod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_nosnowsoilsurfacetemperature(tmin, &
        tmax, &
        globrad, &
        soilCoverage, &
        dampingFactor, &
        soilSurfaceTemperature)
        IMPLICIT NONE
        INTEGER:: i_cyml_r
        REAL, INTENT(IN) :: tmin
        REAL, INTENT(IN) :: tmax
        REAL, INTENT(IN) :: globrad
        REAL, INTENT(IN) :: soilCoverage
        REAL, INTENT(IN) :: dampingFactor
        REAL, INTENT(INOUT) :: soilSurfaceTemperature
        REAL:: shadingCoefficient
        !- Name: NoSnowSoilSurfaceTemperature -Version: 1, -Time step: 1
        !- Description:
    !            * Title: Soil surface temperature
    !            * Authors: Michael Berg-Mohnicke
    !            * Reference: None
    !            * Institution: ZALF e.V.
    !            * ExtendedDescription: None
    !            * ShortDescription: It calculates the soil surface temperature without snow cover
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
    !            * name: soilCoverage
    !                          ** description : soilCoverage
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 0.0
    !                          ** default : 0.0
    !                          ** unit : dimensionless
    !            * name: dampingFactor
    !                          ** description : dampingFactor
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 0.8
    !                          ** unit : dimensionless
    !            * name: soilSurfaceTemperature
    !                          ** description : soilSurfaceTemperature of previous day
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 0.0
    !                          ** unit : °C
        !- outputs:
    !            * name: soilSurfaceTemperature
    !                          ** description : soilSurfaceTemperature
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** unit : °C
        globrad = MAX(8.33, globrad)
        shadingCoefficient = 0.1 + (soilCoverage * dampingFactor + ((1 -  &
                soilCoverage) * (1 - dampingFactor)))
        soilSurfaceTemperature = (1.0 - shadingCoefficient) * (tmin + ((tmax  &
                - tmin) *  ((0.03 * globrad) ** 0.5))) + (shadingCoefficient *  &
                soilSurfaceTemperature)
        IF(soilSurfaceTemperature .LT. 0.0) THEN
            soilSurfaceTemperature = soilSurfaceTemperature * 0.5
        END IF
    END SUBROUTINE model_nosnowsoilsurfacetemperature

END MODULE
