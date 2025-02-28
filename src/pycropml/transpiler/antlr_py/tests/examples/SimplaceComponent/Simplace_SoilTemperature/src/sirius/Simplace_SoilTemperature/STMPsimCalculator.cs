
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
    public class STMPsimCalculator : IStrategySiriusQualitySoilTemperature
    {
        public STMPsimCalculator()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = -1D;
            v1.Description = "Depth of soil layer";
            v1.Id = 0;
            v1.MaxValue = -1D;
            v1.MinValue = -1D;
            v1.Name = "cSoilLayerDepth";
            v1.Size = 1;
            v1.Units = "http://www.wurvoc.org/vocabularies/om-1.8/metre";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = -1D;
            v2.Description = "Mean temperature on first day";
            v2.Id = 0;
            v2.MaxValue = 50.0;
            v2.MinValue = -40.0;
            v2.Name = "cFirstDayMeanTemp";
            v2.Size = 1;
            v2.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = -1D;
            v3.Description = "Constant Temperature of deepest soil layer";
            v3.Id = 0;
            v3.MaxValue = 20.0;
            v3.MinValue = -10.0;
            v3.Name = "cAVT";
            v3.Size = 1;
            v3.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 2.0;
            v4.Description = "Mean bulk density";
            v4.Id = 0;
            v4.MaxValue = 4.0;
            v4.MinValue = 1.0;
            v4.Name = "cABD";
            v4.Size = 1;
            v4.Units = "http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 6.0;
            v5.Description = "Initial value for damping depth of soil";
            v5.Id = 0;
            v5.MaxValue = 20.0;
            v5.MinValue = 1.5;
            v5.Name = "cDampingDepth";
            v5.Size = 1;
            v5.Units = "http://www.wurvoc.org/vocabularies/om-1.8/metre";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v5);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd1.PropertyName = "iSoilWaterContent";
            pd1.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous);
            pd2.PropertyName = "iSoilSurfaceTemperature";
            pd2.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilSurfaceTemperature).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilSurfaceTemperature);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd3.PropertyName = "SoilTempArray";
            pd3.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd4.PropertyName = "pSoilLayerDepth";
            pd4.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth);
            _inputs0_0.Add(pd4);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState);
            pd5.PropertyName = "SoilTempArray";
            pd5.PropertyType = (SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
            _outputs0_0.Add(pd5);
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
            return new List<Type>() {  typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState),  typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary), typeof(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double[] cSoilLayerDepth
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("cSoilLayerDepth");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'cSoilLayerDepth' not found (or found null) in strategy 'STMPsimCalculator'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("cSoilLayerDepth");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'cSoilLayerDepth' not found in strategy 'STMPsimCalculator'");
            }
        }
        public double cFirstDayMeanTemp
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("cFirstDayMeanTemp");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'cFirstDayMeanTemp' not found (or found null) in strategy 'STMPsimCalculator'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("cFirstDayMeanTemp");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'cFirstDayMeanTemp' not found in strategy 'STMPsimCalculator'");
            }
        }
        public double cAVT
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("cAVT");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'cAVT' not found (or found null) in strategy 'STMPsimCalculator'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("cAVT");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'cAVT' not found in strategy 'STMPsimCalculator'");
            }
        }
        public double cABD
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("cABD");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'cABD' not found (or found null) in strategy 'STMPsimCalculator'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("cABD");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'cABD' not found in strategy 'STMPsimCalculator'");
            }
        }
        public double cDampingDepth
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("cDampingDepth");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'cDampingDepth' not found (or found null) in strategy 'STMPsimCalculator'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("cDampingDepth");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'cDampingDepth' not found in strategy 'STMPsimCalculator'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

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

            cAVTVarInfo.Name = "cAVT";
            cAVTVarInfo.Description = "Constant Temperature of deepest soil layer";
            cAVTVarInfo.MaxValue = 20.0;
            cAVTVarInfo.MinValue = -10.0;
            cAVTVarInfo.DefaultValue = -1D;
            cAVTVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            cAVTVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            cABDVarInfo.Name = "cABD";
            cABDVarInfo.Description = "Mean bulk density";
            cABDVarInfo.MaxValue = 4.0;
            cABDVarInfo.MinValue = 1.0;
            cABDVarInfo.DefaultValue = 2.0;
            cABDVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre";
            cABDVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            cDampingDepthVarInfo.Name = "cDampingDepth";
            cDampingDepthVarInfo.Description = "Initial value for damping depth of soil";
            cDampingDepthVarInfo.MaxValue = 20.0;
            cDampingDepthVarInfo.MinValue = 1.5;
            cDampingDepthVarInfo.DefaultValue = 6.0;
            cDampingDepthVarInfo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/metre";
            cDampingDepthVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _cSoilLayerDepthVarInfo = new VarInfo();
        public static VarInfo cSoilLayerDepthVarInfo
        {
            get { return _cSoilLayerDepthVarInfo;} 
        }

        private static VarInfo _cFirstDayMeanTempVarInfo = new VarInfo();
        public static VarInfo cFirstDayMeanTempVarInfo
        {
            get { return _cFirstDayMeanTempVarInfo;} 
        }

        private static VarInfo _cAVTVarInfo = new VarInfo();
        public static VarInfo cAVTVarInfo
        {
            get { return _cAVTVarInfo;} 
        }

        private static VarInfo _cABDVarInfo = new VarInfo();
        public static VarInfo cABDVarInfo
        {
            get { return _cABDVarInfo;} 
        }

        private static VarInfo _cDampingDepthVarInfo = new VarInfo();
        public static VarInfo cDampingDepthVarInfo
        {
            get { return _cDampingDepthVarInfo;} 
        }

        public string TestPostConditions(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.CurrentValue=s.SoilTempArray;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.ValueType)){prc.AddCondition(r10);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.SoilTemperature, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a,SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent.CurrentValue=ex.iSoilWaterContent;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilSurfaceTemperature.CurrentValue=ex.iSoilSurfaceTemperature;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.CurrentValue=s.SoilTempArray;
                SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth.CurrentValue=s.pSoilLayerDepth;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilWaterContent.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilSurfaceTemperature);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenousVarInfo.iSoilSurfaceTemperature.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.SoilTempArray.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemperature.DomainClass.SoilTemperatureStateVarInfo.pSoilLayerDepth.ValueType)){prc.AddCondition(r4);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cSoilLayerDepth")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cFirstDayMeanTemp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cAVT")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cABD")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("cDampingDepth")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.SoilTemperature, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
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

        private void CalculateModel(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            double iSoilWaterContent = ex.iSoilWaterContent;
            double iSoilSurfaceTemperature = ex.iSoilSurfaceTemperature;
            double[] SoilTempArray = s.SoilTempArray;
            double[] pSoilLayerDepth = s.pSoilLayerDepth;
            double XLAG;
            double XLG1;
            double DP;
            double WC;
            double DD;
            double Z1;
            int i;
            double ZD;
            double RATE;
            XLAG = .8d;
            XLG1 = 1 - XLAG;
            DP = 1 + (2.5d * cABD / (cABD + Math.Exp(6.53d - (5.63d * cABD))));
            WC = 0.001d * iSoilWaterContent / ((.356d - (.144d * cABD)) * cSoilLayerDepth[(cSoilLayerDepth.Length - 1)]);
            DD = Math.Exp(Math.Log(0.5d / DP) * ((1 - WC) / (1 + WC)) * 2) * DP;
            Z1 = (double)(0);
            for (i=0 ; i!=SoilTempArray.Length ; i+=1)
            {
                ZD = 0.5d * (Z1 + pSoilLayerDepth[i]) / DD;
                RATE = ZD / (ZD + Math.Exp(-.8669d - (2.0775d * ZD))) * (cAVT - iSoilSurfaceTemperature);
                SoilTempArray[i] = XLAG * SoilTempArray[i] + (XLG1 * (RATE + iSoilSurfaceTemperature));
                Z1 = pSoilLayerDepth[i];
            }
            s.SoilTempArray= SoilTempArray;
        }

        public void Init(SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureState s1, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureRate r, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureAuxiliary a, SiriusQualitySoilTemperature.DomainClass.SoilTemperatureExogenous ex)
        {
            double iSoilWaterContent;
            double iSoilSurfaceTemperature;
            double[] SoilTempArray ;
            double[] pSoilLayerDepth ;
            double tProfileDepth;
            double additionalDepth;
            double firstAdditionalLayerHight;
            int layers;
            double[] tStmp ;
            double[] tz ;
            int i;
            double depth;
            tProfileDepth = cSoilLayerDepth[cSoilLayerDepth.Length - 1];
            additionalDepth = cDampingDepth - tProfileDepth;
            firstAdditionalLayerHight = additionalDepth - (double)(Math.Floor(additionalDepth));
            layers = (int)(Math.Abs((double)((int) Math.Ceiling(additionalDepth)))) + cSoilLayerDepth.Length;
            tStmp = new double[ layers];
            tz = new double[ layers];
            for (i=0 ; i!=tStmp.Length ; i+=1)
            {
                if (i < cSoilLayerDepth.Length)
                {
                    depth = cSoilLayerDepth[i];
                }
                else
                {
                    depth = tProfileDepth + firstAdditionalLayerHight + i - cSoilLayerDepth.Length;
                }
                tz[i] = depth;
                tStmp[i] = (cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT * depth)) / cDampingDepth;
            }
            SoilTempArray = tStmp;
            pSoilLayerDepth = tz;
            s.SoilTempArray= SoilTempArray;
            s.pSoilLayerDepth= pSoilLayerDepth;
        }

    }
}