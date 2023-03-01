MODULE Stmpsimcalculatormod
    IMPLICIT NONE
CONTAINS

    SUBROUTINE model_stmpsimcalculator(cSoilLayerDepth, &
        cFirstDayMeanTemp, &
        cAVT, &
        cABD, &
        cDampingDepth, &
        iSoilWaterContent, &
        iSoilSurfaceTemperature, &
        SoilTempArray, &
        pSoilLayerDepth)
        IMPLICIT NONE
        REAL , DIMENSION(: ), ALLOCATABLE , INTENT(IN) :: cSoilLayerDepth
        REAL, INTENT(IN) :: cFirstDayMeanTemp
        REAL, INTENT(IN) :: cAVT
        REAL, INTENT(IN) :: cABD
        REAL, INTENT(IN) :: cDampingDepth
        REAL, INTENT(IN) :: iSoilWaterContent
        REAL, INTENT(IN) :: iSoilSurfaceTemperature
        REAL , DIMENSION(: ), ALLOCATABLE , INTENT(INOUT) :: SoilTempArray
        REAL , DIMENSION(: ), ALLOCATABLE , INTENT(IN) :: pSoilLayerDepth
        REAL:: XLAG
        REAL:: XLG1
        REAL:: DP
        REAL:: WC
        REAL:: DD
        REAL:: Z1
        INTEGER:: i
        REAL:: ZD
        REAL:: RATE
        !- Name: STMPsimCalculator -Version: 001, -Time step: 1
        !- Description:
    !            * Title: STMPsimCalculator model
    !            * Authors: Gunther Krauss
    !            * Reference: ('http://www.simplace.net/doc/simplace_modules/',)
    !            * Institution: INRES Pflanzenbau, Uni Bonn
    !            * ExtendedDescription: as given in the documentation
    !            * ShortDescription: None
        !- inputs:
    !            * name: cSoilLayerDepth
    !                          ** description : Depth of soil layer
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : 
    !                          ** max : 20.0
    !                          ** min : 0.03
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    !            * name: cFirstDayMeanTemp
    !                          ** description : Mean temperature on first day
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 50.0
    !                          ** min : -40.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: cAVT
    !                          ** description : Constant Temperature of deepest soil layer
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 20.0
    !                          ** min : -10.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: cABD
    !                          ** description : Mean bulk density
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 4.0
    !                          ** min : 1.0
    !                          ** default : 2.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre
    !            * name: cDampingDepth
    !                          ** description : Initial value for damping depth of soil
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 20.0
    !                          ** min : 1.5
    !                          ** default : 6.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    !            * name: iSoilWaterContent
    !                          ** description : Content of water in Soil
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 20.0
    !                          ** min : 1.5
    !                          ** default : 5.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    !            * name: iSoilSurfaceTemperature
    !                          ** description : Temperature at soil surface
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 20.0
    !                          ** min : 1.5
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: SoilTempArray
    !                          ** description : Array of temperature 
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : 
    !                          ** max : 40
    !                          ** min : -20
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: pSoilLayerDepth
    !                          ** description : Depth of soil layer plus additional depth
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : 
    !                          ** max : 20.0
    !                          ** min : 0.03
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
        !- outputs:
    !            * name: SoilTempArray
    !                          ** description : Array of temperature 
    !                          ** datatype : DOUBLEARRAY
    !                          ** variablecategory : state
    !                          ** len : 
    !                          ** max : 40
    !                          ** min : -20
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
        XLAG = .8
        XLG1 = 1 - XLAG
        DP = 1 + (2.5 * cABD / (cABD + EXP(6.53 - (5.63 * cABD))))
        WC = 0.001 * iSoilWaterContent / ((.356 - (.144 * cABD)) *  &
                cSoilLayerDepth((SIZE(cSoilLayerDepth) - 1)+1))
        DD = EXP(LOG(0.5 / DP) * ((1 - WC) / (1 + WC)) * 2) * DP
        Z1 = REAL(0)
        DO i = 0 , SIZE(SoilTempArray)-1, 1
            ZD = 0.5 * (Z1 + pSoilLayerDepth(i+1)) / DD
            RATE = ZD / (ZD + EXP(-.8669 - (2.0775 * ZD))) * (cAVT -  &
                    iSoilSurfaceTemperature)
            SoilTempArray(i+1) = XLAG * SoilTempArray(i+1) + (XLG1 * (RATE +  &
                    iSoilSurfaceTemperature))
            Z1 = pSoilLayerDepth(i+1)
        END DO
    END SUBROUTINE model_stmpsimcalculator

    SUBROUTINE init_stmpsimcalculator(cSoilLayerDepth, &
        cFirstDayMeanTemp, &
        cAVT, &
        cABD, &
        cDampingDepth, &
        iSoilWaterContent, &
        iSoilSurfaceTemperature, &
        SoilTempArray, &
        pSoilLayerDepth)
        IMPLICIT NONE
        REAL , DIMENSION(: ), ALLOCATABLE , INTENT(IN) :: cSoilLayerDepth
        REAL, INTENT(IN) :: cFirstDayMeanTemp
        REAL, INTENT(IN) :: cAVT
        REAL, INTENT(IN) :: cABD
        REAL, INTENT(IN) :: cDampingDepth
        REAL, INTENT(IN) :: iSoilWaterContent
        REAL, INTENT(IN) :: iSoilSurfaceTemperature
        REAL , DIMENSION(: ), ALLOCATABLE , INTENT(OUT) :: SoilTempArray
        REAL , DIMENSION(: ), ALLOCATABLE , INTENT(OUT) :: pSoilLayerDepth
        REAL:: tProfileDepth
        REAL:: additionalDepth
        REAL:: firstAdditionalLayerHight
        INTEGER:: layers
        REAL , DIMENSION(: ), ALLOCATABLE :: tStmp
        REAL , DIMENSION(: ), ALLOCATABLE :: tz
        INTEGER:: i
        REAL:: depth
        tProfileDepth = cSoilLayerDepth(SIZE(cSoilLayerDepth) - 1+1)
        additionalDepth = cDampingDepth - tProfileDepth
        firstAdditionalLayerHight = additionalDepth -  &
                REAL(FLOOR(additionalDepth))
        layers = INT(ABS(REAL(CEILING(additionalDepth)))) +  &
                SIZE(cSoilLayerDepth)
        allocate(tStmp(layers))
        allocate(tz(layers))
        DO i = 0 , SIZE(tStmp)-1, 1
            IF(i .LT. SIZE(cSoilLayerDepth)) THEN
                depth = cSoilLayerDepth(i+1)
            ELSE
                depth = tProfileDepth + firstAdditionalLayerHight + i -  &
                        SIZE(cSoilLayerDepth)
            END IF
            tz(i+1) = depth
            tStmp(i+1) = (cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT *  &
                    depth)) / cDampingDepth
        END DO
        SoilTempArray = tStmp
        pSoilLayerDepth = tz
    END SUBROUTINE init_stmpsimcalculator

END MODULE
