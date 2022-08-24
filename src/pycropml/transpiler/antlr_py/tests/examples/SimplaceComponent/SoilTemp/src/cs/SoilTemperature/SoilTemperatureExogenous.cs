using System;
using System.Collections.Generic;

public class SoilTemperatureExogenous 
{
    private double _iAirTemperatureMax;
    private double _iAirTemperatureMin;
    private double _iGlobalSolarRadiation;
    private double _iRAIN;
    private double _iCropResidues;
    private double _iPotentialSoilEvaporation;
    private double _iLeafAreaIndex;
    private double[] _SoilTempArray = new double[];
    private double _iSoilWaterContent;
    private double _iSoilSurfaceTemperature;
    
    public SoilTemperatureExogenous() { }
    
    
    public SoilTemperatureExogenous(SoilTemperatureExogenous toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _iAirTemperatureMax = toCopy._iAirTemperatureMax;
    _iAirTemperatureMin = toCopy._iAirTemperatureMin;
    _iGlobalSolarRadiation = toCopy._iGlobalSolarRadiation;
    _iRAIN = toCopy._iRAIN;
    _iCropResidues = toCopy._iCropResidues;
    _iPotentialSoilEvaporation = toCopy._iPotentialSoilEvaporation;
    _iLeafAreaIndex = toCopy._iLeafAreaIndex;
    SoilTempArray = new double[];
            for (int i = 0; i < ; i++)
            { _SoilTempArray[i] = toCopy._SoilTempArray[i]; }
    
    _iSoilWaterContent = toCopy._iSoilWaterContent;
    _iSoilSurfaceTemperature = toCopy._iSoilSurfaceTemperature;
    }
    }
    public double iAirTemperatureMax
        {
            get { return this._iAirTemperatureMax; }
            set { this._iAirTemperatureMax= value; } 
        }
    public double iAirTemperatureMin
        {
            get { return this._iAirTemperatureMin; }
            set { this._iAirTemperatureMin= value; } 
        }
    public double iGlobalSolarRadiation
        {
            get { return this._iGlobalSolarRadiation; }
            set { this._iGlobalSolarRadiation= value; } 
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