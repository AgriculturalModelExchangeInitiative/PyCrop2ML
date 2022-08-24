library(gsubfn)

model_stemp_epic <- function (NL,
         ISWWAT,
         BD,
         DLAYR,
         DS,
         DUL,
         LL,
         NLAYR,
         TAMP,
         RAIN,
         CUMDPT,
         DSMID,
         SW,
         TAVG,
         TMAX,
         TMIN,
         TAV,
         SRFTEMP,
         NDays,
         TDL,
         WetDay,
         ST,
         TMA,
         DEPIR,
         BIOMAS,
         MULCHMASS,
         SNOW){
    #'- Name: STEMP_EPIC -Version: 001, -Time step: 1
    #'- Description:
    #'            * Title: model of soil
    #'            * Author: Cyrille
    #'            * Reference: None
    #'            * Institution: INRAE
    #'            * ExtendedDescription: None
    #'            * ShortDescription: None
    #'- inputs:
    #'            * name: NL
    #'                          ** description : Number of soil layers
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : dimensionless
    #'            * name: ISWWAT
    #'                          ** description : Water simulation control switch (Y or N)
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : STRING
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : Y
    #'                          ** unit : dimensionless
    #'            * name: BD
    #'                          ** description : Bulk density, soil layer NL
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : g [soil] / cm3 [soil]
    #'            * name: DLAYR
    #'                          ** description : Thickness of soil layer NL
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm
    #'            * name: DS
    #'                          ** description : Cumulative depth in soil layer NL
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm
    #'            * name: DUL
    #'                          ** description : Volumetric soil water content at Drained Upper Limit in soil layer L
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm3[water]/cm3[soil]
    #'            * name: LL
    #'                          ** description : Volumetric soil water content in soil layer NL at lower limit
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm3 [water] / cm3 [soil]
    #'            * name: NLAYR
    #'                          ** description : Actual number of soil layers
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : dimensionless
    #'            * name: TAMP
    #'                          ** description : Annual amplitude of the average air temperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: RAIN
    #'                          ** description : daily rainfall
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : mm
    #'            * name: CUMDPT
    #'                          ** description : Cumulative depth of soil profile
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : mm
    #'            * name: DSMID
    #'                          ** description : Depth to midpoint of soil layer NL
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm
    #'            * name: SW
    #'                          ** description : Volumetric soil water content in layer NL
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : soil
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm3 [water] / cm3 [soil]
    #'            * name: TAVG
    #'                          ** description : Average daily temperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: TMAX
    #'                          ** description : Maximum daily temperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: TMIN
    #'                          ** description : Maximum Temperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: TAV
    #'                          ** description : Average annual soil temperature, used with TAMP to calculate soil temperature.
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: SRFTEMP
    #'                          ** description : Temperature of soil surface litter
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: NDays
    #'                          ** description : Number of days ...
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : day
    #'            * name: TDL
    #'                          ** description : Total water content of soil at drained upper limit
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm
    #'            * name: WetDay
    #'                          ** description : Wet Days
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : INTARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : day
    #'            * name: ST
    #'                          ** description : Soil temperature in soil layer NL
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: TMA
    #'                          ** description : Array of previous 5 days of average soil temperatures.
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : 5
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: DEPIR
    #'                          ** description : Management variable
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : don't know
    #'            * name: BIOMAS
    #'                          ** description : Biomass
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : kg/ha
    #'            * name: MULCHMASS
    #'                          ** description : Mulch Mass
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : kg/ha
    #'            * name: SNOW
    #'                          ** description : Snow cover
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : mm
    #'- outputs:
    #'            * name: SRFTEMP
    #'                          ** description : Temperature of soil surface litter
    #'                          ** datatype : DOUBLE
    #'                          ** variablecategory : state
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : degC
    #'            * name: NDays
    #'                          ** description : Number of days ...
    #'                          ** datatype : INT
    #'                          ** variablecategory : state
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : day
    #'            * name: TDL
    #'                          ** description : Total water content of soil at drained upper limit
    #'                          ** datatype : DOUBLE
    #'                          ** variablecategory : state
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : cm
    #'            * name: WetDay
    #'                          ** description : Wet Days
    #'                          ** datatype : INTARRAY
    #'                          ** variablecategory : state
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : day
    #'            * name: ST
    #'                          ** description : Soil temperature in soil layer NL
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** variablecategory : state
    #'                          ** len : NL
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : degC
    #'            * name: TMA
    #'                          ** description : Array of previous 5 days of average soil temperatures.
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** variablecategory : state
    #'                          ** len : 5
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** unit : degC
    TBD <- 0.0
    TLL <- 0.0
    TSW <- 0.0
    X2_PREV <- 0.0
    for( L in seq(1, NLAYR + 1-1, 1)){
        TBD <- TBD + (BD[(L - 1)+1] * DLAYR[(L - 1)+1])
        TDL <- TDL + (DUL[(L - 1)+1] * DLAYR[(L - 1)+1])
        TLL <- TLL + (LL[(L - 1)+1] * DLAYR[(L - 1)+1])
        TSW <- TSW + (SW[(L - 1)+1] * DLAYR[(L - 1)+1])
    }
    ABD <- TBD / DS[(NLAYR - 1)+1]
    FX <- ABD / (ABD + (686.0 * exp(-(5.63 * ABD))))
    DP <- 1000.0 + (2500.0 * FX)
    WW <- 0.356 - (0.144 * ABD)
    B <- log(500.0 / DP)
    if (ISWWAT == 'Y')
    {
        PESW <- max(0.0, TSW - TLL)
    }
    else
    {
        PESW <- max(0.0, TDL - TLL)
    }
    if (NDays == 30)
    {
        for( I in seq(1, 29 + 1-1, 1)){
            WetDay[I - 1+1] <- WetDay[I + 1 - 1+1]
        }
    }
    else
    {
        NDays <- NDays + 1
    }
    if (RAIN + DEPIR > 1.E-6)
    {
        WetDay[NDays - 1+1] <- 1
    }
    else
    {
        WetDay[NDays - 1+1] <- 0
    }
    NWetDays <- sum(WetDay)
    WFT <- as.double(NWetDays) / as.double(NDays)
    CV <- (BIOMAS + MULCHMASS) / 1000.
    BCV1 <- CV / (CV + exp(5.3396 - (2.3951 * CV)))
    BCV2 <- SNOW / (SNOW + exp(2.303 - (0.2197 * SNOW)))
    BCV <- max(BCV1, BCV2)
    list[TMA, X2_PREV, ST, SRFTEMP, X2_AVG] <- SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, WetDay[NDays - 1+1], WFT, WW, TMA, X2_PREV, ST)
    return (list ("SRFTEMP" = SRFTEMP,"NDays" = NDays,"TDL" = TDL,"WetDay" = WetDay,"ST" = ST,"TMA" = TMA))
}

