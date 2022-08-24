
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SoilTemperature.DomainClass
{
    public class SoilTemperatureExogenous : ICloneable, IDomainClass
    {
        private double _iAirTemperatureMax;
        private double _iAirTemperatureMin;
        private double _iGlobalSolarRadiation;
        private double _iRAIN;
        private double _iCropResidues;
        private double _iPotentialSoilEvaporation;
        private double _iLeafAreaIndex;
        private double[] _SoilTempArray = new double[];
        private double _iSoilWaterContent;
        private double _iSoilSurfaceTemperature;
        private ParametersIO _parametersIO;

        public SoilTemperatureExogenous()
        {
            _parametersIO = new ParametersIO(this);
        }

        public SoilTemperatureExogenous(SoilTemperatureExogenous toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                _iAirTemperatureMax = toCopy._iAirTemperatureMax;
                _iAirTemperatureMin = toCopy._iAirTemperatureMin;
                _iGlobalSolarRadiation = toCopy._iGlobalSolarRadiation;
                _iRAIN = toCopy._iRAIN;
                _iCropResidues = toCopy._iCropResidues;
                _iPotentialSoilEvaporation = toCopy._iPotentialSoilEvaporation;
                _iLeafAreaIndex = toCopy._iLeafAreaIndex;
                SoilTempArray = new double[];
            for (int i = 0; i < ; i++)
            { _SoilTempArray[i] = toCopy._SoilTempArray[i]; }
    
                _iSoilWaterContent = toCopy._iSoilWaterContent;
                _iSoilSurfaceTemperature = toCopy._iSoilSurfaceTemperature;
            }
        }

        public double iAirTemperatureMax
        {
            get { return this._iAirTemperatureMax; }
            set { this._iAirTemperatureMax= value; } 
        }
        public double iAirTemperatureMin
        {
            get { return this._iAirTemperatureMin; }
            set { this._iAirTemperatureMin= value; } 
        }
        public double iGlobalSolarRadiation
        {
            get { return this._iGlobalSolarRadiation; }
            set { this._iGlobalSolarRadiation= value; } 
        }
        public double iRAIN
        {
            get { return this._iRAIN; }
            set { this._iRAIN= value; } 
        }
        public double iCropResidues
        {
            get { return this._iCropResidues; }
            set { this._iCropResidues= value; } 
        }
        public double iPotentialSoilEvaporation
        {
            get { return this._iPotentialSoilEvaporation; }
            set { this._iPotentialSoilEvaporation= value; } 
        }
        public double iLeafAreaIndex
        {
            get { return this._iLeafAreaIndex; }
            set { this._iLeafAreaIndex= value; } 
        }
        public double[] SoilTempArray
        {
            get { return this._SoilTempArray; }
            set { this._SoilTempArray= value; } 
        }
        public double iSoilWaterContent
        {
            get { return this._iSoilWaterContent; }
            set { this._iSoilWaterContent= value; } 
        }
        public double iSoilSurfaceTemperature
        {
            get { return this._iSoilSurfaceTemperature; }
            set { this._iSoilSurfaceTemperature= value; } 
        }

        public string Description
        {
            get { return "SoilTemperatureExogenous of the component";}
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
             _iAirTemperatureMax = default(double);
             _iAirTemperatureMin = default(double);
             _iGlobalSolarRadiation = default(double);
             _iRAIN = default(double);
             _iCropResidues = default(double);
             _iPotentialSoilEvaporation = default(double);
             _iLeafAreaIndex = default(double);
             _SoilTempArray = new double[];
             _iSoilWaterContent = default(double);
             _iSoilSurfaceTemperature = default(double);
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