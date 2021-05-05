MODULE Initshootnumber_mod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE initshootnumber_(sowingDensity, &
        averageShootNumberPerPlant, &
        canopyShootNumber, &
        tilleringProfile, &
        tillerNumber)
        REAL, INTENT(OUT) :: averageShootNumberPerPlant
        REAL, INTENT(OUT) :: canopyShootNumber
        , INTENT(OUT) :: tilleringProfile
        INTEGER, INTENT(OUT) :: tillerNumber
        REAL, INTENT(IN) :: sowingDensity
        !- Description:
    !            - Model Name: Initialize ShootNumber Model
    !            - Author: Pierre MARTRE
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA/LEPSE Montpellier
    !            - Abstract: calculate the shoot number and update the related variables if needed
        !- inputs:
    !            - name: sowingDensity
    !                          - description : number of plant /m²
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 500
    !                          - default : 288.0
    !                          - unit : plant m-2
    !                          - inputtype : parameter
        !- outputs:
    !            - name: averageShootNumberPerPlant
    !                          - description : average shoot number per plant in the canopy
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : shoot m-2
    !            - name: canopyShootNumber
    !                          - description : shoot number for the whole canopy
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : shoot m-2
    !            - name: tilleringProfile
    !                          - description :  store the amount of new tiller created at each time a new tiller appears
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - unit : 
    !            - name: tillerNumber
    !                          - description :  store the amount of new tiller created at each time a new tiller appears
    !                          - variablecategory : auxiliary
    !                          - datatype : INT
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : 
        canopyShootNumber = sowingDensity
        averageShootNumberPerPlant = 1.0
        call Add(tilleringProfile, sowingDensity)
        tillerNumber = 1
    END SUBROUTINE initshootnumber_
END MODULE
