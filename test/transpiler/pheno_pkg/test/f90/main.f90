PROGRAM testEachModule
    use list_sub
    IMPLICIT NONE

    CALL Test_cumulTTFrom
    CALL Test_IsMomentRegistredZC_39
    CALL Test_leafNumber
    CALL Test_phyllochron
    CALL Test_registerZadock
    CALL Test_shootNumber
    CALL Test_UpdateCalendar
    CALL Test_updateLeafFlag
    CALL Test_updatePhase
    CALL Test_vernalizationProgress
    CALL Test_PhyllSowingDateCorrection
    CALL Test_char
    CALL test_fib

END PROGRAM

SUBROUTINE Test_cumulTTFrom
    USE Cumulttfrom_mod
    REAL,DIMENSION (:), allocatable::calendarCumuls
    REAL :: cumulTT = 972.970888983105
    CHARACTER(LEN=65),DIMENSION(:), allocatable:: calendarMoments

    call add(calendarCumuls,0.0)
    call add(calendarCumuls, 112.330110409888)
    call add(calendarCumuls,354.582294511779)
    call add(calendarCumuls, 741.510096671757)
    call add(calendarCumuls, 853.999637026622)
    call add(calendarCumuls, 954.59002776961)

    call add(calendarMoments,'Sowing')
    call add(calendarMoments,'Emergence')
    call add(calendarMoments,'FloralInitiation')
    call add(calendarMoments,'FlagLeafLiguleJustVisible')
    call add(calendarMoments, 'Heading')
    call add(calendarMoments, 'Anthesis')

    PRINT *, "-----------------------------test_CumulTTFrom------------------------"

    CALL cumulttfrom_(calendarMoments, &
        calendarCumuls, &
        cumulTT, &
        cumulTTFromZC_65, &
        cumulTTFromZC_39, &
        cumulTTFromZC_91)
    PRINT *, "cumulTTFromZC_39 = ", cumulTTFromZC_39,&
    "cumulTTFromZC_65 = ", cumulTTFromZC_65,&
    "cumulTTFromZC_91 = ", cumulTTFromZC_91

END SUBROUTINE

SUBROUTINE test_IsMomentRegistredZC_39
    USE Ismomentregistredzc_39_mod
    IMPLICIT NONE
    INTEGER::isMomentRegistredZC_39
    CHARACTER(LEN=65),DIMENSION(:), allocatable:: calendarMoments
    call add(calendarMoments,'Sowing')
    call add(calendarMoments,'Emergence')
    call add(calendarMoments,'FloralInitiation')
    call add(calendarMoments,'FlagLeafLiguleJustVisible')
    call add(calendarMoments, 'Heading')
    call add(calendarMoments, 'Anthesis')

    PRINT *, "-----------------------------test_IsMomentRegistred------------------------"

    CALL ismomentregistredzc_39_(calendarMoments, &
        isMomentRegistredZC_39)
    PRINT *,"isMomentRegistredZC_39 = ",isMomentRegistredZC_39
END SUBROUTINE

SUBROUTINE test_leafNumber

    USE leafNumber_mod
    IMPLICIT NONE
    INTEGER:: hasFlagLeafLiguleAppeared = 0
    REAL::deltaTT = 23.5895677277199,phyllochron = 91.2, &
    leafNumber = 5.147163833893262, phase = 3

    PRINT *, "-----------------------------test_leafNumber------------------------"

    CALL leafnumber_(deltaTT, &
        phyllochron, &
        hasFlagLeafLiguleAppeared, &
        leafNumber, &
        phase)

    PRINT *, "leafNumber = ",leafNumber

END SUBROUTINE



SUBROUTINE test_phyllochron
    USE Phyllochron_mod
    REAL:: fixPhyll = 91.2,leafNumber = 0,lincr = 8,ldecr = 3,pdecr = 0.4,&
        pincr = 1.25, ptq = 0,gai = 0.279874189539498,pastMaxAI = 0,&
        kl = 0.45, aPTQ = 0.842934,phylPTQ1 = 20, p = 120
    CHARACTER(65):: choosePhyllUse = 'Default'

    PRINT *, "-----------------------------test_phyllochron---------------"
    CALL phyllochron_(fixPhyll, &
        leafNumber, &
        lincr, &
        ldecr, &
        pdecr, &
        pincr, &
        ptq, &
        gai, &
        pastMaxAI, &
        kl, &
        aPTQ, &
        phylPTQ1, &
        p, &
        choosePhyllUse, &
        phyllochron)

    PRINT *, " phyllochron = ", phyllochron, "pastMaxAI", pastMaxAI
END SUBROUTINE


