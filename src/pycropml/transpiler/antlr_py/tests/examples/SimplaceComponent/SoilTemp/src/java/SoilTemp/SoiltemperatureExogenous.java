import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;

public class SoiltemperatureExogenous
{
    private Double iAirTemperatureMax;
    private Double iAirTemperatureMin;
    private Double iGlobalSolarRadiation;
    private Double iRAIN;
    private Double iCropResidues;
    private Double iPotentialSoilEvaporation;
    private Double iLeafAreaIndex;
    private Double [] SoilTempArray;
    private Double iSoilWaterContent;
    private Double iSoilSurfaceTemperature;
    
    public SoiltemperatureExogenous() { }
    
    public SoiltemperatureExogenous(SoiltemperatureExogenous toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.iAirTemperatureMax = toCopy.getiAirTemperatureMax();
            this.iAirTemperatureMin = toCopy.getiAirTemperatureMin();
            this.iGlobalSolarRadiation = toCopy.getiGlobalSolarRadiation();
            this.iRAIN = toCopy.getiRAIN();
            this.iCropResidues = toCopy.getiCropResidues();
            this.iPotentialSoilEvaporation = toCopy.getiPotentialSoilEvaporation();
            this.iLeafAreaIndex = toCopy.getiLeafAreaIndex();
            SoilTempArray = new Double[toCopy.getSoilTempArray().length];
        for (int i = 0; i < toCopy.getSoilTempArray().length; i++)
        {
            SoilTempArray[i] = toCopy.getSoilTempArray()[i];
        }
            this.iSoilWaterContent = toCopy.getiSoilWaterContent();
            this.iSoilSurfaceTemperature = toCopy.getiSoilSurfaceTemperature();
        }
    }
    public Double getiAirTemperatureMax()
    { return iAirTemperatureMax; }

    public void setiAirTemperatureMax(Double _iAirTemperatureMax)
    { this.iAirTemperatureMax= _iAirTemperatureMax; } 
    
    public Double getiAirTemperatureMin()
    { return iAirTemperatureMin; }

    public void setiAirTemperatureMin(Double _iAirTemperatureMin)
    { this.iAirTemperatureMin= _iAirTemperatureMin; } 
    
    public Double getiGlobalSolarRadiation()
    { return iGlobalSolarRadiation; }

    public void setiGlobalSolarRadiation(Double _iGlobalSolarRadiation)
    { this.iGlobalSolarRadiation= _iGlobalSolarRadiation; } 
    
    public Double getiRAIN()
    { return iRAIN; }

    public void setiRAIN(Double _iRAIN)
    { this.iRAIN= _iRAIN; } 
    
    public Double getiCropResidues()
    { return iCropResidues; }

    public void setiCropResidues(Double _iCropResidues)
    { this.iCropResidues= _iCropResidues; } 
    
    public Double getiPotentialSoilEvaporation()
    { return iPotentialSoilEvaporation; }

    public void setiPotentialSoilEvaporation(Double _iPotentialSoilEvaporation)
    { this.iPotentialSoilEvaporation= _iPotentialSoilEvaporation; } 
    
    public Double getiLeafAreaIndex()
    { return iLeafAreaIndex; }

    public void setiLeafAreaIndex(Double _iLeafAreaIndex)
    { this.iLeafAreaIndex= _iLeafAreaIndex; } 
    
    public Double [] getSoilTempArray()
    { return SoilTempArray; }

    public void setSoilTempArray(Double [] _SoilTempArray)
    { this.SoilTempArray= _SoilTempArray; } 
    
    public Double getiSoilWaterContent()
    { return iSoilWaterContent; }

    public void setiSoilWaterContent(Double _iSoilWaterContent)
    { this.iSoilWaterContent= _iSoilWaterContent; } 
    
    public Double getiSoilSurfaceTemperature()
    { return iSoilSurfaceTemperature; }

    public void setiSoilSurfaceTemperature(Double _iSoilSurfaceTemperature)
    { this.iSoilSurfaceTemperature= _iSoilSurfaceTemperature; } 
    
}