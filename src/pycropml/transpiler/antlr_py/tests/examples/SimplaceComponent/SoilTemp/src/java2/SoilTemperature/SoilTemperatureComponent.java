
package SoilTemperature.src.java2.SoilTemperature;
public class SoilTemperatureComponent
{
    
    public SoilTemperatureComponent() { }

    Snowcovercalculator _Snowcovercalculator = new Snowcovercalculator();
    Stmpsimcalculator _Stmpsimcalculator = new Stmpsimcalculator();

    public double getcCarbonContent()
    { return _Snowcovercalculator.getcCarbonContent(); }
    public void setcCarbonContent(double cCarbonContent)
    { _Snowcovercalculator.setcCarbonContent(cCarbonContent); } 

    public Double [] getcSoilLayerDepth()
    { return _Stmpsimcalculator.getcSoilLayerDepth(); }
    public void setcSoilLayerDepth(Double [] cSoilLayerDepth)
    { _Stmpsimcalculator.setcSoilLayerDepth(cSoilLayerDepth); } 

    public double getcFirstDayMeanTemp()
    { return _Stmpsimcalculator.getcFirstDayMeanTemp(); }
    public void setcFirstDayMeanTemp(double cFirstDayMeanTemp)
    { _Stmpsimcalculator.setcFirstDayMeanTemp(cFirstDayMeanTemp); } 

    public double getcAverageGroundTemperature()
    { return _Stmpsimcalculator.getcAVT(); }

    public void setcAverageGroundTemperature(double cAverageGroundTemperature)
    { _Stmpsimcalculator.setcAVT(cAverageGroundTemperature); } 

    public double getcAverageBulkDensity()
    { return _Stmpsimcalculator.getcABD(); }
    public void setcAverageBulkDensity(double cAverageBulkDensity)
    { _Stmpsimcalculator.setcABD(cAverageBulkDensity); } 

    public double getcDampingDepth()
    { return _Stmpsimcalculator.getcDampingDepth(); }
    public void setcDampingDepth(double cDampingDepth)
    { _Stmpsimcalculator.setcDampingDepth(cDampingDepth); } 
    public void  Calculate_soiltemperature(SoiltemperatureState s, SoiltemperatureState s1, SoiltemperatureRate r, SoiltemperatureAuxiliary a, SoiltemperatureExogenous ex)
    {
        ex.setiTempMax(ex.getiAirTemperatureMax());
        ex.setiTempMin(ex.getiAirTemperatureMin());
        ex.setiRadiation(ex.getiGlobalSolarRadiation());
        _Snowcovercalculator.Calculate_snowcovercalculator(s, s1, r, a, ex);
        ex.setiSoilSurfaceTemperature(s.getSoilSurfaceTemperature());
        _Stmpsimcalculator.Calculate_stmpsimcalculator(s, s1, r, a, ex);
    }
    private double cCarbonContent;
    private Double [] cSoilLayerDepth;
    private double cFirstDayMeanTemp;
    private double cAverageGroundTemperature;
    private double cAverageBulkDensity;
    private double cDampingDepth;
    public SoilTemperatureComponent(SoilTemperatureComponent toCopy) // copy constructor 
    {
        this.cCarbonContent = toCopy.getcCarbonContent();
        
        for (int i = 0; i < toCopy.getcSoilLayerDepth().length; i++)
        {
            cSoilLayerDepth[i] = toCopy.getcSoilLayerDepth()[i];
        }
        this.cFirstDayMeanTemp = toCopy.getcFirstDayMeanTemp();
        this.cAverageGroundTemperature = toCopy.getcAverageGroundTemperature();
        this.cAverageBulkDensity = toCopy.getcAverageBulkDensity();
        this.cDampingDepth = toCopy.getcDampingDepth();

    }
}