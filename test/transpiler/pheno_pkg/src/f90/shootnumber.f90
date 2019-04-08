MODULE Shootnumber_mod
    USE list_sub
    USE fibonacci_mod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE shootnumber_(canopyShootNumber, &
        leafNumber, &
        sowingDensity, &
        targetFertileShoot, &
        tilleringProfile, &
        leafTillerNumberArray, &
        tillerNumber, &
        averageShootNumberPerPlant)
        REAL, INTENT(OUT) :: averageShootNumberPerPlant
        REAL:: oldCanopyShootNumber
        INTEGER:: emergedLeaves
        INTEGER:: shoots
        INTEGER:: i
        REAL, INTENT(INOUT) :: canopyShootNumber
        REAL, INTENT(IN) :: leafNumber
        INTEGER, INTENT(IN) :: sowingDensity
        REAL, INTENT(IN) :: targetFertileShoot
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) :: tilleringProfile
        INTEGER, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                leafTillerNumberArray
        INTEGER, INTENT(INOUT) :: tillerNumber
        !- Description:
    !            - Model Name: CalculateShootNumber Model
    !            - Author: Pierre MARTRE
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA/LEPSE Montpellier
    !            - Abstract: calculate the shoot number and update the related variables if needed
        !- inputs:
    !            - name: canopyShootNumber
    !                          - description : shoot number for the whole canopy
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 288.0
    !                          - unit : shoot m-2
    !                          - inputtype : variable
    !            - name: leafNumber
    !                          - description : Leaf number 
    !                          - variablecategory : state
    !                          - inputtype : variable
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 0
    !                          - unit : leaf
    !            - name: sowingDensity
    !                          - description : number of plant /m²
    !                          - parametercategory : species
    !                          - datatype : INT
    !                          - min : 0
    !                          - max : 500
    !                          - default : 288
    !                          - unit : plant m-2
    !                          - inputtype : parameter
    !            - name: targetFertileShoot
    !                          - description : max value of shoot number for the canopy
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 280
    !                          - max : 1000
    !                          - default : 600
    !                          - unit : shoot
    !                          - inputtype : variable
    !            - name: tilleringProfile
    !                          - description :  store the amount of new tiller created at each time a new tiller appears
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - default : [288.0]
    !                          - unit : 
    !                          - inputtype : variable
    !            - name: leafTillerNumberArray
    !                          - description : store the number of tiller for each leaf layer
    !                          - variablecategory : auxiliary
    !                          - datatype : INTLIST
    !                          - unit : leaf
    !                          - default : [1]
    !                          - inputtype : variable
    !            - name: tillerNumber
    !                          - description :  Number of tiller which appears
    !                          - variablecategory : auxiliary
    !                          - datatype : INT
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 1
    !                          - unit : 
    !                          - inputtype : variable
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
    !            - name: leafTillerNumberArray
    !                          - description : store the number of tiller for each leaf layer
    !                          - variablecategory : auxiliary
    !                          - datatype : INTLIST
    !                          - unit : leaf
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
        oldCanopyShootNumber = canopyShootNumber
        emergedLeaves = INT(MAX(1.0, REAL(CEILING(leafNumber - 1))))
        call fibonacci_(emergedLeaves,shoots)
        canopyShootNumber = MIN(REAL(shoots * sowingDensity),  &
                targetFertileShoot)
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity
        IF(canopyShootNumber .NE. oldCanopyShootNumber) THEN
            call Add(tilleringProfile, canopyShootNumber - oldCanopyShootNumber)
        END IF
        tillerNumber = SIZE(tilleringProfile)
        DO i = SIZE(leafTillerNumberArray) + 1  ,  &
                INT(REAL(CEILING(leafNumber))), 1
            call Add(leafTillerNumberArray, tillerNumber)
        END DO
    END SUBROUTINE shootnumber_
END MODULE
