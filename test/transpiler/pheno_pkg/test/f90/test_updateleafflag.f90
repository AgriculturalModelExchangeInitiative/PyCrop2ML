!Test generation'

PROGRAM test_test_wheat1_UpdateLeafFlag:
    REAL:: cumulTT

    REAL:: leafNumber

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarMoments

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarDates

    REAL, ALLOCATABLE, DIMENSION(:):: calendarCumuls

    CHARACTER:: currentdate

    REAL:: finalLeafNumber

    INTEGER:: hasFlagLeafLiguleAppeared

    REAL:: phase

    hasFlagLeafLiguleAppeared = 0

    phase = 3

    calendarMoments = ["Sowing", "Emergence", "EndVernalisation", "MainShootPlus1Tiller", "FloralInitiation", "MainShootPlus2Tiller", "TerminalSpikelet", "PseudoStemErection", "MainShootPlus3Tiller", "1stNodeDetectable", "2ndNodeDetectable", "FlagLeafJustVisible"]

    calendarDates = ["21/3/2007", "27/3/2007", "30/3/2007", "5/4/2007", "9/4/2007", "10/4/2007", "11/4/2007", "12/4/2007", "14/4/2007", "15/4/2007", "19/4/2007", "24/4/2007"]

    calendarCumuls = [0.0, 112.330110409888, 157.969706915664, 280.570678654207, 354.582294511779, 378.453152853726, 402.042720581446, 424.98704708663, 467.23305195298, 487.544313430698, 560.665248444002, 646.389617338974]

    cumulTT = 741.510096671757

    leafNumber = 8.919453833361189

    currentdate = 29/4/2007

    finalLeafNumber = 8.797582013199484

    call updateleafflag_(cumulTT,leafNumber,calendarMoments,calendarDates,calendarCumuls,currentdate,finalLeafNumber,hasFlagLeafLiguleAppeared,phase)
    print *,hasFlagLeafLiguleAppeared,calendarMoments,calendarDates,calendarCumuls
 END PROGRAM

