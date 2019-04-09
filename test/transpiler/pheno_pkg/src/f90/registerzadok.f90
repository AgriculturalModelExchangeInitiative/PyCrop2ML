MODULE Registerzadok_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE registerzadok_(cumulTT, &
        phase, &
        leafNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        cumulTTFromZC_65, &
        currentdate, &
        der, &
        slopeTSFLN, &
        intTSFLN, &
        finalLeafNumber, &
        currentZadokStage, &
        hasZadokStageChanged)
        INTEGER:: roundedFinalLeafNumber
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: phase
        REAL, INTENT(IN) :: leafNumber
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarMoments
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarDates
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) :: calendarCumuls
        REAL, INTENT(IN) :: cumulTTFromZC_65
        CHARACTER(65), INTENT(IN) :: currentdate
        REAL, INTENT(IN) :: der
        REAL, INTENT(IN) :: slopeTSFLN
        REAL, INTENT(IN) :: intTSFLN
        REAL, INTENT(IN) :: finalLeafNumber
        CHARACTER(65), INTENT(INOUT) :: currentZadokStage
        INTEGER, INTENT(INOUT) :: hasZadokStageChanged
        !- Description:
    !            - Model Name: RegisterZadok Model
    !            - Author: Pierre MARTRE
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA/LEPSE Montpellier
    !            - Abstract: Record the zadok stage in the calendar
    !    	
        !- inputs:
    !            - name: cumulTT
    !                          - min : -200
    !                          - default : 354.582294511779
    !                          - max : 10000
    !                          - uri : some url
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : 
    !            - name: phase
    !                          - min : 0
    !                          - default : 2
    !                          - max : 7
    !                          - uri : some url
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    !            - name: leafNumber
    !                          - min : 0
    !                          - default : 4.8854219661087575
    !                          - max : 25
    !                          - uri : some url
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description : Actual number of phytomers
    !            - name: calendarMoments
    !                          - variablecategory : auxiliary
    !                          - datatype : STRINGLIST
    !                          - default : ['Sowing']
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : List containing apparition of each stage
    !            - name: calendarDates
    !                          - variablecategory : auxiliary
    !                          - datatype : DATELIST
    !                          - default : ['21/3/2007']
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : List containing  the dates of the wheat developmental phases
    !            - name: calendarCumuls
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - default : [0.0]
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : list containing for each stage occured its cumulated thermal times
    !            - name: cumulTTFromZC_65
    !                          - min : -200
    !                          - default : 0
    !                          - max : 10000
    !                          - uri : some url
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    !            - name: currentdate
    !                          - min : 
    !                          - default : 9/4/2007
    !                          - max : 
    !                          - uri : some url
    !                          - variablecategory : auxiliary
    !                          - datatype : DATE
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : current date
    !            - name: der
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - uri : some url
    !                          - default : 300.0
    !                          - inputtype : parameter
    !                          - unit : °C d
    !                          - description : Duration of the endosperm endoreduplication phase
    !            - name: slopeTSFLN
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - uri : some url
    !                          - default : 0.9
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : used to calculate Terminal spikelet
    !            - name: intTSFLN
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - uri : some url
    !                          - default : 0.9
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : used to calculate Terminal spikelet
    !            - name: finalLeafNumber
    !                          - min : 0
    !                          - default : 8.797582013199484
    !                          - max : 10000
    !                          - uri : some url
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description : final leaf number
    !            - name: currentZadokStage
    !                          - min : 
    !                          - datatype : STRING
    !                          - max : 
    !                          - uri : some url
    !                          - default : MainShootPlus1Tiller
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : current zadok stage
    !            - name: hasZadokStageChanged
    !                          - min : 0
    !                          - default : 0
    !                          - max : 1
    !                          - uri : some url
    !                          - variablecategory : state
    !                          - datatype : INT
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : true if the zadok stage has changed this time step
        !- outputs:
    !            - name: hasZadokStageChanged
    !                          - min : 0
    !                          - variablecategory : state
    !                          - max : 1
    !                          - uri : some url
    !                          - datatype : INT
    !                          - unit : 
    !                          - description : true if the zadok stage has changed this time step
    !            - name: currentZadokStage
    !                          - datatype : STRING
    !                          - variablecategory : auxiliary
    !                          - uri : some url
    !                          - unit :  
    !                          - description : current zadok stage
    !            - name: calendarMoments
    !                          - variablecategory : auxiliary
    !                          - datatype : STRINGLIST
    !                          - unit : 
    !                          - description :  List containing apparition of each stage
    !            - name: calendarDates
    !                          - variablecategory : auxiliary
    !                          - datatype : DATELIST
    !                          - unit : 
    !                          - description :  List containing  the dates of the wheat developmental phases
    !            - name: calendarCumuls
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - unit : °C d
    !                          - description :  list containing for each stage occured its cumulated thermal times
        roundedFinalLeafNumber = INT(finalLeafNumber + 0.5)
        IF(leafNumber .GE. 4.0 .AND. ALL(calendarMoments .NE.  &
                'MainShootPlus1Tiller')) THEN
            call Add(calendarMoments, 'MainShootPlus1Tiller')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MainShootPlus1Tiller'
        ELSE IF ( leafNumber .GE. 5.0 .AND. ALL(calendarMoments .NE.  &
                'MainShootPlus2Tiller')) THEN
            call Add(calendarMoments, 'MainShootPlus2Tiller')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MainShootPlus2Tiller'
        ELSE IF ( leafNumber .GE. 6.0 .AND. ALL(calendarMoments .NE.  &
                'MainShootPlus3Tiller')) THEN
            call Add(calendarMoments, 'MainShootPlus3Tiller')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MainShootPlus3Tiller'
        ELSE IF ( finalLeafNumber .GT. 0.0 .AND. leafNumber .GE. slopeTSFLN *  &
                finalLeafNumber - intTSFLN .AND. ALL(calendarMoments .NE.  &
                'TerminalSpikelet')) THEN
            call Add(calendarMoments, 'TerminalSpikelet')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'TerminalSpikelet'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 4.0 .AND.  &
                roundedFinalLeafNumber - 4 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                'PseudoStemErection')) THEN
            call Add(calendarMoments, 'PseudoStemErection')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'PseudoStemErection'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 3.0 .AND.  &
                roundedFinalLeafNumber - 3 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                '1stNodeDetectable')) THEN
            call Add(calendarMoments, '1stNodeDetectable')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = '1stNodeDetectable'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 2.0 .AND.  &
                roundedFinalLeafNumber - 2 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                '2ndNodeDetectable')) THEN
            call Add(calendarMoments, '2ndNodeDetectable')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = '2ndNodeDetectable'
        ELSE IF ( leafNumber .GE. roundedFinalLeafNumber - 1.0 .AND.  &
                roundedFinalLeafNumber - 1 .GT. 0 .AND. ALL(calendarMoments .NE.  &
                'FlagLeafJustVisible')) THEN
            call Add(calendarMoments, 'FlagLeafJustVisible')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'FlagLeafJustVisible'
        ELSE IF ( ALL(calendarMoments .NE. 'MidGrainFilling') .AND. phase  &
                .EQ. 4.5 .AND. cumulTTFromZC_65 .GE. der) THEN
            call Add(calendarMoments, 'MidGrainFilling')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
            hasZadokStageChanged = 1
            currentZadokStage = 'MidGrainFilling'
        ELSE
            hasZadokStageChanged = 0
        END IF
    END SUBROUTINE registerzadok_
END MODULE
