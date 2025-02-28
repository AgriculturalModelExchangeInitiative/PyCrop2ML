
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
using SiriusQualityPhenology.DomainClass;
namespace SiriusQualityPhenology.Strategies
{
    public class RegisterZadok : IStrategySiriusQualityPhenology
    {
        public RegisterZadok()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 2.6;
            v1.Description = "Intercept of the relationship between Haun stage at terminal spikelet and final leaf number";
            v1.Id = 0;
            v1.MaxValue = 10000;
            v1.MinValue = 0;
            v1.Name = "intTSFLN";
            v1.Size = 1;
            v1.Units = "";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 300.0;
            v2.Description = "Duration of the endosperm endoreduplication phase";
            v2.Id = 0;
            v2.MaxValue = 10000;
            v2.MinValue = 0;
            v2.Name = "der";
            v2.Size = 1;
            v2.Units = "Â°C d";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 0.9;
            v3.Description = "Slope of the relationship between Haun stage at terminal spikelet and final leaf number";
            v3.Id = 0;
            v3.MaxValue = 10000;
            v3.MinValue = 0;
            v3.Name = "slopeTSFLN";
            v3.Size = 1;
            v3.Units = "";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd1.PropertyName = "calendarCumuls";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd2.PropertyName = "finalLeafNumber";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd3.PropertyName = "cumulTTFromZC_65";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_65).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_65);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd4.PropertyName = "calendarMoments";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd5.PropertyName = "cumulTT";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd6.PropertyName = "calendarDates";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd7.PropertyName = "leafNumber";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "currentZadokStage";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd9.PropertyName = "phase";
            pd9.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd10.PropertyName = "currentdate";
            pd10.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate);
            _inputs0_0.Add(pd10);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd11.PropertyName = "calendarCumuls";
            pd11.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
            _outputs0_0.Add(pd11);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd12.PropertyName = "currentZadokStage";
            pd12.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
            _outputs0_0.Add(pd12);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd13.PropertyName = "calendarMoments";
            pd13.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
            _outputs0_0.Add(pd13);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd14.PropertyName = "calendarDates";
            pd14.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
            _outputs0_0.Add(pd14);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd15.PropertyName = "hasZadokStageChanged";
            pd15.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged);
            _outputs0_0.Add(pd15);
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
            get { return "Record the zadok stage in the calendar    	" ;}
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
            _pd.Add("Creator", "Pierre MARTRE");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA/LEPSE Montpellier "); 
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityPhenology.DomainClass.PhenologyState),  typeof(SiriusQualityPhenology.DomainClass.PhenologyState), typeof(SiriusQualityPhenology.DomainClass.PhenologyRate), typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary), typeof(SiriusQualityPhenology.DomainClass.PhenologyExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double intTSFLN
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("intTSFLN");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'intTSFLN' not found (or found null) in strategy 'RegisterZadok'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("intTSFLN");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'intTSFLN' not found in strategy 'RegisterZadok'");
            }
        }
        public double der
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("der");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'der' not found (or found null) in strategy 'RegisterZadok'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("der");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'der' not found in strategy 'RegisterZadok'");
            }
        }
        public double slopeTSFLN
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("slopeTSFLN");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'slopeTSFLN' not found (or found null) in strategy 'RegisterZadok'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("slopeTSFLN");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'slopeTSFLN' not found in strategy 'RegisterZadok'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            intTSFLNVarInfo.Name = "intTSFLN";
            intTSFLNVarInfo.Description = "Intercept of the relationship between Haun stage at terminal spikelet and final leaf number";
            intTSFLNVarInfo.MaxValue = 10000;
            intTSFLNVarInfo.MinValue = 0;
            intTSFLNVarInfo.DefaultValue = 2.6;
            intTSFLNVarInfo.Units = "";
            intTSFLNVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            derVarInfo.Name = "der";
            derVarInfo.Description = "Duration of the endosperm endoreduplication phase";
            derVarInfo.MaxValue = 10000;
            derVarInfo.MinValue = 0;
            derVarInfo.DefaultValue = 300.0;
            derVarInfo.Units = "Â°C d";
            derVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            slopeTSFLNVarInfo.Name = "slopeTSFLN";
            slopeTSFLNVarInfo.Description = "Slope of the relationship between Haun stage at terminal spikelet and final leaf number";
            slopeTSFLNVarInfo.MaxValue = 10000;
            slopeTSFLNVarInfo.MinValue = 0;
            slopeTSFLNVarInfo.DefaultValue = 0.9;
            slopeTSFLNVarInfo.Units = "";
            slopeTSFLNVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _intTSFLNVarInfo = new VarInfo();
        public static VarInfo intTSFLNVarInfo
        {
            get { return _intTSFLNVarInfo;} 
        }

        private static VarInfo _derVarInfo = new VarInfo();
        public static VarInfo derVarInfo
        {
            get { return _derVarInfo;} 
        }

        private static VarInfo _slopeTSFLNVarInfo = new VarInfo();
        public static VarInfo slopeTSFLNVarInfo
        {
            get { return _slopeTSFLNVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.CurrentValue=s.calendarCumuls;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.CurrentValue=s.currentZadokStage;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.CurrentValue=s.calendarMoments;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.CurrentValue=s.calendarDates;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged.CurrentValue=s.hasZadokStageChanged;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
                if(r15.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.ValueType)){prc.AddCondition(r15);}
                RangeBasedCondition r16 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
                if(r16.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.ValueType)){prc.AddCondition(r16);}
                RangeBasedCondition r17 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
                if(r17.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.ValueType)){prc.AddCondition(r17);}
                RangeBasedCondition r18 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged);
                if(r18.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.hasZadokStageChanged.ValueType)){prc.AddCondition(r18);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.CurrentValue=s.calendarCumuls;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.CurrentValue=s.finalLeafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_65.CurrentValue=a.cumulTTFromZC_65;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.CurrentValue=s.calendarMoments;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.CurrentValue=a.cumulTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.CurrentValue=s.calendarDates;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.CurrentValue=s.currentZadokStage;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.CurrentValue=s.phase;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate.CurrentValue=a.currentdate;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarCumuls.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.finalLeafNumber.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_65);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTTFromZC_65.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarMoments.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.cumulTT.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.calendarDates.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.currentZadokStage.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phase.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.currentdate.ValueType)){prc.AddCondition(r10);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("intTSFLN")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("der")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("slopeTSFLN")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityPhenology, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualityPhenology.DomainClass.PhenologyState s, SiriusQualityPhenology.DomainClass.PhenologyState s1, SiriusQualityPhenology.DomainClass.PhenologyRate r, SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a, SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            List<double> calendarCumuls = s.calendarCumuls;
            double finalLeafNumber = s.finalLeafNumber;
            double cumulTTFromZC_65 = a.cumulTTFromZC_65;
            List<string> calendarMoments = s.calendarMoments;
            double cumulTT = a.cumulTT;
            List<DateTime> calendarDates = s.calendarDates;
            double leafNumber = s.leafNumber;
            string currentZadokStage_t1 = s1.currentZadokStage;
            double phase = s.phase;
            DateTime currentdate = a.currentdate;
            string currentZadokStage;
            int hasZadokStageChanged;
            int roundedFinalLeafNumber;
            currentZadokStage = currentZadokStage_t1;
            roundedFinalLeafNumber = (int)(finalLeafNumber + 0.5d);
            if (leafNumber >= 4.0d && !calendarMoments.Contains("MainShootPlus1Tiller"))
            {
                calendarMoments.Add("MainShootPlus1Tiller");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "MainShootPlus1Tiller";
            }
            else if ( leafNumber >= 5.0d && !calendarMoments.Contains("MainShootPlus2Tiller"))
            {
                calendarMoments.Add("MainShootPlus2Tiller");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "MainShootPlus2Tiller";
            }
            else if ( leafNumber >= 6.0d && !calendarMoments.Contains("MainShootPlus3Tiller"))
            {
                calendarMoments.Add("MainShootPlus3Tiller");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "MainShootPlus3Tiller";
            }
            else if ( finalLeafNumber > 0.0d && (leafNumber >= (slopeTSFLN * finalLeafNumber - intTSFLN) && !calendarMoments.Contains("TerminalSpikelet")))
            {
                calendarMoments.Add("TerminalSpikelet");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "TerminalSpikelet";
            }
            else if ( leafNumber >= (roundedFinalLeafNumber - 4.0d) && (roundedFinalLeafNumber - 4 > 0 && !calendarMoments.Contains("PseudoStemErection")))
            {
                calendarMoments.Add("PseudoStemErection");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "PseudoStemErection";
            }
            else if ( leafNumber >= (roundedFinalLeafNumber - 3.0d) && (roundedFinalLeafNumber - 3 > 0 && !calendarMoments.Contains("1stNodeDetectable")))
            {
                calendarMoments.Add("1stNodeDetectable");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "1stNodeDetectable";
            }
            else if ( leafNumber >= (roundedFinalLeafNumber - 2.0d) && (roundedFinalLeafNumber - 2 > 0 && !calendarMoments.Contains("2ndNodeDetectable")))
            {
                calendarMoments.Add("2ndNodeDetectable");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "2ndNodeDetectable";
            }
            else if ( leafNumber >= (roundedFinalLeafNumber - 1.0d) && (roundedFinalLeafNumber - 1 > 0 && !calendarMoments.Contains("FlagLeafJustVisible")))
            {
                calendarMoments.Add("FlagLeafJustVisible");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "FlagLeafJustVisible";
            }
            else if ( !calendarMoments.Contains("MidGrainFilling") && (phase == 4.5d && cumulTTFromZC_65 >= der))
            {
                calendarMoments.Add("MidGrainFilling");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                hasZadokStageChanged = 1;
                currentZadokStage = "MidGrainFilling";
            }
            else
            {
                hasZadokStageChanged = 0;
            }
            s.calendarCumuls= calendarCumuls;
            s.calendarMoments= calendarMoments;
            s.calendarDates= calendarDates;
            s.currentZadokStage= currentZadokStage;
            s.hasZadokStageChanged= hasZadokStageChanged;
        }

    }
}