SUBROUTINE test_registerZadock
    USE Registerzadok_mod

    CHARACTER(LEN=65)::currentZadokStage = 'MainShootPlus1Tiller'
    CHARACTER(LEN=65)::currentdate = '9/4/2007'
    CHARACTER(LEN=65) ,DIMENSION(:), ALLOCATABLE:: calendarMoments
    CHARACTER(LEN=65), DIMENSION(:), ALLOCATABLE ::calendarDates
    REAL, DIMENSION(:), ALLOCATABLE :: calendarCumuls

    REAL ::cumulTT = 354.582294511779 ,  phase = 2,leafNumber = 4.8854219661087575,&
        cumulTTFromZC_65 = 0,Der = 300.0,slopeTSFLN = 0.9,intTSFLN = 2.6, &
        finalLeafNumber = 8.797582013199484
    INTEGER :: hasZadokStageChanged = 0

    CALL Add(calendarCumuls,0.0)
    CALL Add(calendarCumuls,112.330110409888)
    CALL Add(calendarCumuls,157.969706915664)
    CALL Add(calendarCumuls,280.570678654207)


    !ALLOCATE(calendarDates(1))
    !calendarDates(1)="21/03/2007"
    CALL Add(calendarDates,"21/03/2007")
    CALL Add(calendarDates,"27/03/2007")
    CALL Add(calendarDates,"30/03/2007")
    CALL Add(calendarDates,"05/04/2007")
    !print *, calendarDates(3)

    !ALLOCATE(calendarMoments(1))
    !calendarMoments(1)="Sowing"
    CALL Add(calendarMoments,'Sowing')
    CALL Add(calendarMoments,'Emergence')
    CALL Add(calendarMoments, 'EndVernalisation')
    CALL Add(calendarMoments,'MainShootPlus1Tiller')

    PRINT *, "-----------------------------test_RegisterZadok------------------------"


    CALL registerzadok_(cumulTT, &
        phase, &
        leafNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        cumulTTFromZC_65, &
        currentdate, &
        der, &
        slopeTSFLN, &
        intTSFLN, &
        finalLeafNumber, &
        currentZadokStage, &
        hasZadokStageChanged)

    PRINT *, "hasZadokStageChanged =", hasZadokStageChanged, &
        "currentZadokStage =" ,currentZadokStage

    DO I=1, SIZE(calendarCumuls)
        PRINT *, calendarCumuls(I), calendarDates(I), calendarMoments(I)
    END DO

END SUBROUTINE

SUBROUTINE test_shootNumber
    USE Shootnumber_mod

    IMPLICIT NONE
    INTEGER :: sowingDensity=288, tillerNumber= 1
    REAL ::leafNumber= 3.34348137255,TargetFertileShoot=600.0, &
        canopyShootNumber=288.0, averageShootNumberPerPlant

    INTEGER, DIMENSION(:) , ALLOCATABLE  ::  leafTillerNumberArray
    REAL,DIMENSION(:), ALLOCATABLE  :: tilleringProfile

    CALL Add(tilleringProfile,288.0)

    CALL Add(leafTillerNumberArray, 1)
    CALL Add(leafTillerNumberArray, 1)
    CALL Add(leafTillerNumberArray, 1)

    PRINT *, "-----------------------------test_ShootNumber------------------------"

    CALL shootnumber_(canopyShootNumber, &
        leafNumber, &
        sowingDensity, &
        targetFertileShoot, &
        tilleringProfile, &
        leafTillerNumberArray, &
        tillerNumber, &
        averageShootNumberPerPlant)

    PRINT *, "canopyShootNumber =",canopyShootNumber,"tillerNumber =", tillerNumber &
    , "averageShootNumberPerPlant = ", averageShootNumberPerPlant

    PRINT *, "leafTillerNumberArray =" ,leafTillerNumberArray
    PRINT *, "tilleringProfile ", tilleringProfile


END SUBROUTINE

SUBROUTINE test_UpdateCalendar
    USE Updatecalendar_mod

    CHARACTER(LEN=65)::currentdate = '27/3/2007'
    CHARACTER(LEN=65) ,DIMENSION(:), ALLOCATABLE:: calendarMoments
    CHARACTER(LEN=65), DIMENSION(:), ALLOCATABLE ::calendarDates
    REAL, DIMENSION(:), ALLOCATABLE :: calendarCumuls

    REAL ::cumulTT = 112.330110409888 ,  phase = 1
    CALL Add(calendarCumuls,0.0)

    call Add(calendarDates,"21/03/2007")

    CALL Add(calendarMoments,"Sowing")


    PRINT *, "-----------------------------test_UpdateCalendar------------------------"

    CALL updatecalendar_(cumulTT, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        currentdate, &
        phase)

    PRINT *, "phase =", phase
    DO I=1, SIZE(calendarCumuls)
        PRINT *, calendarCumuls(I), calendarDates(I), calendarMoments(I)
    END DO


