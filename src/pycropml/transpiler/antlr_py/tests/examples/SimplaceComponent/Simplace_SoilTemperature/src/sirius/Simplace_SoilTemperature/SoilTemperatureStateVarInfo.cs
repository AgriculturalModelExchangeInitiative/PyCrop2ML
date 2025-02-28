
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperature.DomainClass
{
    public class SoilTemperatureStateVarInfo : IVarInfoClass
    {
        static VarInfo _Albedo = new VarInfo();
        static VarInfo _SnowWaterContent = new VarInfo();
        static VarInfo _SoilSurfaceTemperature = new VarInfo();
        static VarInfo _AgeOfSnow = new VarInfo();
        static VarInfo _pSoilLayerDepth = new VarInfo();
        static VarInfo _SoilTempArray = new VarInfo();

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

        public static  VarInfo Albedo
        {
            get { return _Albedo;}
        }

        public static  VarInfo SnowWaterContent
        {
            get { return _SnowWaterContent;}
        }

        public static  VarInfo SoilSurfaceTemperature
        {
            get { return _SoilSurfaceTemperature;}
        }

        public static  VarInfo AgeOfSnow
        {
            get { return _AgeOfSnow;}
        }

        public static  VarInfo pSoilLayerDepth
        {
            get { return _pSoilLayerDepth;}
        }

        public static  VarInfo SoilTempArray
        {
            get { return _SoilTempArray;}
        }

        static void DescribeVariables()
        {
            _Albedo.Name = "Albedo";
            _Albedo.Description = "Albedo";
            _Albedo.MaxValue = 1.0;
            _Albedo.MinValue = 0.0;
            _Albedo.DefaultValue = -1D;
            _Albedo.Units = "http://www.wurvoc.org/vocabularies/om-1.8/one";
            _Albedo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _SnowWaterContent.Name = "SnowWaterContent";
            _SnowWaterContent.Description = "Snow water content";
            _SnowWaterContent.MaxValue = 1500.0;
            _SnowWaterContent.MinValue = 0.0;
            _SnowWaterContent.DefaultValue = 0.0;
            _SnowWaterContent.Units = "http://www.wurvoc.org/vocabularies/om-1.8/millimetre";
            _SnowWaterContent.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _SoilSurfaceTemperature.Name = "SoilSurfaceTemperature";
            _SoilSurfaceTemperature.Description = "Soil surface temperature";
            _SoilSurfaceTemperature.MaxValue = 70.0;
            _SoilSurfaceTemperature.MinValue = -40.0;
            _SoilSurfaceTemperature.DefaultValue = 0.0;
            _SoilSurfaceTemperature.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _SoilSurfaceTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _AgeOfSnow.Name = "AgeOfSnow";
            _AgeOfSnow.Description = "Age of snow";
            _AgeOfSnow.MaxValue = null;
            _AgeOfSnow.MinValue = 0;
            _AgeOfSnow.DefaultValue = 0;
            _AgeOfSnow.Units = "http://www.wurvoc.org/vocabularies/om-1.8/one";
            _AgeOfSnow.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            _pSoilLayerDepth.Name = "pSoilLayerDepth";
            _pSoilLayerDepth.Description = "Depth of soil layer plus additional depth";
            _pSoilLayerDepth.MaxValue = -1D;
            _pSoilLayerDepth.MinValue = -1D;
            _pSoilLayerDepth.DefaultValue = -1D;
            _pSoilLayerDepth.Units = "http://www.wurvoc.org/vocabularies/om-1.8/metre";
            _pSoilLayerDepth.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

            _SoilTempArray.Name = "SoilTempArray";
            _SoilTempArray.Description = "Array of temperature ";
            _SoilTempArray.MaxValue = -1D;
            _SoilTempArray.MinValue = -1D;
            _SoilTempArray.DefaultValue = -1D;
            _SoilTempArray.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _SoilTempArray.ValueType = VarInfoValueTypes.GetInstanceForName("DOUBLEARRAY");

        }

    }
}