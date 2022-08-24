
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
using SiriusQualitySoilTemp.DomainClass;
namespace SiriusQualitySoilTemp.Strategies
{
    public class STEMP_EPIC : IStrategySiriusQualitySoilTemp
    {
        public STEMP_EPIC()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = ;
            v1.Description = "Number of soil layers";
            v1.Id = 0;
            v1.MaxValue = ;
            v1.MinValue = ;
            v1.Name = "NL";
            v1.Size = 1;
            v1.Units = "dimensionless";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = "Y";
            v2.Description = "Water simulation control switch (Y or N)";
            v2.Id = 0;
            v2.MaxValue = ;
            v2.MinValue = ;
            v2.Name = "ISWWAT";
            v2.Size = 1;
            v2.Units = "dimensionless";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("String");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = ;
            v3.Description = "Bulk density, soil layer NL";
            v3.Id = 0;
            v3.MaxValue = ;
            v3.MinValue = ;
            v3.Name = "BD";
            v3.Size = 1;
            v3.Units = "g [soil] / cm3 [soil]";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = ;
            v4.Description = "Thickness of soil layer NL";
            v4.Id = 0;
            v4.MaxValue = ;
            v4.MinValue = ;
            v4.Name = "DLAYR";
            v4.Size = 1;
            v4.Units = "cm";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = ;
            v5.Description = "Cumulative depth in soil layer NL";
            v5.Id = 0;
            v5.MaxValue = ;
            v5.MinValue = ;
            v5.Name = "DS";
            v5.Size = 1;
            v5.Units = "cm";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v5);
            VarInfo v6 = new VarInfo();
            v6.DefaultValue = ;
            v6.Description = "Volumetric soil water content at Drained Upper Limit in soil layer L";
            v6.Id = 0;
            v6.MaxValue = ;
            v6.MinValue = ;
            v6.Name = "DUL";
            v6.Size = 1;
            v6.Units = "cm3[water]/cm3[soil]";
            v6.URL = "";
            v6.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v6.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v6);
            VarInfo v7 = new VarInfo();
            v7.DefaultValue = ;
            v7.Description = "Volumetric soil water content in soil layer NL at lower limit";
            v7.Id = 0;
            v7.MaxValue = ;
            v7.MinValue = ;
            v7.Name = "LL";
            v7.Size = 1;
            v7.Units = "cm3 [water] / cm3 [soil]";
            v7.URL = "";
            v7.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v7.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v7);
            VarInfo v8 = new VarInfo();
            v8.DefaultValue = ;
            v8.Description = "Actual number of soil layers";
            v8.Id = 0;
            v8.MaxValue = ;
            v8.MinValue = ;
            v8.Name = "NLAYR";
            v8.Size = 1;
            v8.Units = "dimensionless";
            v8.URL = "";
            v8.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v8.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v8);
            VarInfo v9 = new VarInfo();
            v9.DefaultValue = ;
            v9.Description = "Volumetric soil water content in layer NL";
            v9.Id = 0;
            v9.MaxValue = ;
            v9.MinValue = ;
            v9.Name = "SW";
            v9.Size = 1;
            v9.Units = "cm3 [water] / cm3 [soil]";
            v9.URL = "";
            v9.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v9.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
            _parameters0_0.Add(v9);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd1.PropertyName = "TAMP";
            pd1.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd2.PropertyName = "RAIN";
            pd2.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd3.PropertyName = "CUMDPT";
            pd3.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd4.PropertyName = "DSMID";
            pd4.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd5.PropertyName = "TAVG";
            pd5.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd6.PropertyName = "TMAX";
            pd6.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd7.PropertyName = "TMIN";
            pd7.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd8.PropertyName = "TAV";
            pd8.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd9.PropertyName = "SRFTEMP";
            pd9.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd10.PropertyName = "NDays";
            pd10.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd11.PropertyName = "TDL";
            pd11.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd12.PropertyName = "WetDay";
            pd12.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd13.PropertyName = "ST";
            pd13.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd14.PropertyName = "TMA";
            pd14.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
            _inputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd15.PropertyName = "DEPIR";
            pd15.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR);
            _inputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd16.PropertyName = "BIOMAS";
            pd16.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS);
            _inputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd17.PropertyName = "MULCHMASS";
            pd17.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS);
            _inputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd18.PropertyName = "SNOW";
            pd18.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW);
            _inputs0_0.Add(pd18);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd19.PropertyName = "SRFTEMP";
            pd19.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
            _outputs0_0.Add(pd19);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd20 = new PropertyDescription();
            pd20.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd20.PropertyName = "NDays";
            pd20.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays).ValueType.TypeForCurrentValue;
            pd20.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
            _outputs0_0.Add(pd20);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd21 = new PropertyDescription();
            pd21.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd21.PropertyName = "TDL";
            pd21.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL).ValueType.TypeForCurrentValue;
            pd21.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
            _outputs0_0.Add(pd21);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd22 = new PropertyDescription();
            pd22.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd22.PropertyName = "WetDay";
            pd22.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay).ValueType.TypeForCurrentValue;
            pd22.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
            _outputs0_0.Add(pd22);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd23 = new PropertyDescription();
            pd23.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd23.PropertyName = "ST";
            pd23.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST).ValueType.TypeForCurrentValue;
            pd23.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
            _outputs0_0.Add(pd23);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd24 = new PropertyDescription();
            pd24.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd24.PropertyName = "TMA";
            pd24.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA).ValueType.TypeForCurrentValue;
            pd24.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
            _outputs0_0.Add(pd24);
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
            _pd.Add("Creator", "Cyrille");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRAE");
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState),  typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempRate), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public int NL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("NL");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'NL' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("NL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'NL' not found in strategy 'STEMP_EPIC'");
            }
        }
        public string ISWWAT
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("ISWWAT");
                if (vi != null && vi.CurrentValue!=null) return (string)vi.CurrentValue ;
                else throw new Exception("Parameter 'ISWWAT' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("ISWWAT");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'ISWWAT' not found in strategy 'STEMP_EPIC'");
            }
        }
        public double[] BD
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("BD");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'BD' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("BD");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'BD' not found in strategy 'STEMP_EPIC'");
            }
        }
        public double[] DLAYR
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("DLAYR");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'DLAYR' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("DLAYR");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'DLAYR' not found in strategy 'STEMP_EPIC'");
            }
        }
        public double[] DS
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("DS");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'DS' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("DS");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'DS' not found in strategy 'STEMP_EPIC'");
            }
        }
        public double[] DUL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("DUL");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'DUL' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("DUL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'DUL' not found in strategy 'STEMP_EPIC'");
            }
        }
        public double[] LL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("LL");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'LL' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("LL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'LL' not found in strategy 'STEMP_EPIC'");
            }
        }
        public int NLAYR
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("NLAYR");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'NLAYR' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("NLAYR");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'NLAYR' not found in strategy 'STEMP_EPIC'");
            }
        }
        public double[] SW
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("SW");
                if (vi != null && vi.CurrentValue!=null) return (double[])vi.CurrentValue ;
                else throw new Exception("Parameter 'SW' not found (or found null) in strategy 'STEMP_EPIC'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("SW");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'SW' not found in strategy 'STEMP_EPIC'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            NLVarInfo.Name = "NL";
            NLVarInfo.Description = "Number of soil layers";
            NLVarInfo.MaxValue = ;
            NLVarInfo.MinValue = ;
            NLVarInfo.DefaultValue = ;
            NLVarInfo.Units = "dimensionless";
            NLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            ISWWATVarInfo.Name = "ISWWAT";
            ISWWATVarInfo.Description = "Water simulation control switch (Y or N)";
            ISWWATVarInfo.MaxValue = ;
            ISWWATVarInfo.MinValue = ;
            ISWWATVarInfo.DefaultValue = "Y";
            ISWWATVarInfo.Units = "dimensionless";
            ISWWATVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("String");

            BDVarInfo.Name = "BD";
            BDVarInfo.Description = "Bulk density, soil layer NL";
            BDVarInfo.MaxValue = ;
            BDVarInfo.MinValue = ;
            BDVarInfo.DefaultValue = ;
            BDVarInfo.Units = "g [soil] / cm3 [soil]";
            BDVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            DLAYRVarInfo.Name = "DLAYR";
            DLAYRVarInfo.Description = "Thickness of soil layer NL";
            DLAYRVarInfo.MaxValue = ;
            DLAYRVarInfo.MinValue = ;
            DLAYRVarInfo.DefaultValue = ;
            DLAYRVarInfo.Units = "cm";
            DLAYRVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            DSVarInfo.Name = "DS";
            DSVarInfo.Description = "Cumulative depth in soil layer NL";
            DSVarInfo.MaxValue = ;
            DSVarInfo.MinValue = ;
            DSVarInfo.DefaultValue = ;
            DSVarInfo.Units = "cm";
            DSVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            DULVarInfo.Name = "DUL";
            DULVarInfo.Description = "Volumetric soil water content at Drained Upper Limit in soil layer L";
            DULVarInfo.MaxValue = ;
            DULVarInfo.MinValue = ;
            DULVarInfo.DefaultValue = ;
            DULVarInfo.Units = "cm3[water]/cm3[soil]";
            DULVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            LLVarInfo.Name = "LL";
            LLVarInfo.Description = "Volumetric soil water content in soil layer NL at lower limit";
            LLVarInfo.MaxValue = ;
            LLVarInfo.MinValue = ;
            LLVarInfo.DefaultValue = ;
            LLVarInfo.Units = "cm3 [water] / cm3 [soil]";
            LLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            NLAYRVarInfo.Name = "NLAYR";
            NLAYRVarInfo.Description = "Actual number of soil layers";
            NLAYRVarInfo.MaxValue = ;
            NLAYRVarInfo.MinValue = ;
            NLAYRVarInfo.DefaultValue = ;
            NLAYRVarInfo.Units = "dimensionless";
            NLAYRVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            SWVarInfo.Name = "SW";
            SWVarInfo.Description = "Volumetric soil water content in layer NL";
            SWVarInfo.MaxValue = ;
            SWVarInfo.MinValue = ;
            SWVarInfo.DefaultValue = ;
            SWVarInfo.Units = "cm3 [water] / cm3 [soil]";
            SWVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");
        }

        private static VarInfo _NLVarInfo = new VarInfo();
        public static VarInfo NLVarInfo
        {
            get { return _NLVarInfo;} 
        }

        private static VarInfo _ISWWATVarInfo = new VarInfo();
        public static VarInfo ISWWATVarInfo
        {
            get { return _ISWWATVarInfo;} 
        }

        private static VarInfo _BDVarInfo = new VarInfo();
        public static VarInfo BDVarInfo
        {
            get { return _BDVarInfo;} 
        }

        private static VarInfo _DLAYRVarInfo = new VarInfo();
        public static VarInfo DLAYRVarInfo
        {
            get { return _DLAYRVarInfo;} 
        }

        private static VarInfo _DSVarInfo = new VarInfo();
        public static VarInfo DSVarInfo
        {
            get { return _DSVarInfo;} 
        }

        private static VarInfo _DULVarInfo = new VarInfo();
        public static VarInfo DULVarInfo
        {
            get { return _DULVarInfo;} 
        }

        private static VarInfo _LLVarInfo = new VarInfo();
        public static VarInfo LLVarInfo
        {
            get { return _LLVarInfo;} 
        }

        private static VarInfo _NLAYRVarInfo = new VarInfo();
        public static VarInfo NLAYRVarInfo
        {
            get { return _NLAYRVarInfo;} 
        }

        private static VarInfo _SWVarInfo = new VarInfo();
        public static VarInfo SWVarInfo
        {
            get { return _SWVarInfo;} 
        }

        public string TestPostConditions(SiriusQualitySoilTemp.DomainClass.SoilTempState s,SiriusQualitySoilTemp.DomainClass.SoilTempState s1,SiriusQualitySoilTemp.DomainClass.SoilTempRate r,SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a,SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP.CurrentValue=s.SRFTEMP;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays.CurrentValue=s.NDays;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL.CurrentValue=s.TDL;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay.CurrentValue=s.WetDay;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST.CurrentValue=s.ST;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA.CurrentValue=s.TMA;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r28 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
                if(r28.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP.ValueType)){prc.AddCondition(r28);}
                RangeBasedCondition r29 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
                if(r29.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays.ValueType)){prc.AddCondition(r29);}
                RangeBasedCondition r30 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
                if(r30.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL.ValueType)){prc.AddCondition(r30);}
                RangeBasedCondition r31 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
                if(r31.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay.ValueType)){prc.AddCondition(r31);}
                RangeBasedCondition r32 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
                if(r32.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST.ValueType)){prc.AddCondition(r32);}
                RangeBasedCondition r33 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
                if(r33.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA.ValueType)){prc.AddCondition(r33);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.SoilTemp, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualitySoilTemp.DomainClass.SoilTempState s,SiriusQualitySoilTemp.DomainClass.SoilTempState s1,SiriusQualitySoilTemp.DomainClass.SoilTempRate r,SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a,SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP.CurrentValue=ex.TAMP;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN.CurrentValue=ex.RAIN;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT.CurrentValue=s.CUMDPT;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID.CurrentValue=s.DSMID;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG.CurrentValue=ex.TAVG;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX.CurrentValue=ex.TMAX;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN.CurrentValue=ex.TMIN;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV.CurrentValue=ex.TAV;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP.CurrentValue=s.SRFTEMP;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays.CurrentValue=s.NDays;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL.CurrentValue=s.TDL;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay.CurrentValue=s.WetDay;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST.CurrentValue=s.ST;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA.CurrentValue=s.TMA;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR.CurrentValue=ex.DEPIR;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS.CurrentValue=ex.BIOMAS;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS.CurrentValue=ex.MULCHMASS;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW.CurrentValue=ex.SNOW;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
                if(r13.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR);
                if(r15.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR.ValueType)){prc.AddCondition(r15);}
                RangeBasedCondition r16 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS);
                if(r16.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS.ValueType)){prc.AddCondition(r16);}
                RangeBasedCondition r17 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS);
                if(r17.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS.ValueType)){prc.AddCondition(r17);}
                RangeBasedCondition r18 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW);
                if(r18.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW.ValueType)){prc.AddCondition(r18);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("NL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("ISWWAT")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("BD")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("DLAYR")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("DS")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("DUL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("LL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("NLAYR")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("SW")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.SoilTemp, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualitySoilTemp.DomainClass.SoilTempState s,SiriusQualitySoilTemp.DomainClass.SoilTempState s1,SiriusQualitySoilTemp.DomainClass.SoilTempRate r,SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a,SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualitySoilTemp, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualitySoilTemp.DomainClass.SoilTempState s, SiriusQualitySoilTemp.DomainClass.SoilTempState s1, SiriusQualitySoilTemp.DomainClass.SoilTempRate r, SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a, SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex)
        {
            double TAMP = ex.TAMP;
            double RAIN = ex.RAIN;
            double CUMDPT = s.CUMDPT;
            double[] DSMID = s.DSMID;
            double TAVG = ex.TAVG;
            double TMAX = ex.TMAX;
            double TMIN = ex.TMIN;
            double TAV = ex.TAV;
            double SRFTEMP = s.SRFTEMP;
            int NDays = s.NDays;
            double TDL = s.TDL;
            int[] WetDay = s.WetDay;
            double[] ST = s.ST;
            double[] TMA = s.TMA;
            double DEPIR = ex.DEPIR;
            double BIOMAS = ex.BIOMAS;
            double MULCHMASS = ex.MULCHMASS;
            double SNOW = ex.SNOW;
            int I;
            int L;
            int NWetDays;
            double ABD;
            double B;
            double DP;
            double FX;
            double PESW;
            double TBD;
            double WW;
            double TLL;
            double TSW;
            double X2_AVG;
            double WFT;
            double BCV;
            double CV;
            double BCV1;
            double BCV2;
            double X2_PREV;
            TBD = 0.0d;
            TLL = 0.0d;
            TSW = 0.0d;
            X2_PREV = 0.0d;
            for (L=1 ; L!=NLAYR + 1 ; L+=1)
            {
                TBD = TBD + (BD[(L - 1)] * DLAYR[(L - 1)]);
                TDL = TDL + (DUL[(L - 1)] * DLAYR[(L - 1)]);
                TLL = TLL + (LL[(L - 1)] * DLAYR[(L - 1)]);
                TSW = TSW + (SW[(L - 1)] * DLAYR[(L - 1)]);
            }
            ABD = TBD / DS[(NLAYR - 1)];
            FX = ABD / (ABD + (686.0d * Math.Exp(-(5.63d * ABD))));
            DP = 1000.0d + (2500.0d * FX);
            WW = 0.356d - (0.144d * ABD);
            B = Math.Log(500.0d / DP);
            if (ISWWAT == "Y")
            {
                PESW = Math.Max(0.0d, TSW - TLL);
            }
            else
            {
                PESW = Math.Max(0.0d, TDL - TLL);
            }
            if (NDays == 30)
            {
                for (I=1 ; I!=29 + 1 ; I+=1)
                {
                    WetDay[I - 1] = WetDay[I + 1 - 1];
                }
            }
            else
            {
                NDays = NDays + 1;
            }
            if (RAIN + DEPIR > 1.0E-6d)
            {
                WetDay[NDays - 1] = 1;
            }
            else
            {
                WetDay[NDays - 1] = 0;
            }
            NWetDays = WetDay.Sum();
            WFT = (double)(NWetDays) / (double)(NDays);
            CV = (BIOMAS + MULCHMASS) / 1000.0d;
            BCV1 = CV / (CV + Math.Exp(5.3396d - (2.3951d * CV)));
            BCV2 = SNOW / (SNOW + Math.Exp(2.303d - (0.2197d * SNOW)));
            BCV = Math.Max(BCV1, BCV2);
            Tuple.Create(TMA, X2_PREV, ST, SRFTEMP, X2_AVG) = SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, WetDay[NDays - 1], WFT, WW, TMA, X2_PREV, ST);
            s.SRFTEMP= SRFTEMP;
            s.NDays= NDays;
            s.TDL= TDL;
            s.WetDay= WetDay;
            s.ST= ST;
            s.TMA= TMA;
        }

        public static Tuple<double[],double,double[],double,double>  SOILT_EPIC(int NL, double B, double BCV, double CUMDPT, double DP, double[] DSMID, int NLAYR, double PESW, double TAV, double TAVG, double TMAX, double TMIN, int WetDay, double WFT, double WW, double[] TMA, double X2_PREV, double[] ST)
        {
            int K;
            int L;
            double DD;
            double FX;
            double SRFTEMP;
            double WC;
            double ZD;
            double X1;
            double X2;
            double X3;
            double F;
            double X2_AVG;
            double LAG;
            LAG = 0.5d;
            WC = Math.Max(0.01d, PESW) / (WW * CUMDPT) * 10.0d;
            FX = Math.Exp(B * Math.Pow((1.0d - WC) / (1.0d + WC), 2));
            DD = FX * DP;
            if (WetDay > 0)
            {
                X2 = WFT * (TAVG - TMIN) + TMIN;
            }
            else
            {
                X2 = WFT * (TMAX - TAVG) + TAVG + 2.0d;
            }
            TMA[1 - 1] = X2;
            for (K=5 ; K!=2 - 1 ; K+=-1)
            {
                TMA[K - 1] = TMA[K - 1 - 1];
            }
            X2_AVG = TMA.Sum() / 5.0d;
            X3 = (1.0d - BCV) * X2_AVG + (BCV * X2_PREV);
            SRFTEMP = Math.Min(X2_AVG, X3);
            X1 = TAV - X3;
            for (L=1 ; L!=NLAYR + 1 ; L+=1)
            {
                ZD = DSMID[(L - 1)] / DD;
                F = ZD / (ZD + Math.Exp(-.8669d - (2.0775d * ZD)));
                ST[L - 1] = LAG * ST[(L - 1)] + ((1.0d - LAG) * (F * X1 + X3));
            }
            X2_PREV = X2_AVG;
            return Tuple.Create(TMA, X2_PREV, ST, SRFTEMP, X2_AVG);
        }

        public void Init(SiriusQualitySoilTemp.DomainClass.SoilTempState s, SiriusQualitySoilTemp.DomainClass.SoilTempState s1, SiriusQualitySoilTemp.DomainClass.SoilTempRate r, SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a, SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex)
        {
            double TAMP;
            double RAIN;
            double TAVG;
            double TMAX;
            double TMIN;
            double TAV;
            double DEPIR;
            double BIOMAS;
            double MULCHMASS;
            double SNOW;
            double CUMDPT;
            double[] DSMID = new double[NL];
            double SRFTEMP;
            int NDays;
            double TDL;
            int[] WetDay = new int[NL];
            double[] ST = new double[NL];
            double[] TMA = new double[5];
            int I;
            int L;
            double ABD;
            double B;
            double DP;
            double FX;
            double PESW;
            double TBD;
            double WW;
            double TLL;
            double TSW;
            double X2_AVG;
            double WFT;
            double BCV;
            double CV;
            double BCV1;
            double BCV2;
            double X2_PREV;
            double[] SWI = new double[NL];
            SWI = SW;
            TBD = 0.0d;
            TLL = 0.0d;
            TSW = 0.0d;
            TDL = 0.0d;
            CUMDPT = 0.0d;
            X2_PREV = 0.0d;
            for (L=1 ; L!=NLAYR + 1 ; L+=1)
            {
                DSMID[L - 1] = CUMDPT + (DLAYR[(L - 1)] * 5.0d);
                CUMDPT = CUMDPT + (DLAYR[(L - 1)] * 10.0d);
                TBD = TBD + (BD[(L - 1)] * DLAYR[(L - 1)]);
                TLL = TLL + (LL[(L - 1)] * DLAYR[(L - 1)]);
                TSW = TSW + (SWI[(L - 1)] * DLAYR[(L - 1)]);
                TDL = TDL + (DUL[(L - 1)] * DLAYR[(L - 1)]);
            }
            if (ISWWAT == "Y")
            {
                PESW = Math.Max(0.0d, TSW - TLL);
            }
            else
            {
                PESW = Math.Max(0.0d, TDL - TLL);
            }
            ABD = TBD / DS[(NLAYR - 1)];
            FX = ABD / (ABD + (686.0d * Math.Exp(-(5.63d * ABD))));
            DP = 1000.0d + (2500.0d * FX);
            WW = 0.356d - (0.144d * ABD);
            B = Math.Log(500.0d / DP);
            for (I=1 ; I!=5 + 1 ; I+=1)
            {
                TMA[I - 1] = (int)(TAVG * 10000.0d) / 10000.0d;
            }
            X2_AVG = TMA[(1 - 1)] * 5.0d;
            for (L=1 ; L!=NLAYR + 1 ; L+=1)
            {
                ST[L - 1] = TAVG;
            }
            WFT = 0.1d;
            WetDay = new int[0];
            NDays = 0;
            CV = MULCHMASS / 1000.0d;
            BCV1 = CV / (CV + Math.Exp(5.3396d - (2.3951d * CV)));
            BCV2 = SNOW / (SNOW + Math.Exp(2.303d - (0.2197d * SNOW)));
            BCV = Math.Max(BCV1, BCV2);
            for (I=1 ; I!=8 + 1 ; I+=1)
            {
                Tuple.Create(TMA, X2_PREV, ST, SRFTEMP, X2_AVG) = SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, 0, WFT, WW, TMA, X2_PREV, ST);
            }
            s.CUMDPT= CUMDPT;
            s.DSMID= DSMID;
            s.SRFTEMP= SRFTEMP;
            s.NDays= NDays;
            s.TDL= TDL;
            s.WetDay= WetDay;
            s.ST= ST;
            s.TMA= TMA;
        }

    }
}