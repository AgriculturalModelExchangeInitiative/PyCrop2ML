
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemperatureComp.DomainClass
{
    public class SoilTemperatureCompExogenous : ICloneable, IDomainClass
    {
        private double _tmin;
        private double _tmax;
        private double _globrad;
        private double _soilCoverage;
        private double _soilSurfaceTemperatureBelowSnow;
        private bool _hasSnowCover;
        private ParametersIO _parametersIO;

        public SoilTemperatureCompExogenous()
        {
            _parametersIO = new ParametersIO(this);
        }

        public SoilTemperatureCompExogenous(SoilTemperatureCompExogenous toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                tmin = toCopy.tmin;
                tmax = toCopy.tmax;
                globrad = toCopy.globrad;
                soilCoverage = toCopy.soilCoverage;
                soilSurfaceTemperatureBelowSnow = toCopy.soilSurfaceTemperatureBelowSnow;
                hasSnowCover = toCopy.hasSnowCover;
            }
        }

        public double tmin
        {
            get { return this._tmin; }
            set { this._tmin= value; } 
        }
        public double tmax
        {
            get { return this._tmax; }
            set { this._tmax= value; } 
        }
        public double globrad
        {
            get { return this._globrad; }
            set { this._globrad= value; } 
        }
        public double soilCoverage
        {
            get { return this._soilCoverage; }
            set { this._soilCoverage= value; } 
        }
        public double soilSurfaceTemperatureBelowSnow
        {
            get { return this._soilSurfaceTemperatureBelowSnow; }
            set { this._soilSurfaceTemperatureBelowSnow= value; } 
        }
        public bool hasSnowCover
        {
            get { return this._hasSnowCover; }
            set { this._hasSnowCover= value; } 
        }

        public string Description
        {
            get { return "SoilTemperatureCompExogenous of the component";}
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
             _tmin = default(double);
             _tmax = default(double);
             _globrad = default(double);
             _soilCoverage = default(double);
             _soilSurfaceTemperatureBelowSnow = default(double);
             _hasSnowCover = default(bool);
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