
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
    public class CanopyTemperature : IStrategySiriusQualityEnergyBalance
    {
        public CanopyTemperature()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 2.454;
            v1.Description = "latent heat of vaporization of water";
            v1.Id = 0;
            v1.MaxValue = 10;
            v1.MinValue = 0;
            v1.Name = "lambdaV";
            v1.Size = 1;
            v1.Units = "MJ/kg";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 1.225;
            v2.Description = "Density of air";
            v2.Id = 0;
            v2.MaxValue = 1.225;
            v2.MinValue = 1.225;
            v2.Name = "rhoDensityAir";
            v2.Size = 1;
            v2.Units = "kg/m**3";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 0.00101;
            v3.Description = "Specific heat capacity of dry air";
            v3.Id = 0;
            v3.MaxValue = 0.00101;
            v3.MinValue = 0.00101;
            v3.Name = "specificHeatCapacityAir";
            v3.Size = 1;
            v3.Units = "MJ/kg/degC";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd1.PropertyName = "minTair";
            pd1.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd2.PropertyName = "maxTair";
            pd2.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd3.PropertyName = "cropHeatFlux";
            pd3.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd4.PropertyName = "conductance";
            pd4.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance);
            _inputs0_0.Add(pd4);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd5.PropertyName = "minCanopyTemperature";
            pd5.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature);
            _outputs0_0.Add(pd5);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd6.PropertyName = "maxCanopyTemperature";
            pd6.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature);
            _outputs0_0.Add(pd6);
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
            get { return "It is calculated from the crop heat flux and the boundary layer conductance " ;}
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

        public double lambdaV
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lambdaV");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lambdaV' not found (or found null) in strategy 'CanopyTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("lambdaV");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lambdaV' not found in strategy 'CanopyTemperature'");
            }
        }
        public double rhoDensityAir
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("rhoDensityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'rhoDensityAir' not found (or found null) in strategy 'CanopyTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("rhoDensityAir");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'rhoDensityAir' not found in strategy 'CanopyTemperature'");
            }
        }
        public double specificHeatCapacityAir
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("specificHeatCapacityAir");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found (or found null) in strategy 'CanopyTemperature'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("specificHeatCapacityAir");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'specificHeatCapacityAir' not found in strategy 'CanopyTemperature'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            lambdaVVarInfo.Name = "lambdaV";
            lambdaVVarInfo.Description = "latent heat of vaporization of water";
            lambdaVVarInfo.MaxValue = 10;
            lambdaVVarInfo.MinValue = 0;
            lambdaVVarInfo.DefaultValue = 2.454;
            lambdaVVarInfo.Units = "MJ/kg";
            lambdaVVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            rhoDensityAirVarInfo.Name = "rhoDensityAir";
            rhoDensityAirVarInfo.Description = "Density of air";
            rhoDensityAirVarInfo.MaxValue = 1.225;
            rhoDensityAirVarInfo.MinValue = 1.225;
            rhoDensityAirVarInfo.DefaultValue = 1.225;
            rhoDensityAirVarInfo.Units = "kg/m**3";
            rhoDensityAirVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            specificHeatCapacityAirVarInfo.Name = "specificHeatCapacityAir";
            specificHeatCapacityAirVarInfo.Description = "Specific heat capacity of dry air";
            specificHeatCapacityAirVarInfo.MaxValue = 0.00101;
            specificHeatCapacityAirVarInfo.MinValue = 0.00101;
            specificHeatCapacityAirVarInfo.DefaultValue = 0.00101;
            specificHeatCapacityAirVarInfo.Units = "MJ/kg/degC";
            specificHeatCapacityAirVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _lambdaVVarInfo = new VarInfo();
        public static VarInfo lambdaVVarInfo
        {
            get { return _lambdaVVarInfo;} 
        }

        private static VarInfo _rhoDensityAirVarInfo = new VarInfo();
        public static VarInfo rhoDensityAirVarInfo
        {
            get { return _rhoDensityAirVarInfo;} 
        }

        private static VarInfo _specificHeatCapacityAirVarInfo = new VarInfo();
        public static VarInfo specificHeatCapacityAirVarInfo
        {
            get { return _specificHeatCapacityAirVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature.CurrentValue=s.minCanopyTemperature;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature.CurrentValue=s.maxCanopyTemperature;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature.ValueType)){prc.AddCondition(r9);}
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
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair.CurrentValue=a.minTair;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair.CurrentValue=a.maxTair;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux.CurrentValue=r.cropHeatFlux;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance.CurrentValue=s.conductance;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance.ValueType)){prc.AddCondition(r4);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lambdaV")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("rhoDensityAir")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("specificHeatCapacityAir")));
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
            double minTair = a.minTair;
            double maxTair = a.maxTair;
            double cropHeatFlux = r.cropHeatFlux;
            double conductance = s.conductance;
            double minCanopyTemperature;
            double maxCanopyTemperature;
            minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0d));
            maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0d));
            s.minCanopyTemperature= minCanopyTemperature;
            s.maxCanopyTemperature= maxCanopyTemperature;
        }

    }
}