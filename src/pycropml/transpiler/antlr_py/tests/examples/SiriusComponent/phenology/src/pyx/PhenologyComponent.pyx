from datetime import datetime
from math import *
from phenology.Gaimean import model_gaimean
from phenology.Ptq import model_ptq
from phenology.Cumulttfrom import model_cumulttfrom
from phenology.Ismomentregistredzc_39 import model_ismomentregistredzc_39
from phenology.Vernalizationprogress import model_vernalizationprogress
from phenology.Phylsowingdatecorrection import model_phylsowingdatecorrection
from phenology.Updatephase import model_updatephase
from phenology.Leafnumber import model_leafnumber
from phenology.Shootnumber import model_shootnumber
from phenology.Updateleafflag import model_updateleafflag
from phenology.Registerzadok import model_registerzadok
from phenology.Updatecalendar import model_updatecalendar
from phenology.Phyllochron import model_phyllochron
def model_phenology(float pastMaxAI_t1,
      float tTWindowForPTQ,
      float gAI,
      floatlist listGAITTWindowForPTQ_t1,
      float deltaTT,
      floatlist listTTShootWindowForPTQ1_t1,
      float pAR,
      float kl,
      floatlist listTTShootWindowForPTQ_t1,
      floatlist listPARTTWindowForPTQ_t1,
      stringlist calendarMoments_t1,
      floatlist calendarCumuls_t1,
      float cumulTT,
      float pNini,
      float aMXLFNO,
      float maxTvern,
      float vBEE,
      datetime currentdate,
      float leafNumber_t1,
      float minFinalNumber_t1,
      float minTvern,
      float dayLength,
      float vAI,
      float intTvern,
      int isVernalizable,
      datelist calendarDates_t1,
      float minDL,
      float vernaprog_t1,
      float maxDL,
      float p,
      float latitude,
      float sDsa_nh,
      int sDws,
      int sowingDay,
      float sDsa_sh,
      float rp,
      float finalLeafNumber_t1,
      float dse,
      float dcd,
      float dgf,
      float pHEADANTH,
      float pFLLAnth,
      str choosePhyllUse,
      int hasLastPrimordiumAppeared_t1,
      float phase_t1,
      int ignoreGrainMaturation,
      float sLDL,
      float degfm,
      float grainCumulTT,
      float phyllochron_t1,
      float canopyShootNumber_t1,
      floatlist tilleringProfile_t1,
      intlist leafTillerNumberArray_t1,
      float targetFertileShoot,
      int numberTillerCohort_t1,
      float sowingDensity,
      int hasFlagLeafLiguleAppeared_t1,
      str currentZadokStage_t1,
      float intTSFLN,
      int hasZadokStageChanged_t1,
      float der,
      float slopeTSFLN,
      float pdecr,
      float B,
      float areaSL,
      float lARmin,
      float lincr,
      float pincr,
      float areaSS,
      float lNeff,
      float ldecr,
      float pTQhf,
      float lARmax):
    cdef float gAImean
    cdef float pastMaxAI
    cdef floatlist listTTShootWindowForPTQ1
    cdef floatlist listGAITTWindowForPTQ
    cdef floatlist listPARTTWindowForPTQ
    cdef floatlist listTTShootWindowForPTQ
    cdef float ptq
    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_39
    cdef float cumulTTFromZC_91
    cdef int isMomentRegistredZC_39
    cdef float vernaprog
    cdef float minFinalNumber
    cdef stringlist calendarMoments
    cdef datelist calendarDates
    cdef floatlist calendarCumuls
    cdef float fixPhyll
    cdef float phyllochron
    cdef float finalLeafNumber
    cdef float phase
    cdef int hasLastPrimordiumAppeared
    cdef int hasFlagLeafLiguleAppeared
    cdef float leafNumber
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef intlist leafTillerNumberArray
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
    cdef int hasZadokStageChanged
    cdef str currentZadokStage
    gAImean, pastMaxAI, listTTShootWindowForPTQ1, listGAITTWindowForPTQ = model_gaimean( listTTShootWindowForPTQ1_t1,pastMaxAI_t1,listGAITTWindowForPTQ_t1,gAI,deltaTT,tTWindowForPTQ)
    cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91 = model_cumulttfrom( calendarMoments_t1,calendarCumuls_t1,cumulTT)
    isMomentRegistredZC_39 = model_ismomentregistredzc_39( calendarMoments_t1)
    vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls = model_vernalizationprogress( calendarDates_t1,calendarMoments_t1,minFinalNumber_t1,calendarCumuls_t1,leafNumber_t1,vernaprog_t1,dayLength,deltaTT,cumulTT,currentdate,minTvern,intTvern,vAI,vBEE,minDL,maxDL,maxTvern,pNini,aMXLFNO,isVernalizable)
    fixPhyll = model_phylsowingdatecorrection( sowingDay,latitude,sDsa_sh,rp,sDws,sDsa_nh,p)
    listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq = model_ptq( listGAITTWindowForPTQ,listTTShootWindowForPTQ_t1,listPARTTWindowForPTQ_t1,pAR,deltaTT,tTWindowForPTQ,kl)
    finalLeafNumber, phase, hasLastPrimordiumAppeared = model_updatephase( vernaprog,phyllochron,isMomentRegistredZC_39,minFinalNumber,leafNumber_t1,finalLeafNumber_t1,hasLastPrimordiumAppeared_t1,phase_t1,cumulTT,cumulTTFromZC_39,gAI,grainCumulTT,dayLength,fixPhyll,cumulTTFromZC_91,isVernalizable,dse,pFLLAnth,dcd,dgf,degfm,maxDL,sLDL,ignoreGrainMaturation,pHEADANTH,choosePhyllUse,p)
    leafNumber = model_leafnumber( hasFlagLeafLiguleAppeared,phase,leafNumber_t1,phyllochron_t1,deltaTT)
    averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort = model_shootnumber( leafNumber,numberTillerCohort_t1,canopyShootNumber_t1,leafTillerNumberArray_t1,tilleringProfile_t1,sowingDensity,targetFertileShoot)
    calendarDates, calendarMoments, calendarCumuls, hasFlagLeafLiguleAppeared = model_updateleafflag( calendarDates,calendarMoments,phase,calendarCumuls,leafNumber,finalLeafNumber,hasFlagLeafLiguleAppeared_t1,cumulTT,currentdate)
    phyllochron = model_phyllochron( leafNumber,gAImean,ptq,fixPhyll,lincr,ldecr,pdecr,pincr,kl,pTQhf,B,p,choosePhyllUse,areaSL,areaSS,lARmin,lARmax,sowingDensity,lNeff)
    calendarDates, calendarMoments, calendarCumuls, hasZadokStageChanged, currentZadokStage = model_registerzadok( calendarDates,calendarMoments,phase,calendarCumuls,leafNumber,finalLeafNumber,currentZadokStage_t1,hasZadokStageChanged_t1,cumulTT,cumulTTFromZC_65,currentdate,der,slopeTSFLN,intTSFLN)
    calendarCumuls, calendarDates, calendarMoments = model_updatecalendar( calendarCumuls,calendarDates,calendarMoments,phase,cumulTT,currentdate)
    return gAImean, pastMaxAI, listTTShootWindowForPTQ1, listGAITTWindowForPTQ, listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq, cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91, isMomentRegistredZC_39, vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls, fixPhyll, finalLeafNumber, phase, hasLastPrimordiumAppeared, leafNumber, averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort, hasFlagLeafLiguleAppeared, hasZadokStageChanged, currentZadokStage, phyllochron