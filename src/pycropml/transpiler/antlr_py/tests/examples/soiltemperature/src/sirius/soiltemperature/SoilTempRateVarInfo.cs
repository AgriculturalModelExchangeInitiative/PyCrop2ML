
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemp.DomainClass
{
    public class SoilTempRateVarInfo : IVarInfoClass
    {

        static SoilTempRateVarInfo()
        {
            SoilTempRateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTempRate Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTempRate";}
        }

        static void DescribeVariables()
        {
        }

    }
}