SOILT_EPIC <- function (NL,
         B,
         BCV,
         CUMDPT,
         DP,
         DSMID,
         NLAYR,
         PESW,
         TAV,
         TAVG,
         TMAX,
         TMIN,
         WetDay,
         WFT,
         WW,
         TMA,
         X2_PREV,
         ST){
    LAG <- 0.5
    WC <- max(0.01, PESW) / (WW * CUMDPT) * 10.0
    FX <- exp(B * ((1.0 - WC) / (1.0 + WC)) ^ 2)
    DD <- FX * DP
    if (WetDay > 0)
    {
        X2 <- WFT * (TAVG - TMIN) + TMIN
    }
    else
    {
        X2 <- WFT * (TMAX - TAVG) + TAVG + 2.
    }
    TMA[1 - 1+1] <- X2
    for( K in seq(5, 2 - 1+1, -1)){
        TMA[K - 1+1] <- TMA[K - 1 - 1+1]
    }
    X2_AVG <- sum(TMA) / 5.0
    X3 <- (1. - BCV) * X2_AVG + (BCV * X2_PREV)
    SRFTEMP <- min(X2_AVG, X3)
    X1 <- TAV - X3
    for( L in seq(1, NLAYR + 1-1, 1)){
        ZD <- DSMID[(L - 1)+1] / DD
        F <- ZD / (ZD + exp(-.8669 - (2.0775 * ZD)))
        ST[L - 1+1] <- LAG * ST[(L - 1)+1] + ((1. - LAG) * (F * X1 + X3))
    }
    X2_PREV <- X2_AVG
    return (list ("TMA" = TMA,"X2_PREV" = X2_PREV,"ST" = ST,"SRFTEMP" = SRFTEMP,"X2_AVG" = X2_AVG))
}

