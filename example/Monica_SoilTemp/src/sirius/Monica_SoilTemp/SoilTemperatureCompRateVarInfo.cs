
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperatureComp.DomainClass
{
    public class SoilTemperatureCompRateVarInfo : IVarInfoClass
    {

        static SoilTemperatureCompRateVarInfo()
        {
            SoilTemperatureCompRateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureCompRate Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureCompRate";}
        }

        static void DescribeVariables()
        {
        }

    }
}