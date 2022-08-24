
package SoilTemperature.src.java2.SoilTemperature;

public class SoiltemperatureState
{
    private double SoilSurfaceTemperature;
    private double SnowWaterContent;
    private Double [] SoilTempArray;
    private int AgeOfSnow;
    private double Albedo;
    private Double[] pSoilLayerDepth;
    
    public SoiltemperatureState() { }
    
    public SoiltemperatureState(SoiltemperatureState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SoilSurfaceTemperature = toCopy.getSoilSurfaceTemperature();
            this.SnowWaterContent = toCopy.getSnowWaterContent();
            this.Albedo = toCopy.getAlbedo();
            this.AgeOfSnow = toCopy.getAgeOfSnow();
            SoilTempArray = new Double[toCopy.getSoilTempArray().length];
            for (int i = 0; i < toCopy.getSoilTempArray().length; i++)
            {
                SoilTempArray[i] = toCopy.getSoilTempArray()[i];
            }

            pSoilLayerDepth = new Double[toCopy.getpSoilLayerDepth().length];
            for (int i = 0; i < toCopy.getpSoilLayerDepth().length; i++)
            {
                pSoilLayerDepth[i] = toCopy.getpSoilLayerDepth()[i];
            }
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
    
    
    public double getAlbedo()
    { return Albedo; }

    public void setAlbedo(double _Albedo)
    { this.Albedo= _Albedo; } 
    
    public int getAgeOfSnow()
    { return AgeOfSnow; }

    public void setAgeOfSnow(int _AgeOfSnow)
    { this.AgeOfSnow= _AgeOfSnow; }
    
    

    public Double [] getSoilTempArray()
    { return SoilTempArray; }

    public void setSoilTempArray(Double [] _SoilTempArray)
    { this.SoilTempArray= _SoilTempArray; } 
    

    
    public Double [] getpSoilLayerDepth()
    { return pSoilLayerDepth; }

    public void setpSoilLayerDepth(Double [] _pSoilLayerDepth)
    { this.pSoilLayerDepth= _pSoilLayerDepth; } 
    
}