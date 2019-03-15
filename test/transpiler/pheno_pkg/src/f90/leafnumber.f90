MODULE Leafnumber_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE leafnumber_(deltaTT, &
        phyllochron, &
        hasFlagLeafLiguleAppeared, &
        switchMaize, &
        atip, &
        leaf_tip_emerg, &
        k_bl, &
        nlim, &
        leafNumber, &
        cumulTTPhenoMaizeAtEmergence, &
        cumulTT, &
        phase, &
        ntip)
        REAL, INTENT(OUT) :: ntip
        REAL:: nextstartExpTT
        REAL:: nexttipTT
        REAL:: abl
        REAL:: tt_lim_lip
        REAL:: bbl
        REAL:: tt_bl
        REAL, INTENT(IN) :: deltaTT
        REAL :: phyllochron
        INTEGER, INTENT(IN) :: hasFlagLeafLiguleAppeared
        INTEGER, INTENT(IN) :: switchMaize
        REAL, INTENT(IN) :: atip
        REAL, INTENT(IN) :: leaf_tip_emerg
        REAL, INTENT(IN) :: k_bl
        REAL, INTENT(IN) :: nlim
        REAL, INTENT(INOUT) :: leafNumber
        REAL, INTENT(INOUT) :: cumulTTPhenoMaizeAtEmergence
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: phase
        !- Description:
    !            - Model Name: CalculateLeafNumber Model
    !            - Author: Pierre MARTRE
    !            - Reference: Modeling development phase in the
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
        !- inputs:
    !            - name: deltaTT
    !                          - description : daily delta TT
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : -20
    !                          - max : 100
    !                          - default : 23.5895677277199
    !                          - unit : °C d
    !                          - inputtype : variable
    !            - name: phyllochron
    !                          - description : phyllochron
    !                          - variablecategory : state
    !                          - inputtype : variable
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1000
    !                          - default : 0
    !                          - unit : °C d leaf-1
    !            - name: hasFlagLeafLiguleAppeared
    !                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    !                          - variablecategory : state
    !                          - datatype : INT
    !                          - min : 0
    !                          - max : 1
    !                          - default : 0
    !                          - unit :
    !                          - inputtype : variable
    !            - name: switchMaize
    !                          - description : true if maize
    !                          - parametercategory : constant
    !                          - datatype : INT
    !                          - min : 0
    !                          - max : 1
    !                          - default : 0
    !                          - unit :
    !                          - inputtype : parameter
    !            - name: atip
    !                          - description : slope of leaf initiation
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1000
    !                          - default : 10
    !                          - unit : leaf °C-1 d-2
    !                          - inputtype : parameter
    !            - name: leaf_tip_emerg
    !                          - description : parameter for maize number of tip emerged
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1000
    !                          - default : 10
    !                          - unit :
    !                          - inputtype : parameter
    !            - name: k_bl
    !                          - description :
    !                          - parametercategory : constant
    !                          - inputtype : parameter
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 100
    !                          - default : 1.412
    !                          - unit :
    !            - name: nlim
    !                          - description :
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 6.617
    !                          - min : 0
    !                          - max : 1000
    !                          - unit :
    !                          - inputtype : parameter
    !            - name: leafNumber
    !                          - description :  Actual number of phytomers
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 25
    !                          - default : 0
    !                          - unit : leaf
    !                          - inputtype : variable
    !            - name: cumulTTPhenoMaizeAtEmergence
    !                          - description : cumulTTPhenoMaizeAtEmergence
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - default : 300
    !                          - unit : °C
    !                          - inputtype : variable
    !            - name: cumulTT
    !                          - description : cumul thermal times at current time
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : -200
    !                          - max : 10000
    !                          - unit : °C
    !                          - default : 402.042720581446
    !                          - inputtype : variable
    !            - name: phase
    !                          - description :  the name of the phase
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 7
    !                          - default : 1
    !                          - unit :
    !                          - uri : some url
    !                          - inputtype : variable
        !- outputs:
    !            - name: leafNumber
    !                          - description : Actual number of phytomers
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : leaf
    !                          - uri : some url
    !            - name: ntip
    !                          - description : Maize number of tip
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : leaf
    !                          - uri : some url
    !            - name: cumulTTPhenoMaizeAtEmergence
    !                          - description : cumulTTPhenoMaizeAtEmergence
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 10000
    !                          - unit : °C
        ntip = 0.0
        IF(phase .EQ. 1.0 .AND. cumulTTPhenoMaizeAtEmergence .EQ. 0.0) THEN
            cumulTTPhenoMaizeAtEmergence = cumulTT
        END IF
        IF(phase .GE. 1.0 .AND. phase .LT. 4.0) THEN
            IF(hasFlagLeafLiguleAppeared .EQ. 0) THEN
                IF(switchMaize .EQ. 0) THEN
                    IF(phyllochron .EQ. 0.0) THEN
                        phyllochron = 0.0000001
                    END IF
                    leafNumber = leafNumber + MIN(deltaTT / phyllochron, 0.999)
                    ntip = 0.0
                ELSE
                    IF(leafNumber .LT. leaf_tip_emerg) THEN
                        leafNumber = leaf_tip_emerg
                    ELSE
                        nextstartExpTT = 0.0
                        nexttipTT = (leafNumber + 1 - leaf_tip_emerg) / atip +  &
                                cumulTTPhenoMaizeAtEmergence
                        abl = k_bl * atip
                        tt_lim_lip = (nlim - leaf_tip_emerg) / atip +  &
                                cumulTTPhenoMaizeAtEmergence
                        bbl = nlim - abl * tt_lim_lip
                        tt_bl = (leafNumber + 1 - bbl) / abl
                        IF(tt_bl .GT. nexttipTT) THEN
                            nextstartExpTT = nexttipTT
                        ELSE
                            nextstartExpTT = tt_bl
                        END IF
                        IF(cumulTT .GE. nextstartExpTT) THEN
                            leafNumber = leafNumber + 1
                        END IF
                    END IF
                    ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) +  &
                            leaf_tip_emerg
                END IF
            END IF
        END IF
    END SUBROUTINE leafnumber_
END MODULE
