!Test generation'

PROGRAM test_test_wheat1_IsMomentRegistredZC_39:
    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarMoments

    INTEGER:: isMomentRegistredZC_39

    calendarMoments = ["Sowing", "Emergence", "FloralInitiation", "FlagLeafLiguleJustVisible", "Heading", "Anthesis"]

    call ismomentregistredzc_39_(calendarMoments,isMomentRegistredZC_39)
    print *,isMomentRegistredZC_39
 END PROGRAM

