public class SoilTemperatureComponent
{
    
    public SoilTemperatureComponent() { }

    SnowCoverCalculator _SnowCoverCalculator = new SnowCoverCalculator();
    STMPsimCalculator _STMPsimCalculator = new STMPsimCalculator();

    public Double getcCarbonContent()
    { return _Snowcovercalculator.getcCarbonContent(); }
    public void setcCarbonContent(Double cCarbonContent)
    { _Snowcovercalculator.setcCarbonContent(cCarbonContent); } 

    public Double [] getcSoilLayerDepth()
    { return _Stmpsimcalculator.getcSoilLayerDepth(); }
    public void setcSoilLayerDepth(Double [] cSoilLayerDepth)
    { _Stmpsimcalculator.setcSoilLayerDepth(cSoilLayerDepth); } 

    public Double getcFirstDayMeanTemp()
    { return _Stmpsimcalculator.getcFirstDayMeanTemp(); }
    public void setcFirstDayMeanTemp(Double cFirstDayMeanTemp)
    { _Stmpsimcalculator.setcFirstDayMeanTemp(cFirstDayMeanTemp); } 

    public Double getcAverageGroundTemperature()
    { return _Stmpsimcalculator.getcAverageGroundTemperature(); }
    public void setcAverageGroundTemperature(Double cAverageGroundTemperature)
    { _Stmpsimcalculator.setcAverageGroundTemperature(cAverageGroundTemperature); } 

    public Double getcAVT()
    { return _Stmpsimcalculator.getcAVT(); }
    public void setcAVT(Double cAVT)
    { _Stmpsimcalculator.setcAVT(cAVT); } 

    public Double getcAverageBulkDensity()
    { return _Stmpsimcalculator.getcAverageBulkDensity(); }
    public void setcAverageBulkDensity(Double cAverageBulkDensity)
    { _Stmpsimcalculator.setcAverageBulkDensity(cAverageBulkDensity); } 

    public Double getcABD()
    { return _Stmpsimcalculator.getcABD(); }
    public void setcABD(Double cABD)
    { _Stmpsimcalculator.setcABD(cABD); } 

    public Double getcDampingDepth()
    { return _Stmpsimcalculator.getcDampingDepth(); }
    public void setcDampingDepth(Double cDampingDepth)
    { _Stmpsimcalculator.setcDampingDepth(cDampingDepth); } 
    public void  Calculate_soiltemperature(SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex)
    {
        iTempMax = iAirTemperatureMax;
        iTempMin = iAirTemperatureMin;
        iRadiation = iGlobalSolarRadiation;
        iSoilTempArray = SoilTempArray;
        cAVT = cAverageGroundTemperature;
        cABD = cAverageBulkDensity;
        _Snowcovercalculator.Calculate_snowcovercalculator(s, s1, r, a, ex);
        iSoilSurfaceTemperature = SoilSurfaceTemperature;
        _Stmpsimcalculator.Calculate_stmpsimcalculator(s, s1, r, a, ex);
    }
    private Double cCarbonContent;
    private Double [] cSoilLayerDepth;
    private Double cFirstDayMeanTemp;
    private Double cAverageGroundTemperature;
    private Double cAVT;
    private Double cAverageBulkDensity;
    private Double cABD;
    private Double cDampingDepth;
    public SoiltemperatureComponent(SoiltemperatureComponent toCopy) // copy constructor 
    {
        this.cCarbonContent = toCopy.getcCarbonContent();
        
        for (int i = 0; i < toCopy.getcSoilLayerDepth().length; i++)
        {
            cSoilLayerDepth[i] = toCopy.getcSoilLayerDepth()[i];
        }
        this.cFirstDayMeanTemp = toCopy.getcFirstDayMeanTemp();
        this.cAverageGroundTemperature = toCopy.getcAverageGroundTemperature();
        this.cAVT = toCopy.getcAVT();
        this.cAverageBulkDensity = toCopy.getcAverageBulkDensity();
        this.cABD = toCopy.getcABD();
        this.cDampingDepth = toCopy.getcDampingDepth();

    }
}