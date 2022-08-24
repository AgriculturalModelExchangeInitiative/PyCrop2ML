import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;
public class SoiltemperatureState
{
    private Double SoilSurfaceTemperature;
    private Double SnowWaterContent;
    
    public SoiltemperatureState() { }
    
    public SoiltemperatureState(SoiltemperatureState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SoilSurfaceTemperature = toCopy.getSoilSurfaceTemperature();
            this.SnowWaterContent = toCopy.getSnowWaterContent();
        }
    }
    public Double getSoilSurfaceTemperature()
    { return SoilSurfaceTemperature; }

    public void setSoilSurfaceTemperature(Double _SoilSurfaceTemperature)
    { this.SoilSurfaceTemperature= _SoilSurfaceTemperature; } 
    
    public Double getSnowWaterContent()
    { return SnowWaterContent; }

    public void setSnowWaterContent(Double _SnowWaterContent)
    { this.SnowWaterContent= _SnowWaterContent; } 
    
}