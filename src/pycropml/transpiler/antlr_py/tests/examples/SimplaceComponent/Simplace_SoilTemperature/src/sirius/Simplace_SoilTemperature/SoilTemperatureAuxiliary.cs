
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperature.DomainClass
{
    public class SoilTemperatureAuxiliary : ICloneable, IDomainClass
    {
        private double _SnowIsolationIndex;
        private ParametersIO _parametersIO;

        public SoilTemperatureAuxiliary()
        {
            _parametersIO = new ParametersIO(this);
        }

        public SoilTemperatureAuxiliary(SoilTemperatureAuxiliary toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                _SnowIsolationIndex = toCopy._SnowIsolationIndex;
            }
        }

        public double SnowIsolationIndex
        {
            get { return this._SnowIsolationIndex; }
            set { this._SnowIsolationIndex= value; } 
        }

        public string Description
        {
            get { return "SoilTemperatureAuxiliary of the component";}
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
             _SnowIsolationIndex = default(double);
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