public class SoilTemperatureCompComponent
{
    
    public SoilTemperatureCompComponent() { }

    SoilTemperature _SoilTemperature = new SoilTemperature();
    NoSnowSoilSurfaceTemperature _NoSnowSoilSurfaceTemperature = new NoSnowSoilSurfaceTemperature();
    WithSnowSoilSurfaceTemperature _WithSnowSoilSurfaceTemperature = new WithSnowSoilSurfaceTemperature();

    public double getdampingFactor()
    { return _NoSnowSoilSurfaceTemperature.getdampingFactor(); }
    public void setdampingFactor(double _dampingFactor){
    _NoSnowSoilSurfaceTemperature.setdampingFactor(_dampingFactor);
    }

    public double gettimeStep()
    { return _SoilTemperature.gettimeStep(); }
    public void settimeStep(double _timeStep){
    _SoilTemperature.settimeStep(_timeStep);
    }

    public Double [] getsoilMoistureConst()
    { return _SoilTemperature.getsoilMoistureConst(); }
    public void setsoilMoistureConst(Double [] _soilMoistureConst){
    _SoilTemperature.setsoilMoistureConst(_soilMoistureConst);
    }

    public double getbaseTemp()
    { return _SoilTemperature.getbaseTemp(); }
    public void setbaseTemp(double _baseTemp){
    _SoilTemperature.setbaseTemp(_baseTemp);
    }

    public double getinitialSurfaceTemp()
    { return _SoilTemperature.getinitialSurfaceTemp(); }
    public void setinitialSurfaceTemp(double _initialSurfaceTemp){
    _SoilTemperature.setinitialSurfaceTemp(_initialSurfaceTemp);
    }

    public double getdensityAir()
    { return _SoilTemperature.getdensityAir(); }
    public void setdensityAir(double _densityAir){
    _SoilTemperature.setdensityAir(_densityAir);
    }

    public double getspecificHeatCapacityAir()
    { return _SoilTemperature.getspecificHeatCapacityAir(); }
    public void setspecificHeatCapacityAir(double _specificHeatCapacityAir){
    _SoilTemperature.setspecificHeatCapacityAir(_specificHeatCapacityAir);
    }

    public double getdensityHumus()
    { return _SoilTemperature.getdensityHumus(); }
    public void setdensityHumus(double _densityHumus){
    _SoilTemperature.setdensityHumus(_densityHumus);
    }

    public double getspecificHeatCapacityHumus()
    { return _SoilTemperature.getspecificHeatCapacityHumus(); }
    public void setspecificHeatCapacityHumus(double _specificHeatCapacityHumus){
    _SoilTemperature.setspecificHeatCapacityHumus(_specificHeatCapacityHumus);
    }

    public double getdensityWater()
    { return _SoilTemperature.getdensityWater(); }
    public void setdensityWater(double _densityWater){
    _SoilTemperature.setdensityWater(_densityWater);
    }

    public double getspecificHeatCapacityWater()
    { return _SoilTemperature.getspecificHeatCapacityWater(); }
    public void setspecificHeatCapacityWater(double _specificHeatCapacityWater){
    _SoilTemperature.setspecificHeatCapacityWater(_specificHeatCapacityWater);
    }

    public double getquartzRawDensity()
    { return _SoilTemperature.getquartzRawDensity(); }
    public void setquartzRawDensity(double _quartzRawDensity){
    _SoilTemperature.setquartzRawDensity(_quartzRawDensity);
    }

    public double getspecificHeatCapacityQuartz()
    { return _SoilTemperature.getspecificHeatCapacityQuartz(); }
    public void setspecificHeatCapacityQuartz(double _specificHeatCapacityQuartz){
    _SoilTemperature.setspecificHeatCapacityQuartz(_specificHeatCapacityQuartz);
    }

    public double getnTau()
    { return _SoilTemperature.getnTau(); }
    public void setnTau(double _nTau){
    _SoilTemperature.setnTau(_nTau);
    }

    public Integer getnoOfTempLayers()
    { return _SoilTemperature.getnoOfTempLayers(); }
    public void setnoOfTempLayers(Integer _noOfTempLayers){
    _SoilTemperature.setnoOfTempLayers(_noOfTempLayers);
    }

    public Integer getnoOfTempLayersPlus1()
    { return _SoilTemperature.getnoOfTempLayersPlus1(); }
    public void setnoOfTempLayersPlus1(Integer _noOfTempLayersPlus1){
    _SoilTemperature.setnoOfTempLayersPlus1(_noOfTempLayersPlus1);
    }

