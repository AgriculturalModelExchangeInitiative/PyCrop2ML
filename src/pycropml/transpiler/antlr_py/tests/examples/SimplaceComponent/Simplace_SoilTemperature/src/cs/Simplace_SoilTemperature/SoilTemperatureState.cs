using System;
using System.Collections.Generic;
public class SoilTemperatureState 
{
    private double _Albedo;
    private double _SnowWaterContent;
    private double _SoilSurfaceTemperature;
    private int _AgeOfSnow;
    private double[] _pSoilLayerDepth;
    private double[] _SoilTempArray;
    
    public SoilTemperatureState() { }
    
    
    public SoilTemperatureState(SoilTemperatureState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _Albedo = toCopy._Albedo;
    _SnowWaterContent = toCopy._SnowWaterContent;
    _SoilSurfaceTemperature = toCopy._SoilSurfaceTemperature;
    _AgeOfSnow = toCopy._AgeOfSnow;
    pSoilLayerDepth = new double[toCopy._pSoilLayerDepth.Length];
            for (int i = 0; i < toCopy._pSoilLayerDepth.Length; i++)
            { _pSoilLayerDepth[i] = toCopy._pSoilLayerDepth[i]; }
    
    SoilTempArray = new double[toCopy._SoilTempArray.Length];
            for (int i = 0; i < toCopy._SoilTempArray.Length; i++)
            { _SoilTempArray[i] = toCopy._SoilTempArray[i]; }
    
    }
    }
    public double Albedo
        {
            get { return this._Albedo; }
            set { this._Albedo= value; } 
        }
    public double SnowWaterContent
        {
            get { return this._SnowWaterContent; }
            set { this._SnowWaterContent= value; } 
        }
    public double SoilSurfaceTemperature
        {
            get { return this._SoilSurfaceTemperature; }
            set { this._SoilSurfaceTemperature= value; } 
        }
    public int AgeOfSnow
        {
            get { return this._AgeOfSnow; }
            set { this._AgeOfSnow= value; } 
        }
    public double[] pSoilLayerDepth
        {
            get { return this._pSoilLayerDepth; }
            set { this._pSoilLayerDepth= value; } 
        }
    public double[] SoilTempArray
        {
            get { return this._SoilTempArray; }
            set { this._SoilTempArray= value; } 
        }
}