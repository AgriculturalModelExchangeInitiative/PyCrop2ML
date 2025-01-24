SUBROUTINE model_snowcovercalculator(cCarbonContent, &
        iTempMax, &
        iTempMin, &
        iRadiation, &
        iRAIN, &
        iCropResidues, &
        iPotentialSoilEvaporation, &
        iLeafAreaIndex, &
        iSoilTempArray, &
        Albedo, &
        SnowWaterContent, &
        SoilSurfaceTemperature, &
        AgeOfSnow, &
        SnowIsolationIndex)
    IMPLICIT NONE
    REAL, INTENT(IN) :: cCarbonContent
    REAL, INTENT(IN) :: iTempMax
    REAL, INTENT(IN) :: iTempMin
    REAL, INTENT(IN) :: iRadiation
    REAL, INTENT(IN) :: iRAIN
    REAL, INTENT(IN) :: iCropResidues
    REAL, INTENT(IN) :: iPotentialSoilEvaporation
    REAL, INTENT(IN) :: iLeafAreaIndex
    REAL , DIMENSION(: ), INTENT(IN) :: iSoilTempArray
    REAL, INTENT(IN) :: Albedo
    REAL, INTENT(INOUT) :: SnowWaterContent
    REAL, INTENT(INOUT) :: SoilSurfaceTemperature
    INTEGER, INTENT(INOUT) :: AgeOfSnow
    REAL, INTENT(OUT) :: SnowIsolationIndex
    REAL:: tiCropResidues
    REAL:: tiSoilTempArray
    REAL:: TMEAN
    REAL:: TAMPL
    REAL:: DST
    REAL:: tSoilSurfaceTemperature
    REAL:: tSnowIsolationIndex
    REAL:: SNOWEVAPORATION
    REAL:: SNOWMELT
    REAL:: EAJ
    REAL:: ageOfSnowFactor
    REAL:: SNPKT
    !- Name: SnowCoverCalculator -Version: 001, -Time step: 1
    !- Description:
    !            * Title: SnowCoverCalculator model
    !            * Authors: Gunther Krauss
    !            * Reference: ('http://www.simplace.net/doc/simplace_modules/',)
    !            * Institution: INRES Pflanzenbau, Uni Bonn
    !            * ExtendedDescription: as given in the documentation
    !            * ShortDescription: None
    !- inputs:
    !            * name: cCarbonContent
    !                          ** description : Carbon content of upper soil layer
    !                          ** inputtype : parameter
    !                          ** parametercategory : constant
    !                          ** datatype : DOUBLE
    !                          ** max : 20.0
    !                          ** min : 0.0
    !                          ** default : 0.5
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/percent
    !            * name: iTempMax
    !                          ** description : Daily maximum temperature
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 50.0
    !                          ** min : -40.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: iTempMin
    !                          ** description : Daily minimum temperature
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 50.0
    !                          ** min : -40.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: iRadiation
    !                          ** description : Solar radiation
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 2000.0
    !                          ** min : 0.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/megajoule_per_square_metre
    !            * name: iRAIN
    !                          ** description : Rain amount
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 60.0
    !                          ** min : 0.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    !            * name: iCropResidues
    !                          ** description : Crop residues plus above ground biomass
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 20000.0
    !                          ** min : 0.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/gram_per_square_metre
    !            * name: iPotentialSoilEvaporation
    !                          ** description : Potenial Evaporation
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 12.0
    !                          ** min : 0.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    !            * name: iLeafAreaIndex
    !                          ** description : Leaf area index
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLE
    !                          ** max : 10.0
    !                          ** min : 0.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/square_metre_per_square_metre
    !            * name: iSoilTempArray
    !                          ** description : Soil Temp array of last day
    !                          ** inputtype : variable
    !                          ** variablecategory : exogenous
    !                          ** datatype : DOUBLEARRAY
    !                          ** len : 
    !                          ** max : 35.0
    !                          ** min : -15.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: Albedo
    !                          ** description : Albedo
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 1.0
    !                          ** min : 0.0
    !                          ** default : 
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    !            * name: SnowWaterContent
    !                          ** description : Snow water content
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 1500.0
    !                          ** min : 0.0
    !                          ** default : 0.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    !            * name: SoilSurfaceTemperature
    !                          ** description : Soil surface temperature
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : DOUBLE
    !                          ** max : 70.0
    !                          ** min : -40.0
    !                          ** default : 0.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: AgeOfSnow
    !                          ** description : Age of snow
    !                          ** inputtype : variable
    !                          ** variablecategory : state
    !                          ** datatype : INT
    !                          ** max : null
    !                          ** min : 0
    !                          ** default : 0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    !- outputs:
    !            * name: SnowWaterContent
    !                          ** description : Snow water content
    !                          ** datatype : DOUBLE
    !                          ** variablecategory : state
    !                          ** max : 1500.0
    !                          ** min : 0.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    !            * name: SoilSurfaceTemperature
    !                          ** description : Soil surface temperature
    !                          ** datatype : DOUBLE
    !                          ** variablecategory : state
    !                          ** max : 70.0
    !                          ** min : -40.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    !            * name: AgeOfSnow
    !                          ** description : Age of snow
    !                          ** datatype : INT
    !                          ** variablecategory : state
    !                          ** max : null
    !                          ** min : 0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    !            * name: SnowIsolationIndex
    !                          ** description : Snow isolation index
    !                          ** datatype : DOUBLE
    !                          ** variablecategory : auxiliary
    !                          ** max : 1.0
    !                          ** min : 0.0
    !                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    tiCropResidues = iCropResidues * 10.0
    tiSoilTempArray = iSoilTempArray(1)
    TMEAN = 0.5 * (iTempMax + iTempMin)
    TAMPL = 0.5 * (iTempMax - iTempMin)
    DST = TMEAN + (TAMPL * (iRadiation * (1 - Albedo) - 14) / 20)
    IF(iRAIN .GT. REAL(0) .AND. (tiSoilTempArray .LT. REAL(1) .OR.  &
            (SnowWaterContent .GT. REAL(3) .OR. SoilSurfaceTemperature .LT.  &
            REAL(0)))) THEN
        SnowWaterContent = SnowWaterContent + iRAIN
    END IF
    tSnowIsolationIndex = 1.0
    IF(tiCropResidues .LT. REAL(10)) THEN
        tSnowIsolationIndex = tiCropResidues / (tiCropResidues + EXP(5.34 -  &
                (2.4 * tiCropResidues)))
    END IF
    IF(SnowWaterContent .LT. 1E-10) THEN
        tSnowIsolationIndex = tSnowIsolationIndex * 0.85
        tSoilSurfaceTemperature = 0.5 * (DST + ((1 - tSnowIsolationIndex) *  &
                DST) + (tSnowIsolationIndex * tiSoilTempArray))
    ELSE
        tSnowIsolationIndex = MAX(SnowWaterContent / (SnowWaterContent +  &
                EXP(0.47 - (0.62 * SnowWaterContent))), tSnowIsolationIndex)
        tSoilSurfaceTemperature = (1 - tSnowIsolationIndex) * DST +  &
                (tSnowIsolationIndex * tiSoilTempArray)
    END IF
    IF(SnowWaterContent .EQ. REAL(0) .AND. .NOT. (iRAIN .GT. REAL(0)  &
            .AND. tiSoilTempArray .LT. REAL(1))) THEN
        SnowWaterContent = REAL(0)
    ELSE
        EAJ = .5
        IF(SnowWaterContent .LT. REAL(5)) THEN
            EAJ = EXP(-MAX(0.4 * iLeafAreaIndex, 0.1 * (tiCropResidues + 0.1)))
        END IF
        SNOWEVAPORATION = iPotentialSoilEvaporation * EAJ
        ageOfSnowFactor = AgeOfSnow / (AgeOfSnow + EXP(5.34 - (2.395 *  &
                AgeOfSnow)))
        SNPKT = .3333 * (2 * min(tSoilSurfaceTemperature, tiSoilTempArray) +  &
                iTempMax)
        IF(TMEAN .GT. REAL(0)) THEN
            SNOWMELT = MAX(0.0, SQRT(iTempMax * iRadiation) * (1.52 + (.54 *  &
                    ageOfSnowFactor * SNPKT)))
        ELSE
            SNOWMELT = REAL(0)
        END IF
        IF(SNOWMELT + SNOWEVAPORATION .GT. SnowWaterContent) THEN
            SNOWMELT = SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
            SNOWEVAPORATION = SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) *  &
                    SnowWaterContent
        END IF
        SnowWaterContent = SnowWaterContent - (SNOWMELT + SNOWEVAPORATION)
        IF(SnowWaterContent .LT. REAL(0)) THEN
            SnowWaterContent = REAL(0)
        END IF
        IF(SnowWaterContent .LT. REAL(5)) THEN
            AgeOfSnow = 0
        ELSE
            AgeOfSnow = AgeOfSnow + 1
        END IF
    END IF
    SnowIsolationIndex = tSnowIsolationIndex
    SoilSurfaceTemperature = tSoilSurfaceTemperature
