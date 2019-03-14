MODULE Phyllochron_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE phyllochron_(fixPhyll, &
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
        REAL, INTENT(OUT) :: phyllochron
        REAL:: pastMaxAI1
        REAL, INTENT(IN) :: fixPhyll
        REAL, INTENT(IN) :: leafNumber
        REAL, INTENT(IN) :: lincr
        REAL, INTENT(IN) :: ldecr
        REAL, INTENT(IN) :: pdecr
        REAL, INTENT(IN) :: pincr
        REAL, INTENT(IN) :: ptq
        REAL, INTENT(INOUT) :: gai
        REAL, INTENT(INOUT) :: pastMaxAI
        REAL, INTENT(IN) :: kl
        REAL, INTENT(IN) :: aPTQ
        REAL, INTENT(IN) :: phylPTQ1
        REAL, INTENT(IN) :: p
        CHARACTER(65), INTENT(IN) :: choosePhyllUse
        !- Description:
    !            - Model Name: Phyllochron Model
    !            - Author: Pierre Martre
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: Calculate different types of phyllochron 
        !- inputs:
    !            - name: fixPhyll
    !                          - description : Sowing date corrected Phyllochron
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 5
    !                          - unit : °C d leaf-1
    !                          - uri : some url
    !                          - inputtype : variable
    !            - name: leafNumber
    !                          - description : Actual number of phytomers
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 25
    !                          - default : 0
    !                          - unit : leaf
    !                          - uri : some url
    !                          - inputtype : variable
    !            - name: lincr
    !                          - description : Leaf number above which the phyllochron is increased by Pincr
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 30
    !                          - default : 8
    !                          - unit : leaf
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: ldecr
    !                          - description : Leaf number up to which the phyllochron is decreased by Pdecr
    !                          - parametercategory : species
    !                          - inputtype : parameter
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 30
    !                          - default : 10
    !                          - unit : leaf
    !                          - uri : some url
    !            - name: pdecr
    !                          - description : Factor decreasing the phyllochron for leaf number less than Ldecr
    !                          - parametercategory : constant
    !                          - inputtype : parameter
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10
    !                          - default : 0.4
    !                          - unit : 
    !                          - uri : some url
    !            - name: pincr
    !                          - description : Factor increasing the phyllochron for leaf number higher than Lincr
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.5
    !                          - min : 0
    !                          - max : 10
    !                          - unit : 
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: ptq
    !                          - description : Photothermal quotient 
    !                          - parametercategory : species
    !                          - inputtype : variable
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 0
    !                          - unit : MJ °C-1 d-1 m-2)
    !                          - uri : some url
    !            - name: gai
    !                          - description : Green Area Index
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 0
    !                          - unit : m2 m-2
    !                          - uri : some url
    !                          - inputtype : variable
    !            - name: pastMaxAI
    !                          - description : PhotoThermal Quotien
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 0
    !                          - unit : m2 m-2
    !                          - uri : some url
    !                          - inputtype : variable
    !            - name: kl
    !                          - description : Exctinction Coefficient
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 50
    !                          - default : 0.45
    !                          - unit : 
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: aPTQ
    !                          - description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
    !                          - parametercategory : constant
    !                          - inputtype : variable
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1000
    !                          - default : 0.842934
    !                          - unit : 
    !                          - uri : some url
    !            - name: phylPTQ1
    !                          - description : Phyllochron at PTQ equal 1
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 20
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : °C d leaf-1
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: p
    !                          - description : Phyllochron (Varietal parameter)
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - default : 120
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : °C d leaf-1
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: choosePhyllUse
    !                          - description : Switch to choose the type of phyllochron calculation to be used
    !                          - datatype : STRING
    !                          - default : Default
    !                          - unit : 
    !                          - uri : some url
    !                          - inputtype : parameter
        !- outputs:
    !            - name: phyllochron
    !                          - description :  the rate of leaf appearance 
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1000
    !                          - unit :  °C d leaf-1
    !            - name: pastMaxAI
    !                          - description : Past maximum GAI
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : m2 m-2
    !            - name: gai
    !                          - description : Green Area Index
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : m2 m-2
    !                          - uri : some url
        phyllochron = 0.0
        IF(choosePhyllUse .EQ. 'Default') THEN
            IF(leafNumber .LT. ldecr) THEN
                phyllochron = fixPhyll * pdecr
            ELSE IF ( leafNumber .GE. ldecr .AND. leafNumber .LT. lincr) THEN
                phyllochron = fixPhyll
            ELSE
                phyllochron = fixPhyll * pincr
            END IF
        END IF
        IF(choosePhyllUse .EQ. 'PTQ') THEN
            pastMaxAI1 = pastMaxAI
            gai = MAX(pastMaxAI1, gai)
            pastMaxAI = gai
            IF(gai .GT. 0.0) THEN
                phyllochron = phylPTQ1 * gai * kl / (1 - EXP(-kl * gai)) / (ptq +  &
                        aPTQ)
            ELSE
                phyllochron = phylPTQ1
            END IF
        END IF
        IF(choosePhyllUse .EQ. 'Test') THEN
            IF(leafNumber .LT. ldecr) THEN
                phyllochron = p * pdecr
            ELSE IF ( leafNumber .GE. ldecr .AND. leafNumber .LT. lincr) THEN
                phyllochron = p
            ELSE
                phyllochron = p * pincr
            END IF
        END IF
    END SUBROUTINE phyllochron_
END MODULE
