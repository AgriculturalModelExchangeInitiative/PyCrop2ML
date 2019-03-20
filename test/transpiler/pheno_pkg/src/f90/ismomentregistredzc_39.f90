MODULE Ismomentregistredzc_39_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE ismomentregistredzc_39_(calendarMoments, &
        isMomentRegistredZC_39)
        INTEGER, INTENT(OUT) :: isMomentRegistredZC_39
        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::  &
                calendarMoments
        !- Description:
    !            - Model Name: IsMomentRegistredZC39 Model
    !            - Author: Pierre Martre
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: if FlagLeafLiguleJustVisible is already Registred 
        !- inputs:
    !            - name: calendarMoments
    !                          - variablecategory : auxiliary
    !                          - datatype : STRINGLIST
    !                          - default : ['Sowing']
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : List containing appearance of each stage
        !- outputs:
    !            - name: isMomentRegistredZC_39
    !                          - min : 0
    !                          - datatype : INT
    !                          - max : 1
    !                          - unit : 
    !                          - description :  if Flag leaf ligule has already appeared 
        IF (ANY(calendarMoments .EQ. 'FlagLeafLiguleJustVisible')) THEN
            isMomentRegistredZC_39=1
        ELSE
            isMomentRegistredZC_39=0
        END IF
    END SUBROUTINE ismomentregistredzc_39_
END MODULE
