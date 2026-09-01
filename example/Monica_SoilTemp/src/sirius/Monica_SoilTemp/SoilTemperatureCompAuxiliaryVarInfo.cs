
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperatureComp.DomainClass
{
    public class SoilTemperatureCompAuxiliaryVarInfo : IVarInfoClass
    {

        static SoilTemperatureCompAuxiliaryVarInfo()
        {
            SoilTemperatureCompAuxiliaryVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureCompAuxiliary Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureCompAuxiliary";}
        }

        static void DescribeVariables()
        {
        }

    }
}