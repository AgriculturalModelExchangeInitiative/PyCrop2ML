using System;
using System.Collections.Generic;
using System.Linq;
using SQCrop2ML_Phenology.DomainClass;
using SQCrop2ML_Phenology.Strategies;

namespace SiriusModel.Model.Phenology
{
    class PhenologyWrapper :  UniverseLink
    {
        private PhenologyState s;
        private PhenologyRate r;
        private PhenologyAuxiliary a;
        private PhenologyExogenous ex;
        private PhenologyComponent phenologyComponent;

        public PhenologyWrapper(Universe universe) : base(universe)
        {
            s = new PhenologyState();
            r = new PhenologyRate();
            a = new PhenologyAuxiliary();
            ex = new PhenologyExogenous();
            phenologyComponent = new Phenology();
            loadParameters();
        }

        public List<double> listTTShootWindowForPTQ1{ get { return s.listTTShootWindowForPTQ1;}} 
     
        public double pastMaxAI{ get { return s.pastMaxAI;}} 
     
        public List<double> listGAITTWindowForPTQ{ get { return s.listGAITTWindowForPTQ;}} 
     
        public List<double> listPARTTWindowForPTQ{ get { return s.listPARTTWindowForPTQ;}} 
     
        public List<double> listTTShootWindowForPTQ{ get { return s.listTTShootWindowForPTQ;}} 
     
        public List<double> calendarCumuls{ get { return s.calendarCumuls;}} 
     
        public List<string> calendarMoments{ get { return s.calendarMoments;}} 
     
        public List<DateTime> calendarDates{ get { return s.calendarDates;}} 
     
        public double vernaprog{ get { return s.vernaprog;}} 
     
        public double leafNumber{ get { return s.leafNumber;}} 
     
        public double minFinalNumber{ get { return s.minFinalNumber;}} 
     
        public int hasLastPrimordiumAppeared{ get { return s.hasLastPrimordiumAppeared;}} 
     
        public double finalLeafNumber{ get { return s.finalLeafNumber;}} 
     
        public double phase{ get { return s.phase;}} 
     
        public double phyllochron{ get { return s.phyllochron;}} 
     
        public List<double> tilleringProfile{ get { return s.tilleringProfile;}} 
     
        public List<int> leafTillerNumberArray{ get { return s.leafTillerNumberArray;}} 
     
        public double canopyShootNumber{ get { return s.canopyShootNumber;}} 
     
        public int hasFlagLeafLiguleAppeared{ get { return s.hasFlagLeafLiguleAppeared;}} 
     
        public string currentZadokStage{ get { return s.currentZadokStage;}} 
     
        public double gAImean{ get { return s.gAImean;}} 
     
        public double ptq{ get { return s.ptq;}} 
     
        public int isMomentRegistredZC_39{ get { return s.isMomentRegistredZC_39;}} 
     
        public double averageShootNumberPerPlant{ get { return s.averageShootNumberPerPlant;}} 
     
        public int numberTillerCohort{ get { return s.numberTillerCohort;}} 
     
        public int hasZadokStageChanged{ get { return s.hasZadokStageChanged;}} 
     
        public double cumulTTFromZC_65{ get { return a.cumulTTFromZC_65;}} 
     
        public double cumulTTFromZC_91{ get { return a.cumulTTFromZC_91;}} 
     
        public double cumulTTFromZC_39{ get { return a.cumulTTFromZC_39;}} 
     
        public double fixPhyll{ get { return a.fixPhyll;}} 
     

        public PhenologyWrapper(Universe universe, PhenologyWrapper toCopy, bool copyAll) : base(universe)
        {
            s = (toCopy.s != null) ? new PhenologyState(toCopy.s, copyAll) : null;
            r = (toCopy.r != null) ? new PhenologyRate(toCopy.r, copyAll) : null;
            a = (toCopy.a != null) ? new PhenologyAuxiliary(toCopy.a, copyAll) : null;
            ex = (toCopy.ex != null) ? new PhenologyExogenous(toCopy.ex, copyAll) : null;
            if (copyAll)
            {
                phenologyComponent = (toCopy.phenologyComponent != null) ? new Phenology(toCopy.phenologyComponent) : null;
            }
        }

        public void Init(){
            phenologyComponent.Init(s, r, a);
            loadParameters();
        }

        private void loadParameters()
        {
            phenologyComponent.tTWindowForPTQ = tTWindowForPTQ;
            phenologyComponent.kl = kl;
            phenologyComponent.intTvern = intTvern;
            phenologyComponent.minTvern = minTvern;
            phenologyComponent.vBEE = vBEE;
            phenologyComponent.maxDL = maxDL;
            phenologyComponent.pNini = pNini;
            phenologyComponent.aMXLFNO = aMXLFNO;
            phenologyComponent.maxTvern = maxTvern;
            phenologyComponent.vAI = vAI;
            phenologyComponent.isVernalizable = isVernalizable;
            phenologyComponent.minDL = minDL;
            phenologyComponent.p = p;
            phenologyComponent.sDsa_nh = sDsa_nh;
            phenologyComponent.sowingDay = sowingDay;
            phenologyComponent.sDsa_sh = sDsa_sh;
            phenologyComponent.latitude = latitude;
            phenologyComponent.rp = rp;
            phenologyComponent.sDws = sDws;
            phenologyComponent.ignoreGrainMaturation = ignoreGrainMaturation;
            phenologyComponent.sLDL = sLDL;
            phenologyComponent.pFLLAnth = pFLLAnth;
            phenologyComponent.degfm = degfm;
            phenologyComponent.dgf = dgf;
            phenologyComponent.choosePhyllUse = choosePhyllUse;
            phenologyComponent.dse = dse;
            phenologyComponent.pHEADANTH = pHEADANTH;
            phenologyComponent.dcd = dcd;
            phenologyComponent.sowingDensity = sowingDensity;
            phenologyComponent.targetFertileShoot = targetFertileShoot;
            phenologyComponent.intTSFLN = intTSFLN;
            phenologyComponent.der = der;
            phenologyComponent.slopeTSFLN = slopeTSFLN;
            phenologyComponent.lNeff = lNeff;
            phenologyComponent.B = B;
            phenologyComponent.lARmin = lARmin;
            phenologyComponent.lincr = lincr;
            phenologyComponent.lARmax = lARmax;
            phenologyComponent.areaSL = areaSL;
            phenologyComponent.pdecr = pdecr;
            phenologyComponent.ldecr = ldecr;
            phenologyComponent.pTQhf = pTQhf;
            phenologyComponent.pincr = pincr;
            phenologyComponent.areaSS = areaSS;
        }

        public void EstimatePhenology(double deltaTT, double gAI, double pAR, double cumulTT, double dayLength, DateTime currentdate, double grainCumulTT)
        {
            a.deltaTT = deltaTT;
            a.gAI = gAI;
            a.pAR = pAR;
            a.cumulTT = cumulTT;
            a.dayLength = dayLength;
            a.currentdate = currentdate;
            a.grainCumulTT = grainCumulTT;
            phenologyComponent.CalculateModel(s,s1, r, a, ex);
        }

    }

}