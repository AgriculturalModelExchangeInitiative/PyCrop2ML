!Test generation'

PROGRAM test_test_wheat1_UpdatePhase:
    REAL:: cumulTT

    REAL:: leafNumber

    REAL:: cumulTTFromZC_39

    INTEGER:: isMomentRegistredZC_39

    REAL:: gai

    REAL:: grainCumulTT

    REAL:: dayLength

    REAL:: vernaprog

    REAL:: minFinalNumber

    REAL:: fixPhyll

    INTEGER:: isVernalizable

    REAL:: dse

    REAL:: pFLLAnth

    REAL:: dcd

    REAL:: dgf

    REAL:: degfm

    REAL:: maxDL

    REAL:: sLDL

    LOGICAL:: ignoreGrainMaturation

    REAL:: pHEADANTH

    CHARACTER:: choosePhyllUse

    REAL:: p

    REAL:: phase

    REAL:: cumulTTFromZC_91

    REAL:: phyllochron

    INTEGER:: hasLastPrimordiumAppeared

    REAL:: finalLeafNumber

    choosePhyllUse = "Default"

    phase = 1

    hasLastPrimordiumAppeared = 0

    cumulTT = 354.582294511779

    leafNumber =  4.620511621863958

    cumulTTFromZC_39 = 0

    isMomentRegistredZC_39 = 0

    gai = 0.3255196285135

    grainCumulTT = 0

    dayLength = 12.7433275303389

    vernaprog =  1.0532526829571554

    minFinalNumber = 6.879410413987549

    fixPhyll = 91.2

    isVernalizable = 1

    dse = 105

    pFLLAnth = 2.22

    dcd = 100

    dgf = 450

    degfm = 0

    maxDL = 15

    sLDL = 0.85

    ignoreGrainMaturation = FALSE

    pHEADANTH = 1

    p = 120

    cumulTTFromZC_91 = 0

    phyllochron = 91.2

    finalLeafNumber = 0

    call updatephase_(cumulTT,leafNumber,cumulTTFromZC_39,isMomentRegistredZC_39,gai,grainCumulTT,dayLength,vernaprog,minFinalNumber,fixPhyll,isVernalizable,dse,pFLLAnth,dcd,dgf,degfm,maxDL,sLDL,ignoreGrainMaturation,pHEADANTH,choosePhyllUse,p,phase,cumulTTFromZC_91,phyllochron,hasLastPrimordiumAppeared,finalLeafNumber)
    print *,finalLeafNumber,phase,hasLastPrimordiumAppeared
 END PROGRAM

