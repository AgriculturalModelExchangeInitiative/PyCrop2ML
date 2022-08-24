using System;
using System.Collections.Generic;
public class SoilTemperatureState 
{
    private double _SoilSurfaceTemperature;
    private double _SnowWaterContent;
    
    public SoilTemperatureState() { }
    
    
    public SoilTemperatureState(SoilTemperatureState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _SoilSurfaceTemperature = toCopy._SoilSurfaceTemperature;
    _SnowWaterContent = toCopy._SnowWaterContent;
    }
    }
    public double SoilSurfaceTemperature
        {
            get { return this._SoilSurfaceTemperature; }
            set { this._SoilSurfaceTemperature= value; } 
        }
    public double SnowWaterContent
        {
            get { return this._SnowWaterContent; }
            set { this._SnowWaterContent= value; } 
        }
}