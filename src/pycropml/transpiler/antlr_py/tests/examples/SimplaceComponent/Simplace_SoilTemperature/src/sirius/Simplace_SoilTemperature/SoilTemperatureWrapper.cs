using System;
using System.Collections.Generic;
using System.Linq;
using SQCrop2ML_SoilTemperature.DomainClass;
using SQCrop2ML_SoilTemperature.Strategies;

namespace SiriusModel.Model.SoilTemperature
{
    class SoilTemperatureWrapper :  UniverseLink
    {
        private SoilTemperatureState s;
        private SoilTemperatureRate r;
        private SoilTemperatureAuxiliary a;
        private SoilTemperatureExogenous ex;
        private SoilTemperatureComponent soiltemperatureComponent;

        public SoilTemperatureWrapper(Universe universe) : base(universe)
        {
            s = new SoilTemperatureState();
            r = new SoilTemperatureRate();
            a = new SoilTemperatureAuxiliary();
            ex = new SoilTemperatureExogenous();
            soiltemperatureComponent = new SoilTemperature();
            loadParameters();
        }

        public double SnowWaterContent{ get { return s.SnowWaterContent;}} 
     
        public double SoilSurfaceTemperature{ get { return s.SoilSurfaceTemperature;}} 
     
        public int AgeOfSnow{ get { return s.AgeOfSnow;}} 
     
        public double[] SoilTempArray{ get { return s.SoilTempArray;}} 
     
        public double SnowIsolationIndex{ get { return a.SnowIsolationIndex;}} 
     

        public SoilTemperatureWrapper(Universe universe, SoilTemperatureWrapper toCopy, bool copyAll) : base(universe)
        {
            s = (toCopy.s != null) ? new SoilTemperatureState(toCopy.s, copyAll) : null;
            r = (toCopy.r != null) ? new SoilTemperatureRate(toCopy.r, copyAll) : null;
            a = (toCopy.a != null) ? new SoilTemperatureAuxiliary(toCopy.a, copyAll) : null;
            ex = (toCopy.ex != null) ? new SoilTemperatureExogenous(toCopy.ex, copyAll) : null;
            if (copyAll)
            {
                soiltemperatureComponent = (toCopy.soiltemperatureComponent != null) ? new SoilTemperature(toCopy.soiltemperatureComponent) : null;
            }
        }

        public void Init(){
            soiltemperatureComponent.Init(s, r, a);
            loadParameters();
        }

        private void loadParameters()
        {
            soiltemperatureComponent.cCarbonContent = cCarbonContent;
            soiltemperatureComponent.cSoilLayerDepth = cSoilLayerDepth;
            soiltemperatureComponent.cFirstDayMeanTemp = cFirstDayMeanTemp;
            soiltemperatureComponent.cAverageGroundTemperature = cAverageGroundTemperature;
            soiltemperatureComponent.cAVT = cAVT;
            soiltemperatureComponent.cAverageBulkDensity = cAverageBulkDensity;
            soiltemperatureComponent.cABD = cABD;
            soiltemperatureComponent.cDampingDepth = cDampingDepth;
        }

        public void EstimateSoilTemperature(double iAirTemperatureMax, double iTempMax, double iAirTemperatureMin, double iTempMin, double iGlobalSolarRadiation, double iRadiation, double iRAIN, double iCropResidues, double iPotentialSoilEvaporation, double iLeafAreaIndex, double[] iSoilTempArray, double iSoilWaterContent, double iSoilSurfaceTemperature)
        {
            a.iAirTemperatureMax = iAirTemperatureMax;
            a.iTempMax = iTempMax;
            a.iAirTemperatureMin = iAirTemperatureMin;
            a.iTempMin = iTempMin;
            a.iGlobalSolarRadiation = iGlobalSolarRadiation;
            a.iRadiation = iRadiation;
            a.iRAIN = iRAIN;
            a.iCropResidues = iCropResidues;
            a.iPotentialSoilEvaporation = iPotentialSoilEvaporation;
            a.iLeafAreaIndex = iLeafAreaIndex;
            a.iSoilTempArray = iSoilTempArray;
            a.iSoilWaterContent = iSoilWaterContent;
            a.iSoilSurfaceTemperature = iSoilSurfaceTemperature;
            soiltemperatureComponent.CalculateModel(s,s1, r, a, ex);
        }

    }

}