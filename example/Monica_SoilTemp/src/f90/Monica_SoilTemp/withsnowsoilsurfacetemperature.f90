MODULE Withsnowsoilsurfacetemperaturemod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_withsnowsoilsurfacetemperature(noSnowSoilSurfaceTemperature, &
        soilSurfaceTemperatureBelowSnow, &
        hasSnowCover, &
        soilSurfaceTemperature)
        IMPLICIT NONE
        INTEGER:: i_cyml_r
        REAL, INTENT(IN) :: noSnowSoilSurfaceTemperature
        REAL, INTENT(IN) :: soilSurfaceTemperatureBelowSnow
        LOGICAL, INTENT(IN) :: hasSnowCover
        REAL, INTENT(OUT) :: soilSurfaceTemperature
        !- Name: WithSnowSoilSurfaceTemperature -Version: 1, -Time step: 1
        !- Description:
    !            * Title: Soil surface temperature with potential snow cover
    !            * Authors: Michael Berg-Mohnicke
    !            * Reference: None
    !            * Institution: ZALF e.V.
    !            * ExtendedDescription: None
    !            * ShortDescription: It calculates the soil surface temperature taking a potential snow cover into account
    !        
        !- inputs:
    !            * name: noSnowSoilSurfaceTemperature
    !                          ** description : soilSurfaceTemperature without snow
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** default : 0.0
    !                          ** unit : °C
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
        !- outputs:
    !            * name: soilSurfaceTemperature
    !                          ** description : soilSurfaceTemperature
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 
    !                          ** min : 
    !                          ** unit : °C
        IF(hasSnowCover) THEN
            soilSurfaceTemperature = soilSurfaceTemperatureBelowSnow
        ELSE
            soilSurfaceTemperature = noSnowSoilSurfaceTemperature
        END IF
    END SUBROUTINE model_withsnowsoilsurfacetemperature

END MODULE
