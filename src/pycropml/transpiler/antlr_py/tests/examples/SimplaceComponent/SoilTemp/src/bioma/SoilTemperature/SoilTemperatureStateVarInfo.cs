
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SoilTemperature.DomainClass
{
    public class SoilTemperatureStateVarInfo : IVarInfoClass
    {
        static VarInfo _SoilSurfaceTemperature = new VarInfo();
        static VarInfo _SnowWaterContent = new VarInfo();

        static SoilTemperatureStateVarInfo()
        {
            SoilTemperatureStateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureState Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureState";}
        }

        public static  VarInfo SoilSurfaceTemperature
        {
            get { return _SoilSurfaceTemperature;}
        }

        public static  VarInfo SnowWaterContent
        {
            get { return _SnowWaterContent;}
        }

        static void DescribeVariables()
        {
            _SoilSurfaceTemperature.Name = "SoilSurfaceTemperature";
            _SoilSurfaceTemperature.Description = "Soil surface temperature";
            _SoilSurfaceTemperature.MaxValue = 70.0;
            _SoilSurfaceTemperature.MinValue = -40.0;
            _SoilSurfaceTemperature.DefaultValue = -1D;
            _SoilSurfaceTemperature.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _SoilSurfaceTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _SnowWaterContent.Name = "SnowWaterContent";
            _SnowWaterContent.Description = "Snow water content";
            _SnowWaterContent.MaxValue = 1500.0;
            _SnowWaterContent.MinValue = 0.0;
            _SnowWaterContent.DefaultValue = -1D;
            _SnowWaterContent.Units = "http://www.wurvoc.org/vocabularies/om-1.8/millimetre";
            _SnowWaterContent.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}