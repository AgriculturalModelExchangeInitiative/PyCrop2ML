
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemp.DomainClass
{
    public class SoilTempExogenousVarInfo : IVarInfoClass
    {
        static VarInfo _DEPIR = new VarInfo();
        static VarInfo _BIOMAS = new VarInfo();
        static VarInfo _TAMP = new VarInfo();
        static VarInfo _MULCHMASS = new VarInfo();
        static VarInfo _TMAX = new VarInfo();
        static VarInfo _SNOW = new VarInfo();
        static VarInfo _RAIN = new VarInfo();
        static VarInfo _TAV = new VarInfo();
        static VarInfo _TAVG = new VarInfo();
        static VarInfo _TMIN = new VarInfo();

        static SoilTempExogenousVarInfo()
        {
            SoilTempExogenousVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTempExogenous Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTempExogenous";}
        }

        public static  VarInfo DEPIR
        {
            get { return _DEPIR;}
        }

        public static  VarInfo BIOMAS
        {
            get { return _BIOMAS;}
        }

        public static  VarInfo TAMP
        {
            get { return _TAMP;}
        }

        public static  VarInfo MULCHMASS
        {
            get { return _MULCHMASS;}
        }

        public static  VarInfo TMAX
        {
            get { return _TMAX;}
        }

        public static  VarInfo SNOW
        {
            get { return _SNOW;}
        }

        public static  VarInfo RAIN
        {
            get { return _RAIN;}
        }

        public static  VarInfo TAV
        {
            get { return _TAV;}
        }

        public static  VarInfo TAVG
        {
            get { return _TAVG;}
        }

        public static  VarInfo TMIN
        {
            get { return _TMIN;}
        }

        static void DescribeVariables()
        {
            _DEPIR.Name = "DEPIR";
            _DEPIR.Description = "Management variable";
            _DEPIR.MaxValue = ;
            _DEPIR.MinValue = ;
            _DEPIR.DefaultValue = ;
            _DEPIR.Units = "don't know";
            _DEPIR.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _BIOMAS.Name = "BIOMAS";
            _BIOMAS.Description = "Biomass";
            _BIOMAS.MaxValue = ;
            _BIOMAS.MinValue = ;
            _BIOMAS.DefaultValue = ;
            _BIOMAS.Units = "kg/ha";
            _BIOMAS.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _TAMP.Name = "TAMP";
            _TAMP.Description = "Annual amplitude of the average air temperature";
            _TAMP.MaxValue = ;
            _TAMP.MinValue = ;
            _TAMP.DefaultValue = ;
            _TAMP.Units = "degC";
            _TAMP.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _MULCHMASS.Name = "MULCHMASS";
            _MULCHMASS.Description = "Mulch Mass";
            _MULCHMASS.MaxValue = ;
            _MULCHMASS.MinValue = ;
            _MULCHMASS.DefaultValue = ;
            _MULCHMASS.Units = "kg/ha";
            _MULCHMASS.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _TMAX.Name = "TMAX";
            _TMAX.Description = "Maximum daily temperature";
            _TMAX.MaxValue = ;
            _TMAX.MinValue = ;
            _TMAX.DefaultValue = ;
            _TMAX.Units = "degC";
            _TMAX.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _SNOW.Name = "SNOW";
            _SNOW.Description = "Snow cover";
            _SNOW.MaxValue = ;
            _SNOW.MinValue = ;
            _SNOW.DefaultValue = ;
            _SNOW.Units = "mm";
            _SNOW.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _RAIN.Name = "RAIN";
            _RAIN.Description = "daily rainfall";
            _RAIN.MaxValue = ;
            _RAIN.MinValue = ;
            _RAIN.DefaultValue = ;
            _RAIN.Units = "mm";
            _RAIN.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _TAV.Name = "TAV";
            _TAV.Description = "Average annual soil temperature, used with TAMP to calculate soil temperature.";
            _TAV.MaxValue = ;
            _TAV.MinValue = ;
            _TAV.DefaultValue = ;
            _TAV.Units = "degC";
            _TAV.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _TAVG.Name = "TAVG";
            _TAVG.Description = "Average daily temperature";
            _TAVG.MaxValue = ;
            _TAVG.MinValue = ;
            _TAVG.DefaultValue = ;
            _TAVG.Units = "degC";
            _TAVG.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _TMIN.Name = "TMIN";
            _TMIN.Description = "Maximum Temperature";
            _TMIN.MaxValue = ;
            _TMIN.MinValue = ;
            _TMIN.DefaultValue = ;
            _TMIN.Units = "degC";
            _TMIN.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}