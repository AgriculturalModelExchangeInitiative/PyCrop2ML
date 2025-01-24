
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

using SiriusQualitySoilTemperature.DomainClass;
namespace SiriusQualitySoilTemperature.Strategies
{
    public class SoilTemperatureComponent : IStrategySiriusQualitySoilTemperature
    {
        public SoilTemperatureComponent()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new CompositeStrategyVarInfo(_SnowCoverCalculator, "cCarbonContent");
            _parameters0_0.Add(v1);
            VarInfo v2 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cSoilLayerDepth");
            _parameters0_0.Add(v2);
            VarInfo v3 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cFirstDayMeanTemp");
            _parameters0_0.Add(v3);
            VarInfo v4 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cAverageGroundTemperature");
            _parameters0_0.Add(v4);
            VarInfo v5 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cAVT");
            _parameters0_0.Add(v5);
            VarInfo v6 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cAverageBulkDensity");
            _parameters0_0.Add(v6);
            VarInfo v7 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cABD");
            _parameters0_0.Add(v7);
            VarInfo v8 = new CompositeStrategyVarInfo(_STMPsimCalculator, "cDampingDepth");
            _parameters0_0.Add(v8);
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd1.PropertyName = "iAirTemperatureMax";
            pd1.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd2.PropertyName = "iAirTemperatureMin";
            pd2.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd3.PropertyName = "iGlobalSolarRadiation";
            pd3.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd4.PropertyName = "iRAIN";
            pd4.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd5.PropertyName = "iCropResidues";
            pd5.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd6.PropertyName = "iPotentialSoilEvaporation";
            pd6.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd7.PropertyName = "iLeafAreaIndex";
            pd7.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd8.PropertyName = "SoilTempArray";
            pd8.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd9.PropertyName = "iSoilWaterContent";
            pd9.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd10.PropertyName = "Albedo";
            pd10.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd11.PropertyName = "SnowWaterContent";
            pd11.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd12.PropertyName = "SoilSurfaceTemperature";
            pd12.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd13.PropertyName = "AgeOfSnow";
            pd13.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd14.PropertyName = "pSoilLayerDepth";
            pd14.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth);
            _inputs0_0.Add(pd14);
            mo0_0.Inputs=_inputs0_0;
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd15.PropertyName = "SoilSurfaceTemperature";
            pd15.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
            _outputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary);
            pd16.PropertyName = "SnowIsolationIndex";
            pd16.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex);
            _outputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd17.PropertyName = "SnowWaterContent";
            pd17.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
            _outputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd18.PropertyName = "SoilTempArray";
            pd18.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
            _outputs0_0.Add(pd18);
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd19.PropertyName = "AgeOfSnow";
            pd19.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
            _outputs0_0.Add(pd19);
            mo0_0.Outputs=_outputs0_0;
            List<string> lAssStrat0_0 = new List<string>();
            lAssStrat0_0.Add(typeof(SiriusQualitySoilTemperature.Strategies.SnowCoverCalculator).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualitySoilTemperature.Strategies.STMPsimCalculator).FullName);
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();
        }

        public string Description
        {
            get { return "as given in the documentation" ;}
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
            _pd.Add("Creator", "Gunther Krauss");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRES Pflanzenbau, Uni Bonn "); 
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous)};
        }

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

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
            _SnowCoverCalculator.SetParametersDefaultValue();
            _STMPsimCalculator.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            cCarbonContentVarInfo.Name = "cCarbonContent";
            cCarbonContentVarInfo.Description = "Carbon content of upper soil layer";
            cCarbonContentVarInfo.MaxValue = 20.0;
            cCarbonContentVarInfo.MinValue = 0.0;
            cCarbonContentVarInfo.DefaultValue = 0.5;
            cCarbonContentVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/percent";
            cCarbonContentVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            cSoilLayerDepthVarInfo.Name = "cSoilLayerDepth";
            cSoilLayerDepthVarInfo.Description = "Depth of soil layer";
            cSoilLayerDepthVarInfo.MaxValue = -1D;
            cSoilLayerDepthVarInfo.MinValue = -1D;
            cSoilLayerDepthVarInfo.DefaultValue = -1D;
            cSoilLayerDepthVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/metre";
            cSoilLayerDepthVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            cFirstDayMeanTempVarInfo.Name = "cFirstDayMeanTemp";
            cFirstDayMeanTempVarInfo.Description = "Mean temperature on first day";
            cFirstDayMeanTempVarInfo.MaxValue = 50.0;
            cFirstDayMeanTempVarInfo.MinValue = -40.0;
            cFirstDayMeanTempVarInfo.DefaultValue = -1D;
            cFirstDayMeanTempVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            cFirstDayMeanTempVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            cAverageGroundTemperatureVarInfo.Name = "cAverageGroundTemperature";
            cAverageGroundTemperatureVarInfo.Description = "Constant Temperature of deepest soil layer";
            cAverageGroundTemperatureVarInfo.MaxValue = 20.0;
            cAverageGroundTemperatureVarInfo.MinValue = -10.0;
            cAverageGroundTemperatureVarInfo.DefaultValue = -1D;
            cAverageGroundTemperatureVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            cAverageGroundTemperatureVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            cAverageBulkDensityVarInfo.Name = "cAverageBulkDensity";
            cAverageBulkDensityVarInfo.Description = "Mean bulk density";
            cAverageBulkDensityVarInfo.MaxValue = 4.0;
            cAverageBulkDensityVarInfo.MinValue = 1.0;
            cAverageBulkDensityVarInfo.DefaultValue = 2.0;
            cAverageBulkDensityVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre";
            cAverageBulkDensityVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            cDampingDepthVarInfo.Name = "cDampingDepth";
            cDampingDepthVarInfo.Description = "Initial value for damping depth of soil";
            cDampingDepthVarInfo.MaxValue = 20.0;
            cDampingDepthVarInfo.MinValue = 1.5;
            cDampingDepthVarInfo.DefaultValue = 6.0;
            cDampingDepthVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/metre";
            cDampingDepthVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        public static VarInfo cCarbonContentVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.SnowCoverCalculator.cCarbonContentVarInfo;} 
        }

        public static VarInfo cSoilLayerDepthVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cSoilLayerDepthVarInfo;} 
        }

        public static VarInfo cFirstDayMeanTempVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cFirstDayMeanTempVarInfo;} 
        }

        public static VarInfo cAverageGroundTemperatureVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cAverageGroundTemperatureVarInfo;} 
        }

        public static VarInfo cAVTVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cAVTVarInfo;} 
        }

        public static VarInfo cAverageBulkDensityVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cAverageBulkDensityVarInfo;} 
        }

        public static VarInfo cABDVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cABDVarInfo;} 
        }

        public static VarInfo cDampingDepthVarInfo
        {
            get { return SiriusQualitySoilTemperature.Strategies.STMPsimCalculator.cDampingDepthVarInfo;} 
        }

        public string TestPostConditions(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.CurrentValue=s.SoilSurfaceTemperature;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex.CurrentValue=a.SnowIsolationIndex;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.CurrentValue=s.SnowWaterContent;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.CurrentValue=s.SoilTempArray;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.CurrentValue=s.AgeOfSnow;

                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 

                RangeBasedCondition r21 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
                if(r21.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.ValueType)){prc.AddCondition(r21);}
                RangeBasedCondition r22 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex);
                if(r22.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex.ValueType)){prc.AddCondition(r22);}
                RangeBasedCondition r23 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
                if(r23.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.ValueType)){prc.AddCondition(r23);}
                RangeBasedCondition r24 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
                if(r24.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.ValueType)){prc.AddCondition(r24);}
                RangeBasedCondition r25 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
                if(r25.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.ValueType)){prc.AddCondition(r25);}

                string ret = "";
                ret += _SnowCoverCalculator.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualitySoilTemperature.Strategies.SoilTemperature");
                ret += _STMPsimCalculator.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualitySoilTemperature.Strategies.SoilTemperature");
                if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }

                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.SoilTemperature, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax.CurrentValue=ex.iAirTemperatureMax;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin.CurrentValue=ex.iAirTemperatureMin;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation.CurrentValue=ex.iGlobalSolarRadiation;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN.CurrentValue=ex.iRAIN;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues.CurrentValue=ex.iCropResidues;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation.CurrentValue=ex.iPotentialSoilEvaporation;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex.CurrentValue=ex.iLeafAreaIndex;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray.CurrentValue=ex.SoilTempArray;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent.CurrentValue=ex.iSoilWaterContent;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo.CurrentValue=s.Albedo;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.CurrentValue=s.SnowWaterContent;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.CurrentValue=s.SoilSurfaceTemperature;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.CurrentValue=s.AgeOfSnow;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth.CurrentValue=s.pSoilLayerDepth;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
                if(r13.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth.ValueType)){prc.AddCondition(r14);}

                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cCarbonContent")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cSoilLayerDepth")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cFirstDayMeanTemp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cAverageGroundTemperature")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cAverageBulkDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cDampingDepth")));
                string ret = "";
                ret += _SnowCoverCalculator.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualitySoilTemperature.Strategies.SoilTemperature");
                ret += _STMPsimCalculator.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualitySoilTemperature.Strategies.SoilTemperature");
                if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }

                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.SoilTemperature, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualitySoilTemperature, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            EstimateOfAssociatedClasses(s, s1, r, a, ex);
        }

        //Declaration of the associated strategies
        SnowCoverCalculator _SnowCoverCalculator = new SnowCoverCalculator();
        STMPsimCalculator _STMPsimCalculator = new STMPsimCalculator();

        private void EstimateOfAssociatedClasses(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            ex.iTempMax = ex.iAirTemperatureMax;
            ex.iTempMin = ex.iAirTemperatureMin;
            ex.iRadiation = ex.iGlobalSolarRadiation;
            ex.iSoilTempArray = s.SoilTempArray;
            cAVT = cAverageGroundTemperature;
            cABD = cAverageBulkDensity;
            _SnowCoverCalculator.Estimate(s,s1, r, a, ex);
            ex.iSoilSurfaceTemperature = s.SoilSurfaceTemperature;
            _STMPsimCalculator.Estimate(s,s1, r, a, ex);
        }

        public SoilTemperatureComponent(SoilTemperatureComponent toCopy): this() // copy constructor 
        {
                cCarbonContent = toCopy.cCarbonContent;
                
            for (int i = 0; i < toCopy._cSoilLayerDepth.Length; i++)
            { _cSoilLayerDepth[i] = toCopy._cSoilLayerDepth[i]; }
    
                cFirstDayMeanTemp = toCopy.cFirstDayMeanTemp;
                cAverageGroundTemperature = toCopy.cAverageGroundTemperature;
                cAVT = toCopy.cAVT;
                cAverageBulkDensity = toCopy.cAverageBulkDensity;
                cABD = toCopy.cABD;
                cDampingDepth = toCopy.cDampingDepth;
        }
    }
}