
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
    public class WithSnowSoilSurfaceTemperature : IStrategySoilTemperatureComp
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
            pd1.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd1.PropertyName = "noSnowSoilSurfaceTemperature";
            pd1.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd2.PropertyName = "soilSurfaceTemperatureBelowSnow";
            pd2.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous);
            pd3.PropertyName = "hasSnowCover";
            pd3.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover);
            _inputs0_0.Add(pd3);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState);
            pd4.PropertyName = "soilSurfaceTemperature";
            pd4.PropertyType = (SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
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
            return new List<Type>() {  typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState),  typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompState), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompRate), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary), typeof(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.


        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {
        }

        public string TestPostConditions(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.CurrentValue=s.soilSurfaceTemperature;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r4 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature);
                if(r4.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.soilSurfaceTemperature.ValueType)){prc.AddCondition(r4);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = ".SoilTemperatureComp, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s,SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1,SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r,SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a,SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature.CurrentValue=s.noSnowSoilSurfaceTemperature;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow.CurrentValue=ex.soilSurfaceTemperatureBelowSnow;
                SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover.CurrentValue=ex.hasSnowCover;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature);
                if(r1.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompStateVarInfo.noSnowSoilSurfaceTemperature.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow);
                if(r2.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.soilSurfaceTemperatureBelowSnow.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover);
                if(r3.ApplicableVarInfoValueTypes.Contains( SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenousVarInfo.hasSnowCover.ValueType)){prc.AddCondition(r3);}
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = ".SoilTemperatureComp, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
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

        private void CalculateModel(SoilTemperatureComp.DomainClass.SoilTemperatureCompState s, SoilTemperatureComp.DomainClass.SoilTemperatureCompState s1, SoilTemperatureComp.DomainClass.SoilTemperatureCompRate r, SoilTemperatureComp.DomainClass.SoilTemperatureCompAuxiliary a, SoilTemperatureComp.DomainClass.SoilTemperatureCompExogenous ex)
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