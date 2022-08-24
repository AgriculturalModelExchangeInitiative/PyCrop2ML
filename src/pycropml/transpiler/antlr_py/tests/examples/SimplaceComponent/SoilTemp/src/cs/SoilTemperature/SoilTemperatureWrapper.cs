using System;
using System.Collections.Generic;
using System.Linq;
class SoilTemperatureWrapper
{
    private SoilTemperatureState s;
    private SoilTemperatureRate r;
    private SoilTemperatureAuxiliary a;
    private SoilTemperatureExogenous ex;
    private SoilTemperatureComponent soiltemperatureComponent;

    public SoilTemperatureWrapper()
    {
        s = new SoilTemperatureState();
        r = new SoilTemperatureRate();
        a = new SoilTemperatureAuxiliary();
        ex = new SoilTemperatureExogenous();
        soiltemperatureComponent = new SoilTemperatureComponent();
        loadParameters();
    }

        double cCarbonContent;
    double[] cSoilLayerDepth =  new double [100];
    double cFirstDayMeanTemp;
    double cAverageGroundTemperature;
    double cAverageBulkDensity;
    double cDampingDepth;

    public double SoilSurfaceTemperature{ get { return s.SoilSurfaceTemperature;}} 
     
    public double SnowWaterContent{ get { return s.SnowWaterContent;}} 
     
    public double SnowIsolationIndex{ get { return a.SnowIsolationIndex;}} 
     
    public double[] SoilTempArray{ get { return ex.SoilTempArray;}} 
     

    public SoilTemperatureWrapper(SoilTemperatureWrapper toCopy, bool copyAll) : this()
    {
        s = (toCopy.s != null) ? new SoilTemperatureState(toCopy.s, copyAll) : null;
        r = (toCopy.r != null) ? new SoilTemperatureRate(toCopy.r, copyAll) : null;
        a = (toCopy.a != null) ? new SoilTemperatureAuxiliary(toCopy.a, copyAll) : null;
        ex = (toCopy.ex != null) ? new SoilTemperatureExogenous(toCopy.ex, copyAll) : null;
        if (copyAll)
        {
            soiltemperatureComponent = (toCopy.soiltemperatureComponent != null) ? new SoilTemperatureComponent(toCopy.soiltemperatureComponent) : null;
        }
    }

    public void Init(){
        soiltemperatureComponent.Init(s, r, a);
        loadParameters();
    }

    private void loadParameters()
    {
        soiltemperatureComponent.cCarbonContent = cCarbonContent;
        soiltemperatureComponent.cSoilLayerDepth = cSoilLayerDepth;
        soiltemperatureComponent.cFirstDayMeanTemp = cFirstDayMeanTemp;
        soiltemperatureComponent.cAverageGroundTemperature = cAverageGroundTemperature;
        soiltemperatureComponent.cAverageBulkDensity = cAverageBulkDensity;
        soiltemperatureComponent.cDampingDepth = cDampingDepth;
    }

    public void EstimateSoilTemperature(double SnowIsolationIndex, double iAirTemperatureMax, double iAirTemperatureMin, double iGlobalSolarRadiation, double iRAIN, double iCropResidues, double iPotentialSoilEvaporation, double iLeafAreaIndex, double[] SoilTempArray, double iSoilWaterContent, double iSoilSurfaceTemperature)
    {
        a.SnowIsolationIndex = SnowIsolationIndex;
        a.iAirTemperatureMax = iAirTemperatureMax;
        a.iAirTemperatureMin = iAirTemperatureMin;
        a.iGlobalSolarRadiation = iGlobalSolarRadiation;
        a.iRAIN = iRAIN;
        a.iCropResidues = iCropResidues;
        a.iPotentialSoilEvaporation = iPotentialSoilEvaporation;
        a.iLeafAreaIndex = iLeafAreaIndex;
        a.SoilTempArray = SoilTempArray;
        a.iSoilWaterContent = iSoilWaterContent;
        a.iSoilSurfaceTemperature = iSoilSurfaceTemperature;
        soiltemperatureComponent.CalculateModel(s,s1, r, a, ex);
    }

}