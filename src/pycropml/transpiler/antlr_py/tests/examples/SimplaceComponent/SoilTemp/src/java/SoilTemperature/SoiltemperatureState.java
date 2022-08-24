import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;
public class SoiltemperatureState
{
    private double SoilSurfaceTemperature;
    private double SnowWaterContent;
    
    public SoiltemperatureState() { }
    
    public SoiltemperatureState(SoiltemperatureState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SoilSurfaceTemperature = toCopy.getSoilSurfaceTemperature();
            this.SnowWaterContent = toCopy.getSnowWaterContent();
        }
    }
    public double getSoilSurfaceTemperature()
    { return SoilSurfaceTemperature; }

    public void setSoilSurfaceTemperature(double _SoilSurfaceTemperature)
    { this.SoilSurfaceTemperature= _SoilSurfaceTemperature; } 
    
    public double getSnowWaterContent()
    { return SnowWaterContent; }

    public void setSnowWaterContent(double _SnowWaterContent)
    { this.SnowWaterContent= _SnowWaterContent; } 
    
}