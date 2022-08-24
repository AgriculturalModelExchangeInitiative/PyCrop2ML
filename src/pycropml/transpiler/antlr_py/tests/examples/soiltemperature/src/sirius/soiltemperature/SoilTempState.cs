
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualitySoilTemp.DomainClass
{
    public class SoilTempState : ICloneable, IDomainClass
    {
        private double _SRFTEMP;
        private double[] _TMA = new double[5];
        private double _TDL;
        private double[] _ST = new double[NL];
        private double _CUMDPT;
        private int _NDays;
        private int[] _WetDay = new int[NL];
        private double[] _DSMID = new double[NL];
        private ParametersIO _parametersIO;

        public SoilTempState()
        {
            _parametersIO = new ParametersIO(this);
        }

        public SoilTempState(SoilTempState toCopy, bool copyAll) // copy constructor 
        {
            if (copyAll)
            {
                _SRFTEMP = toCopy._SRFTEMP;
                TMA = new double[5];
            for (int i = 0; i < 5; i++)
            { _TMA[i] = toCopy._TMA[i]; }
    
                _TDL = toCopy._TDL;
                ST = new double[NL];
            for (int i = 0; i < NL; i++)
            { _ST[i] = toCopy._ST[i]; }
    
                _CUMDPT = toCopy._CUMDPT;
                _NDays = toCopy._NDays;
                WetDay = new int[NL];
            for (int i = 0; i < NL; i++)
            { _WetDay[i] = toCopy._WetDay[i]; }
    
                DSMID = new double[NL];
            for (int i = 0; i < NL; i++)
            { _DSMID[i] = toCopy._DSMID[i]; }
    
            }
        }

        public double SRFTEMP
        {
            get { return this._SRFTEMP; }
            set { this._SRFTEMP= value; } 
        }
        public double[] TMA
        {
            get { return this._TMA; }
            set { this._TMA= value; } 
        }
        public double TDL
        {
            get { return this._TDL; }
            set { this._TDL= value; } 
        }
        public double[] ST
        {
            get { return this._ST; }
            set { this._ST= value; } 
        }
        public double CUMDPT
        {
            get { return this._CUMDPT; }
            set { this._CUMDPT= value; } 
        }
        public int NDays
        {
            get { return this._NDays; }
            set { this._NDays= value; } 
        }
        public int[] WetDay
        {
            get { return this._WetDay; }
            set { this._WetDay= value; } 
        }
        public double[] DSMID
        {
            get { return this._DSMID; }
            set { this._DSMID= value; } 
        }

        public string Description
        {
            get { return "SoilTempState of the component";}
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
             _SRFTEMP = default(double);
             _TMA = new double[5];
             _TDL = default(double);
             _ST = new double[NL];
             _CUMDPT = default(double);
             _NDays = default(int);
             _WetDay = new int[NL];
             _DSMID = new double[NL];
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