END SUBROUTINE model_snowcovercalculator

SUBROUTINE init_snowcovercalculator(cCarbonContent, &
        iTempMax, &
        iTempMin, &
        iRadiation, &
        iRAIN, &
        iCropResidues, &
        iPotentialSoilEvaporation, &
        iLeafAreaIndex, &
        iSoilTempArray, &
        Albedo, &
        SnowWaterContent, &
        SoilSurfaceTemperature, &
        AgeOfSnow)
    IMPLICIT NONE
    REAL, INTENT(IN) :: cCarbonContent
    REAL, INTENT(IN) :: iTempMax
    REAL, INTENT(IN) :: iTempMin
    REAL, INTENT(IN) :: iRadiation
    REAL, INTENT(IN) :: iRAIN
    REAL, INTENT(IN) :: iCropResidues
    REAL, INTENT(IN) :: iPotentialSoilEvaporation
    REAL, INTENT(IN) :: iLeafAreaIndex
    REAL , DIMENSION(: ), INTENT(IN) :: iSoilTempArray
    REAL, INTENT(OUT) :: Albedo
    REAL, INTENT(OUT) :: SnowWaterContent
    REAL, INTENT(OUT) :: SoilSurfaceTemperature
    INTEGER, INTENT(OUT) :: AgeOfSnow
    SnowWaterContent = 0.0
    SoilSurfaceTemperature = 0.0
    AgeOfSnow = 0
    Albedo = 0.0
    Albedo = 0.0226 * LOG(cCarbonContent) / LOG(10.0) + 0.1502
END SUBROUTINE init_snowcovercalculator
