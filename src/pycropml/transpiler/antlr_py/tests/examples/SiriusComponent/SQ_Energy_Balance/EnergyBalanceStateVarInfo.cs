
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityEnergyBalance.DomainClass
{
    public class EnergyBalanceStateVarInfo : IVarInfoClass
    {
        static VarInfo _diffusionLimitedEvaporation = new VarInfo();
        static VarInfo _conductance = new VarInfo();
        static VarInfo _minCanopyTemperature = new VarInfo();
        static VarInfo _maxCanopyTemperature = new VarInfo();

        static EnergyBalanceStateVarInfo()
        {
            EnergyBalanceStateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "EnergyBalanceState Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "EnergyBalanceState";}
        }

        public static  VarInfo diffusionLimitedEvaporation
        {
            get { return _diffusionLimitedEvaporation;}
        }

        public static  VarInfo conductance
        {
            get { return _conductance;}
        }

        public static  VarInfo minCanopyTemperature
        {
            get { return _minCanopyTemperature;}
        }

        public static  VarInfo maxCanopyTemperature
        {
            get { return _maxCanopyTemperature;}
        }

        static void DescribeVariables()
        {
            _diffusionLimitedEvaporation.Name = "diffusionLimitedEvaporation";
            _diffusionLimitedEvaporation.Description = "the evaporation from the diffusion limited soil ";
            _diffusionLimitedEvaporation.MaxValue = 5000;
            _diffusionLimitedEvaporation.MinValue = 0;
            _diffusionLimitedEvaporation.DefaultValue = -1D;
            _diffusionLimitedEvaporation.Units = "g m-2 d-1";
            _diffusionLimitedEvaporation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _conductance.Name = "conductance";
            _conductance.Description = "the boundary layer conductance";
            _conductance.MaxValue = 10000;
            _conductance.MinValue = 0;
            _conductance.DefaultValue = -1D;
            _conductance.Units = "m/d";
            _conductance.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _minCanopyTemperature.Name = "minCanopyTemperature";
            _minCanopyTemperature.Description = "minimal Canopy Temperature  ";
            _minCanopyTemperature.MaxValue = 45;
            _minCanopyTemperature.MinValue = -30;
            _minCanopyTemperature.DefaultValue = -1D;
            _minCanopyTemperature.Units = "degC";
            _minCanopyTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _maxCanopyTemperature.Name = "maxCanopyTemperature";
            _maxCanopyTemperature.Description = "maximal Canopy Temperature ";
            _maxCanopyTemperature.MaxValue = 45;
            _maxCanopyTemperature.MinValue = -30;
            _maxCanopyTemperature.DefaultValue = -1D;
            _maxCanopyTemperature.Units = "degC";
            _maxCanopyTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}