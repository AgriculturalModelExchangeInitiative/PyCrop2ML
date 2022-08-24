
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
    public class SoilTempComponent : IStrategySiriusQualitySoilTemp
    {
        public SoilTempComponent()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new CompositeStrategyVarInfo(_STEMP_EPIC, "BD");
            _parameters0_0.Add(v1);
            VarInfo v2 = new CompositeStrategyVarInfo(_STEMP_EPIC, "NL");
            _parameters0_0.Add(v2);
            VarInfo v3 = new CompositeStrategyVarInfo(_STEMP_EPIC, "NLAYR");
            _parameters0_0.Add(v3);
            VarInfo v4 = new CompositeStrategyVarInfo(_STEMP_EPIC, "SW");
            _parameters0_0.Add(v4);
            VarInfo v5 = new CompositeStrategyVarInfo(_STEMP_EPIC, "DS");
            _parameters0_0.Add(v5);
            VarInfo v6 = new CompositeStrategyVarInfo(_STEMP_EPIC, "DLAYR");
            _parameters0_0.Add(v6);
            VarInfo v7 = new CompositeStrategyVarInfo(_STEMP_EPIC, "ISWWAT");
            _parameters0_0.Add(v7);
            VarInfo v8 = new CompositeStrategyVarInfo(_STEMP_EPIC, "DUL");
            _parameters0_0.Add(v8);
            VarInfo v9 = new CompositeStrategyVarInfo(_STEMP_EPIC, "LL");
            _parameters0_0.Add(v9);
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd1.PropertyName = "SRFTEMP";
            pd1.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd2.PropertyName = "TMA";
            pd2.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd3.PropertyName = "DEPIR";
            pd3.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd4.PropertyName = "BIOMAS";
            pd4.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd5.PropertyName = "TDL";
            pd5.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd6.PropertyName = "TAMP";
            pd6.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd7.PropertyName = "MULCHMASS";
            pd7.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd8.PropertyName = "TMAX";
            pd8.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd9.PropertyName = "SNOW";
            pd9.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd10.PropertyName = "RAIN";
            pd10.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN);
            _inputs0_0.Add(pd10);
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd11.PropertyName = "TAV";
            pd11.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV);
            _inputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd12.PropertyName = "TAVG";
            pd12.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG);
            _inputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous);
            pd13.PropertyName = "TMIN";
            pd13.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN);
            _inputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd14.PropertyName = "ST";
            pd14.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
            _inputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd15.PropertyName = "CUMDPT";
            pd15.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT);
            _inputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd16.PropertyName = "NDays";
            pd16.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
            _inputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd17.PropertyName = "WetDay";
            pd17.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
            _inputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd18.PropertyName = "DSMID";
            pd18.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID);
            _inputs0_0.Add(pd18);
            mo0_0.Inputs=_inputs0_0;
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd19.PropertyName = "SRFTEMP";
            pd19.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
            _outputs0_0.Add(pd19);
            PropertyDescription pd20 = new PropertyDescription();
            pd20.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd20.PropertyName = "NDays";
            pd20.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays).ValueType.TypeForCurrentValue;
            pd20.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
            _outputs0_0.Add(pd20);
            PropertyDescription pd21 = new PropertyDescription();
            pd21.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd21.PropertyName = "TDL";
            pd21.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL).ValueType.TypeForCurrentValue;
            pd21.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
            _outputs0_0.Add(pd21);
            PropertyDescription pd22 = new PropertyDescription();
            pd22.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd22.PropertyName = "WetDay";
            pd22.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay).ValueType.TypeForCurrentValue;
            pd22.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
            _outputs0_0.Add(pd22);
            PropertyDescription pd23 = new PropertyDescription();
            pd23.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd23.PropertyName = "ST";
            pd23.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST).ValueType.TypeForCurrentValue;
            pd23.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
            _outputs0_0.Add(pd23);
            PropertyDescription pd24 = new PropertyDescription();
            pd24.DomainClassType = typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState);
            pd24.PropertyName = "TMA";
            pd24.PropertyType = (SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA).ValueType.TypeForCurrentValue;
            pd24.PropertyVarInfo =(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
            _outputs0_0.Add(pd24);
            mo0_0.Outputs=_outputs0_0;
            List<string> lAssStrat0_0 = new List<string>();
            lAssStrat0_0.Add(typeof(SiriusQualitySoilTemp.Strategies.STEMP_EPIC).FullName);
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();
        }

        public string Description
        {
            get { return "I don't know" ;}
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
            return new List<Type>() {  typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempState), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempRate), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary), typeof(SiriusQualitySoilTemp.DomainClass.SoilTempExogenous)};
        }

        public double[] BD
        {
            get
            {
                 return _STEMP_EPIC.BD; 
            }
            set
            {
                _STEMP_EPIC.BD = value;
            }
        }
        public int NL
        {
            get
            {
                 return _STEMP_EPIC.NL; 
            }
            set
            {
                _STEMP_EPIC.NL = value;
            }
        }
        public int NLAYR
        {
            get
            {
                 return _STEMP_EPIC.NLAYR; 
            }
            set
            {
                _STEMP_EPIC.NLAYR = value;
            }
        }
        public double[] SW
        {
            get
            {
                 return _STEMP_EPIC.SW; 
            }
            set
            {
                _STEMP_EPIC.SW = value;
            }
        }
        public double[] DS
        {
            get
            {
                 return _STEMP_EPIC.DS; 
            }
            set
            {
                _STEMP_EPIC.DS = value;
            }
        }
        public double[] DLAYR
        {
            get
            {
                 return _STEMP_EPIC.DLAYR; 
            }
            set
            {
                _STEMP_EPIC.DLAYR = value;
            }
        }
        public string ISWWAT
        {
            get
            {
                 return _STEMP_EPIC.ISWWAT; 
            }
            set
            {
                _STEMP_EPIC.ISWWAT = value;
            }
        }
        public double[] DUL
        {
            get
            {
                 return _STEMP_EPIC.DUL; 
            }
            set
            {
                _STEMP_EPIC.DUL = value;
            }
        }
        public double[] LL
        {
            get
            {
                 return _STEMP_EPIC.LL; 
            }
            set
            {
                _STEMP_EPIC.LL = value;
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
            _STEMP_EPIC.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            BDVarInfo.Name = "BD";
            BDVarInfo.Description = "Bulk density, soil layer NL";
            BDVarInfo.MaxValue = ;
            BDVarInfo.MinValue = ;
            BDVarInfo.DefaultValue = ;
            BDVarInfo.Units = "g [soil] / cm3 [soil]";
            BDVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            NLVarInfo.Name = "NL";
            NLVarInfo.Description = "Number of soil layers";
            NLVarInfo.MaxValue = ;
            NLVarInfo.MinValue = ;
            NLVarInfo.DefaultValue = ;
            NLVarInfo.Units = "dimensionless";
            NLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

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

            DSVarInfo.Name = "DS";
            DSVarInfo.Description = "Cumulative depth in soil layer NL";
            DSVarInfo.MaxValue = ;
            DSVarInfo.MinValue = ;
            DSVarInfo.DefaultValue = ;
            DSVarInfo.Units = "cm";
            DSVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            DLAYRVarInfo.Name = "DLAYR";
            DLAYRVarInfo.Description = "Thickness of soil layer NL";
            DLAYRVarInfo.MaxValue = ;
            DLAYRVarInfo.MinValue = ;
            DLAYRVarInfo.DefaultValue = ;
            DLAYRVarInfo.Units = "cm";
            DLAYRVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            ISWWATVarInfo.Name = "ISWWAT";
            ISWWATVarInfo.Description = "Water simulation control switch (Y or N)";
            ISWWATVarInfo.MaxValue = ;
            ISWWATVarInfo.MinValue = ;
            ISWWATVarInfo.DefaultValue = "Y";
            ISWWATVarInfo.Units = "dimensionless";
            ISWWATVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("String");

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
        }

        public static VarInfo BDVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.BDVarInfo;} 
        }

        public static VarInfo NLVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.NLVarInfo;} 
        }

        public static VarInfo NLAYRVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.NLAYRVarInfo;} 
        }

        public static VarInfo SWVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.SWVarInfo;} 
        }

        public static VarInfo DSVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.DSVarInfo;} 
        }

        public static VarInfo DLAYRVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.DLAYRVarInfo;} 
        }

        public static VarInfo ISWWATVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.ISWWATVarInfo;} 
        }

        public static VarInfo DULVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.DULVarInfo;} 
        }

        public static VarInfo LLVarInfo
        {
            get { return SiriusQualitySoilTemp.Strategies.STEMP_EPIC.LLVarInfo;} 
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

                string ret = "";
                ret += _STEMP_EPIC.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualitySoilTemp.Strategies.SoilTemp");
                if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }

                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.SoilTemp, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualitySoilTemp.DomainClass.SoilTempState s,SiriusQualitySoilTemp.DomainClass.SoilTempState s1,SiriusQualitySoilTemp.DomainClass.SoilTempRate r,SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a,SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP.CurrentValue=s.SRFTEMP;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA.CurrentValue=s.TMA;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR.CurrentValue=ex.DEPIR;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS.CurrentValue=ex.BIOMAS;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL.CurrentValue=s.TDL;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP.CurrentValue=ex.TAMP;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS.CurrentValue=ex.MULCHMASS;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX.CurrentValue=ex.TMAX;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW.CurrentValue=ex.SNOW;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN.CurrentValue=ex.RAIN;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV.CurrentValue=ex.TAV;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG.CurrentValue=ex.TAVG;
                SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN.CurrentValue=ex.TMIN;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST.CurrentValue=s.ST;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT.CurrentValue=s.CUMDPT;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays.CurrentValue=s.NDays;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay.CurrentValue=s.WetDay;
                SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID.CurrentValue=s.DSMID;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.SRFTEMP.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TMA.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.DEPIR.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.BIOMAS.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.TDL.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAMP.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.MULCHMASS.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMAX.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.SNOW.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.RAIN.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAV.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TAVG.ValueType)){prc.AddCondition(r12);}
                RangeBasedCondition r13 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN);
                if(r13.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempExogenousVarInfo.TMIN.ValueType)){prc.AddCondition(r13);}
                RangeBasedCondition r14 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST);
                if(r14.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.ST.ValueType)){prc.AddCondition(r14);}
                RangeBasedCondition r15 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT);
                if(r15.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.CUMDPT.ValueType)){prc.AddCondition(r15);}
                RangeBasedCondition r16 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays);
                if(r16.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.NDays.ValueType)){prc.AddCondition(r16);}
                RangeBasedCondition r17 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay);
                if(r17.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.WetDay.ValueType)){prc.AddCondition(r17);}
                RangeBasedCondition r18 = new RangeBasedCondition(SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID);
                if(r18.ApplicableVarInfoValueTypes.Contains( SiriusQualitySoilTemp.DomainClass.SoilTempStateVarInfo.DSMID.ValueType)){prc.AddCondition(r18);}

                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("BD")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("NL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("NLAYR")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("SW")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("DS")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("DLAYR")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("ISWWAT")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("DUL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("LL")));
                string ret = "";
                ret += _STEMP_EPIC.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualitySoilTemp.Strategies.SoilTemp");
                if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }

                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.SoilTemp, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
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

        private void CalculateModel(SiriusQualitySoilTemp.DomainClass.SoilTempState s,SiriusQualitySoilTemp.DomainClass.SoilTempState s1,SiriusQualitySoilTemp.DomainClass.SoilTempRate r,SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a,SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex)
        {
            EstimateOfAssociatedClasses(s, s1, r, a, ex);
        }

        //Declaration of the associated strategies
        STEMP_EPIC _STEMP_EPIC = new STEMP_EPIC();

        private void EstimateOfAssociatedClasses(SiriusQualitySoilTemp.DomainClass.SoilTempState s,SiriusQualitySoilTemp.DomainClass.SoilTempState s1,SiriusQualitySoilTemp.DomainClass.SoilTempRate r,SiriusQualitySoilTemp.DomainClass.SoilTempAuxiliary a,SiriusQualitySoilTemp.DomainClass.SoilTempExogenous ex)
        {
            _stemp_epic.Estimate(s,s1, r, a, ex);
        }

        public SoilTempComponent(SoilTempComponent toCopy): this() // copy constructor 
        {
                
            for (int i = 0; i < NL; i++)
            { _BD[i] = toCopy._BD[i]; }
    
                NL = toCopy.NL;
                NLAYR = toCopy.NLAYR;
                
            for (int i = 0; i < NL; i++)
            { _SW[i] = toCopy._SW[i]; }
    
                
            for (int i = 0; i < NL; i++)
            { _DS[i] = toCopy._DS[i]; }
    
                
            for (int i = 0; i < NL; i++)
            { _DLAYR[i] = toCopy._DLAYR[i]; }
    
                ISWWAT = toCopy.ISWWAT;
                
            for (int i = 0; i < NL; i++)
            { _DUL[i] = toCopy._DUL[i]; }
    
                
            for (int i = 0; i < NL; i++)
            { _LL[i] = toCopy._LL[i]; }
    
        }
    }
}