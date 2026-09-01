import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;

public class SoilTemperatureCompExogenous
{
    private double tmin;
    private double tmax;
    private double globrad;
    private double soilCoverage;
    private double soilSurfaceTemperatureBelowSnow;
    private Boolean hasSnowCover;
    
    public SoilTemperatureCompExogenous() { }
    
    public SoilTemperatureCompExogenous(SoilTemperatureCompExogenous toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.tmin = toCopy.gettmin();
            this.tmax = toCopy.gettmax();
            this.globrad = toCopy.getglobrad();
            this.soilCoverage = toCopy.getsoilCoverage();
            this.soilSurfaceTemperatureBelowSnow = toCopy.getsoilSurfaceTemperatureBelowSnow();
            this.hasSnowCover = toCopy.gethasSnowCover();
        }
    }
    public double gettmin()
    { return tmin; }

    public void settmin(double _tmin)
    { this.tmin= _tmin; } 
    
    public double gettmax()
    { return tmax; }

    public void settmax(double _tmax)
    { this.tmax= _tmax; } 
    
    public double getglobrad()
    { return globrad; }

    public void setglobrad(double _globrad)
    { this.globrad= _globrad; } 
    
    public double getsoilCoverage()
    { return soilCoverage; }

    public void setsoilCoverage(double _soilCoverage)
    { this.soilCoverage= _soilCoverage; } 
    
    public double getsoilSurfaceTemperatureBelowSnow()
    { return soilSurfaceTemperatureBelowSnow; }

    public void setsoilSurfaceTemperatureBelowSnow(double _soilSurfaceTemperatureBelowSnow)
    { this.soilSurfaceTemperatureBelowSnow= _soilSurfaceTemperatureBelowSnow; } 
    
    public Boolean gethasSnowCover()
    { return hasSnowCover; }

    public void sethasSnowCover(Boolean _hasSnowCover)
    { this.hasSnowCover= _hasSnowCover; } 
    
}