
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
using SiriusQualityEnergyBalance.DomainClass;
namespace SiriusQualityEnergyBalance.Strategies
{
    public class EvapoTranspiration : IStrategySiriusQualityEnergyBalance
    {
        public EvapoTranspiration()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 1;
            v1.Description = "if wind and vapour pressure are defined";
            v1.Id = 0;
            v1.MaxValue = 1;
            v1.MinValue = 0;
            v1.Name = "isWindVpDefined";
            v1.Size = 1;
            v1.Units = "";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v1);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd1.PropertyName = "evapoTranspirationPriestlyTaylor";
            pd1.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd2.PropertyName = "evapoTranspirationPenman";
            pd2.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman);
            _inputs0_0.Add(pd2);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd3.PropertyName = "evapoTranspiration";
            pd3.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration);
            _outputs0_0.Add(pd3);
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
            get { return "According to the availability of wind and/or vapor pressure daily data, the            SiriusQuality2 model calculates the evapotranspiration rate using the Penman (if wind            and vapor pressure data are available) (Penman 1948) or the Priestly-Taylor            (Priestley and Taylor 1972) method " ;}
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
            _pd.Add("Creator", "Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. "); 
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState),  typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public int isWindVpDefined
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("isWindVpDefined");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'isWindVpDefined' not found (or found null) in strategy 'EvapoTranspiration'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("isWindVpDefined");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'isWindVpDefined' not found in strategy 'EvapoTranspiration'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            isWindVpDefinedVarInfo.Name = "isWindVpDefined";
            isWindVpDefinedVarInfo.Description = "if wind and vapour pressure are defined";
            isWindVpDefinedVarInfo.MaxValue = 1;
            isWindVpDefinedVarInfo.MinValue = 0;
            isWindVpDefinedVarInfo.DefaultValue = 1;
            isWindVpDefinedVarInfo.Units = "";
            isWindVpDefinedVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
        }

        private static VarInfo _isWindVpDefinedVarInfo = new VarInfo();
        public static VarInfo isWindVpDefinedVarInfo
        {
            get { return _isWindVpDefinedVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration.CurrentValue=r.evapoTranspiration;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration.ValueType)){prc.AddCondition(r4);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.EnergyBalance, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor.CurrentValue=r.evapoTranspirationPriestlyTaylor;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman.CurrentValue=r.evapoTranspirationPenman;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman.ValueType)){prc.AddCondition(r2);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("isWindVpDefined")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.EnergyBalance, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityEnergyBalance, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s, SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1, SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r, SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a, SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex)
        {
            double evapoTranspirationPriestlyTaylor = r.evapoTranspirationPriestlyTaylor;
            double evapoTranspirationPenman = r.evapoTranspirationPenman;
            double evapoTranspiration;
            if (isWindVpDefined == 1)
            {
                evapoTranspiration = evapoTranspirationPenman;
            }
            else
            {
                evapoTranspiration = evapoTranspirationPriestlyTaylor;
            }
            r.evapoTranspiration = evapoTranspiration;
        }

    }
}