END SUBROUTINE

SUBROUTINE test_updateLeafFlag
    USE Updateleafflag_mod

    CHARACTER(LEN=65)::currentdate = '29/4/2007'
    CHARACTER(LEN=65) ,DIMENSION(:), ALLOCATABLE:: calendarMoments
    CHARACTER(LEN=65), DIMENSION(:), ALLOCATABLE ::calendarDates
    REAL, DIMENSION(:), ALLOCATABLE :: calendarCumuls

    REAL ::cumulTT = 741.510096671757 ,  phase = 3, leafNumber = 8.919453833361189,&
        finalLeafNumber = 8.797582013199484
    INTEGER:: hasFlagLeafLiguleAppeared = 0

    CALL Add(calendarCumuls,0.0)
    CALL Add(calendarCumuls,112.330110409888)
    CALL Add(calendarCumuls,157.969706915664)
    CALL Add(calendarCumuls,280.570678654207)
    CALL Add(calendarCumuls,354.582294511779)
    CALL Add(calendarCumuls,378.453152853726)
    CALL Add(calendarCumuls,402.042720581446)
    CALL Add(calendarCumuls,424.98704708663)
    CALL Add(calendarCumuls,467.23305195298)
    CALL Add(calendarCumuls,487.544313430698)
    CALL Add(calendarCumuls,560.665248444002)
    CALL Add(calendarCumuls,646.389617338974)

    ALLOCATE(calendarDates(1))
    calendarDates(1)="21/03/2007"
    CALL Add(calendarDates,"27/3/2007")
    CALL Add(calendarDates,"30/3/2007")
    CALL Add(calendarDates,"5/4/2007")
    CALL Add(calendarDates,"9/4/2007")
    CALL Add(calendarDates,"10/4/2007")
    CALL Add(calendarDates,"11/4/2007")
    CALL Add(calendarDates,"12/4/2007")
    CALL Add(calendarDates,"14/4/2007")
    CALL Add(calendarDates,"15/4/2007")
    CALL Add(calendarDates,"19/4/2007")
    CALL Add(calendarDates,"24/4/2007")

    ALLOCATE(calendarMoments(1))
    calendarMoments(1)="Sowing"
    CALL Add(calendarMoments,"Emergence")
    CALL Add(calendarMoments,"EndVernalisation")
    CALL Add(calendarMoments,"MainShootPlus1Tiller")
    CALL Add(calendarMoments,"FloralInitiation")
    CALL Add(calendarMoments,"MainShootPlus2Tiller")
    CALL Add(calendarMoments,"TerminalSpikelet")
    CALL Add(calendarMoments,"PseudoStemErection")
    CALL Add(calendarMoments,"MainShootPlus3Tiller")
    CALL Add(calendarMoments,"1stNodeDetectable")
    CALL Add(calendarMoments,"2ndNodeDetectable")
    CALL Add(calendarMoments, "FlagLeafJustVisible")

    PRINT *, "------------------------- Test updateLeafFlag---------------"

    CALL updateleafflag_(cumulTT, &
        leafNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        currentdate, &
        finalLeafNumber, &
        hasFlagLeafLiguleAppeared, &
        phase)

    PRINT *, "hasFlagLeafLiguleAppeared =", hasFlagLeafLiguleAppeared

    PRINT *, "calendarCumuls, CalendarDates,    CalendarMoments"
    DO I=1, SIZE(calendarCumuls)
        PRINT *, calendarCumuls(I), calendarDates(I), calendarMoments(I)
    END DO

END SUBROUTINE test_updateLeafFlag

SUBROUTINE test_updatePhase

    USE Updatephase_mod
    IMPLICIT NONE

    REAL:: cumulTT = 354.582294511779, leafNumber =  4.620511621863958, &
        cumulTTFromZC_39 = 0, gai = 0.3255196285135,&
        grainCumulTT = 0, dayLength = 12.7433275303389, vernaprog =  1.0532526829571554, &
        minFinalNumber = 6.879410413987549, fixPhyll = 91.2,dse = 105,PFLLAnth = 2.22,&
        Dcd = 100,Dgf = 450, Degfm = 0, maxDL = 15,SLDL = 0.85, pHEADANTH = 1,&
        p = 120,phase = 1,cumulTTFromZC_91 = 0, phyllochron = 91.2, finalLeafNumber

    INTEGER::isVernalizable = 1,hasLastPrimordiumAppeared = 0, isMomentRegistredZC_39 = 0
    LOGICAL:: ignoreGrainMaturation = .FALSE.
    CHARACTER(65) :: choosePhyllUse = "Default"

    PRINT *, "---------------------------- test updatePhase----------------------"

    CALL updatephase_(cumulTT, &
        leafNumber, &
        cumulTTFromZC_39, &
        isMomentRegistredZC_39, &
        gai, &
        grainCumulTT, &
        dayLength, &
        vernaprog, &
        minFinalNumber, &
        fixPhyll, &
        isVernalizable, &
        dse, &
        pFLLAnth, &
        dcd, &
        dgf, &
        degfm, &
        maxDL, &
        sLDL, &
        ignoreGrainMaturation, &
        pHEADANTH, &
        choosePhyllUse, &
        p, &
        phase, &
        cumulTTFromZC_91, &
        phyllochron, &
        hasLastPrimordiumAppeared, &
        finalLeafNumber)
    PRINT *, "finalLeafNumber =  ", finalLeafNumber
    PRINT *, "Phase =  ", phase
    PRINT *, "hasLastPrimordiumAppeared=  ", hasLastPrimordiumAppeared


