
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityEnergyBalance.DomainClass
{
    public class EnergyBalanceAuxiliaryVarInfo : IVarInfoClass
    {
        static VarInfo _minTair = new VarInfo();
        static VarInfo _maxTair = new VarInfo();
        static VarInfo _solarRadiation = new VarInfo();
        static VarInfo _vaporPressure = new VarInfo();
        static VarInfo _extraSolarRadiation = new VarInfo();
        static VarInfo _hslope = new VarInfo();
        static VarInfo _plantHeight = new VarInfo();
        static VarInfo _wind = new VarInfo();
        static VarInfo _deficitOnTopLayers = new VarInfo();
        static VarInfo _VPDair = new VarInfo();
        static VarInfo _netRadiation = new VarInfo();
        static VarInfo _netOutGoingLongWaveRadiation = new VarInfo();
        static VarInfo _netRadiationEquivalentEvaporation = new VarInfo();
        static VarInfo _energyLimitedEvaporation = new VarInfo();
        static VarInfo _soilEvaporation = new VarInfo();

        static EnergyBalanceAuxiliaryVarInfo()
        {
            EnergyBalanceAuxiliaryVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "EnergyBalanceAuxiliary Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "EnergyBalanceAuxiliary";}
        }

        public static  VarInfo minTair
        {
            get { return _minTair;}
        }

        public static  VarInfo maxTair
        {
            get { return _maxTair;}
        }

        public static  VarInfo solarRadiation
        {
            get { return _solarRadiation;}
        }

        public static  VarInfo vaporPressure
        {
            get { return _vaporPressure;}
        }

        public static  VarInfo extraSolarRadiation
        {
            get { return _extraSolarRadiation;}
        }

        public static  VarInfo hslope
        {
            get { return _hslope;}
        }

        public static  VarInfo plantHeight
        {
            get { return _plantHeight;}
        }

        public static  VarInfo wind
        {
            get { return _wind;}
        }

        public static  VarInfo deficitOnTopLayers
        {
            get { return _deficitOnTopLayers;}
        }

        public static  VarInfo VPDair
        {
            get { return _VPDair;}
        }

        public static  VarInfo netRadiation
        {
            get { return _netRadiation;}
        }

        public static  VarInfo netOutGoingLongWaveRadiation
        {
            get { return _netOutGoingLongWaveRadiation;}
        }

        public static  VarInfo netRadiationEquivalentEvaporation
        {
            get { return _netRadiationEquivalentEvaporation;}
        }

        public static  VarInfo energyLimitedEvaporation
        {
            get { return _energyLimitedEvaporation;}
        }

        public static  VarInfo soilEvaporation
        {
            get { return _soilEvaporation;}
        }

        static void DescribeVariables()
        {
            _minTair.Name = "minTair";
            _minTair.Description = "minimum air temperature";
            _minTair.MaxValue = 45;
            _minTair.MinValue = -30;
            _minTair.DefaultValue = 0.7;
            _minTair.Units = "°C";
            _minTair.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _maxTair.Name = "maxTair";
            _maxTair.Description = "maximum air Temperature";
            _maxTair.MaxValue = 45;
            _maxTair.MinValue = -30;
            _maxTair.DefaultValue = 7.2;
            _maxTair.Units = "°C";
            _maxTair.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _solarRadiation.Name = "solarRadiation";
            _solarRadiation.Description = "solar Radiation";
            _solarRadiation.MaxValue = 1000;
            _solarRadiation.MinValue = 0;
            _solarRadiation.DefaultValue = 3;
            _solarRadiation.Units = "MJ m-2 d-1";
            _solarRadiation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _vaporPressure.Name = "vaporPressure";
            _vaporPressure.Description = "vapor Pressure";
            _vaporPressure.MaxValue = 1000;
            _vaporPressure.MinValue = 0;
            _vaporPressure.DefaultValue = 6.1;
            _vaporPressure.Units = "hPa";
            _vaporPressure.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _extraSolarRadiation.Name = "extraSolarRadiation";
            _extraSolarRadiation.Description = "extra Solar Radiation";
            _extraSolarRadiation.MaxValue = 1000;
            _extraSolarRadiation.MinValue = 0;
            _extraSolarRadiation.DefaultValue = 11.7;
            _extraSolarRadiation.Units = "MJ m2 d-1";
            _extraSolarRadiation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _hslope.Name = "hslope";
            _hslope.Description = "the slope of saturated vapor pressure temperature curve at a given temperature ";
            _hslope.MaxValue = 1000;
            _hslope.MinValue = 0;
            _hslope.DefaultValue = 0.584;
            _hslope.Units = "hPa °C-1";
            _hslope.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _plantHeight.Name = "plantHeight";
            _plantHeight.Description = "plant Height";
            _plantHeight.MaxValue = 1000;
            _plantHeight.MinValue = 0;
            _plantHeight.DefaultValue = 0;
            _plantHeight.Units = "mm";
            _plantHeight.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _wind.Name = "wind";
            _wind.Description = "wind";
            _wind.MaxValue = 1000000;
            _wind.MinValue = 0;
            _wind.DefaultValue = 124000;
            _wind.Units = "m/d";
            _wind.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _deficitOnTopLayers.Name = "deficitOnTopLayers";
            _deficitOnTopLayers.Description = "deficit On TopLayers";
            _deficitOnTopLayers.MaxValue = 10000;
            _deficitOnTopLayers.MinValue = 0;
            _deficitOnTopLayers.DefaultValue = 5341;
            _deficitOnTopLayers.Units = "g m-2 d-1";
            _deficitOnTopLayers.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _VPDair.Name = "VPDair";
            _VPDair.Description = " vapour pressure density";
            _VPDair.MaxValue = 1000;
            _VPDair.MinValue = 0;
            _VPDair.DefaultValue = 2.19;
            _VPDair.Units = "hPa";
            _VPDair.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _netRadiation.Name = "netRadiation";
            _netRadiation.Description = " net radiation ";
            _netRadiation.MaxValue = 5000;
            _netRadiation.MinValue = 0;
            _netRadiation.DefaultValue = -1D;
            _netRadiation.Units = "MJ m-2 d-1";
            _netRadiation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _netOutGoingLongWaveRadiation.Name = "netOutGoingLongWaveRadiation";
            _netOutGoingLongWaveRadiation.Description = "net OutGoing Long Wave Radiation ";
            _netOutGoingLongWaveRadiation.MaxValue = 5000;
            _netOutGoingLongWaveRadiation.MinValue = 0;
            _netOutGoingLongWaveRadiation.DefaultValue = -1D;
            _netOutGoingLongWaveRadiation.Units = "g m-2 d-1";
            _netOutGoingLongWaveRadiation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _netRadiationEquivalentEvaporation.Name = "netRadiationEquivalentEvaporation";
            _netRadiationEquivalentEvaporation.Description = "net Radiation in Equivalent Evaporation ";
            _netRadiationEquivalentEvaporation.MaxValue = 5000;
            _netRadiationEquivalentEvaporation.MinValue = 0;
            _netRadiationEquivalentEvaporation.DefaultValue = -1D;
            _netRadiationEquivalentEvaporation.Units = "g m-2 d-1";
            _netRadiationEquivalentEvaporation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _energyLimitedEvaporation.Name = "energyLimitedEvaporation";
            _energyLimitedEvaporation.Description = "energy Limited Evaporation ";
            _energyLimitedEvaporation.MaxValue = 5000;
            _energyLimitedEvaporation.MinValue = 0;
            _energyLimitedEvaporation.DefaultValue = -1D;
            _energyLimitedEvaporation.Units = "g m-2 d-1";
            _energyLimitedEvaporation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _soilEvaporation.Name = "soilEvaporation";
            _soilEvaporation.Description = "soil Evaporation";
            _soilEvaporation.MaxValue = 5000;
            _soilEvaporation.MinValue = 0;
            _soilEvaporation.DefaultValue = -1D;
            _soilEvaporation.Units = "g m-2 d-1";
            _soilEvaporation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}