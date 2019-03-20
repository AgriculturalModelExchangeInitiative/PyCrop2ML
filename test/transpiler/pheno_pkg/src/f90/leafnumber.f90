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
        REAL, INTENT(IN) :: phyllochron
        INTEGER, INTENT(IN) :: hasFlagLeafLiguleAppeared
        INTEGER, INTENT(IN) :: switchMaize
        REAL, INTENT(IN) :: atip
        REAL, INTENT(IN) :: leaf_tip_emerg
        REAL, INTENT(IN) :: k_bl
        REAL, INTENT(IN) :: nlim
        REAL, INTENT(INOUT) :: leafNumber
        REAL, INTENT(IN) :: cumulTTPhenoMaizeAtEmergence
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
    !                          - min : -20
    !                          - default : 23.5895677277199
    !                          - max : 100
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : daily delta TT 
    !            - name: phyllochron
    !                          - min : 0
    !                          - default : 0
    !                          - max : 1000
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d leaf-1
    !                          - description : phyllochron
    !            - name: hasFlagLeafLiguleAppeared
    !                          - min : 0
    !                          - default : 0
    !                          - max : 1
    !                          - variablecategory : state
    !                          - datatype : INT
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    !            - name: switchMaize
    !                          - parametercategory : constant
    !                          - min : 0
    !                          - datatype : INT
    !                          - max : 1
    !                          - default : 0
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : true if maize
    !            - name: atip
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 10
    !                          - inputtype : parameter
    !                          - unit : leaf °C-1 d-2
    !                          - description : slope of leaf initiation
    !            - name: leaf_tip_emerg
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 10
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : parameter for maize number of tip emerged
    !            - name: k_bl
    !                          - parametercategory : constant
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 100
    !                          - default : 1.412
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : 
    !            - name: nlim
    !                          - parametercategory : constant
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 6.617
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : 
    !            - name: leafNumber
    !                          - min : 0
    !                          - default : 0
    !                          - max : 25
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description :  Actual number of phytomers
    !            - name: cumulTTPhenoMaizeAtEmergence
    !                          - min : 0
    !                          - default : 300
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C
    !                          - description : cumulTTPhenoMaizeAtEmergence
    !            - name: cumulTT
    !                          - min : -200
    !                          - default : 402.042720581446
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C
    !                          - description : cumul thermal times at current time 
    !            - name: phase
    !                          - min : 0
    !                          - default : 1
    !                          - max : 7
    !                          - uri : some url
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit :  
    !                          - description :  the name of the phase
        !- outputs:
    !            - name: leafNumber
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - uri : some url
    !                          - unit : leaf
    !                          - description : Actual number of phytomers
    !            - name: ntip
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - uri : some url
    !                          - unit : leaf
    !                          - description : Maize number of tip
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
