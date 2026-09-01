
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
using SiriusQualitySoilTemperatureComp.DomainClass;
namespace SiriusQualitySoilTemperatureComp.Strategies
{
    public class SoilTemperature : IStrategySiriusQualitySoilTemperatureComp
    {
        public SoilTemperature()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 20;
            v1.Description = "noOfSoilLayers";
            v1.Id = 0;
            v1.MaxValue = -1D;
            v1.MinValue = -1D;
            v1.Name = "noOfSoilLayers";
            v1.Size = 1;
            v1.Units = "dimensionless";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 22;
            v2.Description = "noOfTempLayers=noOfSoilLayers+2";
            v2.Id = 0;
            v2.MaxValue = -1D;
            v2.MinValue = -1D;
            v2.Name = "noOfTempLayers";
            v2.Size = 1;
            v2.Units = "dimensionless";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 23;
            v3.Description = "for matrixSecondaryDiagonal";
            v3.Id = 0;
            v3.MaxValue = -1D;
            v3.MinValue = -1D;
            v3.Name = "noOfTempLayersPlus1";
            v3.Size = 1;
            v3.Units = "dimensionless";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 1.0;
            v4.Description = "timeStep";
            v4.Id = 0;
            v4.MaxValue = -1D;
            v4.MinValue = -1D;
            v4.Name = "timeStep";
            v4.Size = 1;
            v4.Units = "dimensionless";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = -1D;
            v5.Description = "constant soilmoisture during the model run";
            v5.Id = 0;
            v5.MaxValue = -1D;
            v5.MinValue = -1D;
            v5.Name = "soilMoistureConst";
            v5.Size = 1;
            v5.Units = "m**3/m**3";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");
            _parameters0_0.Add(v5);
            VarInfo v6 = new VarInfo();
            v6.DefaultValue = 9.5;
            v6.Description = "baseTemperature";
            v6.Id = 0;
            v6.MaxValue = -1D;
            v6.MinValue = -1D;
            v6.Name = "baseTemp";
            v6.Size = 1;
            v6.Units = "°C";
            v6.URL = "";
            v6.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v6.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v6);
            VarInfo v7 = new VarInfo();
            v7.DefaultValue = 10.0;
            v7.Description = "initialSurfaceTemperature";
            v7.Id = 0;
            v7.MaxValue = -1D;
            v7.MinValue = -1D;
            v7.Name = "initialSurfaceTemp";
            v7.Size = 1;
            v7.Units = "°C";
            v7.URL = "";
            v7.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v7.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v7);
            VarInfo v8 = new VarInfo();
            v8.DefaultValue = 1.25;
            v8.Description = "DensityAir";
            v8.Id = 0;
            v8.MaxValue = -1D;
            v8.MinValue = -1D;
            v8.Name = "densityAir";
            v8.Size = 1;
            v8.Units = "kg/m**3";
            v8.URL = "";
            v8.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v8.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v8);
            VarInfo v9 = new VarInfo();
            v9.DefaultValue = 1005.0;
            v9.Description = "SpecificHeatCapacityAir";
            v9.Id = 0;
            v9.MaxValue = -1D;
            v9.MinValue = -1D;
            v9.Name = "specificHeatCapacityAir";
            v9.Size = 1;
            v9.Units = "J/kg/K";
            v9.URL = "";
            v9.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v9.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v9);
            VarInfo v10 = new VarInfo();
            v10.DefaultValue = 1300.0;
            v10.Description = "DensityHumus";
            v10.Id = 0;
            v10.MaxValue = -1D;
            v10.MinValue = -1D;
            v10.Name = "densityHumus";
            v10.Size = 1;
            v10.Units = "kg/m**3";
            v10.URL = "";
            v10.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v10.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v10);
            VarInfo v11 = new VarInfo();
            v11.DefaultValue = 1920.0;
            v11.Description = "SpecificHeatCapacityHumus";
            v11.Id = 0;
            v11.MaxValue = -1D;
            v11.MinValue = -1D;
            v11.Name = "specificHeatCapacityHumus";
            v11.Size = 1;
            v11.Units = "J/kg/K";
            v11.URL = "";
            v11.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v11.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v11);
            VarInfo v12 = new VarInfo();
            v12.DefaultValue = 1000.0;
            v12.Description = "DensityWater";
            v12.Id = 0;
            v12.MaxValue = -1D;
            v12.MinValue = -1D;
            v12.Name = "densityWater";
            v12.Size = 1;
            v12.Units = "kg/m**3";
            v12.URL = "";
            v12.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v12.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v12);
            VarInfo v13 = new VarInfo();
            v13.DefaultValue = 4192.0;
            v13.Description = "SpecificHeatCapacityWater";
            v13.Id = 0;
            v13.MaxValue = -1D;
            v13.MinValue = -1D;
            v13.Name = "specificHeatCapacityWater";
            v13.Size = 1;
            v13.Units = "J/kg/K";
            v13.URL = "";
            v13.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v13.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v13);
            VarInfo v14 = new VarInfo();
            v14.DefaultValue = 2650.0;
            v14.Description = "QuartzRawDensity";
            v14.Id = 0;
            v14.MaxValue = -1D;
            v14.MinValue = -1D;
            v14.Name = "quartzRawDensity";
            v14.Size = 1;
            v14.Units = "kg/m**3";
            v14.URL = "";
            v14.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v14.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v14);
            VarInfo v15 = new VarInfo();
            v15.DefaultValue = 750.0;
            v15.Description = "SpecificHeatCapacityQuartz";
            v15.Id = 0;
            v15.MaxValue = -1D;
            v15.MinValue = -1D;
            v15.Name = "specificHeatCapacityQuartz";
            v15.Size = 1;
            v15.Units = "J/kg/K";
            v15.URL = "";
            v15.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v15.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v15);
            VarInfo v16 = new VarInfo();
            v16.DefaultValue = 0.65;
            v16.Description = "NTau";
            v16.Id = 0;
            v16.MaxValue = -1D;
            v16.MinValue = -1D;
            v16.Name = "nTau";
            v16.Size = 1;
            v16.Units = "?";
            v16.URL = "";
            v16.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v16.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v16);
            VarInfo v17 = new VarInfo();
            v17.DefaultValue = -1D;
            v17.Description = "layerThickness";
            v17.Id = 0;
            v17.MaxValue = -1D;
            v17.MinValue = -1D;
            v17.Name = "layerThickness";
            v17.Size = 1;
            v17.Units = "m";
            v17.URL = "";
            v17.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v17.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");
            _parameters0_0.Add(v17);
            VarInfo v18 = new VarInfo();
            v18.DefaultValue = -1D;
            v18.Description = "bulkDensity";
            v18.Id = 0;
            v18.MaxValue = -1D;
            v18.MinValue = -1D;
            v18.Name = "soilBulkDensity";
            v18.Size = 1;
            v18.Units = "kg/m**3";
            v18.URL = "";
            v18.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v18.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");
            _parameters0_0.Add(v18);
            VarInfo v19 = new VarInfo();
            v19.DefaultValue = -1D;
            v19.Description = "saturation";
            v19.Id = 0;
            v19.MaxValue = -1D;
            v19.MinValue = -1D;
            v19.Name = "saturation";
            v19.Size = 1;
            v19.Units = "m**3/m**3";
            v19.URL = "";
            v19.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v19.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");
            _parameters0_0.Add(v19);
            VarInfo v20 = new VarInfo();
            v20.DefaultValue = -1D;
            v20.Description = "soilOrganicMatter";
            v20.Id = 0;
            v20.MaxValue = -1D;
            v20.MinValue = -1D;
            v20.Name = "soilOrganicMatter";
            v20.Size = 1;
            v20.Units = "m**3/m**3";
            v20.URL = "";
            v20.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v20.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");
            _parameters0_0.Add(v20);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd1.PropertyName = "soilSurfaceTemperature";
            pd1.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd2.PropertyName = "soilTemperature";
            pd2.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd3.PropertyName = "V";
            pd3.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd4.PropertyName = "B";
            pd4.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd5.PropertyName = "volumeMatrix";
            pd5.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd6.PropertyName = "volumeMatrixOld";
            pd6.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd7.PropertyName = "matrixPrimaryDiagonal";
            pd7.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd8.PropertyName = "matrixSecondaryDiagonal";
            pd8.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd9.PropertyName = "heatConductivity";
            pd9.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd10.PropertyName = "heatConductivityMean";
            pd10.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd11.PropertyName = "heatCapacity";
            pd11.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd12.PropertyName = "solution";
            pd12.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd13.PropertyName = "matrixDiagonal";
            pd13.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd14.PropertyName = "matrixLowerTriangle";
            pd14.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle);
            _inputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd15.PropertyName = "heatFlow";
            pd15.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow);
            _inputs0_0.Add(pd15);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd16.PropertyName = "soilTemperature";
            pd16.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature);
            _outputs0_0.Add(pd16);
            mo0_0.Outputs=_outputs0_0;
            //Associated strategies
            List<string> lAssStrat0_0 = new List<string>();
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            //Adding the modeling options to the modeling options manager
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();

        }

        public string Description
        {
            
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
            return new List<Type>() {  typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState),  typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState), typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate), typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary), typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public int noOfSoilLayers
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("noOfSoilLayers");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'noOfSoilLayers' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("noOfSoilLayers");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'noOfSoilLayers' not found in strategy 'SoilTemperature'");
            }
        }
        public int noOfTempLayers
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("noOfTempLayers");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'noOfTempLayers' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("noOfTempLayers");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'noOfTempLayers' not found in strategy 'SoilTemperature'");
            }
        }
        public int noOfTempLayersPlus1
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("noOfTempLayersPlus1");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'noOfTempLayersPlus1' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("noOfTempLayersPlus1");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'noOfTempLayersPlus1' not found in strategy 'SoilTemperature'");
            }
        }
        public double timeStep
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("timeStep");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'timeStep' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("timeStep");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'timeStep' not found in strategy 'SoilTemperature'");
            }
        }
        public double[] soilMoistureConst
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("soilMoistureConst");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'soilMoistureConst' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("soilMoistureConst");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'soilMoistureConst' not found in strategy 'SoilTemperature'");
            }
        }
        public double baseTemp
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("baseTemp");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'baseTemp' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("baseTemp");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'baseTemp' not found in strategy 'SoilTemperature'");
            }
        }
        public double initialSurfaceTemp
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("initialSurfaceTemp");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'initialSurfaceTemp' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("initialSurfaceTemp");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'initialSurfaceTemp' not found in strategy 'SoilTemperature'");
            }
        }
        public double densityAir
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("densityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'densityAir' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("densityAir");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'densityAir' not found in strategy 'SoilTemperature'");
            }
        }
        public double specificHeatCapacityAir
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("specificHeatCapacityAir");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found in strategy 'SoilTemperature'");
            }
        }
        public double densityHumus
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("densityHumus");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'densityHumus' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("densityHumus");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'densityHumus' not found in strategy 'SoilTemperature'");
            }
        }
        public double specificHeatCapacityHumus
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityHumus");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityHumus' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("specificHeatCapacityHumus");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityHumus' not found in strategy 'SoilTemperature'");
            }
        }
        public double densityWater
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("densityWater");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'densityWater' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("densityWater");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'densityWater' not found in strategy 'SoilTemperature'");
            }
        }
        public double specificHeatCapacityWater
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityWater");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityWater' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("specificHeatCapacityWater");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityWater' not found in strategy 'SoilTemperature'");
            }
        }
        public double quartzRawDensity
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("quartzRawDensity");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'quartzRawDensity' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("quartzRawDensity");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'quartzRawDensity' not found in strategy 'SoilTemperature'");
            }
        }
        public double specificHeatCapacityQuartz
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityQuartz");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityQuartz' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("specificHeatCapacityQuartz");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityQuartz' not found in strategy 'SoilTemperature'");
            }
        }
        public double nTau
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("nTau");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'nTau' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("nTau");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'nTau' not found in strategy 'SoilTemperature'");
            }
        }
        public double[] layerThickness
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("layerThickness");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'layerThickness' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("layerThickness");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'layerThickness' not found in strategy 'SoilTemperature'");
            }
        }
        public double[] soilBulkDensity
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("soilBulkDensity");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'soilBulkDensity' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("soilBulkDensity");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'soilBulkDensity' not found in strategy 'SoilTemperature'");
            }
        }
        public double[] saturation
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("saturation");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'saturation' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("saturation");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'saturation' not found in strategy 'SoilTemperature'");
            }
        }
        public double[] soilOrganicMatter
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("soilOrganicMatter");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'soilOrganicMatter' not found (or found null) in strategy 'SoilTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("soilOrganicMatter");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'soilOrganicMatter' not found in strategy 'SoilTemperature'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            noOfSoilLayersVarInfo.Name = "noOfSoilLayers";
            noOfSoilLayersVarInfo.Description = "noOfSoilLayers";
            noOfSoilLayersVarInfo.MaxValue = -1D;
            noOfSoilLayersVarInfo.MinValue = -1D;
            noOfSoilLayersVarInfo.DefaultValue = 20;
            noOfSoilLayersVarInfo.Units = "dimensionless";
            noOfSoilLayersVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

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

        private static VarInfo _noOfSoilLayersVarInfo = new VarInfo();
        public static VarInfo noOfSoilLayersVarInfo
        {
            get { return _noOfSoilLayersVarInfo;} 
        }

        private static VarInfo _noOfTempLayersVarInfo = new VarInfo();
        public static VarInfo noOfTempLayersVarInfo
        {
            get { return _noOfTempLayersVarInfo;} 
        }

        private static VarInfo _noOfTempLayersPlus1VarInfo = new VarInfo();
        public static VarInfo noOfTempLayersPlus1VarInfo
        {
            get { return _noOfTempLayersPlus1VarInfo;} 
        }

        private static VarInfo _timeStepVarInfo = new VarInfo();
        public static VarInfo timeStepVarInfo
        {
            get { return _timeStepVarInfo;} 
        }

        private static VarInfo _soilMoistureConstVarInfo = new VarInfo();
        public static VarInfo soilMoistureConstVarInfo
        {
            get { return _soilMoistureConstVarInfo;} 
        }

        private static VarInfo _baseTempVarInfo = new VarInfo();
        public static VarInfo baseTempVarInfo
        {
            get { return _baseTempVarInfo;} 
        }

        private static VarInfo _initialSurfaceTempVarInfo = new VarInfo();
        public static VarInfo initialSurfaceTempVarInfo
        {
            get { return _initialSurfaceTempVarInfo;} 
        }

        private static VarInfo _densityAirVarInfo = new VarInfo();
        public static VarInfo densityAirVarInfo
        {
            get { return _densityAirVarInfo;} 
        }

        private static VarInfo _specificHeatCapacityAirVarInfo = new VarInfo();
        public static VarInfo specificHeatCapacityAirVarInfo
        {
            get { return _specificHeatCapacityAirVarInfo;} 
        }

        private static VarInfo _densityHumusVarInfo = new VarInfo();
        public static VarInfo densityHumusVarInfo
        {
            get { return _densityHumusVarInfo;} 
        }

        private static VarInfo _specificHeatCapacityHumusVarInfo = new VarInfo();
        public static VarInfo specificHeatCapacityHumusVarInfo
        {
            get { return _specificHeatCapacityHumusVarInfo;} 
        }

        private static VarInfo _densityWaterVarInfo = new VarInfo();
        public static VarInfo densityWaterVarInfo
        {
            get { return _densityWaterVarInfo;} 
        }

        private static VarInfo _specificHeatCapacityWaterVarInfo = new VarInfo();
        public static VarInfo specificHeatCapacityWaterVarInfo
        {
            get { return _specificHeatCapacityWaterVarInfo;} 
        }

        private static VarInfo _quartzRawDensityVarInfo = new VarInfo();
        public static VarInfo quartzRawDensityVarInfo
        {
            get { return _quartzRawDensityVarInfo;} 
        }

        private static VarInfo _specificHeatCapacityQuartzVarInfo = new VarInfo();
        public static VarInfo specificHeatCapacityQuartzVarInfo
        {
            get { return _specificHeatCapacityQuartzVarInfo;} 
        }

        private static VarInfo _nTauVarInfo = new VarInfo();
        public static VarInfo nTauVarInfo
        {
            get { return _nTauVarInfo;} 
        }

        private static VarInfo _layerThicknessVarInfo = new VarInfo();
        public static VarInfo layerThicknessVarInfo
        {
            get { return _layerThicknessVarInfo;} 
        }

        private static VarInfo _soilBulkDensityVarInfo = new VarInfo();
        public static VarInfo soilBulkDensityVarInfo
        {
            get { return _soilBulkDensityVarInfo;} 
        }

        private static VarInfo _saturationVarInfo = new VarInfo();
        public static VarInfo saturationVarInfo
        {
            get { return _saturationVarInfo;} 
        }

        private static VarInfo _soilOrganicMatterVarInfo = new VarInfo();
        public static VarInfo soilOrganicMatterVarInfo
        {
            get { return _soilOrganicMatterVarInfo;} 
        }

        public string TestPostConditions(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature.CurrentValue=s.soilTemperature;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r36 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature);
                if(r36.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature.ValueType)){prc.AddCondition(r36);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.SoilTemperatureComp, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.CurrentValue=s.soilSurfaceTemperature;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature.CurrentValue=s.soilTemperature;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V.CurrentValue=s.V;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B.CurrentValue=s.B;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix.CurrentValue=s.volumeMatrix;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld.CurrentValue=s.volumeMatrixOld;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal.CurrentValue=s.matrixPrimaryDiagonal;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal.CurrentValue=s.matrixSecondaryDiagonal;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity.CurrentValue=s.heatConductivity;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean.CurrentValue=s.heatConductivityMean;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity.CurrentValue=s.heatCapacity;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution.CurrentValue=s.solution;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal.CurrentValue=s.matrixDiagonal;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle.CurrentValue=s.matrixLowerTriangle;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow.CurrentValue=s.heatFlow;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilTemperature.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.V.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.B.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrix.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.volumeMatrixOld.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixPrimaryDiagonal.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixSecondaryDiagonal.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivity.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatConductivityMean.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatCapacity.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.solution.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal);
                if(r13.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixDiagonal.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.matrixLowerTriangle.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow);
                if(r15.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.heatFlow.ValueType)){prc.AddCondition(r15);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("noOfSoilLayers")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("noOfTempLayers")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("noOfTempLayersPlus1")));
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
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("layerThickness")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("soilBulkDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("saturation")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("soilOrganicMatter")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.SoilTemperatureComp, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualitySoilTemperatureComp, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        public void Init(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            double soilSurfaceTemperature = 0.0;
            double[] soilTemperature =  new double [noOfTempLayers];
            double[] V =  new double [noOfTempLayers];
            double[] B =  new double [noOfTempLayers];
            double[] volumeMatrix =  new double [noOfTempLayers];
            double[] volumeMatrixOld =  new double [noOfTempLayers];
            double[] matrixPrimaryDiagonal =  new double [noOfTempLayers];
            double[] matrixSecondaryDiagonal =  new double [noOfTempLayersPlus1];
            double[] heatConductivity =  new double [noOfTempLayers];
            double[] heatConductivityMean =  new double [noOfTempLayers];
            double[] heatCapacity =  new double [noOfTempLayers];
            double[] solution =  new double [noOfTempLayers];
            double[] matrixDiagonal =  new double [noOfTempLayers];
            double[] matrixLowerTriangle =  new double [noOfTempLayers];
            double[] heatFlow =  new double [noOfTempLayers];
            soilTemperature = new double[noOfTempLayers];
            V = new double[noOfTempLayers];
            B = new double[noOfTempLayers];
            volumeMatrix = new double[noOfTempLayers];
            volumeMatrixOld = new double[noOfTempLayers];
            matrixPrimaryDiagonal = new double[noOfTempLayers];
            matrixSecondaryDiagonal = new double[noOfTempLayersPlus1];
            heatConductivity = new double[noOfTempLayers];
            heatConductivityMean = new double[noOfTempLayers];
            heatCapacity = new double[noOfTempLayers];
            solution = new double[noOfTempLayers];
            matrixDiagonal = new double[noOfTempLayers];
            matrixLowerTriangle = new double[noOfTempLayers];
            heatFlow = new double[noOfTempLayers];
            int groundLayer;
            int bottomLayer;
            double lti_1;
            double lti;
            double ts;
            double dw;
            double cw;
            double dq;
            double cq;
            double da;
            double ca;
            double dh;
            double ch;
            double sbdi;
            double smi;
            double sati;
            double somi;
            double hci_1;
            double hci;
            int i;
            for (i=0 ; i!=noOfSoilLayers ; i+=1)
            {
                soilTemperature[i] = (1.00d - ((double)(i) / noOfSoilLayers)) * initialSurfaceTemp + ((double)(i) / noOfSoilLayers * baseTemp);
            }
            groundLayer = noOfTempLayers - 2;
            bottomLayer = noOfTempLayers - 1;
            layerThickness[groundLayer] = 2.00d * layerThickness[(groundLayer - 1)];
            layerThickness[bottomLayer] = 1.00d;
            soilTemperature[groundLayer] = (soilTemperature[groundLayer - 1] + baseTemp) * 0.50d;
            soilTemperature[bottomLayer] = baseTemp;
            V[0] = layerThickness[0];
            B[0] = 2.00d / layerThickness[0];
            for (i=1 ; i!=noOfTempLayers ; i+=1)
            {
                lti_1 = layerThickness[i - 1];
                lti = layerThickness[i];
                B[i] = 2.00d / (lti + lti_1);
                V[i] = lti * nTau;
            }
            ts = timeStep;
            dw = densityWater;
            cw = specificHeatCapacityWater;
            dq = quartzRawDensity;
            cq = specificHeatCapacityQuartz;
            da = densityAir;
            ca = specificHeatCapacityAir;
            dh = densityHumus;
            ch = specificHeatCapacityHumus;
            for (i=0 ; i!=noOfSoilLayers ; i+=1)
            {
                sbdi = soilBulkDensity[i];
                smi = soilMoistureConst[i];
                heatConductivity[i] = (3.00d * (sbdi / 1000.00d) - 1.70d) * 0.0010d / (1.00d + ((11.50d - (5.00d * (sbdi / 1000.00d))) * Math.Exp(-50.00d * Math.Pow(smi / (sbdi / 1000.00d), 1.50d)))) * 86400.00d * ts * 100.00d * 4.1840d;
                sati = saturation[i];
                somi = soilOrganicMatter[i] / da * sbdi;
                heatCapacity[i] = smi * dw * cw + ((sati - smi) * da * ca) + (somi * dh * ch) + ((1.00d - sati - somi) * dq * cq);
            }
            heatCapacity[groundLayer] = heatCapacity[groundLayer - 1];
            heatCapacity[bottomLayer] = heatCapacity[groundLayer];
            heatConductivity[groundLayer] = heatConductivity[groundLayer - 1];
            heatConductivity[bottomLayer] = heatConductivity[groundLayer];
            soilSurfaceTemperature = initialSurfaceTemp;
            heatConductivityMean[0] = heatConductivity[0];
            for (i=1 ; i!=noOfTempLayers ; i+=1)
            {
                lti_1 = layerThickness[i - 1];
                lti = layerThickness[i];
                hci_1 = heatConductivity[i - 1];
                hci = heatConductivity[i];
                heatConductivityMean[i] = (lti_1 * hci_1 + (lti * hci)) / (lti + lti_1);
            }
            for (i=0 ; i!=noOfTempLayers ; i+=1)
            {
                volumeMatrix[i] = V[i] * heatCapacity[i];
                volumeMatrixOld[i] = volumeMatrix[i];
                matrixSecondaryDiagonal[i] = -B[i] * heatConductivityMean[i];
            }
            matrixSecondaryDiagonal[bottomLayer + 1] = 0.00d;
            for (i=0 ; i!=noOfTempLayers ; i+=1)
            {
                matrixPrimaryDiagonal[i] = volumeMatrix[i] - matrixSecondaryDiagonal[i] - matrixSecondaryDiagonal[i + 1];
            }
            s.soilSurfaceTemperature= soilSurfaceTemperature;
            s.soilTemperature= soilTemperature;
            s.V= V;
            s.B= B;
            s.volumeMatrix= volumeMatrix;
            s.volumeMatrixOld= volumeMatrixOld;
            s.matrixPrimaryDiagonal= matrixPrimaryDiagonal;
            s.matrixSecondaryDiagonal= matrixSecondaryDiagonal;
            s.heatConductivity= heatConductivity;
            s.heatConductivityMean= heatConductivityMean;
            s.heatCapacity= heatCapacity;
            s.solution= solution;
            s.matrixDiagonal= matrixDiagonal;
            s.matrixLowerTriangle= matrixLowerTriangle;
            s.heatFlow= heatFlow;
        }

        private void CalculateModel(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            double soilSurfaceTemperature = s.soilSurfaceTemperature;
            double[] soilTemperature = s.soilTemperature;
            double[] V = s.V;
            double[] B = s.B;
            double[] volumeMatrix = s.volumeMatrix;
            double[] volumeMatrixOld = s.volumeMatrixOld;
            double[] matrixPrimaryDiagonal = s.matrixPrimaryDiagonal;
            double[] matrixSecondaryDiagonal = s.matrixSecondaryDiagonal;
            double[] heatConductivity = s.heatConductivity;
            double[] heatConductivityMean = s.heatConductivityMean;
            double[] heatCapacity = s.heatCapacity;
            double[] solution = s.solution;
            double[] matrixDiagonal = s.matrixDiagonal;
            double[] matrixLowerTriangle = s.matrixLowerTriangle;
            double[] heatFlow = s.heatFlow;
            int groundLayer;
            int bottomLayer;
            int i;
            int j;
            int j_1;
            groundLayer = noOfTempLayers - 2;
            bottomLayer = noOfTempLayers - 1;
            heatFlow[0] = soilSurfaceTemperature * B[0] * heatConductivityMean[0];
            for (i=0 ; i!=noOfTempLayers ; i+=1)
            {
                solution[i] = (volumeMatrixOld[i] + ((volumeMatrix[i] - volumeMatrixOld[i]) / layerThickness[i])) * soilTemperature[i] + heatFlow[i];
            }
            matrixDiagonal[0] = matrixPrimaryDiagonal[0];
            for (i=1 ; i!=noOfTempLayers ; i+=1)
            {
                matrixLowerTriangle[i] = matrixSecondaryDiagonal[i] / matrixDiagonal[(i - 1)];
                matrixDiagonal[i] = matrixPrimaryDiagonal[i] - (matrixLowerTriangle[i] * matrixSecondaryDiagonal[i]);
            }
            for (i=1 ; i!=noOfTempLayers ; i+=1)
            {
                solution[i] = solution[i] - (matrixLowerTriangle[i] * solution[(i - 1)]);
            }
            solution[bottomLayer] = solution[bottomLayer] / matrixDiagonal[bottomLayer];
            for (i=0 ; i!=bottomLayer ; i+=1)
            {
                j = bottomLayer - 1 - i;
                j_1 = j + 1;
                solution[j] = solution[j] / matrixDiagonal[j] - (matrixLowerTriangle[j_1] * solution[j_1]);
            }
            for (i=0 ; i!=noOfTempLayers ; i+=1)
            {
                soilTemperature[i] = solution[i];
            }
            for (i=0 ; i!=noOfSoilLayers ; i+=1)
            {
                volumeMatrixOld[i] = volumeMatrix[i];
            }
            volumeMatrixOld[groundLayer] = volumeMatrix[groundLayer];
            volumeMatrixOld[bottomLayer] = volumeMatrix[bottomLayer];
            s.soilTemperature= soilTemperature;
        }

    }
}