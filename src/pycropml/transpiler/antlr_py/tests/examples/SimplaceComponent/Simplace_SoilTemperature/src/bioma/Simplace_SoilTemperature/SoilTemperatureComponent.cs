
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

using SoilTemperature.DomainClass;
namespace SoilTemperature.Strategies
{
    public class SoilTemperatureComponent : IStrategySoilTemperature
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
            pd1.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd1.PropertyName = "iAirTemperatureMax";
            pd1.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd2.PropertyName = "iAirTemperatureMin";
            pd2.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd3.PropertyName = "iGlobalSolarRadiation";
            pd3.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd4.PropertyName = "iRAIN";
            pd4.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd5.PropertyName = "iCropResidues";
            pd5.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd6.PropertyName = "iPotentialSoilEvaporation";
            pd6.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd7.PropertyName = "iLeafAreaIndex";
            pd7.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd8.PropertyName = "SoilTempArray";
            pd8.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd9.PropertyName = "iSoilWaterContent";
            pd9.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd10.PropertyName = "Albedo";
            pd10.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd11.PropertyName = "SnowWaterContent";
            pd11.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd12.PropertyName = "SoilSurfaceTemperature";
            pd12.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd13.PropertyName = "AgeOfSnow";
            pd13.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd14.PropertyName = "pSoilLayerDepth";
            pd14.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth);
            _inputs0_0.Add(pd14);
            mo0_0.Inputs=_inputs0_0;
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd15.PropertyName = "SoilSurfaceTemperature";
            pd15.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
            _outputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureAuxiliary);
            pd16.PropertyName = "SnowIsolationIndex";
            pd16.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex);
            _outputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd17.PropertyName = "SnowWaterContent";
            pd17.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
            _outputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd18.PropertyName = "SoilTempArray";
            pd18.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
            _outputs0_0.Add(pd18);
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SoilTemperature.DomainClass.SoilTemperatureState);
            pd19.PropertyName = "AgeOfSnow";
            pd19.PropertyType = (SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
            _outputs0_0.Add(pd19);
            mo0_0.Outputs=_outputs0_0;
            List<string> lAssStrat0_0 = new List<string>();
            lAssStrat0_0.Add(typeof(SoilTemperature.Strategies.SnowCoverCalculator).FullName);
            lAssStrat0_0.Add(typeof(SoilTemperature.Strategies.STMPsimCalculator).FullName);
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
            return new List<Type>() {  typeof(SoilTemperature.DomainClass.SoilTemperatureState), typeof(SoilTemperature.DomainClass.SoilTemperatureState), typeof(SoilTemperature.DomainClass.SoilTemperatureRate), typeof(SoilTemperature.DomainClass.SoilTemperatureAuxiliary), typeof(SoilTemperature.DomainClass.SoilTemperatureExogenous)};
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
            cSoilLayerDepthVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

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
            get { return SoilTemperature.Strategies.SnowCoverCalculator.cCarbonContentVarInfo;} 
        }

        public static VarInfo cSoilLayerDepthVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cSoilLayerDepthVarInfo;} 
        }

        public static VarInfo cFirstDayMeanTempVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cFirstDayMeanTempVarInfo;} 
        }

        public static VarInfo cAverageGroundTemperatureVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cAverageGroundTemperatureVarInfo;} 
        }

        public static VarInfo cAVTVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cAVTVarInfo;} 
        }

        public static VarInfo cAverageBulkDensityVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cAverageBulkDensityVarInfo;} 
        }

        public static VarInfo cABDVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cABDVarInfo;} 
        }

        public static VarInfo cDampingDepthVarInfo
        {
            get { return SoilTemperature.Strategies.STMPsimCalculator.cDampingDepthVarInfo;} 
        }

        public string TestPostConditions(SoilTemperature.DomainClass.SoilTemperatureState s,SoilTemperature.DomainClass.SoilTemperatureState s1,SoilTemperature.DomainClass.SoilTemperatureRate r,SoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SoilTemperature.DomainClass.SoilTemperatureExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.CurrentValue=s.SoilSurfaceTemperature;
                SoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex.CurrentValue=a.SnowIsolationIndex;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.CurrentValue=s.SnowWaterContent;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.CurrentValue=s.SoilTempArray;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.CurrentValue=s.AgeOfSnow;

                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 

                RangeBasedCondition r21 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
                if(r21.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.ValueType)){prc.AddCondition(r21);}
                RangeBasedCondition r22 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex);
                if(r22.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureAuxiliaryVarInfo.SnowIsolationIndex.ValueType)){prc.AddCondition(r22);}
                RangeBasedCondition r23 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
                if(r23.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.ValueType)){prc.AddCondition(r23);}
                RangeBasedCondition r24 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
                if(r24.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.ValueType)){prc.AddCondition(r24);}
                RangeBasedCondition r25 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
                if(r25.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.ValueType)){prc.AddCondition(r25);}

                string ret = "";
                ret += _SnowCoverCalculator.TestPostConditions(s, s1, r, a, ex, " strategy SoilTemperature.Strategies.SoilTemperature");
                ret += _STMPsimCalculator.TestPostConditions(s, s1, r, a, ex, " strategy SoilTemperature.Strategies.SoilTemperature");
                if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }

                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component .SoilTemperature, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SoilTemperature.DomainClass.SoilTemperatureState s,SoilTemperature.DomainClass.SoilTemperatureState s1,SoilTemperature.DomainClass.SoilTemperatureRate r,SoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SoilTemperature.DomainClass.SoilTemperatureExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax.CurrentValue=ex.iAirTemperatureMax;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin.CurrentValue=ex.iAirTemperatureMin;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation.CurrentValue=ex.iGlobalSolarRadiation;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN.CurrentValue=ex.iRAIN;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues.CurrentValue=ex.iCropResidues;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation.CurrentValue=ex.iPotentialSoilEvaporation;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex.CurrentValue=ex.iLeafAreaIndex;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray.CurrentValue=ex.SoilTempArray;
                SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent.CurrentValue=ex.iSoilWaterContent;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo.CurrentValue=s.Albedo;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.CurrentValue=s.SnowWaterContent;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.CurrentValue=s.SoilSurfaceTemperature;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.CurrentValue=s.AgeOfSnow;
                SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth.CurrentValue=s.pSoilLayerDepth;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax);
                if(r1.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMax.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin);
                if(r2.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iAirTemperatureMin.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation);
                if(r3.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iGlobalSolarRadiation.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN);
                if(r4.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iRAIN.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues);
                if(r5.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iCropResidues.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation);
                if(r6.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iPotentialSoilEvaporation.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex);
                if(r7.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iLeafAreaIndex.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray);
                if(r8.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.SoilTempArray.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent);
                if(r9.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo);
                if(r10.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.Albedo.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent);
                if(r11.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SnowWaterContent.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature);
                if(r12.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilSurfaceTemperature.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow);
                if(r13.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.AgeOfSnow.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth);
                if(r14.ApplicableVarInfoValueTypes.Contains( SoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth.ValueType)){prc.AddCondition(r14);}

                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cCarbonContent")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cSoilLayerDepth")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cFirstDayMeanTemp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cAverageGroundTemperature")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cAverageBulkDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cDampingDepth")));
                string ret = "";
                ret += _SnowCoverCalculator.TestPreConditions(s, s1, r, a, ex, " strategy SoilTemperature.Strategies.SoilTemperature");
                ret += _STMPsimCalculator.TestPreConditions(s, s1, r, a, ex, " strategy SoilTemperature.Strategies.SoilTemperature");
                if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }

                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component .SoilTemperature, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SoilTemperature.DomainClass.SoilTemperatureState s,SoilTemperature.DomainClass.SoilTemperatureState s1,SoilTemperature.DomainClass.SoilTemperatureRate r,SoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SoilTemperature, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SoilTemperature.DomainClass.SoilTemperatureState s,SoilTemperature.DomainClass.SoilTemperatureState s1,SoilTemperature.DomainClass.SoilTemperatureRate r,SoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            EstimateOfAssociatedClasses(s, s1, r, a, ex);
        }

        //Declaration of the associated strategies
        SnowCoverCalculator _SnowCoverCalculator = new SnowCoverCalculator();
        STMPsimCalculator _STMPsimCalculator = new STMPsimCalculator();

        private void EstimateOfAssociatedClasses(SoilTemperature.DomainClass.SoilTemperatureState s,SoilTemperature.DomainClass.SoilTemperatureState s1,SoilTemperature.DomainClass.SoilTemperatureRate r,SoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            ex.iTempMax = ex.iAirTemperatureMax;
            ex.iTempMin = ex.iAirTemperatureMin;
            ex.iRadiation = ex.iGlobalSolarRadiation;
            ex.iSoilTempArray = s.SoilTempArray;
            cAVT = cAverageGroundTemperature;
            cABD = cAverageBulkDensity;
            _snowcovercalculator.Estimate(s,s1, r, a, ex);
            ex.iSoilSurfaceTemperature = s.SoilSurfaceTemperature;
            _stmpsimcalculator.Estimate(s,s1, r, a, ex);
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