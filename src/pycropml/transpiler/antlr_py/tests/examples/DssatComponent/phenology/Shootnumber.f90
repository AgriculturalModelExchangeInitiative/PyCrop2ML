MODULE Shootnumbermod
    USE list_sub
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_ShootNumber(canopyShootNumber_t1, &
        leafNumber, &
        sowingDensity, &
        targetFertileShoot, &
        tilleringProfile_t1, &
        leafTillerNumberArray_t1, &
        numberTillerCohort_t1, &
        averageShootNumberPerPlant, &
        canopyShootNumber, &
        leafTillerNumberArray, &
        tilleringProfile, &
        numberTillerCohort)
        IMPLICIT NONE
        REAL :: canopyShootNumber_t1
        REAL, INTENT(IN) :: leafNumber
        REAL, INTENT(IN) :: sowingDensity
        REAL, INTENT(IN) :: targetFertileShoot
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) :: tilleringProfile_t1
        INTEGER, ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                leafTillerNumberArray_t1
        INTEGER, INTENT(IN) :: numberTillerCohort_t1
        REAL, INTENT(OUT) :: averageShootNumberPerPlant
        REAL, INTENT(OUT) :: canopyShootNumber
        INTEGER, ALLOCATABLE , DIMENSION(:), INTENT(OUT) ::  &
                leafTillerNumberArray
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(OUT) :: tilleringProfile
        INTEGER, INTENT(OUT) :: numberTillerCohort
        INTEGER:: emergedLeaves
        INTEGER:: shoots
        INTEGER:: i
        INTEGER, ALLOCATABLE , DIMENSION(:):: lNumberArray_rate
        tilleringProfile = tilleringProfile_t1
        !- Name: ShootNumber -Version: 1.0, -Time step: 1
        !- Description:
    !            * Title: CalculateShootNumber Model
    !            * Author: Pierre MARTRE
    !            * Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            * Institution: INRA/LEPSE Montpellier
    !            * Abstract: calculate the shoot number and update the related variables if needed
        !- inputs:
    !            * name: canopyShootNumber_t1
    !                          ** description : shoot number for the whole canopy
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 288.0
    !                          ** unit : shoot m-2
    !                          ** inputtype : variable
    !            * name: leafNumber
    !                          ** description : Leaf number 
    !                          ** variablecategory : state
    !                          ** inputtype : variable
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 3.34
    !                          ** unit : leaf
    !            * name: sowingDensity
    !                          ** description : number of plant /m²
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 500
    !                          ** default : 288.0
    !                          ** unit : plant m-2
    !                          ** inputtype : parameter
    !            * name: targetFertileShoot
    !                          ** description : max value of shoot number for the canopy
    !                          ** parametercategory : species
    !                          ** datatype : DOUBLE
    !                          ** min : 280
    !                          ** max : 1000
    !                          ** default : 600.0
    !                          ** unit : shoot
    !                          ** inputtype : variable
    !            * name: tilleringProfile_t1
    !                          ** description :  store the amount of new tiller created at each time a new tiller appears
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** default : [288.0]
    !                          ** unit : 
    !                          ** inputtype : variable
    !            * name: leafTillerNumberArray_t1
    !                          ** description : store the number of tiller for each leaf layer
    !                          ** variablecategory : state
    !                          ** datatype : INTLIST
    !                          ** unit : leaf
    !                          ** default : [1, 1, 1]
    !                          ** inputtype : variable
    !            * name: numberTillerCohort_t1
    !                          ** description :  Number of tiller which appears
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** default : 1
    !                          ** unit : 
    !                          ** inputtype : variable
        !- outputs:
    !            * name: averageShootNumberPerPlant
    !                          ** description : average shoot number per plant in the canopy
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : shoot m-2
    !            * name: canopyShootNumber
    !                          ** description : shoot number for the whole canopy
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : shoot m-2
    !            * name: leafTillerNumberArray
    !                          ** description : store the number of tiller for each leaf layer
    !                          ** variablecategory : state
    !                          ** datatype : INTLIST
    !                          ** unit : leaf
    !            * name: tilleringProfile
    !                          ** description :  store the amount of new tiller created at each time a new tiller appears
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLELIST
    !                          ** unit : dimensionless
    !            * name: numberTillerCohort
    !                          ** description : Number of tiller which appears
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** min : 0
    !                          ** max : 10000
    !                          ** unit : dimensionless
        emergedLeaves = MAX(1, CEILING(leafNumber - 1.0))
        shoots = fibonacci(emergedLeaves)
        canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity
        IF(canopyShootNumber .NE. canopyShootNumber_t1) THEN
            tilleringProfile = tilleringProfile_t1
            call Add(tilleringProfile,canopyShootNumber - canopyShootNumber_t1)
        END IF
        numberTillerCohort = SIZE(tilleringProfile)
        DO i = SIZE(leafTillerNumberArray_t1) , CEILING(leafNumber)-1, 1
            call Add(lNumberArray_rate, numberTillerCohort)
        END DO
        leafTillerNumberArray = leafTillerNumberArray_t1
        call Add(leafTillerNumberArray,lNumberArray_rate)
    END SUBROUTINE model_ShootNumber

    RECURSIVE FUNCTION fibonacci(n) RESULT(res_cyml)
        IMPLICIT NONE
        INTEGER, INTENT(IN) :: n
        INTEGER:: res_cyml
        IF(n .LE. 1) THEN
            res_cyml = n
        ELSE
            res_cyml = fibonacci(n - 1) + fibonacci(n - 2)
        END IF
    END FUNCTION fibonacci

    SUBROUTINE init_ShootNumber(sowingDensity, &
        targetFertileShoot, &
        averageShootNumberPerPlant, &
        canopyShootNumber, &
        leafTillerNumberArray, &
        tilleringProfile, &
        numberTillerCohort)
        IMPLICIT NONE
        REAL, INTENT(IN) :: sowingDensity
        REAL, INTENT(IN) :: targetFertileShoot
        REAL:: canopyShootNumber_t1
        REAL:: leafNumber
        REAL, ALLOCATABLE , DIMENSION(:):: tilleringProfile_t1
        INTEGER, ALLOCATABLE , DIMENSION(:):: leafTillerNumberArray_t1
        INTEGER:: numberTillerCohort_t1
        REAL, INTENT(OUT) :: averageShootNumberPerPlant
        REAL, INTENT(OUT) :: canopyShootNumber
        INTEGER, ALLOCATABLE , DIMENSION(:), INTENT(OUT) ::  &
                leafTillerNumberArray
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(OUT) :: tilleringProfile
        INTEGER, INTENT(OUT) :: numberTillerCohort
        canopyShootNumber = sowingDensity
        averageShootNumberPerPlant = 1.0
        call Add(tilleringProfile, sowingDensity)
        numberTillerCohort = 1
        deallocate(leafTillerNumberArray)

    END SUBROUTINE init_ShootNumber

END MODULE
