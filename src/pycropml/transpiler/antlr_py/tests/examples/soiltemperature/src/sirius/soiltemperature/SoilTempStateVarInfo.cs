
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemp.DomainClass
{
    public class SoilTempStateVarInfo : IVarInfoClass
    {
        static VarInfo _SRFTEMP = new VarInfo();
        static VarInfo _TMA = new VarInfo();
        static VarInfo _TDL = new VarInfo();
        static VarInfo _ST = new VarInfo();
        static VarInfo _CUMDPT = new VarInfo();
        static VarInfo _NDays = new VarInfo();
        static VarInfo _WetDay = new VarInfo();
        static VarInfo _DSMID = new VarInfo();

        static SoilTempStateVarInfo()
        {
            SoilTempStateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTempState Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTempState";}
        }

        public static  VarInfo SRFTEMP
        {
            get { return _SRFTEMP;}
        }

        public static  VarInfo TMA
        {
            get { return _TMA;}
        }

        public static  VarInfo TDL
        {
            get { return _TDL;}
        }

        public static  VarInfo ST
        {
            get { return _ST;}
        }

        public static  VarInfo CUMDPT
        {
            get { return _CUMDPT;}
        }

        public static  VarInfo NDays
        {
            get { return _NDays;}
        }

        public static  VarInfo WetDay
        {
            get { return _WetDay;}
        }

        public static  VarInfo DSMID
        {
            get { return _DSMID;}
        }

        static void DescribeVariables()
        {
            _SRFTEMP.Name = "SRFTEMP";
            _SRFTEMP.Description = "Temperature of soil surface litter";
            _SRFTEMP.MaxValue = ;
            _SRFTEMP.MinValue = ;
            _SRFTEMP.DefaultValue = ;
            _SRFTEMP.Units = "degC";
            _SRFTEMP.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _TMA.Name = "TMA";
            _TMA.Description = "Array of previous 5 days of average soil temperatures.";
            _TMA.MaxValue = ;
            _TMA.MinValue = ;
            _TMA.DefaultValue = ;
            _TMA.Units = "degC";
            _TMA.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            _TDL.Name = "TDL";
            _TDL.Description = "Total water content of soil at drained upper limit";
            _TDL.MaxValue = ;
            _TDL.MinValue = ;
            _TDL.DefaultValue = ;
            _TDL.Units = "cm";
            _TDL.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _ST.Name = "ST";
            _ST.Description = "Soil temperature in soil layer NL";
            _ST.MaxValue = ;
            _ST.MinValue = ;
            _ST.DefaultValue = ;
            _ST.Units = "degC";
            _ST.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            _CUMDPT.Name = "CUMDPT";
            _CUMDPT.Description = "Cumulative depth of soil profile";
            _CUMDPT.MaxValue = ;
            _CUMDPT.MinValue = ;
            _CUMDPT.DefaultValue = ;
            _CUMDPT.Units = "mm";
            _CUMDPT.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _NDays.Name = "NDays";
            _NDays.Description = "Number of days ...";
            _NDays.MaxValue = ;
            _NDays.MinValue = ;
            _NDays.DefaultValue = ;
            _NDays.Units = "day";
            _NDays.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            _WetDay.Name = "WetDay";
            _WetDay.Description = "Wet Days";
            _WetDay.MaxValue = ;
            _WetDay.MinValue = ;
            _WetDay.DefaultValue = ;
            _WetDay.Units = "day";
            _WetDay.ValueType = VarInfoValueTypes.GetInstanceForName("INTARRAY");

            _DSMID.Name = "DSMID";
            _DSMID.Description = "Depth to midpoint of soil layer NL";
            _DSMID.MaxValue = ;
            _DSMID.MinValue = ;
            _DSMID.DefaultValue = ;
            _DSMID.Units = "cm";
            _DSMID.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

        }

    }
}