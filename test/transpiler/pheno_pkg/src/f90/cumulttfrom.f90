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
    !                          - description : List containing appearance of each stage
    !                          - variablecategory : auxiliary
    !                          - datatype : STRINGLIST
    !                          - default : ['Sowing']
    !                          - unit : 
    !                          - inputtype : variable
    !            - name: calendarCumuls
    !                          - description : list containing for each stage occured its cumulated thermal times
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLELIST
    !                          - default : [0.0]
    !                          - unit : °C d
    !                          - inputtype : variable
    !            - name: cumulTT
    !                          - description : cumul TT at current date
    !                          - datatype : DOUBLE
    !                          - variablecategory : auxiliary
    !                          - min : -200
    !                          - max : 10000
    !                          - default : 8
    !                          - unit : °C d
    !                          - inputtype : variable
        !- outputs:
    !            - name: cumulTTFromZC_65
    !                          - description :  cumul TT from Anthesis to current date 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : °C d
    !            - name: cumulTTFromZC_39
    !                          - description :  cumul TT from FlagLeafLiguleJustVisible to current date 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : °C d
    !            - name: cumulTTFromZC_91
    !                          - description :  cumul TT from EndGrainFilling to current date 
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : °C d
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
