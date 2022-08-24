
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemp.DomainClass
{
    public class SoilTempAuxiliaryVarInfo : IVarInfoClass
    {

        static SoilTempAuxiliaryVarInfo()
        {
            SoilTempAuxiliaryVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTempAuxiliary Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTempAuxiliary";}
        }

        static void DescribeVariables()
        {
        }

    }
}