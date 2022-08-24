package SoilTemperature.src.java2.SoilTemperature;

public class SoiltemperatureExogenous
{
    private double iAirTemperatureMax;
    private double iAirTemperatureMin;
    private double iTempMax;
    private double iTempMin;
    private double iGlobalSolarRadiation;
    private double iRadiation;
    private double iRAIN;
    private double iCropResidues;
    private double iPotentialSoilEvaporation;
    private double iLeafAreaIndex;
    private Double [] iSoilTempArray;
    private double iSoilWaterContent;
    private double iSoilSurfaceTemperature;
    
    public SoiltemperatureExogenous() { }
    
    public SoiltemperatureExogenous(SoiltemperatureExogenous toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.iAirTemperatureMax = toCopy.getiAirTemperatureMax();
            this.iAirTemperatureMin = toCopy.getiAirTemperatureMin();
            this.iTempMax = toCopy.getiTempMax();
            this.iTempMin = toCopy.getiTempMin();
            this.iGlobalSolarRadiation = toCopy.getiGlobalSolarRadiation();
            this.iRadiation = toCopy.getiRadiation();
            this.iRAIN = toCopy.getiRAIN();
            this.iCropResidues = toCopy.getiCropResidues();
            this.iPotentialSoilEvaporation = toCopy.getiPotentialSoilEvaporation();
            this.iLeafAreaIndex = toCopy.getiLeafAreaIndex();
            iSoilTempArray = new Double[toCopy.getiSoilTempArray().length];
            for (int i = 0; i < toCopy.getiSoilTempArray().length; i++)
            {
                iSoilTempArray[i] = toCopy.getiSoilTempArray()[i];
            }
            this.iSoilWaterContent = toCopy.getiSoilWaterContent();
            this.iSoilSurfaceTemperature = toCopy.getiSoilSurfaceTemperature();
        }
    }
    public double getiAirTemperatureMax()
    { return iAirTemperatureMax; }

    public void setiAirTemperatureMax(double _iAirTemperatureMax)
    { this.iAirTemperatureMax= _iAirTemperatureMax; } 
    
    public double getiTempMax()
    { return iTempMax; }

    public void setiTempMax(double _iTempMax)
    { this.iTempMax= _iTempMax; } 
    
    
    public double getiAirTemperatureMin()
    { return iAirTemperatureMin; }

    public void setiAirTemperatureMin(double _iAirTemperatureMin)
    { this.iAirTemperatureMin= _iAirTemperatureMin; } 
    
    public double getiTempMin()
    { return iTempMin; }

    public void setiTempMin(double _iTempMin)
    { this.iTempMin= _iTempMin; }
    
    public double getiGlobalSolarRadiation()
    { return iGlobalSolarRadiation; }
    
    public double getiRadiation()
    { return iRadiation; }

    public void setiGlobalSolarRadiation(double _iGlobalSolarRadiation)
    { this.iGlobalSolarRadiation= _iGlobalSolarRadiation; } 
    
    public void setiRadiation(double _iRadiation)
    { this.iRadiation= _iRadiation; } 
    
    public double getiRAIN()
    { return iRAIN; }

    public void setiRAIN(double _iRAIN)
    { this.iRAIN= _iRAIN; } 
    
    public double getiCropResidues()
    { return iCropResidues; }

    public void setiCropResidues(double _iCropResidues)
    { this.iCropResidues= _iCropResidues; } 
    
    public double getiPotentialSoilEvaporation()
    { return iPotentialSoilEvaporation; }

    public void setiPotentialSoilEvaporation(double _iPotentialSoilEvaporation)
    { this.iPotentialSoilEvaporation= _iPotentialSoilEvaporation; } 
    
    public double getiLeafAreaIndex()
    { return iLeafAreaIndex; }

    public void setiLeafAreaIndex(double _iLeafAreaIndex)
    { this.iLeafAreaIndex= _iLeafAreaIndex; } 

    public Double [] getiSoilTempArray()
    { return iSoilTempArray; }

    public void setiSoilTempArray(Double [] _iSoilTempArray)
    { this.iSoilTempArray= _iSoilTempArray; } 
    
    
    public double getiSoilWaterContent()
    { return iSoilWaterContent; }

    public void setiSoilWaterContent(double _iSoilWaterContent)
    { this.iSoilWaterContent= _iSoilWaterContent; } 
    
    public double getiSoilSurfaceTemperature()
    { return iSoilSurfaceTemperature; }

    public void setiSoilSurfaceTemperature(double _iSoilSurfaceTemperature)
    { this.iSoilSurfaceTemperature= _iSoilSurfaceTemperature; } 
    
}