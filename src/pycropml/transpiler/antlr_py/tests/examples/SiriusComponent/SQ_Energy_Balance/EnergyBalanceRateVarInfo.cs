
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityEnergyBalance.DomainClass
{
    public class EnergyBalanceRateVarInfo : IVarInfoClass
    {
        static VarInfo _evapoTranspirationPriestlyTaylor = new VarInfo();
        static VarInfo _evapoTranspirationPenman = new VarInfo();
        static VarInfo _evapoTranspiration = new VarInfo();
        static VarInfo _potentialTranspiration = new VarInfo();
        static VarInfo _soilHeatFlux = new VarInfo();
        static VarInfo _cropHeatFlux = new VarInfo();

        static EnergyBalanceRateVarInfo()
        {
            EnergyBalanceRateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "EnergyBalanceRate Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "EnergyBalanceRate";}
        }

        public static  VarInfo evapoTranspirationPriestlyTaylor
        {
            get { return _evapoTranspirationPriestlyTaylor;}
        }

        public static  VarInfo evapoTranspirationPenman
        {
            get { return _evapoTranspirationPenman;}
        }

        public static  VarInfo evapoTranspiration
        {
            get { return _evapoTranspiration;}
        }

        public static  VarInfo potentialTranspiration
        {
            get { return _potentialTranspiration;}
        }

        public static  VarInfo soilHeatFlux
        {
            get { return _soilHeatFlux;}
        }

        public static  VarInfo cropHeatFlux
        {
            get { return _cropHeatFlux;}
        }

        static void DescribeVariables()
        {
            _evapoTranspirationPriestlyTaylor.Name = "evapoTranspirationPriestlyTaylor";
            _evapoTranspirationPriestlyTaylor.Description = "evapoTranspiration of Priestly Taylor ";
            _evapoTranspirationPriestlyTaylor.MaxValue = 10000;
            _evapoTranspirationPriestlyTaylor.MinValue = 0;
            _evapoTranspirationPriestlyTaylor.DefaultValue = -1D;
            _evapoTranspirationPriestlyTaylor.Units = "g m-2 d-1";
            _evapoTranspirationPriestlyTaylor.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _evapoTranspirationPenman.Name = "evapoTranspirationPenman";
            _evapoTranspirationPenman.Description = " evapoTranspiration of Penman Monteith";
            _evapoTranspirationPenman.MaxValue = 5000;
            _evapoTranspirationPenman.MinValue = 0;
            _evapoTranspirationPenman.DefaultValue = -1D;
            _evapoTranspirationPenman.Units = "g m-2 d-1";
            _evapoTranspirationPenman.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _evapoTranspiration.Name = "evapoTranspiration";
            _evapoTranspiration.Description = "evapoTranspiration";
            _evapoTranspiration.MaxValue = 10000;
            _evapoTranspiration.MinValue = 0;
            _evapoTranspiration.DefaultValue = -1D;
            _evapoTranspiration.Units = "mm";
            _evapoTranspiration.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _potentialTranspiration.Name = "potentialTranspiration";
            _potentialTranspiration.Description = "potential Transpiration ";
            _potentialTranspiration.MaxValue = 10000;
            _potentialTranspiration.MinValue = 0;
            _potentialTranspiration.DefaultValue = -1D;
            _potentialTranspiration.Units = "g m-2 d-1";
            _potentialTranspiration.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _soilHeatFlux.Name = "soilHeatFlux";
            _soilHeatFlux.Description = "soil Heat Flux ";
            _soilHeatFlux.MaxValue = 10000;
            _soilHeatFlux.MinValue = 0;
            _soilHeatFlux.DefaultValue = -1D;
            _soilHeatFlux.Units = "g m-2 d-1";
            _soilHeatFlux.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _cropHeatFlux.Name = "cropHeatFlux";
            _cropHeatFlux.Description = " crop Heat Flux";
            _cropHeatFlux.MaxValue = 10000;
            _cropHeatFlux.MinValue = 0;
            _cropHeatFlux.DefaultValue = -1D;
            _cropHeatFlux.Units = "g m-2 d-1";
            _cropHeatFlux.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}