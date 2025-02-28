
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperature.DomainClass
{
    public class SoilTemperatureAuxiliaryVarInfo : IVarInfoClass
    {
        static VarInfo _SnowIsolationIndex = new VarInfo();

        static SoilTemperatureAuxiliaryVarInfo()
        {
            SoilTemperatureAuxiliaryVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureAuxiliary Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureAuxiliary";}
        }

        public static  VarInfo SnowIsolationIndex
        {
            get { return _SnowIsolationIndex;}
        }

        static void DescribeVariables()
        {
            _SnowIsolationIndex.Name = "SnowIsolationIndex";
            _SnowIsolationIndex.Description = "Snow isolation index";
            _SnowIsolationIndex.MaxValue = 1.0;
            _SnowIsolationIndex.MinValue = 0.0;
            _SnowIsolationIndex.DefaultValue = -1D;
            _SnowIsolationIndex.Units = "http://www.wurvoc.org/vocabularies/om-1.8/one";
            _SnowIsolationIndex.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}