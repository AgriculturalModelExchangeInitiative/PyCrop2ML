
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SoilTemperature.DomainClass
{
    public class SoilTemperatureRateVarInfo : IVarInfoClass
    {

        static SoilTemperatureRateVarInfo()
        {
            SoilTemperatureRateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureRate Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureRate";}
        }

        static void DescribeVariables()
        {
        }

    }
}