
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SoilTemperature.DomainClass
{
    public class SoilTemperatureState : ICloneable, IDomainClass
    {
        private double _SoilSurfaceTemperature;
        private double _SnowWaterContent;
        private ParametersIO _parametersIO;

        public SoilTemperatureState()
        {
            _parametersIO = new ParametersIO(this);
        }

        public SoilTemperatureState(SoilTemperatureState toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                _SoilSurfaceTemperature = toCopy._SoilSurfaceTemperature;
                _SnowWaterContent = toCopy._SnowWaterContent;
            }
        }

        public double SoilSurfaceTemperature
        {
            get { return this._SoilSurfaceTemperature; }
            set { this._SoilSurfaceTemperature= value; } 
        }
        public double SnowWaterContent
        {
            get { return this._SnowWaterContent; }
            set { this._SnowWaterContent= value; } 
        }

        public string Description
        {
            get { return "SoilTemperatureState of the component";}
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
             _SoilSurfaceTemperature = default(double);
             _SnowWaterContent = default(double);
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