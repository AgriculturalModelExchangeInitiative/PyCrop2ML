using System;
using System.Collections.Generic;
using System.Linq;
class SoilTemperatureCompWrapper
{
    private SoilTemperatureCompState s;
    private SoilTemperatureCompState s1;
    private SoilTemperatureCompRate r;
    private SoilTemperatureCompAuxiliary a;
    private SoilTemperatureCompExogenous ex;
    private SoilTemperatureCompComponent soiltemperaturecompComponent;

    public SoilTemperatureCompWrapper()
    {
        s = new SoilTemperatureCompState();
        r = new SoilTemperatureCompRate();
        a = new SoilTemperatureCompAuxiliary();
        ex = new SoilTemperatureCompExogenous();
        soiltemperaturecompComponent = new SoilTemperatureCompComponent();
        loadParameters();
    }

        double dampingFactor;
    double timeStep;
    double[] soilMoistureConst =  new double [100];
    double baseTemp;
    double initialSurfaceTemp;
    double densityAir;
    double specificHeatCapacityAir;
    double densityHumus;
    double specificHeatCapacityHumus;
    double densityWater;
    double specificHeatCapacityWater;
    double quartzRawDensity;
    double specificHeatCapacityQuartz;
    double nTau;
    int noOfTempLayers;
    int noOfTempLayersPlus1;
    int noOfSoilLayers;
    double[] layerThickness =  new double [100];
    double[] soilBulkDensity =  new double [100];
    double[] saturation =  new double [100];
    double[] soilOrganicMatter =  new double [100];

    public double soilSurfaceTemperature{ get { return s.soilSurfaceTemperature;}} 
     
    public double[] soilTemperature{ get { return s.soilTemperature;}} 
     

    public SoilTemperatureCompWrapper(SoilTemperatureCompWrapper toCopy, bool copyAll) : this()
    {
        s = (toCopy.s != null) ? new SoilTemperatureCompState(toCopy.s, copyAll) : null;
        r = (toCopy.r != null) ? new SoilTemperatureCompRate(toCopy.r, copyAll) : null;
        a = (toCopy.a != null) ? new SoilTemperatureCompAuxiliary(toCopy.a, copyAll) : null;
        ex = (toCopy.ex != null) ? new SoilTemperatureCompExogenous(toCopy.ex, copyAll) : null;
        if (copyAll)
        {
            soiltemperaturecompComponent = (toCopy.soiltemperaturecompComponent != null) ? new SoilTemperatureCompComponent(toCopy.soiltemperaturecompComponent) : null;
        }
    }

    public void Init(){
        soiltemperaturecompComponent.Init(s, r, a);
        loadParameters();
    }

    private void loadParameters()
    {
        soiltemperaturecompComponent.dampingFactor = dampingFactor;
        soiltemperaturecompComponent.timeStep = timeStep;
        soiltemperaturecompComponent.soilMoistureConst = soilMoistureConst;
        soiltemperaturecompComponent.baseTemp = baseTemp;
        soiltemperaturecompComponent.initialSurfaceTemp = initialSurfaceTemp;
        soiltemperaturecompComponent.densityAir = densityAir;
        soiltemperaturecompComponent.specificHeatCapacityAir = specificHeatCapacityAir;
        soiltemperaturecompComponent.densityHumus = densityHumus;
        soiltemperaturecompComponent.specificHeatCapacityHumus = specificHeatCapacityHumus;
        soiltemperaturecompComponent.densityWater = densityWater;
        soiltemperaturecompComponent.specificHeatCapacityWater = specificHeatCapacityWater;
        soiltemperaturecompComponent.quartzRawDensity = quartzRawDensity;
        soiltemperaturecompComponent.specificHeatCapacityQuartz = specificHeatCapacityQuartz;
        soiltemperaturecompComponent.nTau = nTau;
        soiltemperaturecompComponent.noOfTempLayers = noOfTempLayers;
        soiltemperaturecompComponent.noOfTempLayersPlus1 = noOfTempLayersPlus1;
        soiltemperaturecompComponent.noOfSoilLayers = noOfSoilLayers;
        soiltemperaturecompComponent.layerThickness = layerThickness;
        soiltemperaturecompComponent.soilBulkDensity = soilBulkDensity;
        soiltemperaturecompComponent.saturation = saturation;
        soiltemperaturecompComponent.soilOrganicMatter = soilOrganicMatter;
    }

    public void EstimateSoilTemperatureComp(double tmin, double tmax, double globrad, double soilCoverage, double soilSurfaceTemperatureBelowSnow, bool hasSnowCover)
    {
        a.tmin = tmin;
        a.tmax = tmax;
        a.globrad = globrad;
        a.soilCoverage = soilCoverage;
        a.soilSurfaceTemperatureBelowSnow = soilSurfaceTemperatureBelowSnow;
        a.hasSnowCover = hasSnowCover;
        soiltemperaturecompComponent.CalculateModel(s,s1, r, a, ex);
    }

}