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
    !                          - min : 0
    !                          - default : 288.0
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : shoot m-2
    !                          - description : shoot number for the whole canopy
    !            - name: leafNumber
    !                          - min : 0
    !                          - default : 0
    !                          - max : 10000
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description : Leaf number 
    !            - name: sowingDensity
    !                          - parametercategory : constant
    !                          - min : 0
    !                          - datatype : INT
    !                          - max : 500
    !                          - default : 288
    !                          - inputtype : parameter
    !                          - unit : plant m-2
    !                          - description : number of plant /m²
    !            - name: targetFertileShoot
    !                          - min : 280
    !                          - default : 600
    !                          - max : 1000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : shoot
    !                          - description : max value of shoot number for the canopy
    !            - name: tilleringProfile
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - default : [288.0]
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description :  store the amount of new tiller created at each time a new tiller appears
    !            - name: leafTillerNumberArray
    !                          - variablecategory : auxiliary
    !                          - datatype : INTLIST
    !                          - default : [1]
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description : store the number of tiller for each leaf layer
    !            - name: tillerNumber
    !                          - min : 0
    !                          - default : 1
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : INT
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description :  store the amount of tiller created at each time a tiller appears
        !- outputs:
    !            - name: averageShootNumberPerPlant
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : auxiliary
    !                          - max : 10000
    !                          - unit : shoot m-2
    !                          - description : average shoot number per plant in the canopy
    !            - name: canopyShootNumber
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : auxiliary
    !                          - max : 10000
    !                          - unit : m2 m-2
    !                          - description : shoot number for the whole canopy
    !            - name: leafTillerNumberArray
    !                          - variablecategory : auxiliary
    !                          - datatype : INTLIST
    !                          - unit : leaf
    !                          - description : store the number of tiller for each leaf layer
    !            - name: tilleringProfile
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - unit : 
    !                          - description :  store the amount of new tiller created at each time a new tiller appears
    !            - name: tillerNumber
    !                          - datatype : INT
    !                          - min : 0
    !                          - variablecategory : auxiliary
    !                          - max : 10000
    !                          - unit : 
    !                          - description :  store the amount of new tiller created at each time a new tiller appears
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
                INT(REAL(CEILING(leafNumber))) , 1
            call Add(leafTillerNumberArray, tillerNumber)
        END DO
    END SUBROUTINE shootnumber_
END MODULE
