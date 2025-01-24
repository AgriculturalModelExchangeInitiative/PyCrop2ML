import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;
public class SoilTemperatureState
{
    private Double Albedo;
    private Double SnowWaterContent;
    private Double SoilSurfaceTemperature;
    private Integer AgeOfSnow;
    private Double [] pSoilLayerDepth;
    private Double [] SoilTempArray;
    
    public SoilTemperatureState() { }
    
    public SoilTemperatureState(SoilTemperatureState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.Albedo = toCopy.getAlbedo();
            this.SnowWaterContent = toCopy.getSnowWaterContent();
            this.SoilSurfaceTemperature = toCopy.getSoilSurfaceTemperature();
            this.AgeOfSnow = toCopy.getAgeOfSnow();
            pSoilLayerDepth = new Double[toCopy.getpSoilLayerDepth().length];
        for (int i = 0; i < toCopy.getpSoilLayerDepth().length; i++)
        {
            pSoilLayerDepth[i] = toCopy.getpSoilLayerDepth()[i];
        }
            SoilTempArray = new Double[toCopy.getSoilTempArray().length];
        for (int i = 0; i < toCopy.getSoilTempArray().length; i++)
        {
            SoilTempArray[i] = toCopy.getSoilTempArray()[i];
        }
        }
    }
    public Double getAlbedo()
    { return Albedo; }

    public void setAlbedo(Double _Albedo)
    { this.Albedo= _Albedo; } 
    
    public Double getSnowWaterContent()
    { return SnowWaterContent; }

    public void setSnowWaterContent(Double _SnowWaterContent)
    { this.SnowWaterContent= _SnowWaterContent; } 
    
    public Double getSoilSurfaceTemperature()
    { return SoilSurfaceTemperature; }

    public void setSoilSurfaceTemperature(Double _SoilSurfaceTemperature)
    { this.SoilSurfaceTemperature= _SoilSurfaceTemperature; } 
    
    public Integer getAgeOfSnow()
    { return AgeOfSnow; }

    public void setAgeOfSnow(Integer _AgeOfSnow)
    { this.AgeOfSnow= _AgeOfSnow; } 
    
    public Double [] getpSoilLayerDepth()
    { return pSoilLayerDepth; }

    public void setpSoilLayerDepth(Double [] _pSoilLayerDepth)
    { this.pSoilLayerDepth= _pSoilLayerDepth; } 
    
    public Double [] getSoilTempArray()
    { return SoilTempArray; }

    public void setSoilTempArray(Double [] _SoilTempArray)
    { this.SoilTempArray= _SoilTempArray; } 
    
}