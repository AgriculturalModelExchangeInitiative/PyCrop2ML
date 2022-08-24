
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       

using SiriusQualityEnergyBalance.DomainClass;
namespace SiriusQualityEnergyBalance.Strategies
{
    public class EnergyBalanceComponent : IStrategySiriusQualityEnergyBalance
    {
        public EnergyBalanceComponent()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new CompositeStrategyVarInfo(_NetRadiation, "albedoCoefficient");
            _parameters0_0.Add(v1);
            VarInfo v2 = new CompositeStrategyVarInfo(_NetRadiation, "stefanBoltzman");
            _parameters0_0.Add(v2);
            VarInfo v3 = new CompositeStrategyVarInfo(_NetRadiation, "elevation");
            _parameters0_0.Add(v3);
            VarInfo v4 = new CompositeStrategyVarInfo(_NetRadiationEquivalentEvaporation, "lambdaV");
            _parameters0_0.Add(v4);
            VarInfo v5 = new CompositeStrategyVarInfo(_Penman, "lambdaV");
            _parameters0_0.Add(v5);
            VarInfo v6 = new CompositeStrategyVarInfo(_CanopyTemperature, "lambdaV");
            _parameters0_0.Add(v6);
            VarInfo v7 = new CompositeStrategyVarInfo(_PriestlyTaylor, "psychrometricConstant");
            _parameters0_0.Add(v7);
            VarInfo v8 = new CompositeStrategyVarInfo(_Penman, "psychrometricConstant");
            _parameters0_0.Add(v8);
            VarInfo v9 = new CompositeStrategyVarInfo(_PriestlyTaylor, "Alpha");
            _parameters0_0.Add(v9);
            VarInfo v10 = new CompositeStrategyVarInfo(_Penman, "Alpha");
            _parameters0_0.Add(v10);
            VarInfo v11 = new CompositeStrategyVarInfo(_PtSoil, "Alpha");
            _parameters0_0.Add(v11);
            VarInfo v12 = new CompositeStrategyVarInfo(_Conductance, "vonKarman");
            _parameters0_0.Add(v12);
            VarInfo v13 = new CompositeStrategyVarInfo(_Conductance, "heightWeatherMeasurements");
            _parameters0_0.Add(v13);
            VarInfo v14 = new CompositeStrategyVarInfo(_Conductance, "zm");
            _parameters0_0.Add(v14);
            VarInfo v15 = new CompositeStrategyVarInfo(_Conductance, "d");
            _parameters0_0.Add(v15);
            VarInfo v16 = new CompositeStrategyVarInfo(_Conductance, "zh");
            _parameters0_0.Add(v16);
            VarInfo v17 = new CompositeStrategyVarInfo(_DiffusionLimitedEvaporation, "soilDiffusionConstant");
            _parameters0_0.Add(v17);
            VarInfo v18 = new CompositeStrategyVarInfo(_Penman, "rhoDensityAir");
            _parameters0_0.Add(v18);
            VarInfo v19 = new CompositeStrategyVarInfo(_CanopyTemperature, "rhoDensityAir");
            _parameters0_0.Add(v19);
            VarInfo v20 = new CompositeStrategyVarInfo(_Penman, "specificHeatCapacityAir");
            _parameters0_0.Add(v20);
            VarInfo v21 = new CompositeStrategyVarInfo(_CanopyTemperature, "specificHeatCapacityAir");
            _parameters0_0.Add(v21);
            VarInfo v22 = new CompositeStrategyVarInfo(_PtSoil, "tau");
            _parameters0_0.Add(v22);
            VarInfo v23 = new CompositeStrategyVarInfo(_SoilHeatFlux, "tau");
            _parameters0_0.Add(v23);
            VarInfo v24 = new CompositeStrategyVarInfo(_PotentialTranspiration, "tau");
            _parameters0_0.Add(v24);
            VarInfo v25 = new CompositeStrategyVarInfo(_PtSoil, "tauAlpha");
            _parameters0_0.Add(v25);
            VarInfo v26 = new CompositeStrategyVarInfo(_EvapoTranspiration, "isWindVpDefined");
            _parameters0_0.Add(v26);
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd1.PropertyName = "minTair";
            pd1.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd2.PropertyName = "maxTair";
            pd2.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd3.PropertyName = "solarRadiation";
            pd3.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.solarRadiation).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.solarRadiation);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd4.PropertyName = "vaporPressure";
            pd4.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.vaporPressure).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.vaporPressure);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd5.PropertyName = "extraSolarRadiation";
            pd5.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.extraSolarRadiation).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.extraSolarRadiation);
            _inputs0_0.Add(pd5);
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd6.PropertyName = "hslope";
            pd6.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.hslope).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.hslope);
            _inputs0_0.Add(pd6);
            PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd7.PropertyName = "plantHeight";
            pd7.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.plantHeight).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.plantHeight);
            _inputs0_0.Add(pd7);
            PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd8.PropertyName = "wind";
            pd8.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.wind).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.wind);
            _inputs0_0.Add(pd8);
            PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd9.PropertyName = "deficitOnTopLayers";
            pd9.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.deficitOnTopLayers).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.deficitOnTopLayers);
            _inputs0_0.Add(pd9);
            PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd10.PropertyName = "VPDair";
            pd10.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.VPDair).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.VPDair);
            _inputs0_0.Add(pd10);
            mo0_0.Inputs=_inputs0_0;
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd11 = new PropertyDescription();
            pd11.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd11.PropertyName = "netRadiation";
            pd11.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiation).ValueType.TypeForCurrentValue;
            pd11.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiation);
            _outputs0_0.Add(pd11);
            PropertyDescription pd12 = new PropertyDescription();
            pd12.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd12.PropertyName = "netOutGoingLongWaveRadiation";
            pd12.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation).ValueType.TypeForCurrentValue;
            pd12.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation);
            _outputs0_0.Add(pd12);
            PropertyDescription pd13 = new PropertyDescription();
            pd13.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd13.PropertyName = "netRadiationEquivalentEvaporation";
            pd13.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation).ValueType.TypeForCurrentValue;
            pd13.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation);
            _outputs0_0.Add(pd13);
            PropertyDescription pd14 = new PropertyDescription();
            pd14.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd14.PropertyName = "evapoTranspirationPriestlyTaylor";
            pd14.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor).ValueType.TypeForCurrentValue;
            pd14.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor);
            _outputs0_0.Add(pd14);
            PropertyDescription pd15 = new PropertyDescription();
            pd15.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd15.PropertyName = "diffusionLimitedEvaporation";
            pd15.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.diffusionLimitedEvaporation).ValueType.TypeForCurrentValue;
            pd15.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.diffusionLimitedEvaporation);
            _outputs0_0.Add(pd15);
            PropertyDescription pd16 = new PropertyDescription();
            pd16.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd16.PropertyName = "energyLimitedEvaporation";
            pd16.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.energyLimitedEvaporation).ValueType.TypeForCurrentValue;
            pd16.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.energyLimitedEvaporation);
            _outputs0_0.Add(pd16);
            PropertyDescription pd17 = new PropertyDescription();
            pd17.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd17.PropertyName = "conductance";
            pd17.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance).ValueType.TypeForCurrentValue;
            pd17.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance);
            _outputs0_0.Add(pd17);
            PropertyDescription pd18 = new PropertyDescription();
            pd18.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd18.PropertyName = "evapoTranspirationPenman";
            pd18.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman).ValueType.TypeForCurrentValue;
            pd18.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman);
            _outputs0_0.Add(pd18);
            PropertyDescription pd19 = new PropertyDescription();
            pd19.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary);
            pd19.PropertyName = "soilEvaporation";
            pd19.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.soilEvaporation).ValueType.TypeForCurrentValue;
            pd19.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.soilEvaporation);
            _outputs0_0.Add(pd19);
            PropertyDescription pd20 = new PropertyDescription();
            pd20.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd20.PropertyName = "evapoTranspiration";
            pd20.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration).ValueType.TypeForCurrentValue;
            pd20.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration);
            _outputs0_0.Add(pd20);
            PropertyDescription pd21 = new PropertyDescription();
            pd21.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd21.PropertyName = "potentialTranspiration";
            pd21.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.potentialTranspiration).ValueType.TypeForCurrentValue;
            pd21.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.potentialTranspiration);
            _outputs0_0.Add(pd21);
            PropertyDescription pd22 = new PropertyDescription();
            pd22.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd22.PropertyName = "soilHeatFlux";
            pd22.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.soilHeatFlux).ValueType.TypeForCurrentValue;
            pd22.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.soilHeatFlux);
            _outputs0_0.Add(pd22);
            PropertyDescription pd23 = new PropertyDescription();
            pd23.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate);
            pd23.PropertyName = "cropHeatFlux";
            pd23.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux).ValueType.TypeForCurrentValue;
            pd23.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux);
            _outputs0_0.Add(pd23);
            PropertyDescription pd24 = new PropertyDescription();
            pd24.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd24.PropertyName = "minCanopyTemperature";
            pd24.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature).ValueType.TypeForCurrentValue;
            pd24.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature);
            _outputs0_0.Add(pd24);
            PropertyDescription pd25 = new PropertyDescription();
            pd25.DomainClassType = typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState);
            pd25.PropertyName = "maxCanopyTemperature";
            pd25.PropertyType = (SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature).ValueType.TypeForCurrentValue;
            pd25.PropertyVarInfo =(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature);
            _outputs0_0.Add(pd25);
            mo0_0.Outputs=_outputs0_0;
            List<string> lAssStrat0_0 = new List<string>();
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.NetRadiation).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.NetRadiationEquivalentEvaporation).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.PriestlyTaylor).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.Conductance).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.DiffusionLimitedEvaporation).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.Penman).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.PtSoil).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.SoilEvaporation).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.EvapoTranspiration).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.SoilHeatFlux).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.PotentialTranspiration).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.CropHeatFlux).FullName);
            lAssStrat0_0.Add(typeof(SiriusQualityEnergyBalance.Strategies.CanopyTemperature).FullName);
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();
        }

        public string Description
        {
            get { return "Modelling energy balance in the wheat crop model SiriusQuality2: Evapotranspiration and canopy and soil temperature calculations                        see documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=547    " ;}
        }

        public string URL
        {
            get { return "" ;}
        }

        public string Domain
        {
            get { return "";}
        }

        public string ModelType
        {
            get { return "";}
        }

        public bool IsContext
        {
            get { return false;}
        }

        public IList<int> TimeStep
        {
            get
            {
                IList<int> ts = new List<int>();
                return ts;
            }
        }

        private  PublisherData _pd;
        public PublisherData PublisherData
        {
            get { return _pd;} 
        }

        private  void SetPublisherData()
        {
            _pd = new CRA.ModelLayer.MetadataTypes.PublisherData();
            _pd.Add("Creator", "Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. "); 
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary), typeof(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous)};
        }

        public double albedoCoefficient
        {
            get
            {
                 return _NetRadiation.albedoCoefficient; 
            }
            set
            {
                _NetRadiation.albedoCoefficient = value;
            }
        }
        public double stefanBoltzman
        {
            get
            {
                 return _NetRadiation.stefanBoltzman; 
            }
            set
            {
                _NetRadiation.stefanBoltzman = value;
            }
        }
        public double elevation
        {
            get
            {
                 return _NetRadiation.elevation; 
            }
            set
            {
                _NetRadiation.elevation = value;
            }
        }
        public double lambdaV
        {
            get
            {
                 return _NetRadiationEquivalentEvaporation.lambdaV; 
            }
            set
            {
                _NetRadiationEquivalentEvaporation.lambdaV = value;
                _Penman.lambdaV = value;
                _CanopyTemperature.lambdaV = value;
            }
        }
        public double psychrometricConstant
        {
            get
            {
                 return _PriestlyTaylor.psychrometricConstant; 
            }
            set
            {
                _PriestlyTaylor.psychrometricConstant = value;
                _Penman.psychrometricConstant = value;
            }
        }
        public double Alpha
        {
            get
            {
                 return _PriestlyTaylor.Alpha; 
            }
            set
            {
                _PriestlyTaylor.Alpha = value;
                _Penman.Alpha = value;
                _PtSoil.Alpha = value;
            }
        }
        public double vonKarman
        {
            get
            {
                 return _Conductance.vonKarman; 
            }
            set
            {
                _Conductance.vonKarman = value;
            }
        }
        public double heightWeatherMeasurements
        {
            get
            {
                 return _Conductance.heightWeatherMeasurements; 
            }
            set
            {
                _Conductance.heightWeatherMeasurements = value;
            }
        }
        public double zm
        {
            get
            {
                 return _Conductance.zm; 
            }
            set
            {
                _Conductance.zm = value;
            }
        }
        public double d
        {
            get
            {
                 return _Conductance.d; 
            }
            set
            {
                _Conductance.d = value;
            }
        }
        public double zh
        {
            get
            {
                 return _Conductance.zh; 
            }
            set
            {
                _Conductance.zh = value;
            }
        }
        public double soilDiffusionConstant
        {
            get
            {
                 return _DiffusionLimitedEvaporation.soilDiffusionConstant; 
            }
            set
            {
                _DiffusionLimitedEvaporation.soilDiffusionConstant = value;
            }
        }
        public double rhoDensityAir
        {
            get
            {
                 return _Penman.rhoDensityAir; 
            }
            set
            {
                _Penman.rhoDensityAir = value;
                _CanopyTemperature.rhoDensityAir = value;
            }
        }
        public double specificHeatCapacityAir
        {
            get
            {
                 return _Penman.specificHeatCapacityAir; 
            }
            set
            {
                _Penman.specificHeatCapacityAir = value;
                _CanopyTemperature.specificHeatCapacityAir = value;
            }
        }
        public double tau
        {
            get
            {
                 return _PtSoil.tau; 
            }
            set
            {
                _PtSoil.tau = value;
                _SoilHeatFlux.tau = value;
                _PotentialTranspiration.tau = value;
            }
        }
        public double tauAlpha
        {
            get
            {
                 return _PtSoil.tauAlpha; 
            }
            set
            {
                _PtSoil.tauAlpha = value;
            }
        }
        public int isWindVpDefined
        {
            get
            {
                 return _EvapoTranspiration.isWindVpDefined; 
            }
            set
            {
                _EvapoTranspiration.isWindVpDefined = value;
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
            _NetRadiation.SetParametersDefaultValue();
            _NetRadiationEquivalentEvaporation.SetParametersDefaultValue();
            _PriestlyTaylor.SetParametersDefaultValue();
            _Conductance.SetParametersDefaultValue();
            _DiffusionLimitedEvaporation.SetParametersDefaultValue();
            _Penman.SetParametersDefaultValue();
            _PtSoil.SetParametersDefaultValue();
            _SoilEvaporation.SetParametersDefaultValue();
            _EvapoTranspiration.SetParametersDefaultValue();
            _SoilHeatFlux.SetParametersDefaultValue();
            _PotentialTranspiration.SetParametersDefaultValue();
            _CropHeatFlux.SetParametersDefaultValue();
            _CanopyTemperature.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            albedoCoefficientVarInfo.Name = "albedoCoefficient";
            albedoCoefficientVarInfo.Description = "albedo Coefficient";
            albedoCoefficientVarInfo.MaxValue = 1;
            albedoCoefficientVarInfo.MinValue = 0;
            albedoCoefficientVarInfo.DefaultValue = 0.23;
            albedoCoefficientVarInfo.Units = "";
            albedoCoefficientVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            stefanBoltzmanVarInfo.Name = "stefanBoltzman";
            stefanBoltzmanVarInfo.Description = "stefan Boltzman constant";
            stefanBoltzmanVarInfo.MaxValue = 1;
            stefanBoltzmanVarInfo.MinValue = 0;
            stefanBoltzmanVarInfo.DefaultValue = 4.903E-09;
            stefanBoltzmanVarInfo.Units = "";
            stefanBoltzmanVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            elevationVarInfo.Name = "elevation";
            elevationVarInfo.Description = "elevation";
            elevationVarInfo.MaxValue = 10000;
            elevationVarInfo.MinValue = -500;
            elevationVarInfo.DefaultValue = 0;
            elevationVarInfo.Units = "m";
            elevationVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lambdaVVarInfo.Name = "lambdaV";
            lambdaVVarInfo.Description = "latent heat of vaporization of water";
            lambdaVVarInfo.MaxValue = 10;
            lambdaVVarInfo.MinValue = 0;
            lambdaVVarInfo.DefaultValue = 2.454;
            lambdaVVarInfo.Units = "MJ kg-1";
            lambdaVVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            psychrometricConstantVarInfo.Name = "psychrometricConstant";
            psychrometricConstantVarInfo.Description = "psychrometric constant";
            psychrometricConstantVarInfo.MaxValue = 1;
            psychrometricConstantVarInfo.MinValue = 0;
            psychrometricConstantVarInfo.DefaultValue = 0.66;
            psychrometricConstantVarInfo.Units = "";
            psychrometricConstantVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            AlphaVarInfo.Name = "Alpha";
            AlphaVarInfo.Description = "Priestley-Taylor evapotranspiration proportionality constant";
            AlphaVarInfo.MaxValue = 100;
            AlphaVarInfo.MinValue = 0;
            AlphaVarInfo.DefaultValue = 1.5;
            AlphaVarInfo.Units = "";
            AlphaVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            vonKarmanVarInfo.Name = "vonKarman";
            vonKarmanVarInfo.Description = "von Karman constant";
            vonKarmanVarInfo.MaxValue = 1;
            vonKarmanVarInfo.MinValue = 0;
            vonKarmanVarInfo.DefaultValue = 0.42;
            vonKarmanVarInfo.Units = "dimensionless";
            vonKarmanVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            heightWeatherMeasurementsVarInfo.Name = "heightWeatherMeasurements";
            heightWeatherMeasurementsVarInfo.Description = "reference height of wind and humidity measurements";
            heightWeatherMeasurementsVarInfo.MaxValue = 10;
            heightWeatherMeasurementsVarInfo.MinValue = 0;
            heightWeatherMeasurementsVarInfo.DefaultValue = 2;
            heightWeatherMeasurementsVarInfo.Units = "m";
            heightWeatherMeasurementsVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            zmVarInfo.Name = "zm";
            zmVarInfo.Description = "roughness length governing momentum transfer, FAO";
            zmVarInfo.MaxValue = 1;
            zmVarInfo.MinValue = 0;
            zmVarInfo.DefaultValue = 0.13;
            zmVarInfo.Units = "m";
            zmVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            dVarInfo.Name = "d";
            dVarInfo.Description = "corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO";
            dVarInfo.MaxValue = 1;
            dVarInfo.MinValue = 0;
            dVarInfo.DefaultValue = 0.67;
            dVarInfo.Units = "dimensionless";
            dVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            zhVarInfo.Name = "zh";
            zhVarInfo.Description = "roughness length governing transfer of heat and vapour, FAO";
            zhVarInfo.MaxValue = 1;
            zhVarInfo.MinValue = 0;
            zhVarInfo.DefaultValue = 0.013;
            zhVarInfo.Units = "m";
            zhVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            soilDiffusionConstantVarInfo.Name = "soilDiffusionConstant";
            soilDiffusionConstantVarInfo.Description = "soil Diffusion Constant";
            soilDiffusionConstantVarInfo.MaxValue = 10;
            soilDiffusionConstantVarInfo.MinValue = 0;
            soilDiffusionConstantVarInfo.DefaultValue = 4.2;
            soilDiffusionConstantVarInfo.Units = "";
            soilDiffusionConstantVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            rhoDensityAirVarInfo.Name = "rhoDensityAir";
            rhoDensityAirVarInfo.Description = "Density of air";
            rhoDensityAirVarInfo.MaxValue = 1.225;
            rhoDensityAirVarInfo.MinValue = 1.225;
            rhoDensityAirVarInfo.DefaultValue = 1.225;
            rhoDensityAirVarInfo.Units = "";
            rhoDensityAirVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            specificHeatCapacityAirVarInfo.Name = "specificHeatCapacityAir";
            specificHeatCapacityAirVarInfo.Description = "Specific heat capacity of dry air";
            specificHeatCapacityAirVarInfo.MaxValue = 1;
            specificHeatCapacityAirVarInfo.MinValue = 0;
            specificHeatCapacityAirVarInfo.DefaultValue = 0.00101;
            specificHeatCapacityAirVarInfo.Units = "";
            specificHeatCapacityAirVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            tauVarInfo.Name = "tau";
            tauVarInfo.Description = "plant cover factor";
            tauVarInfo.MaxValue = 100;
            tauVarInfo.MinValue = 0;
            tauVarInfo.DefaultValue = 0.9983;
            tauVarInfo.Units = "";
            tauVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            tauAlphaVarInfo.Name = "tauAlpha";
            tauAlphaVarInfo.Description = "Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1";
            tauAlphaVarInfo.MaxValue = 1;
            tauAlphaVarInfo.MinValue = 0;
            tauAlphaVarInfo.DefaultValue = 0.3;
            tauAlphaVarInfo.Units = "";
            tauAlphaVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            isWindVpDefinedVarInfo.Name = "isWindVpDefined";
            isWindVpDefinedVarInfo.Description = "if wind and vapour pressure are defined";
            isWindVpDefinedVarInfo.MaxValue = 1;
            isWindVpDefinedVarInfo.MinValue = 0;
            isWindVpDefinedVarInfo.DefaultValue = 1;
            isWindVpDefinedVarInfo.Units = "";
            isWindVpDefinedVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
        }

        public static VarInfo albedoCoefficientVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.NetRadiation.albedoCoefficientVarInfo;} 
        }

        public static VarInfo stefanBoltzmanVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.NetRadiation.stefanBoltzmanVarInfo;} 
        }

        public static VarInfo elevationVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.NetRadiation.elevationVarInfo;} 
        }

        public static VarInfo lambdaVVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.NetRadiationEquivalentEvaporation.lambdaVVarInfo;} 
        }

        public static VarInfo psychrometricConstantVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.PriestlyTaylor.psychrometricConstantVarInfo;} 
        }

        public static VarInfo AlphaVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.PriestlyTaylor.AlphaVarInfo;} 
        }

        public static VarInfo vonKarmanVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Conductance.vonKarmanVarInfo;} 
        }

        public static VarInfo heightWeatherMeasurementsVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Conductance.heightWeatherMeasurementsVarInfo;} 
        }

        public static VarInfo zmVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Conductance.zmVarInfo;} 
        }

        public static VarInfo dVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Conductance.dVarInfo;} 
        }

        public static VarInfo zhVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Conductance.zhVarInfo;} 
        }

        public static VarInfo soilDiffusionConstantVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.DiffusionLimitedEvaporation.soilDiffusionConstantVarInfo;} 
        }

        public static VarInfo rhoDensityAirVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Penman.rhoDensityAirVarInfo;} 
        }

        public static VarInfo specificHeatCapacityAirVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.Penman.specificHeatCapacityAirVarInfo;} 
        }

        public static VarInfo tauVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.PtSoil.tauVarInfo;} 
        }

        public static VarInfo tauAlphaVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.PtSoil.tauAlphaVarInfo;} 
        }

        public static VarInfo isWindVpDefinedVarInfo
        {
            get { return SiriusQualityEnergyBalance.Strategies.EvapoTranspiration.isWindVpDefinedVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiation.CurrentValue=a.netRadiation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation.CurrentValue=a.netOutGoingLongWaveRadiation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation.CurrentValue=a.netRadiationEquivalentEvaporation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor.CurrentValue=r.evapoTranspirationPriestlyTaylor;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.diffusionLimitedEvaporation.CurrentValue=s.diffusionLimitedEvaporation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.energyLimitedEvaporation.CurrentValue=a.energyLimitedEvaporation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance.CurrentValue=s.conductance;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman.CurrentValue=r.evapoTranspirationPenman;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.soilEvaporation.CurrentValue=a.soilEvaporation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration.CurrentValue=r.evapoTranspiration;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.potentialTranspiration.CurrentValue=r.potentialTranspiration;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.soilHeatFlux.CurrentValue=r.soilHeatFlux;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux.CurrentValue=r.cropHeatFlux;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature.CurrentValue=s.minCanopyTemperature;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature.CurrentValue=s.maxCanopyTemperature;

                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 

                RangeBasedCondition r28 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiation);
                if(r28.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiation.ValueType)){prc.AddCondition(r28);}
                RangeBasedCondition r29 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation);
                if(r29.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netOutGoingLongWaveRadiation.ValueType)){prc.AddCondition(r29);}
                RangeBasedCondition r30 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation);
                if(r30.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.netRadiationEquivalentEvaporation.ValueType)){prc.AddCondition(r30);}
                RangeBasedCondition r31 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor);
                if(r31.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPriestlyTaylor.ValueType)){prc.AddCondition(r31);}
                RangeBasedCondition r32 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.diffusionLimitedEvaporation);
                if(r32.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.diffusionLimitedEvaporation.ValueType)){prc.AddCondition(r32);}
                RangeBasedCondition r33 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.energyLimitedEvaporation);
                if(r33.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.energyLimitedEvaporation.ValueType)){prc.AddCondition(r33);}
                RangeBasedCondition r34 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance);
                if(r34.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.conductance.ValueType)){prc.AddCondition(r34);}
                RangeBasedCondition r35 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman);
                if(r35.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspirationPenman.ValueType)){prc.AddCondition(r35);}
                RangeBasedCondition r36 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.soilEvaporation);
                if(r36.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.soilEvaporation.ValueType)){prc.AddCondition(r36);}
                RangeBasedCondition r37 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration);
                if(r37.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.evapoTranspiration.ValueType)){prc.AddCondition(r37);}
                RangeBasedCondition r38 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.potentialTranspiration);
                if(r38.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.potentialTranspiration.ValueType)){prc.AddCondition(r38);}
                RangeBasedCondition r39 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.soilHeatFlux);
                if(r39.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.soilHeatFlux.ValueType)){prc.AddCondition(r39);}
                RangeBasedCondition r40 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux);
                if(r40.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRateVarInfo.cropHeatFlux.ValueType)){prc.AddCondition(r40);}
                RangeBasedCondition r41 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature);
                if(r41.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.minCanopyTemperature.ValueType)){prc.AddCondition(r41);}
                RangeBasedCondition r42 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature);
                if(r42.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceStateVarInfo.maxCanopyTemperature.ValueType)){prc.AddCondition(r42);}

                string ret = "";
                ret += _NetRadiation.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _NetRadiationEquivalentEvaporation.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _PriestlyTaylor.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _Conductance.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _DiffusionLimitedEvaporation.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _Penman.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _PtSoil.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _SoilEvaporation.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _EvapoTranspiration.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _SoilHeatFlux.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _PotentialTranspiration.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _CropHeatFlux.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _CanopyTemperature.TestPostConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                if (ret != "") { pre.TestsOut(ret, true, "   postconditions tests of associated classes"); }

                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.EnergyBalance, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair.CurrentValue=a.minTair;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair.CurrentValue=a.maxTair;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.solarRadiation.CurrentValue=a.solarRadiation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.vaporPressure.CurrentValue=a.vaporPressure;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.extraSolarRadiation.CurrentValue=a.extraSolarRadiation;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.hslope.CurrentValue=a.hslope;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.plantHeight.CurrentValue=a.plantHeight;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.wind.CurrentValue=a.wind;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.deficitOnTopLayers.CurrentValue=a.deficitOnTopLayers;
                SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.VPDair.CurrentValue=a.VPDair;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.minTair.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.maxTair.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.solarRadiation);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.solarRadiation.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.vaporPressure);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.vaporPressure.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.extraSolarRadiation);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.extraSolarRadiation.ValueType)){prc.AddCondition(r5);}
                RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.hslope);
                if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.hslope.ValueType)){prc.AddCondition(r6);}
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.plantHeight);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.plantHeight.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.wind);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.wind.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.deficitOnTopLayers);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.deficitOnTopLayers.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.VPDair);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliaryVarInfo.VPDair.ValueType)){prc.AddCondition(r10);}

                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("albedoCoefficient")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("stefanBoltzman")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("elevation")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lambdaV")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("psychrometricConstant")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("Alpha")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("vonKarman")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("heightWeatherMeasurements")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("zm")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("d")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("zh")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("soilDiffusionConstant")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("rhoDensityAir")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("specificHeatCapacityAir")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("tau")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("tauAlpha")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("isWindVpDefined")));
                string ret = "";
                ret += _NetRadiation.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _NetRadiationEquivalentEvaporation.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _PriestlyTaylor.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _Conductance.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _DiffusionLimitedEvaporation.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _Penman.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _PtSoil.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _SoilEvaporation.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _EvapoTranspiration.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _SoilHeatFlux.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _PotentialTranspiration.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _CropHeatFlux.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                ret += _CanopyTemperature.TestPreConditions(s, s1, r, a, ex, " strategy SiriusQualityEnergyBalance.Strategies.EnergyBalance");
                if (ret != "") { pre.TestsOut(ret, true, "   preconditions tests of associated classes"); }

                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "Component SiriusQuality.EnergyBalance, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityEnergyBalance, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void CalculateModel(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex)
        {
            EstimateOfAssociatedClasses(s, s1, r, a, ex);
        }

        //Declaration of the associated strategies
        NetRadiation _NetRadiation = new NetRadiation();
        NetRadiationEquivalentEvaporation _NetRadiationEquivalentEvaporation = new NetRadiationEquivalentEvaporation();
        PriestlyTaylor _PriestlyTaylor = new PriestlyTaylor();
        Conductance _Conductance = new Conductance();
        DiffusionLimitedEvaporation _DiffusionLimitedEvaporation = new DiffusionLimitedEvaporation();
        Penman _Penman = new Penman();
        PtSoil _PtSoil = new PtSoil();
        SoilEvaporation _SoilEvaporation = new SoilEvaporation();
        EvapoTranspiration _EvapoTranspiration = new EvapoTranspiration();
        SoilHeatFlux _SoilHeatFlux = new SoilHeatFlux();
        PotentialTranspiration _PotentialTranspiration = new PotentialTranspiration();
        CropHeatFlux _CropHeatFlux = new CropHeatFlux();
        CanopyTemperature _CanopyTemperature = new CanopyTemperature();

        private void EstimateOfAssociatedClasses(SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceState s1,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceRate r,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceAuxiliary a,SiriusQualityEnergyBalance.DomainClass.EnergyBalanceExogenous ex)
        {
            _netradiation.Estimate(s,s1, r, a, ex);
            _conductance.Estimate(s,s1, r, a, ex);
            _diffusionlimitedevaporation.Estimate(s,s1, r, a, ex);
            _netradiationequivalentevaporation.Estimate(s,s1, r, a, ex);
            _priestlytaylor.Estimate(s,s1, r, a, ex);
            _ptsoil.Estimate(s,s1, r, a, ex);
            _penman.Estimate(s,s1, r, a, ex);
            _soilevaporation.Estimate(s,s1, r, a, ex);
            _evapotranspiration.Estimate(s,s1, r, a, ex);
            _soilheatflux.Estimate(s,s1, r, a, ex);
            _potentialtranspiration.Estimate(s,s1, r, a, ex);
            _cropheatflux.Estimate(s,s1, r, a, ex);
            _canopytemperature.Estimate(s,s1, r, a, ex);
        }

        public EnergyBalanceComponent(EnergyBalanceComponent toCopy): this() // copy constructor 
        {
                albedoCoefficient = toCopy.albedoCoefficient;
                stefanBoltzman = toCopy.stefanBoltzman;
                elevation = toCopy.elevation;
                lambdaV = toCopy.lambdaV;
                psychrometricConstant = toCopy.psychrometricConstant;
                Alpha = toCopy.Alpha;
                vonKarman = toCopy.vonKarman;
                heightWeatherMeasurements = toCopy.heightWeatherMeasurements;
                zm = toCopy.zm;
                d = toCopy.d;
                zh = toCopy.zh;
                soilDiffusionConstant = toCopy.soilDiffusionConstant;
                rhoDensityAir = toCopy.rhoDensityAir;
                specificHeatCapacityAir = toCopy.specificHeatCapacityAir;
                tau = toCopy.tau;
                tauAlpha = toCopy.tauAlpha;
                isWindVpDefined = toCopy.isWindVpDefined;
        }
    }
}