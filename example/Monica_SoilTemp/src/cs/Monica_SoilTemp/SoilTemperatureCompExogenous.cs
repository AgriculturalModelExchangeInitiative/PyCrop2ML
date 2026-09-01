using System;
using System.Collections.Generic;

public class SoilTemperatureCompExogenous 
{
    private double _tmin;
    private double _tmax;
    private double _globrad;
    private double _soilCoverage;
    private double _soilSurfaceTemperatureBelowSnow;
    private bool _hasSnowCover;
    
        public SoilTemperatureCompExogenous() { }
    
    
    public SoilTemperatureCompExogenous(SoilTemperatureCompExogenous toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    tmin = toCopy.tmin;
    tmax = toCopy.tmax;
    globrad = toCopy.globrad;
    soilCoverage = toCopy.soilCoverage;
    soilSurfaceTemperatureBelowSnow = toCopy.soilSurfaceTemperatureBelowSnow;
    hasSnowCover = toCopy.hasSnowCover;
    }
    }
    public double tmin
        {
            get { return this._tmin; }
            set { this._tmin= value; } 
        }
    public double tmax
        {
            get { return this._tmax; }
            set { this._tmax= value; } 
        }
    public double globrad
        {
            get { return this._globrad; }
            set { this._globrad= value; } 
        }
    public double soilCoverage
        {
            get { return this._soilCoverage; }
            set { this._soilCoverage= value; } 
        }
    public double soilSurfaceTemperatureBelowSnow
        {
            get { return this._soilSurfaceTemperatureBelowSnow; }
            set { this._soilSurfaceTemperatureBelowSnow= value; } 
        }
    public bool hasSnowCover
        {
            get { return this._hasSnowCover; }
            set { this._hasSnowCover= value; } 
        }
}