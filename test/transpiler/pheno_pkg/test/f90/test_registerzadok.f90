!Test generation'

PROGRAM test_test_wheat1_RegisterZadok:
    REAL:: cumulTT

    REAL:: phase

    REAL:: leafNumber

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarMoments

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarDates

    REAL, ALLOCATABLE, DIMENSION(:):: calendarCumuls

    REAL:: cumulTTFromZC_65

    CHARACTER:: currentdate

    REAL:: der

    REAL:: slopeTSFLN

    REAL:: intTSFLN

    REAL:: finalLeafNumber

    CHARACTER:: currentZadokStage

    INTEGER:: hasZadokStageChanged

    slopeTSFLN = 0.9

    intTSFLN = 2.6

    calendarMoments = ["Sowing","Emergence","EndVernalisation","MainShootPlus1Tiller"]

    calendarDates = ["21/3/2007","27/3/2007","30/3/2007","5/4/2007"]

    calendarCumuls = [ 0.0, 112.330110409888,157.969706915664, 280.570678654207]

    phase = 2

    cumulTT = 354.582294511779

    leafNumber = 4.8854219661087575

    cumulTTFromZC_65 = 0

    currentdate = 9/4/2007

    der = 300.0

    finalLeafNumber = 8.797582013199484

    currentZadokStage = MainShootPlus1Tiller

    hasZadokStageChanged = 0

    call registerzadok_(cumulTT,phase,leafNumber,calendarMoments,calendarDates,calendarCumuls,cumulTTFromZC_65,currentdate,der,slopeTSFLN,intTSFLN,finalLeafNumber,currentZadokStage,hasZadokStageChanged)
    print *,hasZadokStageChanged,currentZadokStage,calendarMoments,calendarDates,calendarCumuls
 END PROGRAM

