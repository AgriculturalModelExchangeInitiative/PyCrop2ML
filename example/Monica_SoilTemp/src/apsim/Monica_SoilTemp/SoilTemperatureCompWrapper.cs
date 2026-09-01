using APSIM.Shared.Utilities;
using Models.Climate;
using Models.Core;
using Models.Interfaces;
using Models.PMF;
using Models.Soils;
using Models.Surface;
using System;
using System.Collections.Generic;
using System.Linq;
namespace Models.Crop2ML;

/// <summary>
///  This class encapsulates the SoilTemperatureCompComponent
/// </summary>
[Serializable]
[PresenterName("UserInterface.Presenters.PropertyPresenter")]
[ViewName("UserInterface.Views.PropertyView")]
[ValidParent(ParentType = typeof(Zone))]
class SoilTemperatureCompWrapper :  Model
{
    [Link] Clock clock = null;
    //[Link] Weather weather = null; // other links

    private SoilTemperatureCompState s;
    private SoilTemperatureCompState s1;
    private SoilTemperatureCompRate r;
    private SoilTemperatureCompAuxiliary a;
    private SoilTemperatureCompExogenous ex;
    private SoilTemperatureCompComponent soiltemperaturecompComponent;

    /// <summary>
    ///  The constructor of the Wrapper of the SoilTemperatureCompComponent
    /// </summary>
    public SoilTemperatureCompWrapper()
    {
        s = new SoilTemperatureCompState();
        s1 = new SoilTemperatureCompState();
        r = new SoilTemperatureCompRate();
        a = new SoilTemperatureCompAuxiliary();
        ex = new SoilTemperatureCompExogenous();
        soiltemperaturecompComponent = new SoilTemperatureCompComponent();
    }

    /// <summary>
    ///  The get method of the soilSurfaceTemperature output variable
    /// </summary>
    [Description("soilSurfaceTemperature")]
    [Units("°C")]
    public double soilSurfaceTemperature{ get { return s.soilSurfaceTemperature;}} 
     

    /// <summary>
    ///  The get method of the soilTemperature next day output variable
    /// </summary>
    [Description("soilTemperature next day")]
    [Units("°C")]
    public double[] soilTemperature{ get { return s.soilTemperature;}} 
     

    /// <summary>
    ///  The Constructor copy of the wrapper of the SoilTemperatureCompComponent
    /// </summary>
    /// <param name="toCopy"></param>
    /// <param name="copyAll"></param>
    public SoilTemperatureCompWrapper(SoilTemperatureCompWrapper toCopy, bool copyAll) 
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

    /// <summary>
    ///  The Initialization method of the wrapper of the SoilTemperatureCompComponent
    /// </summary>
    public void Init(){
        setExogenous();
        loadParameters();
        soiltemperaturecompComponent.Init(s, s1, r, a, ex);
    }

    /// <summary>
    ///  Load parameters of the wrapper of the SoilTemperatureCompComponent
    /// </summary>
    private void loadParameters()
    {
        soiltemperaturecompComponent.dampingFactor = null; // To be modified
        soiltemperaturecompComponent.timeStep = null; // To be modified
        soiltemperaturecompComponent.soilMoistureConst = null; // To be modified
        soiltemperaturecompComponent.baseTemp = null; // To be modified
        soiltemperaturecompComponent.initialSurfaceTemp = null; // To be modified
        soiltemperaturecompComponent.densityAir = null; // To be modified
        soiltemperaturecompComponent.specificHeatCapacityAir = null; // To be modified
        soiltemperaturecompComponent.densityHumus = null; // To be modified
        soiltemperaturecompComponent.specificHeatCapacityHumus = null; // To be modified
        soiltemperaturecompComponent.densityWater = null; // To be modified
        soiltemperaturecompComponent.specificHeatCapacityWater = null; // To be modified
        soiltemperaturecompComponent.quartzRawDensity = null; // To be modified
        soiltemperaturecompComponent.specificHeatCapacityQuartz = null; // To be modified
        soiltemperaturecompComponent.nTau = null; // To be modified
        soiltemperaturecompComponent.noOfTempLayers = null; // To be modified
        soiltemperaturecompComponent.noOfTempLayersPlus1 = null; // To be modified
        soiltemperaturecompComponent.noOfSoilLayers = null; // To be modified
        soiltemperaturecompComponent.layerThickness = null; // To be modified
        soiltemperaturecompComponent.soilBulkDensity = null; // To be modified
        soiltemperaturecompComponent.saturation = null; // To be modified
        soiltemperaturecompComponent.soilOrganicMatter = null; // To be modified
    }

    /// <summary>
    ///  Set exogenous variables of the wrapper of the SoilTemperatureCompComponent
    /// </summary>
    private void setExogenous()
    {
        ex.tmin = null; // To be modified
        ex.tmax = null; // To be modified
        ex.globrad = null; // To be modified
        ex.soilCoverage = null; // To be modified
        ex.soilSurfaceTemperatureBelowSnow = null; // To be modified
        ex.hasSnowCover = null; // To be modified
    }

    [EventSubscribe("Crop2MLProcess")]
    public void CalculateModel(object sender, EventArgs e)
    {
        if (clock.Today == clock.StartDate)
        {
            Init();
        }
        setExogenous();
        soiltemperaturecompComponent.CalculateModel(s,s1, r, a, ex);
    }

}