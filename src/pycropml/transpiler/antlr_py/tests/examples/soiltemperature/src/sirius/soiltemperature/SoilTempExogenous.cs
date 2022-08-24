
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemp.DomainClass
{
    public class SoilTempExogenous : ICloneable, IDomainClass
    {
        private double _DEPIR;
        private double _BIOMAS;
        private double _TAMP;
        private double _MULCHMASS;
        private double _TMAX;
        private double _SNOW;
        private double _RAIN;
        private double _TAV;
        private double _TAVG;
        private double _TMIN;
        private ParametersIO _parametersIO;

        public SoilTempExogenous()
        {
            _parametersIO = new ParametersIO(this);
        }

        public SoilTempExogenous(SoilTempExogenous toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                _DEPIR = toCopy._DEPIR;
                _BIOMAS = toCopy._BIOMAS;
                _TAMP = toCopy._TAMP;
                _MULCHMASS = toCopy._MULCHMASS;
                _TMAX = toCopy._TMAX;
                _SNOW = toCopy._SNOW;
                _RAIN = toCopy._RAIN;
                _TAV = toCopy._TAV;
                _TAVG = toCopy._TAVG;
                _TMIN = toCopy._TMIN;
            }
        }

        public double DEPIR
        {
            get { return this._DEPIR; }
            set { this._DEPIR= value; } 
        }
        public double BIOMAS
        {
            get { return this._BIOMAS; }
            set { this._BIOMAS= value; } 
        }
        public double TAMP
        {
            get { return this._TAMP; }
            set { this._TAMP= value; } 
        }
        public double MULCHMASS
        {
            get { return this._MULCHMASS; }
            set { this._MULCHMASS= value; } 
        }
        public double TMAX
        {
            get { return this._TMAX; }
            set { this._TMAX= value; } 
        }
        public double SNOW
        {
            get { return this._SNOW; }
            set { this._SNOW= value; } 
        }
        public double RAIN
        {
            get { return this._RAIN; }
            set { this._RAIN= value; } 
        }
        public double TAV
        {
            get { return this._TAV; }
            set { this._TAV= value; } 
        }
        public double TAVG
        {
            get { return this._TAVG; }
            set { this._TAVG= value; } 
        }
        public double TMIN
        {
            get { return this._TMIN; }
            set { this._TMIN= value; } 
        }

        public string Description
        {
            get { return "SoilTempExogenous of the component";}
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
             _DEPIR = default(double);
             _BIOMAS = default(double);
             _TAMP = default(double);
             _MULCHMASS = default(double);
             _TMAX = default(double);
             _SNOW = default(double);
             _RAIN = default(double);
             _TAV = default(double);
             _TAVG = default(double);
             _TMIN = default(double);
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