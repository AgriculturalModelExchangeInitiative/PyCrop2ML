import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
public class WithSnowSoilSurfaceTemperature
{
    
    public WithSnowSoilSurfaceTemperature() { }
    public void  Calculate_Model(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a,  SoilTemperatureCompExogenous ex)
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
        double noSnowSoilSurfaceTemperature = s.getnoSnowSoilSurfaceTemperature();
        double soilSurfaceTemperatureBelowSnow = ex.getsoilSurfaceTemperatureBelowSnow();
        Boolean hasSnowCover = ex.gethasSnowCover();
        double soilSurfaceTemperature;
        if (hasSnowCover)
        {
            soilSurfaceTemperature = soilSurfaceTemperatureBelowSnow;
        }
        else
        {
            soilSurfaceTemperature = noSnowSoilSurfaceTemperature;
        }
        s.setsoilSurfaceTemperature(soilSurfaceTemperature);
    }
}