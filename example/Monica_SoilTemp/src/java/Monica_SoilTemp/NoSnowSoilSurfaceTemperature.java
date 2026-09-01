import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
public class NoSnowSoilSurfaceTemperature
{
    private double dampingFactor;
    public double getdampingFactor()
    { return dampingFactor; }

    public void setdampingFactor(double _dampingFactor)
    { this.dampingFactor= _dampingFactor; } 
    
    public NoSnowSoilSurfaceTemperature() { }
    public void  Calculate_Model(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a,  SoilTemperatureCompExogenous ex)
    {
        //- Name: NoSnowSoilSurfaceTemperature -Version: 1, -Time step: 1
        //- Description:
    //            * Title: Soil surface temperature
    //            * Authors: Michael Berg-Mohnicke
    //            * Reference: None
    //            * Institution: ZALF e.V.
    //            * ExtendedDescription: None
    //            * ShortDescription: It calculates the soil surface temperature without snow cover
        //- inputs:
    //            * name: tmin
    //                          ** description : the days min air temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 70.0
    //                          ** min : -50.0
    //                          ** default : 
    //                          ** unit : °C
    //            * name: tmax
    //                          ** description : the days max air temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 70.0
    //                          ** min : -50.0
    //                          ** default : 
    //                          ** unit : °C
    //            * name: globrad
    //                          ** description : the days global radiation
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 30.0
    //                          ** min : 0.0
    //                          ** default : 0.0
    //                          ** unit : MJ/m**2/d
    //            * name: soilCoverage
    //                          ** description : soilCoverage
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 0.0
    //                          ** default : 0.0
    //                          ** unit : dimensionless
    //            * name: dampingFactor
    //                          ** description : dampingFactor
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 0.8
    //                          ** unit : dimensionless
    //            * name: soilSurfaceTemperature
    //                          ** description : soilSurfaceTemperature of previous day
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 0.0
    //                          ** unit : °C
        //- outputs:
    //            * name: soilSurfaceTemperature
    //                          ** description : soilSurfaceTemperature
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : °C
        double tmin = ex.gettmin();
        double tmax = ex.gettmax();
        double globrad = ex.getglobrad();
        double soilCoverage = ex.getsoilCoverage();
        double soilSurfaceTemperature = s.getsoilSurfaceTemperature();
        double shadingCoefficient;
        globrad = Math.max(8.33d, globrad);
        shadingCoefficient = 0.1d + (soilCoverage * dampingFactor + ((1 - soilCoverage) * (1 - dampingFactor)));
        soilSurfaceTemperature = (1.0d - shadingCoefficient) * (tmin + ((tmax - tmin) * Math.pow(0.03d * globrad, 0.5d))) + (shadingCoefficient * soilSurfaceTemperature);
        if (soilSurfaceTemperature < 0.0d)
        {
            soilSurfaceTemperature = soilSurfaceTemperature * 0.5d;
        }
        s.setsoilSurfaceTemperature(soilSurfaceTemperature);
    }
}