init_stemp_epic <- function (NL,
         ISWWAT,
         BD,
         DLAYR,
         DS,
         DUL,
         LL,
         NLAYR,
         TAMP,
         RAIN,
         SW,
         TAVG,
         TMAX,
         TMIN,
         TAV,
         DEPIR,
         BIOMAS,
         MULCHMASS,
         SNOW){
    DSMID <- array(dim=c(NL,1,1))
    WetDay <- array(dim=c(NL,1,1))
    ST <- array(dim=c(NL,1,1))
    TMA <- array(dim=c(5,1,1))
    SWI <- array(dim=c(NL,1,1))
    SWI <- SW
    TBD <- 0.0
    TLL <- 0.0
    TSW <- 0.0
    TDL <- 0.0
    CUMDPT <- 0.0
    X2_PREV <- 0.0
    for( L in seq(1, NLAYR + 1-1, 1)){
        DSMID[L - 1+1] <- CUMDPT + (DLAYR[(L - 1)+1] * 5.0)
        CUMDPT <- CUMDPT + (DLAYR[(L - 1)+1] * 10.0)
        TBD <- TBD + (BD[(L - 1)+1] * DLAYR[(L - 1)+1])
        TLL <- TLL + (LL[(L - 1)+1] * DLAYR[(L - 1)+1])
        TSW <- TSW + (SWI[(L - 1)+1] * DLAYR[(L - 1)+1])
        TDL <- TDL + (DUL[(L - 1)+1] * DLAYR[(L - 1)+1])
    }
    if (ISWWAT == 'Y')
    {
        PESW <- max(0.0, TSW - TLL)
    }
    else
    {
        PESW <- max(0.0, TDL - TLL)
    }
    ABD <- TBD / DS[(NLAYR - 1)+1]
    FX <- ABD / (ABD + (686.0 * exp(-(5.63 * ABD))))
    DP <- 1000.0 + (2500.0 * FX)
    WW <- 0.356 - (0.144 * ABD)
    B <- log(500.0 / DP)
    for( I in seq(1, 5 + 1-1, 1)){
        TMA[I - 1+1] <- as.integer(TAVG * 10000.) / 10000.
    }
    X2_AVG <- TMA[(1 - 1)+1] * 5.0
    for( L in seq(1, NLAYR + 1-1, 1)){
        ST[L - 1+1] <- TAVG
    }
    WFT <- 0.1
    WetDay <-  array(c(0), dim=c(30,1,1))
    NDays <- 0
    CV <- MULCHMASS / 1000.
    BCV1 <- CV / (CV + exp(5.3396 - (2.3951 * CV)))
    BCV2 <- SNOW / (SNOW + exp(2.303 - (0.2197 * SNOW)))
    BCV <- max(BCV1, BCV2)
    for( I in seq(1, 8 + 1-1, 1)){
        list[TMA, X2_PREV, ST, SRFTEMP, X2_AVG] <- SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, 0, WFT, WW, TMA, X2_PREV, ST)
    }
    return (list ("CUMDPT" = CUMDPT,"DSMID" = DSMID,"SRFTEMP" = SRFTEMP,"NDays" = NDays,"TDL" = TDL,"WetDay" = WetDay,"ST" = ST,"TMA" = TMA))
}