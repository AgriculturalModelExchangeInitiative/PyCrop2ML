public class SoilTemperatureCompComponent
{
    
        public SoilTemperatureCompComponent() { }
    

    //Declaration of the associated strategies
    SoilTemperature _SoilTemperature = new SoilTemperature();
    NoSnowSoilSurfaceTemperature _NoSnowSoilSurfaceTemperature = new NoSnowSoilSurfaceTemperature();
    WithSnowSoilSurfaceTemperature _WithSnowSoilSurfaceTemperature = new WithSnowSoilSurfaceTemperature();

    public double dampingFactor
    {
        get
        {
             return _NoSnowSoilSurfaceTemperature.dampingFactor; 
        }
        set
        {
            _NoSnowSoilSurfaceTemperature.dampingFactor = value;
        }
    }
    public double timeStep
    {
        get
        {
             return _SoilTemperature.timeStep; 
        }
        set
        {
            _SoilTemperature.timeStep = value;
        }
    }
    public double[] soilMoistureConst
    {
        get
        {
             return _SoilTemperature.soilMoistureConst; 
        }
        set
        {
            _SoilTemperature.soilMoistureConst = value;
        }
    }
    public double baseTemp
    {
        get
        {
             return _SoilTemperature.baseTemp; 
        }
        set
        {
            _SoilTemperature.baseTemp = value;
        }
    }
    public double initialSurfaceTemp
    {
        get
        {
             return _SoilTemperature.initialSurfaceTemp; 
        }
        set
        {
            _SoilTemperature.initialSurfaceTemp = value;
        }
    }
    public double densityAir
    {
        get
        {
             return _SoilTemperature.densityAir; 
        }
        set
        {
            _SoilTemperature.densityAir = value;
        }
    }
    public double specificHeatCapacityAir
    {
        get
        {
             return _SoilTemperature.specificHeatCapacityAir; 
        }
        set
        {
            _SoilTemperature.specificHeatCapacityAir = value;
        }
    }
    public double densityHumus
    {
        get
        {
             return _SoilTemperature.densityHumus; 
        }
        set
        {
            _SoilTemperature.densityHumus = value;
        }
    }
    public double specificHeatCapacityHumus
    {
        get
        {
             return _SoilTemperature.specificHeatCapacityHumus; 
        }
        set
        {
            _SoilTemperature.specificHeatCapacityHumus = value;
        }
    }
    public double densityWater
    {
        get
        {
             return _SoilTemperature.densityWater; 
        }
        set
        {
            _SoilTemperature.densityWater = value;
        }
    }
    public double specificHeatCapacityWater
    {
        get
        {
             return _SoilTemperature.specificHeatCapacityWater; 
        }
        set
        {
            _SoilTemperature.specificHeatCapacityWater = value;
        }
    }
    public double quartzRawDensity
    {
        get
        {
             return _SoilTemperature.quartzRawDensity; 
        }
        set
        {
            _SoilTemperature.quartzRawDensity = value;
        }
    }
    public double specificHeatCapacityQuartz
    {
        get
        {
             return _SoilTemperature.specificHeatCapacityQuartz; 
        }
        set
        {
            _SoilTemperature.specificHeatCapacityQuartz = value;
        }
    }
    public double nTau
    {
        get
        {
             return _SoilTemperature.nTau; 
        }
        set
        {
            _SoilTemperature.nTau = value;
        }
    }
    public int noOfTempLayers
    {
        get
        {
             return _SoilTemperature.noOfTempLayers; 
        }
        set
        {
            _SoilTemperature.noOfTempLayers = value;
        }
    }
    public int noOfTempLayersPlus1
    {
        get
        {
             return _SoilTemperature.noOfTempLayersPlus1; 
        }
        set
        {
            _SoilTemperature.noOfTempLayersPlus1 = value;
        }
    }
    public int noOfSoilLayers
    {
        get
        {
             return _SoilTemperature.noOfSoilLayers; 
        }
        set
        {
            _SoilTemperature.noOfSoilLayers = value;
        }
    }
    public double[] layerThickness
    {
        get
        {
             return _SoilTemperature.layerThickness; 
        }
        set
        {
            _SoilTemperature.layerThickness = value;
        }
    }
    public double[] soilBulkDensity
    {
        get
        {
             return _SoilTemperature.soilBulkDensity; 
        }
        set
        {
            _SoilTemperature.soilBulkDensity = value;
        }
    }
    public double[] saturation
    {
        get
        {
             return _SoilTemperature.saturation; 
        }
        set
        {
            _SoilTemperature.saturation = value;
        }
    }
    public double[] soilOrganicMatter
    {
        get
        {
             return _SoilTemperature.soilOrganicMatter; 
        }
        set
        {
            _SoilTemperature.soilOrganicMatter = value;
        }
    }

    public void  CalculateModel(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a, SoilTemperatureCompExogenous ex)
    {
        _NoSnowSoilSurfaceTemperature.CalculateModel(s,s1, r, a, ex);
        s.noSnowSoilSurfaceTemperature = s.soilSurfaceTemperature;
        _WithSnowSoilSurfaceTemperature.CalculateModel(s,s1, r, a, ex);
        _SoilTemperature.CalculateModel(s,s1, r, a, ex);
    }
    
    public SoilTemperatureCompComponent(SoilTemperatureCompComponent toCopy): this() // copy constructor 
    {

        dampingFactor = toCopy.dampingFactor;
        timeStep = toCopy.timeStep;
        
            for (int i = 0; i < 100; i++)
            { soilMoistureConst[i] = toCopy.soilMoistureConst[i]; }
    
        baseTemp = toCopy.baseTemp;
        initialSurfaceTemp = toCopy.initialSurfaceTemp;
        densityAir = toCopy.densityAir;
        specificHeatCapacityAir = toCopy.specificHeatCapacityAir;
        densityHumus = toCopy.densityHumus;
        specificHeatCapacityHumus = toCopy.specificHeatCapacityHumus;
        densityWater = toCopy.densityWater;
        specificHeatCapacityWater = toCopy.specificHeatCapacityWater;
        quartzRawDensity = toCopy.quartzRawDensity;
        specificHeatCapacityQuartz = toCopy.specificHeatCapacityQuartz;
        nTau = toCopy.nTau;
        noOfTempLayers = toCopy.noOfTempLayers;
        noOfTempLayersPlus1 = toCopy.noOfTempLayersPlus1;
        noOfSoilLayers = toCopy.noOfSoilLayers;
        
            for (int i = 0; i < 100; i++)
            { layerThickness[i] = toCopy.layerThickness[i]; }
    
        
            for (int i = 0; i < 100; i++)
            { soilBulkDensity[i] = toCopy.soilBulkDensity[i]; }
    
        
            for (int i = 0; i < 100; i++)
            { saturation[i] = toCopy.saturation[i]; }
    
        
            for (int i = 0; i < 100; i++)
            { soilOrganicMatter[i] = toCopy.soilOrganicMatter[i]; }
    
    }
}