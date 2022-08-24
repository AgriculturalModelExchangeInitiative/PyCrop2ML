using System;
using System.Collections.Generic;
using System.Linq;
using SQCrop2ML_SoilTemp.DomainClass;
using SQCrop2ML_SoilTemp.Strategies;

namespace SiriusModel.Model.SoilTemp
{
    class SoilTempWrapper :  UniverseLink
    {
        private SoilTempState s;
        private SoilTempRate r;
        private SoilTempAuxiliary a;
        private SoilTempExogenous ex;
        private SoilTempComponent soiltempComponent;

        public SoilTempWrapper(Universe universe) : base(universe)
        {
            s = new SoilTempState();
            r = new SoilTempRate();
            a = new SoilTempAuxiliary();
            ex = new SoilTempExogenous();
            soiltempComponent = new SoilTemp();
            loadParameters();
        }

        public double SRFTEMP{ get { return s.SRFTEMP;}} 
     
        public double[] TMA{ get { return s.TMA;}} 
     
        public double TDL{ get { return s.TDL;}} 
     
        public double[] ST{ get { return s.ST;}} 
     
        public int NDays{ get { return s.NDays;}} 
     
        public int[] WetDay{ get { return s.WetDay;}} 
     

        public SoilTempWrapper(Universe universe, SoilTempWrapper toCopy, bool copyAll) : base(universe)
        {
            s = (toCopy.s != null) ? new SoilTempState(toCopy.s, copyAll) : null;
            r = (toCopy.r != null) ? new SoilTempRate(toCopy.r, copyAll) : null;
            a = (toCopy.a != null) ? new SoilTempAuxiliary(toCopy.a, copyAll) : null;
            ex = (toCopy.ex != null) ? new SoilTempExogenous(toCopy.ex, copyAll) : null;
            if (copyAll)
            {
                soiltempComponent = (toCopy.soiltempComponent != null) ? new SoilTemp(toCopy.soiltempComponent) : null;
            }
        }

        public void Init(){
            soiltempComponent.Init(s, r, a);
            loadParameters();
        }

        private void loadParameters()
        {
            soiltempComponent.BD = BD;
            soiltempComponent.NL = NL;
            soiltempComponent.NLAYR = NLAYR;
            soiltempComponent.SW = SW;
            soiltempComponent.DS = DS;
            soiltempComponent.DLAYR = DLAYR;
            soiltempComponent.ISWWAT = ISWWAT;
            soiltempComponent.DUL = DUL;
            soiltempComponent.LL = LL;
        }

        public void EstimateSoilTemp(double DEPIR, double BIOMAS, double TAMP, double MULCHMASS, double TMAX, double SNOW, double RAIN, double TAV, double TAVG, double TMIN)
        {
            a.DEPIR = DEPIR;
            a.BIOMAS = BIOMAS;
            a.TAMP = TAMP;
            a.MULCHMASS = MULCHMASS;
            a.TMAX = TMAX;
            a.SNOW = SNOW;
            a.RAIN = RAIN;
            a.TAV = TAV;
            a.TAVG = TAVG;
            a.TMIN = TMIN;
            soiltempComponent.CalculateModel(s,s1, r, a, ex);
        }

    }

}