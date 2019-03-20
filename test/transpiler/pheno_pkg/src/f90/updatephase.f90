MODULE Updatephase_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE updatephase_(cumulTT, &
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
        switchMaize, &
        choosePhyllUse, &
        p, &
        phase, &
        cumulTTFromZC_91, &
        phyllochron, &
        hasLastPrimordiumAppeared, &
        finalLeafNumber)
        REAL, INTENT(OUT) :: finalLeafNumber
        REAL:: phase1
        REAL:: ttFromLastLeafToHeading
        REAL:: appFLN
        REAL:: localDegfm
        REAL:: ttFromLastLeafToAnthesis
        REAL, INTENT(IN) :: cumulTT
        REAL, INTENT(IN) :: leafNumber
        REAL, INTENT(IN) :: cumulTTFromZC_39
        INTEGER, INTENT(IN) :: isMomentRegistredZC_39
        REAL, INTENT(IN) :: gai
        REAL, INTENT(IN) :: grainCumulTT
        REAL, INTENT(IN) :: dayLength
        REAL, INTENT(IN) :: vernaprog
        REAL, INTENT(IN) :: minFinalNumber
        REAL, INTENT(IN) :: fixPhyll
        INTEGER, INTENT(IN) :: isVernalizable
        REAL, INTENT(IN) :: dse
        REAL, INTENT(IN) :: pFLLAnth
        REAL, INTENT(IN) :: dcd
        REAL, INTENT(IN) :: dgf
        REAL, INTENT(IN) :: degfm
        REAL, INTENT(IN) :: maxDL
        REAL, INTENT(IN) :: sLDL
        LOGICAL, INTENT(IN) :: ignoreGrainMaturation
        REAL, INTENT(IN) :: pHEADANTH
        INTEGER, INTENT(IN) :: switchMaize
        CHARACTER(65), INTENT(IN) :: choosePhyllUse
        REAL, INTENT(IN) :: p
        REAL, INTENT(INOUT) :: phase
        REAL, INTENT(IN) :: cumulTTFromZC_91
        REAL, INTENT(IN) :: phyllochron
        INTEGER, INTENT(INOUT) :: hasLastPrimordiumAppeared
        !- Description:
    !            - Model Name: UpdatePhase Model
    !            - Author: Pierre MARTRE
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: This strategy advances the phase and calculate the final leaf number
    !    	
        !- inputs:
    !            - name: cumulTT
    !                          - min : -200
    !                          - default : 354.582294511779
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : cumul thermal times at current date
    !            - name: leafNumber
    !                          - min : 0
    !                          - default :  4.620511621863958
    !                          - max : 25
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description : Actual number of phytomers
    !            - name: cumulTTFromZC_39
    !                          - min : 0
    !                          - default : 0
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d-1
    !                          - description : cumul of the thermal time ( DeltaTT) since the moment ZC_39
    !            - name: isMomentRegistredZC_39
    !                          - min : 0
    !                          - default : 0
    !                          - max : 1
    !                          - variablecategory : auxiliary
    !                          - datatype : INT
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : true if ZC_39 is registered in the calendar
    !            - name: gai
    !                          - min : 0
    !                          - default : 0.3255196285135
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : used to calculate Terminal spikelet
    !            - name: grainCumulTT
    !                          - min : 0
    !                          - default : 0
    !                          - max : 10000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : cumulTT used for the grain developpment
    !            - name: dayLength
    !                          - min : 0
    !                          - default : 12.7433275303389
    !                          - max : 24
    !                          - datatype : DOUBLE
    !                          - variablecategory : auxiliary
    !                          - inputtype : variable
    !                          - unit : h
    !                          - description : length of the day
    !            - name: vernaprog
    !                          - min : 0
    !                          - default :  1.0532526829571554
    !                          - max : 10
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : progression on a 0  to 1 scale of the vernalization
    !            - name: minFinalNumber
    !                          - min : 0
    !                          - default : 6.879410413987549
    !                          - max : 25
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : leaf
    !                          - description : minimum final leaf number
    !            - name: fixPhyll
    !                          - min : 0
    !                          - default : 91.2
    !                          - max : 10000
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d
    !                          - description : Phyllochron with sowing date fix
    !            - name: isVernalizable
    !                          - parametercategory : constant
    !                          - min : 0
    !                          - datatype : INT
    !                          - max : 1
    !                          - default : 1
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : true if the plant is vernalizable
    !            - name: dse
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 105
    !                          - inputtype : parameter
    !                          - unit : °C d
    !                          - description : Thermal time from sowing to emergence
    !            - name: pFLLAnth
    !                          - parametercategory : constant
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 2.22
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
    !            - name: dcd
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - default : 100
    !                          - inputtype : parameter
    !                          - unit : °C d
    !                          - description : Duration of the endosperm cell division phase
    !            - name: dgf
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 10000
    !                          - default : 450
    !                          - inputtype : parameter
    !                          - unit : °C d
    !                          - description : Grain filling duration (from anthesis to physiological maturity)
    !            - name: degfm
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 50
    !                          - default : 0
    !                          - inputtype : parameter
    !                          - unit : °C d
    !                          - description : Grain maturation duration (from physiological maturity to harvest ripeness)
    !            - name: maxDL
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 24
    !                          - default : 15
    !                          - inputtype : parameter
    !                          - unit : h
    !                          - description : Saturating photoperiod above which final leaf number is not influenced by daylength
    !            - name: sLDL
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1
    !                          - default : 0.85
    !                          - inputtype : parameter
    !                          - unit : leaf h-1
    !                          - description : Daylength response of leaf production
    !            - name: ignoreGrainMaturation
    !                          - default : FALSE
    !                          - datatype : BOOLEAN
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : true to ignore grain maturation
    !            - name: pHEADANTH
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 1
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : Number of phyllochron between heading and anthesiss
    !            - name: switchMaize
    !                          - min : 0
    !                          - datatype : INT
    !                          - max : 1
    !                          - default : 0
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : true if maize
    !            - name: choosePhyllUse
    !                          - default : Default
    !                          - datatype : STRING
    !                          - inputtype : parameter
    !                          - unit : 
    !                          - description : Switch to choose the type of phyllochron calculation to be used
    !            - name: p
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - default : 120
    !                          - inputtype : parameter
    !                          - unit : °C d leaf-1
    !                          - description : Phyllochron (Varietal parameter)
    !            - name: phase
    !                          - min : 0
    !                          - default : 1
    !                          - max : 7
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description :  the name of the phase
    !            - name: cumulTTFromZC_91
    !                          - min : 0
    !                          - default : 0
    !                          - max : 5000
    !                          - variablecategory : auxiliary
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d-1
    !                          - description : cumul of the thermal time (DeltaTT) since the moment ZC_91
    !            - name: phyllochron
    !                          - min : 0
    !                          - default : 91.2
    !                          - max : 1000
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - inputtype : variable
    !                          - unit : °C d leaf-1
    !                          - description : Phyllochron
    !            - name: hasLastPrimordiumAppeared
    !                          - min : 0
    !                          - default : 0
    !                          - max : 1
    !                          - variablecategory : state
    !                          - datatype : INT
    !                          - inputtype : variable
    !                          - unit : 
    !                          - description : if Last Primordium has Appeared
        !- outputs:
    !            - name: finalLeafNumber
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : state
    !                          - max : 25
    !                          - unit : leaf
    !                          - description : final leaf number
    !            - name: phase
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - variablecategory : state
    !                          - max : 7
    !                          - unit : 
    !                          - description : the name of the phase
    !            - name: hasLastPrimordiumAppeared
    !                          - datatype : INT
    !                          - min : 0
    !                          - variablecategory : state
    !                          - max : 1
    !                          - unit : 
    !                          - description : if Last Primordium has Appeared
        phase1 = phase
        IF(phase1 .GE. 0.0 .AND. phase1 .LT. 1.0) THEN
            IF(switchMaize .EQ. 0) THEN
                IF(cumulTT .GE. dse) THEN
                    phase = 1.0
                ELSE
                    phase = phase1
                END IF
            ELSE
                IF(cumulTT .GE. dse) THEN
                    phase = 1.0
                ELSE
                    phase = phase1
                END IF
            END IF
        ELSE IF ( phase1 .GE. 1.0 .AND. phase1 .LT. 2.0) THEN
            IF(isVernalizable .EQ. 1 .AND. vernaprog .GE. 1.0 .OR. isVernalizable  &
                    .EQ. 0) THEN
                IF(switchMaize .EQ. 0) THEN
                    IF(dayLength .GT. maxDL) THEN
                        finalLeafNumber = minFinalNumber
                        hasLastPrimordiumAppeared = 1
                    ELSE
                        appFLN = minFinalNumber + sLDL * (maxDL - dayLength)
                        IF(appFLN / 2.0 .LE. leafNumber) THEN
                            finalLeafNumber = appFLN
                            hasLastPrimordiumAppeared = 1
                        ELSE
                            phase = phase1
                        END IF
                    END IF
                ELSE
                    hasLastPrimordiumAppeared = 1
                END IF
                IF(hasLastPrimordiumAppeared .EQ. 1) THEN
                    phase = 2.0
                END IF
            ELSE
                phase = phase1
            END IF
        ELSE IF ( phase1 .GE. 2.0 .AND. phase1 .LT. 4.0) THEN
            IF(isMomentRegistredZC_39 .EQ. 1) THEN
                IF(phase1 .LT. 3.0) THEN
                    ttFromLastLeafToHeading = 0.0
                    IF(choosePhyllUse .EQ. 'Default') THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll
                    ELSE IF ( choosePhyllUse .EQ. 'PTQ') THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
                    ELSE IF ( choosePhyllUse .EQ. 'Test') THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                    END IF
                    IF(cumulTTFromZC_39 .GE. ttFromLastLeafToHeading) THEN
                        phase = 3.0
                    ELSE
                        phase = phase1
                    END IF
                ELSE
                    phase = phase1
                END IF
                ttFromLastLeafToAnthesis = 0.0
                IF(choosePhyllUse .EQ. 'Default') THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
                ELSE IF ( choosePhyllUse .EQ. 'PTQ') THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
                ELSE IF ( choosePhyllUse .EQ. 'Test') THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * p
                END IF
                IF(cumulTTFromZC_39 .GE. ttFromLastLeafToAnthesis) THEN
                    phase = 4.0
                END IF
            ELSE
                phase = phase1
            END IF
        ELSE IF ( phase1 .EQ. 4.0) THEN
            IF(grainCumulTT .GE. dcd) THEN
                phase = 4.5
            ELSE
                phase = phase1
            END IF
        ELSE IF ( phase1 .EQ. 4.5) THEN
            IF(grainCumulTT .GE. dgf .OR. gai .LE. 0.0) THEN
                phase = 5.0
            ELSE
                phase = phase1
            END IF
        ELSE IF ( phase1 .GE. 5.0 .AND. phase1 .LT. 6.0) THEN
            localDegfm = degfm
            IF(ignoreGrainMaturation) THEN
                localDegfm = -1.0
            END IF
            IF(cumulTTFromZC_91 .GE. localDegfm) THEN
                phase = 6.0
            ELSE
                phase = phase1
            END IF
        ELSE IF ( phase1 .GE. 6.0 .AND. phase1 .LT. 7.0) THEN
            phase = phase1
        END IF
    END SUBROUTINE updatephase_
END MODULE