END SUBROUTINE

SUBROUTINE test_vernalizationProgress

    USE Vernalizationprogress_mod

    REAL::dayLength = 12.3037621834005,deltaTT = 20.3429985011972,&
        cumulTT =  112.330110409888,leafNumber = 0,minTvern = 0.0,&
        intTvern =  11.0, vAI =  0.015,vBEE = 0.01, minDL = 8.0,maxDL = 15.0, &
        maxTvern =  23.0,pNini = 4.0, aMXLFNO = 24.0, vernaprog =  0.5517254187376879,&
        minFinalNumber = 5.5

    INTEGER::isVernalizable =1
    CHARACTER(LEN=65)::currentdate = '27/3/2007'
    CHARACTER(LEN=65) ,DIMENSION(:), ALLOCATABLE:: calendarMoments
    CHARACTER(LEN=65), DIMENSION(:), ALLOCATABLE ::calendarDates
    REAL, DIMENSION(:), ALLOCATABLE :: calendarCumuls

    CALL Add(calendarCumuls,0.0)
    call Add(calendarDates, "21/03/2007")
    call Add(calendarMoments, "Sowing")

    PRINT *, "------------------------- test_vernalizationProgress----------------"
    CALL vernalizationprogress_(dayLength, &
        deltaTT, &
        cumulTT, &
        leafNumber, &
        calendarMoments, &
        calendarDates, &
        calendarCumuls, &
        minTvern, &
        intTvern, &
        vAI, &
        vBEE, &
        minDL, &
        maxDL, &
        maxTvern, &
        pNini, &
        aMXLFNO, &
        vernaprog, &
        currentdate, &
        isVernalizable, &
        minFinalNumber)

    PRINT *, "minFinalNumber  = ", minFinalNumber
    PRINT *, "vernaprog = ", vernaprog

    DO I=1, SIZE(calendarCumuls)
        PRINT *, calendarCumuls(I), calendarDates(I), calendarMoments(I)
    END DO

END SUBROUTINE

SUBROUTINE test_PhyllSowingDateCorrection
    USE Phylsowingdatecorrection_mod
    IMPLICIT NONE

    INTEGER::sowingDay = 80,sDws = 90, sDsa_sh = 151, sDsa_nh = 200
    REAL:: latitude = 33.069,  rp = 0.003, p = 120, fixPhyll

    PRINT *, "------------------------ test_phyllSowingDateCorrection------------------"

    CALL phylsowingdatecorrection_(sowingDay, &
        latitude, &
        sDsa_sh, &
        rp, &
        sDws, &
        sDsa_nh, &
        p, &
        fixPhyll)

    PRINT *,  "fixPhyll = ", fixPhyll

END SUBROUTINE




SUBROUTINE Test_char
    USE list_sub
    REAL, allocatable ::  calendarCumuls(:)
    CHARACTER(LEN=65), DIMENSION(:), ALLOCATABLE ::calendarDates
    PRINT *, "------------------------ test_char-----------------"
    CALL Add(calendarCumuls,0.0)
    CALL Add(calendarCumuls,112.330110409888)
    CALL Add(calendarCumuls,157.969706915664)
    CALL Add(calendarCumuls,280.570678654207)

    CALL Add(calendarDates,"27/3/2007")
    CALL Add(calendarDates,"30/3/2007")
    CALL Add(calendarDates,"5/4/2007")
    CALL Add(calendarDates,"9/4/2007")
    CALL Add(calendarDates,"10/4/2007")
    CALL Add(calendarDates,"11/4/2007")

    DO I=1, SIZE(calendarCumuls)
        PRINT *,  calendarCumuls(I), calendarDates(I)

    END DO
END SUBROUTINE

subroutine test_fib
    use Fibonacci_mod
    integer :: result
    call fibonacci_(3, result)
    PRINT *, "------------------------ test_fib-----------------"
    print *, result
end subroutine


