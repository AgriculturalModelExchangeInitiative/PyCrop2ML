!Test generation'

PROGRAM test_test_wheat1_VernalizationProgress:
    REAL:: dayLength

    REAL:: deltaTT

    REAL:: cumulTT

    REAL:: leafNumber

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarMoments

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarDates

    REAL, ALLOCATABLE, DIMENSION(:):: calendarCumuls

    REAL:: minTvern

    REAL:: intTvern

    REAL:: vAI

    REAL:: vBEE

    REAL:: minDL

    REAL:: maxDL

    REAL:: maxTvern

    REAL:: pNini

    REAL:: aMXLFNO

    REAL:: vernaprog

    CHARACTER:: currentdate

    INTEGER:: isVernalizable

    REAL:: minFinalNumber

    isVernalizable = 1

    cumulTT =  112.330110409888

    dayLength = 12.3037621834005

    deltaTT = 20.3429985011972

    leafNumber = 0

    calendarMoments = ['Sowing']

    calendarDates = ['21/3/2007']

    calendarCumuls = [0.0]

    minTvern = 0.0

    intTvern =  11.0

    vAI =  0.015

    vBEE = 0.01

    minDL = 8.0

    maxDL = 15.0

    maxTvern =  23.0

    pNini = 4.0

    aMXLFNO = 24.0

    vernaprog =  0.5517254187376879

    currentdate = 27/3/2007

    minFinalNumber = 5.5

    call vernalizationprogress_(dayLength,deltaTT,cumulTT,leafNumber,calendarMoments,calendarDates,calendarCumuls,minTvern,intTvern,vAI,vBEE,minDL,maxDL,maxTvern,pNini,aMXLFNO,vernaprog,currentdate,isVernalizable,minFinalNumber)
    print *,vernaprog,minFinalNumber,calendarMoments,calendarDates,calendarCumuls
 END PROGRAM

