
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperatureComp.DomainClass
{
    public class SoilTemperatureCompExogenousVarInfo : IVarInfoClass
    {
        static VarInfo _tmin = new VarInfo();
        static VarInfo _tmax = new VarInfo();
        static VarInfo _globrad = new VarInfo();
        static VarInfo _soilCoverage = new VarInfo();
        static VarInfo _soilSurfaceTemperatureBelowSnow = new VarInfo();
        static VarInfo _hasSnowCover = new VarInfo();

        static SoilTemperatureCompExogenousVarInfo()
        {
            SoilTemperatureCompExogenousVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureCompExogenous Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureCompExogenous";}
        }

        public static  VarInfo tmin
        {
            get { return _tmin;}
        }

        public static  VarInfo tmax
        {
            get { return _tmax;}
        }

        public static  VarInfo globrad
        {
            get { return _globrad;}
        }

        public static  VarInfo soilCoverage
        {
            get { return _soilCoverage;}
        }

        public static  VarInfo soilSurfaceTemperatureBelowSnow
        {
            get { return _soilSurfaceTemperatureBelowSnow;}
        }

        public static  VarInfo hasSnowCover
        {
            get { return _hasSnowCover;}
        }

        static void DescribeVariables()
        {
            _tmin.Name = "tmin";
            _tmin.Description = "the days min air temperature";
            _tmin.MaxValue = 70.0;
            _tmin.MinValue = -50.0;
            _tmin.DefaultValue = -1D;
            _tmin.Units = "°C";
            _tmin.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _tmax.Name = "tmax";
            _tmax.Description = "the days max air temperature";
            _tmax.MaxValue = 70.0;
            _tmax.MinValue = -50.0;
            _tmax.DefaultValue = -1D;
            _tmax.Units = "°C";
            _tmax.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _globrad.Name = "globrad";
            _globrad.Description = "the days global radiation";
            _globrad.MaxValue = 30.0;
            _globrad.MinValue = 0.0;
            _globrad.DefaultValue = 0.0;
            _globrad.Units = "MJ/m**2/d";
            _globrad.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _soilCoverage.Name = "soilCoverage";
            _soilCoverage.Description = "soilCoverage";
            _soilCoverage.MaxValue = -1D;
            _soilCoverage.MinValue = 0.0;
            _soilCoverage.DefaultValue = 0.0;
            _soilCoverage.Units = "dimensionless";
            _soilCoverage.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _soilSurfaceTemperatureBelowSnow.Name = "soilSurfaceTemperatureBelowSnow";
            _soilSurfaceTemperatureBelowSnow.Description = "soilSurfaceTemperature below snow cover";
            _soilSurfaceTemperatureBelowSnow.MaxValue = -1D;
            _soilSurfaceTemperatureBelowSnow.MinValue = -1D;
            _soilSurfaceTemperatureBelowSnow.DefaultValue = 0.0;
            _soilSurfaceTemperatureBelowSnow.Units = "°C";
            _soilSurfaceTemperatureBelowSnow.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _hasSnowCover.Name = "hasSnowCover";
            _hasSnowCover.Description = "is soil covered by snow";
            _hasSnowCover.MaxValue = -1D;
            _hasSnowCover.MinValue = -1D;
            _hasSnowCover.DefaultValue = -1D;
            _hasSnowCover.Units = "dimensionless";
            _hasSnowCover.ValueType = VarInfoValueTypes.GetInstanceForName("Boolean");

        }

    }
}