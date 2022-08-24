
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityEnergyBalance.DomainClass
{
    public class EnergyBalanceExogenousVarInfo : IVarInfoClass
    {

        static EnergyBalanceExogenousVarInfo()
        {
            EnergyBalanceExogenousVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "EnergyBalanceExogenous Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "EnergyBalanceExogenous";}
        }

        static void DescribeVariables()
        {
        }

    }
}