MODULE Leafnumber_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE leafnumber_(deltaTT, &
        phyllochron, &
        hasFlagLeafLiguleAppeared, &
        leafNumber, &
        phase)
        REAL:: phyllochron_
        REAL, INTENT(IN) :: deltaTT
        REAL, INTENT(IN) :: phyllochron
        INTEGER, INTENT(IN) :: hasFlagLeafLiguleAppeared
        REAL, INTENT(INOUT) :: leafNumber
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
    !            - name: leafNumber
    !                          - min : 0
    !                          - default : 0
    !                          - max : 25
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description :  Actual number of phytomers
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
        IF(phase .GE. 1.0 .AND. phase .LT. 4.0) THEN
            IF(hasFlagLeafLiguleAppeared .EQ. 0) THEN
                IF(phyllochron .EQ. 0.0) THEN
                    phyllochron_ = 0.0000001
                ELSE
                    phyllochron_ = phyllochron
                END IF
                leafNumber = leafNumber + MIN(deltaTT / phyllochron_, 0.999)
            END IF
        END IF
    END SUBROUTINE leafnumber_
END MODULE
