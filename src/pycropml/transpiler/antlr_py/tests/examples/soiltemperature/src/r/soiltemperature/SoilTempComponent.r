library(gsubfn)
library (gsubfn) 
setwd('C:/Users/midingoy/Documents/pycropml_pheno/src/pycropml/transpiler/antlr_py/tests/examples/soiltemperature/src/r')
source('Stemp_epic.r')

model_soiltemp <- function (BD,
         SRFTEMP,
         TMA,
         DEPIR,
         BIOMAS,
         TDL,
         NL,
         TAMP,
         MULCHMASS,
         TMAX,
         SNOW,
         RAIN,
         NLAYR,
         TAV,
         TAVG,
         TMIN,
         SW,
         ST,
         DS,
         DLAYR,
         CUMDPT,
         NDays,
         ISWWAT,
         DUL,
         WetDay,
         DSMID,
         LL){
    #'- Name: SoilTemp -Version: 001, -Time step: 1
    #'- Description:
    #'            * Title: SoilTemp model
    #'            * Author: Cyrille
    #'            * Reference: ('http://ooooo.html',)
    #'            * Institution: INRAE
    #'            * ExtendedDescription: I don't know
    #'            * ShortDescription: None
    #'- inputs:
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
    #'            * name: SRFTEMP
    #'                          ** description : Temperature of soil surface litter
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
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
    #'            * name: TDL
    #'                          ** description : Total water content of soil at drained upper limit
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : cm
    #'            * name: NL
    #'                          ** description : Number of soil layers
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
    #'            * name: MULCHMASS
    #'                          ** description : Mulch Mass
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : kg/ha
    #'            * name: TMAX
    #'                          ** description : Maximum daily temperature
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: SNOW
    #'                          ** description : Snow cover
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : mm
    #'            * name: RAIN
    #'                          ** description : daily rainfall
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : mm
    #'            * name: NLAYR
    #'                          ** description : Actual number of soil layers
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : dimensionless
    #'            * name: TAV
    #'                          ** description : Average annual soil temperature, used with TAMP to calculate soil temperature.
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : degC
    #'            * name: TAVG
    #'                          ** description : Average daily temperature
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
    #'            * name: CUMDPT
    #'                          ** description : Cumulative depth of soil profile
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLE
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : mm
    #'            * name: NDays
    #'                          ** description : Number of days ...
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : INT
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : 
    #'                          ** unit : day
    #'            * name: ISWWAT
    #'                          ** description : Water simulation control switch (Y or N)
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : STRING
    #'                          ** max : 
    #'                          ** min : 
    #'                          ** default : Y
    #'                          ** unit : dimensionless
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
    list[SRFTEMP, NDays, TDL, WetDay, ST, TMA] <- model_stemp_epic(NL, ISWWAT, BD, DLAYR, DS, DUL, LL, NLAYR, TAMP, RAIN, CUMDPT, DSMID, SW, TAVG, TMAX, TMIN, TAV, SRFTEMP, NDays, TDL, WetDay, ST, TMA, DEPIR, BIOMAS, MULCHMASS, SNOW)
    return (list ("SRFTEMP" = SRFTEMP,"NDays" = NDays,"TDL" = TDL,"WetDay" = WetDay,"ST" = ST,"TMA" = TMA))
}