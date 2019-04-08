MODULE Canopytemperature_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE canopytemperature_(minTair, &
        maxTair, &
        cropHeatFlux, &
        conductance, &
        minCanopyTemperature, &
        maxCanopyTemperature)
        REAL, INTENT(OUT) :: minCanopyTemperature
        REAL, INTENT(OUT) :: maxCanopyTemperature
        REAL, INTENT(IN) :: minTair
        REAL, INTENT(IN) :: maxTair
        REAL, INTENT(IN) :: cropHeatFlux
        REAL, INTENT(IN) :: conductance
        REAL, PARAMETER :: lambdaV = 2.454
        REAL, PARAMETER :: rhoDensityAir = 1.225
        REAL, PARAMETER :: specificHeatCapacityAir = 0.00101
        !- Description:
    !            - Model Name: CanopyTemperature Model
    !            - Author: Pierre Martre
    !            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            - Institution: INRA/LEPSE Montpellier
    !            - Abstract: It is calculated from the crop heat flux and the boundary layer conductance 
        !- inputs:
    !            - name: minTair
    !                          - description : minimum air temperature
    !                          - datatype : DOUBLE
    !                          - variablecategory : auxiliary
    !                          - min : -30
    !                          - max : 45
    !                          - default : 0.7
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: maxTair
    !                          - description : maximum air Temperature
    !                          - datatype : DOUBLE
    !                          - variablecategory : auxiliary
    !                          - min : -30
    !                          - max : 45
    !                          - default : 7.2
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: cropHeatFlux
    !                          - description : Crop heat flux
    !                          - variablecategory : rate
    !                          - inputtype : variable
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 447.912
    !                          - unit : g m² d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: conductance
    !                          - description : the boundary layer conductance
    !                          - variablecategory : state
    !                          - inputtype : variable
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 598.685
    !                          - unit : m d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: lambdaV
    !                          - description : latent heat of vaporization of water
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 2.454
    !                          - min : 0
    !                          - max : 10
    !                          - unit : MJ kg-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: rhoDensityAir
    !                          - description : Density of air
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.225
    !                          - unit : kg m3
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: specificHeatCapacityAir
    !                          - description : Specific heat capacity of dry air
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 0.00101
    !                          - unit : MJ kg-1 °C-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
        !- outputs:
    !            - name: minCanopyTemperature
    !                          - description : minimal Canopy Temperature  
    !                          - datatype : DOUBLE
    !                          - min : -30
    !                          - max : 45
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !            - name: maxCanopyTemperature
    !                          - description : maximal Canopy Temperature 
    !                          - datatype : DOUBLE
    !                          - min : -30
    !                          - max : 45
    !                          - unit : °C
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        minCanopyTemperature = minTair + cropHeatFlux / rhoDensityAir *  &
                specificHeatCapacityAir * conductance / lambdaV * 1000
        maxCanopyTemperature = maxTair + cropHeatFlux / rhoDensityAir *  &
                specificHeatCapacityAir * conductance / lambdaV * 1000
    END SUBROUTINE canopytemperature_
END MODULE
