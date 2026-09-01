using System;
using System.Collections.Generic;
using System.Linq;    
using Models.Core;   
namespace Models.Crop2ML;

/// <summary>
///- Name: NoSnowSoilSurfaceTemperature -Version: 1, -Time step: 1
///- Description:
///            * Title: Soil surface temperature
///            * Authors: Michael Berg-Mohnicke
///            * Reference: None
///            * Institution: ZALF e.V.
///            * ExtendedDescription: None
///            * ShortDescription: It calculates the soil surface temperature without snow cover
///- inputs:
///            * name: tmin
///                          ** description : the days min air temperature
///                          ** inputtype : variable
///                          ** variablecategory : exogenous
///                          ** datatype : DOUBLE
///                          ** max : 70.0
///                          ** min : -50.0
///                          ** default : 
///                          ** unit : °C
///            * name: tmax
///                          ** description : the days max air temperature
///                          ** inputtype : variable
///                          ** variablecategory : exogenous
///                          ** datatype : DOUBLE
///                          ** max : 70.0
///                          ** min : -50.0
///                          ** default : 
///                          ** unit : °C
///            * name: globrad
///                          ** description : the days global radiation
///                          ** inputtype : variable
///                          ** variablecategory : exogenous
///                          ** datatype : DOUBLE
///                          ** max : 30.0
///                          ** min : 0.0
///                          ** default : 0.0
///                          ** unit : MJ/m**2/d
///            * name: soilCoverage
///                          ** description : soilCoverage
///                          ** inputtype : variable
///                          ** variablecategory : exogenous
///                          ** datatype : DOUBLE
///                          ** max : 
///                          ** min : 0.0
///                          ** default : 0.0
///                          ** unit : dimensionless
///            * name: dampingFactor
///                          ** description : dampingFactor
///                          ** inputtype : parameter
///                          ** parametercategory : constant
///                          ** datatype : DOUBLE
///                          ** max : 
///                          ** min : 
///                          ** default : 0.8
///                          ** unit : dimensionless
///            * name: soilSurfaceTemperature
///                          ** description : soilSurfaceTemperature of previous day
///                          ** inputtype : variable
///                          ** variablecategory : state
///                          ** datatype : DOUBLE
///                          ** max : 
///                          ** min : 
///                          ** default : 0.0
///                          ** unit : °C
///- outputs:
///            * name: soilSurfaceTemperature
///                          ** description : soilSurfaceTemperature
///                          ** variablecategory : state
///                          ** datatype : DOUBLE
///                          ** max : 
///                          ** min : 
///                          ** unit : °C
/// </summary>
public class NoSnowSoilSurfaceTemperature
{

    private double _dampingFactor;
    /// <summary>
    /// Gets and sets the dampingFactor
    /// </summary>
    [Description("dampingFactor")] 
    [Units("dimensionless")] 
    //[Crop2ML(datatype="DOUBLE", min=null, max=null, default=0.8, parametercategory=constant, inputtype="parameter")] 
    public double dampingFactor
    {
        get { return this._dampingFactor; }
        set { this._dampingFactor= value; } 
    }

    
    /// <summary>
    /// Constructor of the NoSnowSoilSurfaceTemperature component")
    /// </summary>  
    public NoSnowSoilSurfaceTemperature() { }
    
    /// <summary>
    /// Algorithm of the NoSnowSoilSurfaceTemperature component
    /// </summary>
    public void  CalculateModel(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a, SoilTemperatureCompExogenous ex)
    {
        double tmin = ex.tmin;
        double tmax = ex.tmax;
        double globrad = ex.globrad;
        double soilCoverage = ex.soilCoverage;
        double soilSurfaceTemperature = s.soilSurfaceTemperature;
        double shadingCoefficient;
        globrad = Math.Max(8.33, globrad);
        shadingCoefficient = 0.1 + (soilCoverage * dampingFactor + ((1 - soilCoverage) * (1 - dampingFactor)));
        soilSurfaceTemperature = (1.0 - shadingCoefficient) * (tmin + ((tmax - tmin) * Math.Pow(0.03 * globrad, 0.5))) + (shadingCoefficient * soilSurfaceTemperature);
        if (soilSurfaceTemperature < 0.0)
        {
            soilSurfaceTemperature = soilSurfaceTemperature * 0.5;
        }
        s.soilSurfaceTemperature= soilSurfaceTemperature;
    }
}