    public Integer getnoOfSoilLayers()
    { return _SoilTemperature.getnoOfSoilLayers(); }
    public void setnoOfSoilLayers(Integer _noOfSoilLayers){
    _SoilTemperature.setnoOfSoilLayers(_noOfSoilLayers);
    }

    public Double [] getlayerThickness()
    { return _SoilTemperature.getlayerThickness(); }
    public void setlayerThickness(Double [] _layerThickness){
    _SoilTemperature.setlayerThickness(_layerThickness);
    }

    public Double [] getsoilBulkDensity()
    { return _SoilTemperature.getsoilBulkDensity(); }
    public void setsoilBulkDensity(Double [] _soilBulkDensity){
    _SoilTemperature.setsoilBulkDensity(_soilBulkDensity);
    }

    public Double [] getsaturation()
    { return _SoilTemperature.getsaturation(); }
    public void setsaturation(Double [] _saturation){
    _SoilTemperature.setsaturation(_saturation);
    }

    public Double [] getsoilOrganicMatter()
    { return _SoilTemperature.getsoilOrganicMatter(); }
    public void setsoilOrganicMatter(Double [] _soilOrganicMatter){
    _SoilTemperature.setsoilOrganicMatter(_soilOrganicMatter);
    }
    public void  Calculate_Model(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a, SoilTemperatureCompExogenous ex)
    {
        _NoSnowSoilSurfaceTemperature.Calculate_Model(s, s1, r, a, ex);
        s.setnoSnowSoilSurfaceTemperature(s.getsoilSurfaceTemperature());
        _WithSnowSoilSurfaceTemperature.Calculate_Model(s, s1, r, a, ex);
        _SoilTemperature.Calculate_Model(s, s1, r, a, ex);
    }
    private double dampingFactor;
    private double timeStep;
    private Double [] soilMoistureConst;
    private double baseTemp;
    private double initialSurfaceTemp;
    private double densityAir;
    private double specificHeatCapacityAir;
    private double densityHumus;
    private double specificHeatCapacityHumus;
    private double densityWater;
    private double specificHeatCapacityWater;
    private double quartzRawDensity;
    private double specificHeatCapacityQuartz;
    private double nTau;
    private Integer noOfTempLayers;
    private Integer noOfTempLayersPlus1;
    private Integer noOfSoilLayers;
    private Double [] layerThickness;
    private Double [] soilBulkDensity;
    private Double [] saturation;
    private Double [] soilOrganicMatter;
    public SoilTemperatureCompComponent(SoilTemperatureCompComponent toCopy) // copy constructor 
    {
        this.dampingFactor = toCopy.getdampingFactor();
        this.timeStep = toCopy.gettimeStep();
        
        for (int i = 0; i < toCopy.getsoilMoistureConst().length; i++)
        {
            soilMoistureConst[i] = toCopy.getsoilMoistureConst()[i];
        }
        this.baseTemp = toCopy.getbaseTemp();
        this.initialSurfaceTemp = toCopy.getinitialSurfaceTemp();
        this.densityAir = toCopy.getdensityAir();
        this.specificHeatCapacityAir = toCopy.getspecificHeatCapacityAir();
        this.densityHumus = toCopy.getdensityHumus();
        this.specificHeatCapacityHumus = toCopy.getspecificHeatCapacityHumus();
        this.densityWater = toCopy.getdensityWater();
        this.specificHeatCapacityWater = toCopy.getspecificHeatCapacityWater();
        this.quartzRawDensity = toCopy.getquartzRawDensity();
        this.specificHeatCapacityQuartz = toCopy.getspecificHeatCapacityQuartz();
        this.nTau = toCopy.getnTau();
        this.noOfTempLayers = toCopy.getnoOfTempLayers();
        this.noOfTempLayersPlus1 = toCopy.getnoOfTempLayersPlus1();
        this.noOfSoilLayers = toCopy.getnoOfSoilLayers();
        
        for (int i = 0; i < toCopy.getlayerThickness().length; i++)
        {
            layerThickness[i] = toCopy.getlayerThickness()[i];
        }
        
        for (int i = 0; i < toCopy.getsoilBulkDensity().length; i++)
        {
            soilBulkDensity[i] = toCopy.getsoilBulkDensity()[i];
        }
        
        for (int i = 0; i < toCopy.getsaturation().length; i++)
        {
            saturation[i] = toCopy.getsaturation()[i];
        }
        
        for (int i = 0; i < toCopy.getsoilOrganicMatter().length; i++)
        {
            soilOrganicMatter[i] = toCopy.getsoilOrganicMatter()[i];
        }

    }
}