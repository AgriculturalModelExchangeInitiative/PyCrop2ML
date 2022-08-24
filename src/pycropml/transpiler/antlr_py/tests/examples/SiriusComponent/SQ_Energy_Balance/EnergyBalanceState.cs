
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityEnergyBalance.DomainClass
{
    public class EnergyBalanceState : ICloneable, IDomainClass
    {
        private double _diffusionLimitedEvaporation;
        private double _conductance;
        private double _minCanopyTemperature;
        private double _maxCanopyTemperature;
        private ParametersIO _parametersIO;

        public EnergyBalanceState()
        {
            _parametersIO = new ParametersIO(this);
        }

        public EnergyBalanceState(EnergyBalanceState toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                _diffusionLimitedEvaporation = toCopy._diffusionLimitedEvaporation;
                _conductance = toCopy._conductance;
                _minCanopyTemperature = toCopy._minCanopyTemperature;
                _maxCanopyTemperature = toCopy._maxCanopyTemperature;
            }
        }

        public double diffusionLimitedEvaporation
        {
            get { return this._diffusionLimitedEvaporation; }
            set { this._diffusionLimitedEvaporation= value; } 
        }
        public double conductance
        {
            get { return this._conductance; }
            set { this._conductance= value; } 
        }
        public double minCanopyTemperature
        {
            get { return this._minCanopyTemperature; }
            set { this._minCanopyTemperature= value; } 
        }
        public double maxCanopyTemperature
        {
            get { return this._maxCanopyTemperature; }
            set { this._maxCanopyTemperature= value; } 
        }

        public string Description
        {
            get { return "EnergyBalanceState of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public virtual IDictionary<string, PropertyInfo> PropertiesDescription
        {
            get { return _parametersIO.GetCachedProperties(typeof(IDomainClass));}
        }

        public virtual Boolean ClearValues()
        {
             _diffusionLimitedEvaporation = default(double);
             _conductance = default(double);
             _minCanopyTemperature = default(double);
             _maxCanopyTemperature = default(double);
            return true;
        }

        public virtual Object Clone()
        {
            IDomainClass myclass = (IDomainClass) this.MemberwiseClone();
            _parametersIO.PopulateClonedCopy(myclass);
            return myclass;
        }
    }
}