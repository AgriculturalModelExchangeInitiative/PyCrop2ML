!Test generation'

PROGRAM test_test_wheat1_CumulTTFrom:
    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarMoments

    REAL, ALLOCATABLE, DIMENSION(:):: calendarCumuls

    REAL:: cumulTT

    REAL:: cumulTTFromZC_65

    REAL:: cumulTTFromZC_39

    REAL:: cumulTTFromZC_91

    calendarMoments = ["Sowing", "Emergence", "FloralInitiation", "FlagLeafLiguleJustVisible", "Heading", "Anthesis"]

    calendarCumuls = [0.0, 112.330110409888, 354.582294511779, 741.510096671757, 853.999637026622, 954.59002776961]

    cumulTT = 972.970888983105

    call cumulttfrom_(calendarMoments,calendarCumuls,cumulTT,cumulTTFromZC_65,cumulTTFromZC_39,cumulTTFromZC_91)
    print *,cumulTTFromZC_65,cumulTTFromZC_39,cumulTTFromZC_91
 END PROGRAM

