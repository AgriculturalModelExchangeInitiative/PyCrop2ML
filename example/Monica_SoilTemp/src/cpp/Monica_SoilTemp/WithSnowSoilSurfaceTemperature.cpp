#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <array>
#include <map>
#include <tuple>
#include "WithSnowSoilSurfaceTemperature.h"
using namespace Monica_SoilTemp;
WithSnowSoilSurfaceTemperature::WithSnowSoilSurfaceTemperature() {}
void WithSnowSoilSurfaceTemperature::Calculate_Model(SoilTemperatureCompState &s, SoilTemperatureCompState &s1, SoilTemperatureCompRate &r, SoilTemperatureCompAuxiliary &a, SoilTemperatureCompExogenous &ex)
{
    //- Name: WithSnowSoilSurfaceTemperature -Version: 1, -Time step: 1
    //- Description:
    //            * Title: Soil surface temperature with potential snow cover
    //            * Authors: Michael Berg-Mohnicke
    //            * Reference: None
    //            * Institution: ZALF e.V.
    //            * ExtendedDescription: None
    //            * ShortDescription: It calculates the soil surface temperature taking a potential snow cover into account
    //        
    //- inputs:
    //            * name: noSnowSoilSurfaceTemperature
    //                          ** description : soilSurfaceTemperature without snow
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 0.0
    //                          ** unit : °C
    //            * name: soilSurfaceTemperatureBelowSnow
    //                          ** description : soilSurfaceTemperature below snow cover
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 0.0
    //                          ** unit : °C
    //            * name: hasSnowCover
    //                          ** description : is soil covered by snow
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : BOOLEAN
    //                          ** max : 
    //                          ** min : 
    //                          ** default : false
    //                          ** unit : dimensionless
    //- outputs:
    //            * name: soilSurfaceTemperature
    //                          ** description : soilSurfaceTemperature
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : °C
    if (ex.hasSnowCover)
    {
        s.soilSurfaceTemperature = ex.soilSurfaceTemperatureBelowSnow;
    }
    else
    {
        s.soilSurfaceTemperature = s.noSnowSoilSurfaceTemperature;
    }
}