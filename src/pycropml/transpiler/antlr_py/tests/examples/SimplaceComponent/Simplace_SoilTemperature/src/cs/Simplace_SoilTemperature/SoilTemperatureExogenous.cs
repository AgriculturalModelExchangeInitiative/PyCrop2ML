using System;
using System.Collections.Generic;

public class SoilTemperatureExogenous 
{
    private double _iAirTemperatureMax;
    private double _iTempMax;
    private double _iAirTemperatureMin;
    private double _iTempMin;
    private double _iGlobalSolarRadiation;
    private double _iRadiation;
    private double _iRAIN;
    private double _iCropResidues;
    private double _iPotentialSoilEvaporation;
    private double _iLeafAreaIndex;
    private double[] _SoilTempArray;
    private double[] _iSoilTempArray;
    private double _iSoilWaterContent;
    private double _iSoilSurfaceTemperature;
    
    public SoilTemperatureExogenous() { }
    
    
    public SoilTemperatureExogenous(SoilTemperatureExogenous toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _iAirTemperatureMax = toCopy._iAirTemperatureMax;
    _iTempMax = toCopy._iTempMax;
    _iAirTemperatureMin = toCopy._iAirTemperatureMin;
    _iTempMin = toCopy._iTempMin;
    _iGlobalSolarRadiation = toCopy._iGlobalSolarRadiation;
    _iRadiation = toCopy._iRadiation;
    _iRAIN = toCopy._iRAIN;
    _iCropResidues = toCopy._iCropResidues;
    _iPotentialSoilEvaporation = toCopy._iPotentialSoilEvaporation;
    _iLeafAreaIndex = toCopy._iLeafAreaIndex;
    SoilTempArray = new double[toCopy._SoilTempArray.Length];
            for (int i = 0; i < toCopy._SoilTempArray.Length; i++)
            { _SoilTempArray[i] = toCopy._SoilTempArray[i]; }
    
    iSoilTempArray = new double[toCopy._iSoilTempArray.Length];
            for (int i = 0; i < toCopy._iSoilTempArray.Length; i++)
            { _iSoilTempArray[i] = toCopy._iSoilTempArray[i]; }
    
    _iSoilWaterContent = toCopy._iSoilWaterContent;
    _iSoilSurfaceTemperature = toCopy._iSoilSurfaceTemperature;
    }
    }
    public double iAirTemperatureMax
        {
            get { return this._iAirTemperatureMax; }
            set { this._iAirTemperatureMax= value; } 
        }
    public double iTempMax
        {
            get { return this._iTempMax; }
            set { this._iTempMax= value; } 
        }
    public double iAirTemperatureMin
        {
            get { return this._iAirTemperatureMin; }
            set { this._iAirTemperatureMin= value; } 
        }
    public double iTempMin
        {
            get { return this._iTempMin; }
            set { this._iTempMin= value; } 
        }
    public double iGlobalSolarRadiation
        {
            get { return this._iGlobalSolarRadiation; }
            set { this._iGlobalSolarRadiation= value; } 
        }
    public double iRadiation
        {
            get { return this._iRadiation; }
            set { this._iRadiation= value; } 
        }
    public double iRAIN
        {
            get { return this._iRAIN; }
            set { this._iRAIN= value; } 
        }
    public double iCropResidues
        {
            get { return this._iCropResidues; }
            set { this._iCropResidues= value; } 
        }
    public double iPotentialSoilEvaporation
        {
            get { return this._iPotentialSoilEvaporation; }
            set { this._iPotentialSoilEvaporation= value; } 
        }
    public double iLeafAreaIndex
        {
            get { return this._iLeafAreaIndex; }
            set { this._iLeafAreaIndex= value; } 
        }
    public double[] SoilTempArray
        {
            get { return this._SoilTempArray; }
            set { this._SoilTempArray= value; } 
        }
    public double[] iSoilTempArray
        {
            get { return this._iSoilTempArray; }
            set { this._iSoilTempArray= value; } 
        }
    public double iSoilWaterContent
        {
            get { return this._iSoilWaterContent; }
            set { this._iSoilWaterContent= value; } 
        }
    public double iSoilSurfaceTemperature
        {
            get { return this._iSoilSurfaceTemperature; }
            set { this._iSoilSurfaceTemperature= value; } 
        }
}