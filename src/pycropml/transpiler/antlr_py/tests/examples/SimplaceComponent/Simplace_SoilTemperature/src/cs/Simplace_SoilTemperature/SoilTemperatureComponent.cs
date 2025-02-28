public class SoilTemperatureComponent
{
    
    public SoilTemperatureComponent() { }
    

    //Declaration of the associated strategies
    SnowCoverCalculator _SnowCoverCalculator = new SnowCoverCalculator();
    STMPsimCalculator _STMPsimCalculator = new STMPsimCalculator();

    public double cCarbonContent
    {
        get
        {
             return _SnowCoverCalculator.cCarbonContent; 
        }
        set
        {
            _SnowCoverCalculator.cCarbonContent = value;
        }
    }
    public double[] cSoilLayerDepth
    {
        get
        {
             return _STMPsimCalculator.cSoilLayerDepth; 
        }
        set
        {
            _STMPsimCalculator.cSoilLayerDepth = value;
        }
    }
    public double cFirstDayMeanTemp
    {
        get
        {
             return _STMPsimCalculator.cFirstDayMeanTemp; 
        }
        set
        {
            _STMPsimCalculator.cFirstDayMeanTemp = value;
        }
    }
    public double cAverageGroundTemperature
    {
        get
        {
             return _STMPsimCalculator.cAverageGroundTemperature; 
        }
        set
        {
            _STMPsimCalculator.cAverageGroundTemperature = value;
        }
    }
    public double cAVT
    {
        get
        {
             return _STMPsimCalculator.cAVT; 
        }
        set
        {
            _STMPsimCalculator.cAVT = value;
        }
    }
    public double cAverageBulkDensity
    {
        get
        {
             return _STMPsimCalculator.cAverageBulkDensity; 
        }
        set
        {
            _STMPsimCalculator.cAverageBulkDensity = value;
        }
    }
    public double cABD
    {
        get
        {
             return _STMPsimCalculator.cABD; 
        }
        set
        {
            _STMPsimCalculator.cABD = value;
        }
    }
    public double cDampingDepth
    {
        get
        {
             return _STMPsimCalculator.cDampingDepth; 
        }
        set
        {
            _STMPsimCalculator.cDampingDepth = value;
        }
    }

    public void  CalculateModel(SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex)
    {
        ex.iTempMax = ex.iAirTemperatureMax;
        ex.iTempMin = ex.iAirTemperatureMin;
        ex.iRadiation = ex.iGlobalSolarRadiation;
        ex.iSoilTempArray = s.SoilTempArray;
        cAVT = cAverageGroundTemperature;
        cABD = cAverageBulkDensity;
        _snowcovercalculator.CalculateModel(s,s1, r, a, ex);
        ex.iSoilSurfaceTemperature = s.SoilSurfaceTemperature;
        _stmpsimcalculator.CalculateModel(s,s1, r, a, ex);
    }
    
    public SoilTemperatureComponent(SoilTemperatureComponent toCopy): this() // copy constructor 
    {

        cCarbonContent = toCopy.cCarbonContent;
        
            for (int i = 0; i < 100; i++)
            { _cSoilLayerDepth[i] = toCopy._cSoilLayerDepth[i]; }
    
        cFirstDayMeanTemp = toCopy.cFirstDayMeanTemp;
        cAverageGroundTemperature = toCopy.cAverageGroundTemperature;
        cAVT = toCopy.cAVT;
        cAverageBulkDensity = toCopy.cAverageBulkDensity;
        cABD = toCopy.cABD;
        cDampingDepth = toCopy.cDampingDepth;
    }
}