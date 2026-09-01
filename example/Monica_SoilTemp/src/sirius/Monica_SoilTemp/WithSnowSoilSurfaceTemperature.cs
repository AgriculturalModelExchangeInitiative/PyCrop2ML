
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
    public class WithSnowSoilSurfaceTemperature : IStrategySiriusQualitySoilTemperatureComp
    {
        public WithSnowSoilSurfaceTemperature()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd1.PropertyName = "noSnowSoilSurfaceTemperature";
            pd1.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd2.PropertyName = "soilSurfaceTemperatureBelowSnow";
            pd2.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd3.PropertyName = "hasSnowCover";
            pd3.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover);
            _inputs0_0.Add(pd3);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd4.PropertyName = "soilSurfaceTemperature";
            pd4.PropertyType = (SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
            _outputs0_0.Add(pd4);
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


        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {
        }

        public string TestPostConditions(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.CurrentValue=s.soilSurfaceTemperature;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.ValueType)){prc.AddCondition(r4);}
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
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature.CurrentValue=s.noSnowSoilSurfaceTemperature;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow.CurrentValue=ex.soilSurfaceTemperatureBelowSnow;
                SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover.CurrentValue=ex.hasSnowCover;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover.ValueType)){prc.AddCondition(r3);}
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

        private void CalculateModel(SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompState s1, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompRate r, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a, SiriusQualitySoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
        {
            double noSnowSoilSurfaceTemperature = s.noSnowSoilSurfaceTemperature;
            double soilSurfaceTemperatureBelowSnow = ex.soilSurfaceTemperatureBelowSnow;
            bool hasSnowCover = ex.hasSnowCover;
            double soilSurfaceTemperature;
            if (hasSnowCover)
            {
                soilSurfaceTemperature = soilSurfaceTemperatureBelowSnow;
            }
            else
            {
                soilSurfaceTemperature = noSnowSoilSurfaceTemperature;
            }
            s.soilSurfaceTemperature= soilSurfaceTemperature;
        }

    }
}