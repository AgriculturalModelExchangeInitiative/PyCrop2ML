!Test generation'

PROGRAM test_test_wheat1_Phyllochron:
    REAL:: fixPhyll

    REAL:: leafNumber

    REAL:: lincr

    REAL:: ldecr

    REAL:: pdecr

    REAL:: pincr

    REAL:: ptq

    REAL:: gai

    REAL:: pastMaxAI

    REAL:: kl

    REAL:: aPTQ

    REAL:: phylPTQ1

    REAL:: p

    CHARACTER:: choosePhyllUse

    REAL:: phyllochron

    lincr = 8

    ldecr = 3

    pdecr = 0.4

    pincr = 1.25

    fixPhyll = 91.2

    gai = 0.279874189539498

    leafNumber = 0

    ptq = 0

    pastMaxAI = 0

    kl = 0.45

    aPTQ = 0.842934

    phylPTQ1 = 20

    p = 120

    choosePhyllUse = Default

    call phyllochron_(fixPhyll,leafNumber,lincr,ldecr,pdecr,pincr,ptq,gai,pastMaxAI,kl,aPTQ,phylPTQ1,p,choosePhyllUse,phyllochron)
    print *,phyllochron,pastMaxAI
 END PROGRAM

