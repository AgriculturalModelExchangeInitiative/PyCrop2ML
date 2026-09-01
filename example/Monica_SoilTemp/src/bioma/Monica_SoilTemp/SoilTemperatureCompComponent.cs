
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       

using SoilTemperatureComp.DomainClass;
namespace SoilTemperatureComp.Strategies
{
    public class SoilTemperatureCompComponent : IStrategySoilTemperatureComp
    {
        public SoilTemperatureCompComponent()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new CompositeStrategyVarInfo(_NoSnowSoilSurfaceTemperature, "dampingFactor");
            _parameters0_0.Add(v1);
            VarInfo v2 = new CompositeStrategyVarInfo(_SoilTemperature, "timeStep");
            _parameters0_0.Add(v2);
            VarInfo v3 = new CompositeStrategyVarInfo(_SoilTemperature, "soilMoistureConst");
            _parameters0_0.Add(v3);
            VarInfo v4 = new CompositeStrategyVarInfo(_SoilTemperature, "baseTemp");
            _parameters0_0.Add(v4);
            VarInfo v5 = new CompositeStrategyVarInfo(_SoilTemperature, "initialSurfaceTemp");
            _parameters0_0.Add(v5);
            VarInfo v6 = new CompositeStrategyVarInfo(_SoilTemperature, "densityAir");
            _parameters0_0.Add(v6);
            VarInfo v7 = new CompositeStrategyVarInfo(_SoilTemperature, "specificHeatCapacityAir");
            _parameters0_0.Add(v7);
            VarInfo v8 = new CompositeStrategyVarInfo(_SoilTemperature, "densityHumus");
            _parameters0_0.Add(v8);
            VarInfo v9 = new CompositeStrategyVarInfo(_SoilTemperature, "specificHeatCapacityHumus");
            _parameters0_0.Add(v9);
            VarInfo v10 = new CompositeStrategyVarInfo(_SoilTemperature, "densityWater");
            _parameters0_0.Add(v10);
            VarInfo v11 = new CompositeStrategyVarInfo(_SoilTemperature, "specificHeatCapacityWater");
            _parameters0_0.Add(v11);
            VarInfo v12 = new CompositeStrategyVarInfo(_SoilTemperature, "quartzRawDensity");
            _parameters0_0.Add(v12);
            VarInfo v13 = new CompositeStrategyVarInfo(_SoilTemperature, "specificHeatCapacityQuartz");
            _parameters0_0.Add(v13);
            VarInfo v14 = new CompositeStrategyVarInfo(_SoilTemperature, "nTau");
            _parameters0_0.Add(v14);
            VarInfo v15 = new CompositeStrategyVarInfo(_SoilTemperature, "noOfTempLayers");
            _parameters0_0.Add(v15);
            VarInfo v16 = new CompositeStrategyVarInfo(_SoilTemperature, "noOfTempLayersPlus1");
            _parameters0_0.Add(v16);
            VarInfo v17 = new CompositeStrategyVarInfo(_SoilTemperature, "noOfSoilLayers");
            _parameters0_0.Add(v17);
            VarInfo v18 = new CompositeStrategyVarInfo(_SoilTemperature, "layerThickness");
            _parameters0_0.Add(v18);
            VarInfo v19 = new CompositeStrategyVarInfo(_SoilTemperature, "soilBulkDensity");
            _parameters0_0.Add(v19);
            VarInfo v20 = new CompositeStrategyVarInfo(_SoilTemperature, "saturation");
            _parameters0_0.Add(v20);
            VarInfo v21 = new CompositeStrategyVarInfo(_SoilTemperature, "soilOrganicMatter");
            _parameters0_0.Add(v21);
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd1.PropertyName = "tmin";
            pd1.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmin).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmin);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd2.PropertyName = "tmax";
            pd2.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmax).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmax);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd3.PropertyName = "globrad";
            pd3.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.globrad).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.globrad);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd4.PropertyName = "soilCoverage";
            pd4.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilCoverage).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilCoverage);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd5.PropertyName = "soilSurfaceTemperatureBelowSnow";
            pd5.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd6.PropertyName = "hasSnowCover";
            pd6.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd7.PropertyName = "V";
            pd7.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd8.PropertyName = "B";
            pd8.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd9.PropertyName = "volumeMatrix";
            pd9.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd10.PropertyName = "volumeMatrixOld";
            pd10.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd11.PropertyName = "matrixPrimaryDiagonal";
            pd11.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd12.PropertyName = "matrixSecondaryDiagonal";
            pd12.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd13.PropertyName = "heatConductivity";
            pd13.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd14.PropertyName = "heatConductivityMean";
            pd14.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean);
            _inputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd15.PropertyName = "heatCapacity";
            pd15.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity);
            _inputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd16.PropertyName = "solution";
            pd16.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution);
            _inputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd17.PropertyName = "matrixDiagonal";
            pd17.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal);
            _inputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd18.PropertyName = "matrixLowerTriangle";
            pd18.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle);
            _inputs0_0.Add(pd18);
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd19.PropertyName = "heatFlow";
            pd19.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow);
            _inputs0_0.Add(pd19);
            mo0_0.Inputs=_inputs0_0;
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd20 = new PropertyDescription();
            pd20.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd20.PropertyName = "soilSurfaceTemperature";
            pd20.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd20.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
            _outputs0_0.Add(pd20);
            PropertyDescription pd21 = new PropertyDescription();
            pd21.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd21.PropertyName = "soilTemperature";
            pd21.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature).ValueType.TypeForCurrentValue;
            pd21.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature);
            _outputs0_0.Add(pd21);
            mo0_0.Outputs=_outputs0_0;
            List<string> lAssStrat0_0 = new List<string>();
            lAssStrat0_0.Add(typeof(SoilTemperatureComp.Strategies.SoilTemperature).FullName);
            lAssStrat0_0.Add(typeof(SoilTemperatureComp.Strategies.NoSnowSoilSurfaceTemperature).FullName);
            lAssStrat0_0.Add(typeof(SoilTemperatureComp.Strategies.WithSnowSoilSurfaceTemperature).FullName);
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();
        }

        public string Description
        {
            get { return "" ;}
        }

        public string URL
        {
            get { return "" ;}
        }

        public string Domain
        {
            get { return "";}
        }

        public string ModelType
        {
            get { return "";}
        }

        public bool IsContext
        {
            get { return false;}
        }

        public IList<int> TimeStep
        {
            get
            {
                IList<int> ts = new List<int>();
                return ts;
            }
        }

        private  PublisherData _pd;
        public PublisherData PublisherData
        {
            get { return _pd;} 
        }

        private  void SetPublisherData()
        {
            _pd = new CRA.ModelLayer.MetadataTypes.PublisherData();
            _pd.Add("Creator", "Michael Berg-Mohnicke");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "ZALF e.V. "); 
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompRate), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous)};
        }

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

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
            _SoilTemperature.SetParametersDefaultValue();
            _NoSnowSoilSurfaceTemperature.SetParametersDefaultValue();
            _WithSnowSoilSurfaceTemperature.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            dampingFactorVarInfo.Name = "dampingFactor";
            dampingFactorVarInfo.Description = "dampingFactor";
            dampingFactorVarInfo.MaxValue = -1D;
            dampingFactorVarInfo.MinValue = -1D;
            dampingFactorVarInfo.DefaultValue = 0.8;
            dampingFactorVarInfo.Units = "dimensionless";
            dampingFactorVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            timeStepVarInfo.Name = "timeStep";
            timeStepVarInfo.Description = "timeStep";
            timeStepVarInfo.MaxValue = -1D;
            timeStepVarInfo.MinValue = -1D;
            timeStepVarInfo.DefaultValue = 1.0;
            timeStepVarInfo.Units = "dimensionless";
            timeStepVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            soilMoistureConstVarInfo.Name = "soilMoistureConst";
            soilMoistureConstVarInfo.Description = "constant soilmoisture during the model run";
            soilMoistureConstVarInfo.MaxValue = -1D;
            soilMoistureConstVarInfo.MinValue = -1D;
            soilMoistureConstVarInfo.DefaultValue = -1D;
            soilMoistureConstVarInfo.Units = "m**3/m**3";
            soilMoistureConstVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            baseTempVarInfo.Name = "baseTemp";
            baseTempVarInfo.Description = "baseTemperature";
            baseTempVarInfo.MaxValue = -1D;
            baseTempVarInfo.MinValue = -1D;
            baseTempVarInfo.DefaultValue = 9.5;
            baseTempVarInfo.Units = "°C";
            baseTempVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            initialSurfaceTempVarInfo.Name = "initialSurfaceTemp";
            initialSurfaceTempVarInfo.Description = "initialSurfaceTemperature";
            initialSurfaceTempVarInfo.MaxValue = -1D;
            initialSurfaceTempVarInfo.MinValue = -1D;
            initialSurfaceTempVarInfo.DefaultValue = 10.0;
            initialSurfaceTempVarInfo.Units = "°C";
            initialSurfaceTempVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            densityAirVarInfo.Name = "densityAir";
            densityAirVarInfo.Description = "DensityAir";
            densityAirVarInfo.MaxValue = -1D;
            densityAirVarInfo.MinValue = -1D;
            densityAirVarInfo.DefaultValue = 1.25;
            densityAirVarInfo.Units = "kg/m**3";
            densityAirVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            specificHeatCapacityAirVarInfo.Name = "specificHeatCapacityAir";
            specificHeatCapacityAirVarInfo.Description = "SpecificHeatCapacityAir";
            specificHeatCapacityAirVarInfo.MaxValue = -1D;
            specificHeatCapacityAirVarInfo.MinValue = -1D;
            specificHeatCapacityAirVarInfo.DefaultValue = 1005.0;
            specificHeatCapacityAirVarInfo.Units = "J/kg/K";
            specificHeatCapacityAirVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            densityHumusVarInfo.Name = "densityHumus";
            densityHumusVarInfo.Description = "DensityHumus";
            densityHumusVarInfo.MaxValue = -1D;
            densityHumusVarInfo.MinValue = -1D;
            densityHumusVarInfo.DefaultValue = 1300.0;
            densityHumusVarInfo.Units = "kg/m**3";
            densityHumusVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            specificHeatCapacityHumusVarInfo.Name = "specificHeatCapacityHumus";
            specificHeatCapacityHumusVarInfo.Description = "SpecificHeatCapacityHumus";
            specificHeatCapacityHumusVarInfo.MaxValue = -1D;
            specificHeatCapacityHumusVarInfo.MinValue = -1D;
            specificHeatCapacityHumusVarInfo.DefaultValue = 1920.0;
            specificHeatCapacityHumusVarInfo.Units = "J/kg/K";
            specificHeatCapacityHumusVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            densityWaterVarInfo.Name = "densityWater";
            densityWaterVarInfo.Description = "DensityWater";
            densityWaterVarInfo.MaxValue = -1D;
            densityWaterVarInfo.MinValue = -1D;
            densityWaterVarInfo.DefaultValue = 1000.0;
            densityWaterVarInfo.Units = "kg/m**3";
            densityWaterVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            specificHeatCapacityWaterVarInfo.Name = "specificHeatCapacityWater";
            specificHeatCapacityWaterVarInfo.Description = "SpecificHeatCapacityWater";
            specificHeatCapacityWaterVarInfo.MaxValue = -1D;
            specificHeatCapacityWaterVarInfo.MinValue = -1D;
            specificHeatCapacityWaterVarInfo.DefaultValue = 4192.0;
            specificHeatCapacityWaterVarInfo.Units = "J/kg/K";
            specificHeatCapacityWaterVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            quartzRawDensityVarInfo.Name = "quartzRawDensity";
            quartzRawDensityVarInfo.Description = "QuartzRawDensity";
            quartzRawDensityVarInfo.MaxValue = -1D;
            quartzRawDensityVarInfo.MinValue = -1D;
            quartzRawDensityVarInfo.DefaultValue = 2650.0;
            quartzRawDensityVarInfo.Units = "kg/m**3";
            quartzRawDensityVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            specificHeatCapacityQuartzVarInfo.Name = "specificHeatCapacityQuartz";
            specificHeatCapacityQuartzVarInfo.Description = "SpecificHeatCapacityQuartz";
            specificHeatCapacityQuartzVarInfo.MaxValue = -1D;
            specificHeatCapacityQuartzVarInfo.MinValue = -1D;
            specificHeatCapacityQuartzVarInfo.DefaultValue = 750.0;
            specificHeatCapacityQuartzVarInfo.Units = "J/kg/K";
            specificHeatCapacityQuartzVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            nTauVarInfo.Name = "nTau";
            nTauVarInfo.Description = "NTau";
            nTauVarInfo.MaxValue = -1D;
            nTauVarInfo.MinValue = -1D;
            nTauVarInfo.DefaultValue = 0.65;
            nTauVarInfo.Units = "?";
            nTauVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            noOfTempLayersVarInfo.Name = "noOfTempLayers";
            noOfTempLayersVarInfo.Description = "noOfTempLayers=noOfSoilLayers+2";
            noOfTempLayersVarInfo.MaxValue = -1D;
            noOfTempLayersVarInfo.MinValue = -1D;
            noOfTempLayersVarInfo.DefaultValue = 22;
            noOfTempLayersVarInfo.Units = "dimensionless";
            noOfTempLayersVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            noOfTempLayersPlus1VarInfo.Name = "noOfTempLayersPlus1";
            noOfTempLayersPlus1VarInfo.Description = "for matrixSecondaryDiagonal";
            noOfTempLayersPlus1VarInfo.MaxValue = -1D;
            noOfTempLayersPlus1VarInfo.MinValue = -1D;
            noOfTempLayersPlus1VarInfo.DefaultValue = 23;
            noOfTempLayersPlus1VarInfo.Units = "dimensionless";
            noOfTempLayersPlus1VarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            noOfSoilLayersVarInfo.Name = "noOfSoilLayers";
            noOfSoilLayersVarInfo.Description = "noOfSoilLayers";
            noOfSoilLayersVarInfo.MaxValue = -1D;
            noOfSoilLayersVarInfo.MinValue = -1D;
            noOfSoilLayersVarInfo.DefaultValue = 20;
            noOfSoilLayersVarInfo.Units = "dimensionless";
            noOfSoilLayersVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            layerThicknessVarInfo.Name = "layerThickness";
            layerThicknessVarInfo.Description = "layerThickness";
            layerThicknessVarInfo.MaxValue = -1D;
            layerThicknessVarInfo.MinValue = -1D;
            layerThicknessVarInfo.DefaultValue = -1D;
            layerThicknessVarInfo.Units = "m";
            layerThicknessVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            soilBulkDensityVarInfo.Name = "soilBulkDensity";
            soilBulkDensityVarInfo.Description = "bulkDensity";
            soilBulkDensityVarInfo.MaxValue = -1D;
            soilBulkDensityVarInfo.MinValue = -1D;
            soilBulkDensityVarInfo.DefaultValue = -1D;
            soilBulkDensityVarInfo.Units = "kg/m**3";
            soilBulkDensityVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            saturationVarInfo.Name = "saturation";
            saturationVarInfo.Description = "saturation";
            saturationVarInfo.MaxValue = -1D;
            saturationVarInfo.MinValue = -1D;
            saturationVarInfo.DefaultValue = -1D;
            saturationVarInfo.Units = "m**3/m**3";
            saturationVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            soilOrganicMatterVarInfo.Name = "soilOrganicMatter";
            soilOrganicMatterVarInfo.Description = "soilOrganicMatter";
            soilOrganicMatterVarInfo.MaxValue = -1D;
            soilOrganicMatterVarInfo.MinValue = -1D;
            soilOrganicMatterVarInfo.DefaultValue = -1D;
            soilOrganicMatterVarInfo.Units = "m**3/m**3";
            soilOrganicMatterVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");
        }

        public static VarInfo dampingFactorVarInfo
        {
            get { return SoilTemperatureComp.Strategies.NoSnowSoilSurfaceTemperature.dampingFactorVarInfo;} 
        }

        public static VarInfo timeStepVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.timeStepVarInfo;} 
        }

        public static VarInfo soilMoistureConstVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.soilMoistureConstVarInfo;} 
        }

        public static VarInfo baseTempVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.baseTempVarInfo;} 
        }

        public static VarInfo initialSurfaceTempVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.initialSurfaceTempVarInfo;} 
        }

        public static VarInfo densityAirVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.densityAirVarInfo;} 
        }

        public static VarInfo specificHeatCapacityAirVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.specificHeatCapacityAirVarInfo;} 
        }

        public static VarInfo densityHumusVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.densityHumusVarInfo;} 
        }

        public static VarInfo specificHeatCapacityHumusVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.specificHeatCapacityHumusVarInfo;} 
        }

        public static VarInfo densityWaterVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.densityWaterVarInfo;} 
        }

        public static VarInfo specificHeatCapacityWaterVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.specificHeatCapacityWaterVarInfo;} 
        }

        public static VarInfo quartzRawDensityVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.quartzRawDensityVarInfo;} 
        }

        public static VarInfo specificHeatCapacityQuartzVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.specificHeatCapacityQuartzVarInfo;} 
        }

        public static VarInfo nTauVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.nTauVarInfo;} 
        }

        public static VarInfo noOfTempLayersVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.noOfTempLayersVarInfo;} 
        }

        public static VarInfo noOfTempLayersPlus1VarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.noOfTempLayersPlus1VarInfo;} 
        }

        public static VarInfo noOfSoilLayersVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.noOfSoilLayersVarInfo;} 
        }

        public static VarInfo layerThicknessVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.layerThicknessVarInfo;} 
        }

        public static VarInfo soilBulkDensityVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.soilBulkDensityVarInfo;} 
        }

        public static VarInfo saturationVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.saturationVarInfo;} 
        }

        public static VarInfo soilOrganicMatterVarInfo
        {
            get { return SoilTemperatureComp.Strategies.SoilTemperature.soilOrganicMatterVarInfo;} 
        }

        public string TestPostConditions(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.CurrentValue=s.soilSurfaceTemperature;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature.CurrentValue=s.soilTemperature;

                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 

                RangeBasedCondition r41 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
                if(r41.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.ValueType)){prc.AddCondition(r41);}
                RangeBasedCondition r42 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature);
                if(r42.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature.ValueType)){prc.AddCondition(r42);}

                string ret = "";
                ret += _SoilTemperature.TestPostConditions(s, s1, r, a, ex, " strategy SoilTemperatureComp.Strategies.SoilTemperatureComp");
                ret += _NoSnowSoilSurfaceTemperature.TestPostConditions(s, s1, r, a, ex, " strategy SoilTemperatureComp.Strategies.SoilTemperatureComp");
                ret += _WithSnowSoilSurfaceTemperature.TestPostConditions(s, s1, r, a, ex, " strategy SoilTemperatureComp.Strategies.SoilTemperatureComp");
                if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }

                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component .SoilTemperatureComp, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmin.CurrentValue=ex.tmin;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmax.CurrentValue=ex.tmax;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.globrad.CurrentValue=ex.globrad;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilCoverage.CurrentValue=ex.soilCoverage;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow.CurrentValue=ex.soilSurfaceTemperatureBelowSnow;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover.CurrentValue=ex.hasSnowCover;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V.CurrentValue=s.V;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B.CurrentValue=s.B;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix.CurrentValue=s.volumeMatrix;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld.CurrentValue=s.volumeMatrixOld;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal.CurrentValue=s.matrixPrimaryDiagonal;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal.CurrentValue=s.matrixSecondaryDiagonal;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity.CurrentValue=s.heatConductivity;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean.CurrentValue=s.heatConductivityMean;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity.CurrentValue=s.heatCapacity;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution.CurrentValue=s.solution;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal.CurrentValue=s.matrixDiagonal;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle.CurrentValue=s.matrixLowerTriangle;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow.CurrentValue=s.heatFlow;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmin);
                if(r1.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmin.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmax);
                if(r2.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.tmax.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.globrad);
                if(r3.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.globrad.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilCoverage);
                if(r4.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilCoverage.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow);
                if(r5.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover);
                if(r6.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V);
                if(r7.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B);
                if(r8.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix);
                if(r9.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld);
                if(r10.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal);
                if(r11.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal);
                if(r12.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity);
                if(r13.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean);
                if(r14.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity);
                if(r15.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity.ValueType)){prc.AddCondition(r15);}
                RangeBasedCondition r16 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution);
                if(r16.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution.ValueType)){prc.AddCondition(r16);}
                RangeBasedCondition r17 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal);
                if(r17.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal.ValueType)){prc.AddCondition(r17);}
                RangeBasedCondition r18 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle);
                if(r18.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle.ValueType)){prc.AddCondition(r18);}
                RangeBasedCondition r19 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow);
                if(r19.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow.ValueType)){prc.AddCondition(r19);}

                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("dampingFactor")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("timeStep")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("soilMoistureConst")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("baseTemp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("initialSurfaceTemp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("densityAir")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("specificHeatCapacityAir")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("densityHumus")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("specificHeatCapacityHumus")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("densityWater")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("specificHeatCapacityWater")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("quartzRawDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("specificHeatCapacityQuartz")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("nTau")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("noOfTempLayers")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("noOfTempLayersPlus1")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("noOfSoilLayers")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("layerThickness")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("soilBulkDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("saturation")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("soilOrganicMatter")));
                string ret = "";
                ret += _SoilTemperature.TestPreConditions(s, s1, r, a, ex, " strategy SoilTemperatureComp.Strategies.SoilTemperatureComp");
                ret += _NoSnowSoilSurfaceTemperature.TestPreConditions(s, s1, r, a, ex, " strategy SoilTemperatureComp.Strategies.SoilTemperatureComp");
                ret += _WithSnowSoilSurfaceTemperature.TestPreConditions(s, s1, r, a, ex, " strategy SoilTemperatureComp.Strategies.SoilTemperatureComp");
                if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }

                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component .SoilTemperatureComp, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SoilTemperatureComp, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            EstimateOfAssociatedClasses(s, s1, r, a, ex);
        }

        //Declaration of the associated strategies
        SoilTemperature _SoilTemperature = new SoilTemperature();
        NoSnowSoilSurfaceTemperature _NoSnowSoilSurfaceTemperature = new NoSnowSoilSurfaceTemperature();
        WithSnowSoilSurfaceTemperature _WithSnowSoilSurfaceTemperature = new WithSnowSoilSurfaceTemperature();

        private void EstimateOfAssociatedClasses(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            _nosnowsoilsurfacetemperature.Estimate(s,s1, r, a, ex);
            s.noSnowSoilSurfaceTemperature = s.soilSurfaceTemperature;
            _withsnowsoilsurfacetemperature.Estimate(s,s1, r, a, ex);
            _soiltemperature.Estimate(s,s1, r, a, ex);
        }

        public SoilTemperatureCompComponent(SoilTemperatureCompComponent toCopy): this() // copy constructor 
        {
                dampingFactor = toCopy.dampingFactor;
                timeStep = toCopy.timeStep;
                
            for (int i = 0; i < noOfSoilLayers; i++)
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
                
            for (int i = 0; i < noOfTempLayers; i++)
            { layerThickness[i] = toCopy.layerThickness[i]; }
    
                
            for (int i = 0; i < noOfSoilLayers; i++)
            { soilBulkDensity[i] = toCopy.soilBulkDensity[i]; }
    
                
            for (int i = 0; i < noOfSoilLayers; i++)
            { saturation[i] = toCopy.saturation[i]; }
    
                
            for (int i = 0; i < noOfSoilLayers; i++)
            { soilOrganicMatter[i] = toCopy.soilOrganicMatter[i]; }
    
        }
    }
}