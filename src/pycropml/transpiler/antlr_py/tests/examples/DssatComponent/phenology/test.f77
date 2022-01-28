        SUBROUTINE modelCumulTTFrom(calendarMomentst1,calendarCumulst1,cumulTT,cumulTTFromZC65, cumulTTFromZC39, cumulTTFromZC91)
                        IMPLICIT NONE
                        CHARACTER(65), ALLOCATABLE , DIMENSION(:), INTENT(IN) ::
                                calendarMomentst1
                        REAL, ALLOCATABLE , DIMENSION(:), INTENT(IN) :: calendarCumulst1
                        REAL, INTENT(IN) :: cumulTT
                        REAL, INTENT(OUT) :: cumulTTFromZC65
                        REAL, INTENT(OUT) :: cumulTTFromZC39
                        REAL, INTENT(OUT) :: cumulTTFromZC91
                        cumulTTFromZC65 = 0.0
                        cumulTTFromZC39 = 0.0
                        cumulTTFromZC91 = 0.0
                        IF(ANY(calendarMomentst1 .EQ. 'Anthesis')) THEN
                            cumulTTFromZC65 = cumulTT -  
                            calendarCumulst1(indice(calendarMomentst1, 'Anthesis'))
                        END IF
                        IF(ANY(calendarMomentst1 .EQ. 'FlagLeafLiguleJustVisible')) THEN
                            cumulTTFromZC39 = cumulTT -  
                                    calendarCumulst1(indice(calendarMomentst1,  
                                    'FlagLeafLiguleJustVisible'))
                        END IF
                        IF(ANY(calendarMomentst1 .EQ. 'EndGrainFilling')) THEN
                            cumulTTFromZC91 = cumulTT -  
                                    calendarCumulst1(indice(calendarMomentst1, 'EndGrainFilling'))
                        END IF
                    END SUBROUTINE modelCumulTTFrom

        END MODULE
