MODULE Updatecalendar_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE updatecalendar_(cumulTT, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        currentdate, &
        phase)
        REAL, INTENT(IN) :: cumulTT
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarMoments
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  &
                calendarDates
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) :: calendarCumuls
        CHARACTER(65), INTENT(IN) :: currentdate
        REAL, INTENT(IN) :: phase
        !- Description:
    !            - Model Name: Calendar Model
    !            - Author: Pierre Martre
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
        !- inputs:
    !            - name: cumulTT
    !                          - min : -200
    !                          - default : 741.510096671757
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : cumul thermal times at current date
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
    !            - name: currentdate
    !                          - variablecategory : auxiliary
    !                          - datatype : DATE
    !                          - default : 27/3/2007
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : current date
    !            - name: phase
    !                          - min : 0
    !                          - default : 1
    !                          - max : 7
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description :  the name of the phase
        !- outputs:
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
    !                          - datatype : DOUBLELIST
    !                          - unit : °C d
    !                          - description :  list containing for each stage occured its cumulated thermal times
        IF(phase .GE. 1.0 .AND. phase .LT. 2.0 .AND. ALL(calendarMoments .NE.  &
                'Emergence')) THEN
            call Add(calendarMoments, 'Emergence')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 2.0 .AND. phase .LT. 3.0 .AND.  &
                ALL(calendarMoments .NE. 'FloralInitiation')) THEN
            call Add(calendarMoments, 'FloralInitiation')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 3.0 .AND. phase .LT. 4.0 .AND.  &
                ALL(calendarMoments .NE. 'Heading')) THEN
            call Add(calendarMoments, 'Heading')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .EQ. 4.0 .AND. ALL(calendarMoments .NE. 'Anthesis'))  &
                THEN
            call Add(calendarMoments, 'Anthesis')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .EQ. 4.5 .AND. ALL(calendarMoments .NE.  &
                'EndCellDivision')) THEN
            call Add(calendarMoments, 'EndCellDivision')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 5.0 .AND. phase .LT. 6.0 .AND.  &
                ALL(calendarMoments .NE. 'EndGrainFilling')) THEN
            call Add(calendarMoments, 'EndGrainFilling')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        ELSE IF ( phase .GE. 6.0 .AND. phase .LT. 7.0 .AND.  &
                ALL(calendarMoments .NE. 'Maturity')) THEN
            call Add(calendarMoments, 'Maturity')
            call Add(calendarCumuls, cumulTT)
            call Add(calendarDates, currentdate)
        END IF
    END SUBROUTINE updatecalendar_
END MODULE
