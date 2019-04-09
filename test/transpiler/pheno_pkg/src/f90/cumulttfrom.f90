MODULE Cumulttfrom_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE cumulttfrom_(calendarMoments, &
        calendarCumuls, &
        cumulTT, &
        cumulTTFromZC_65, &
        cumulTTFromZC_39, &
        cumulTTFromZC_91)
        REAL, INTENT(OUT) :: cumulTTFromZC_65
        REAL, INTENT(OUT) :: cumulTTFromZC_39
        REAL, INTENT(OUT) :: cumulTTFromZC_91
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                calendarMoments
        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) :: calendarCumuls
        REAL, INTENT(IN) :: cumulTT
        !- Description:
    !            - Model Name: CumulTTFrom Model
    !            - Author: Pierre Martre
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: Calculate CumulTT 
        !- inputs:
    !            - name: calendarMoments
    !                          - variablecategory : auxiliary
    !                          - datatype : STRINGLIST
    !                          - default : ['Sowing']
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : List containing appearance of each stage
    !            - name: calendarCumuls
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - default : [0.0]
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : list containing for each stage occured its cumulated thermal times
    !            - name: cumulTT
    !                          - min : -200
    !                          - default : 8
    !                          - max : 10000
    !                          - datatype : DOUBLE
    !                          - variablecategory : auxiliary
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : cumul TT at current date
        !- outputs:
    !            - name: cumulTTFromZC_65
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : auxiliary
    !                          - max : 5000
    !                          - unit : °C d
    !                          - description :  cumul TT from Anthesis to current date 
    !            - name: cumulTTFromZC_39
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : auxiliary
    !                          - max : 5000
    !                          - unit : °C d
    !                          - description :  cumul TT from FlagLeafLiguleJustVisible to current date 
    !            - name: cumulTTFromZC_91
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : auxiliary
    !                          - max : 5000
    !                          - unit : °C d
    !                          - description :  cumul TT from EndGrainFilling to current date 
        cumulTTFromZC_65 = 0.0
        cumulTTFromZC_39 = 0.0
        cumulTTFromZC_91 = 0.0
        IF(ANY(calendarMoments .EQ. 'Anthesis')) THEN
            cumulTTFromZC_65 = cumulTT - calendarCumuls(indice(calendarMoments,  &
                    'Anthesis'))
        END IF
        IF(ANY(calendarMoments .EQ. 'FlagLeafLiguleJustVisible')) THEN
            cumulTTFromZC_39 = cumulTT - calendarCumuls(indice(calendarMoments,  &
                    'FlagLeafLiguleJustVisible'))
        END IF
        IF(ANY(calendarMoments .EQ. 'EndGrainFilling')) THEN
            cumulTTFromZC_91 = cumulTT - calendarCumuls(indice(calendarMoments,  &
                    'EndGrainFilling'))
        END IF
    END SUBROUTINE cumulttfrom_
END MODULE
