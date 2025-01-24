from datetime import datetime
from math import *
from original.Gaimean import model_gaimean
from original.Ptq import model_ptq
from original.Cumulttfrom import model_cumulttfrom
from original.Ismomentregistredzc_39 import model_ismomentregistredzc_39
from original.Vernalizationprogress import model_vernalizationprogress
from original.Phylsowingdatecorrection import model_phylsowingdatecorrection
from original.Updatephase import model_updatephase
from original.Leafnumber import model_leafnumber
from original.Shootnumber import model_shootnumber
from original.Updateleafflag import model_updateleafflag
from original.Registerzadok import model_registerzadok
from original.Updatecalendar import model_updatecalendar
from original.Phyllochron import model_phyllochron
def model_phenology(float deltaTT,
      float gAI,
      float tTWindowForPTQ,
      floatlist listTTShootWindowForPTQ1_t1,
      float pastMaxAI_t1,
      floatlist listGAITTWindowForPTQ_t1,
      floatlist listPARTTWindowForPTQ_t1,
      float pAR,
      floatlist listTTShootWindowForPTQ_t1,
      float kl,
      float cumulTT,
      floatlist calendarCumuls_t1,
      stringlist calendarMoments_t1,
      float intTvern,
      float minTvern,
      float vBEE,
      datelist calendarDates_t1,
      float maxDL,
      float pNini,
      float dayLength,
      float vernaprog_t1,
      float aMXLFNO,
      float maxTvern,
      float vAI,
      float leafNumber_t1,
      int isVernalizable,
      float minDL,
      float minFinalNumber_t1,
      datetime currentdate,
      float p,
      float sDsa_nh,
      int sowingDay,
      float sDsa_sh,
      float latitude,
      float rp,
      int sDws,
      int hasLastPrimordiumAppeared_t1,
      int ignoreGrainMaturation,
      float grainCumulTT,
      float sLDL,
      float pFLLAnth,
      float finalLeafNumber_t1,
      float degfm,
      float phase_t1,
      float dgf,
      str choosePhyllUse,
      float dse,
      float pHEADANTH,
      float dcd,
      float phyllochron_t1,
      floatlist tilleringProfile_t1,
      float sowingDensity,
      intlist leafTillerNumberArray_t1,
      float targetFertileShoot,
      float canopyShootNumber_t1,
      int hasFlagLeafLiguleAppeared_t1,
      float intTSFLN,
      float der,
      float slopeTSFLN,
      str currentZadokStage_t1,
      float lNeff,
      float B,
      float lARmin,
      float lincr,
      float lARmax,
      float areaSL,
      float pdecr,
      float ldecr,
      float pTQhf,
      float pincr,
      float areaSS):
    cdef floatlist listGAITTWindowForPTQ
    cdef float pastMaxAI
    cdef floatlist listTTShootWindowForPTQ1
    cdef float gAImean
    cdef floatlist listTTShootWindowForPTQ
    cdef floatlist listPARTTWindowForPTQ
    cdef float ptq
    cdef float cumulTTFromZC_65
    cdef float cumulTTFromZC_91
    cdef float cumulTTFromZC_39
    cdef int isMomentRegistredZC_39
    cdef float minFinalNumber
    cdef floatlist calendarCumuls
    cdef float vernaprog
    cdef stringlist calendarMoments
    cdef datelist calendarDates
    cdef float fixPhyll
    cdef float phyllochron
    cdef float phase
    cdef int hasLastPrimordiumAppeared
    cdef float finalLeafNumber
    cdef int hasFlagLeafLiguleAppeared
    cdef float leafNumber
    cdef float averageShootNumberPerPlant
    cdef intlist leafTillerNumberArray
    cdef float canopyShootNumber
    cdef int numberTillerCohort
    cdef floatlist tilleringProfile
    cdef str currentZadokStage
    cdef int hasZadokStageChanged
    listGAITTWindowForPTQ, pastMaxAI, listTTShootWindowForPTQ1, gAImean = model_gaimean( deltaTT,gAI,tTWindowForPTQ,listTTShootWindowForPTQ1_t1,pastMaxAI_t1,listGAITTWindowForPTQ_t1)
    cumulTTFromZC_65, cumulTTFromZC_91, cumulTTFromZC_39 = model_cumulttfrom( cumulTT,calendarMoments_t1,calendarCumuls_t1)
    isMomentRegistredZC_39 = model_ismomentregistredzc_39( calendarMoments_t1)
    minFinalNumber, calendarCumuls, vernaprog, calendarMoments, calendarDates = model_vernalizationprogress( intTvern,minTvern,vBEE,calendarDates_t1,deltaTT,maxDL,pNini,dayLength,cumulTT,calendarMoments_t1,vernaprog_t1,aMXLFNO,maxTvern,calendarCumuls_t1,vAI,leafNumber_t1,isVernalizable,minDL,minFinalNumber_t1,currentdate)
    fixPhyll = model_phylsowingdatecorrection( p,sDsa_nh,sowingDay,sDsa_sh,latitude,rp,sDws)
    listTTShootWindowForPTQ, listPARTTWindowForPTQ, ptq = model_ptq( deltaTT,listPARTTWindowForPTQ_t1,listGAITTWindowForPTQ,pAR,listTTShootWindowForPTQ_t1,kl,tTWindowForPTQ)
    phase, hasLastPrimordiumAppeared, finalLeafNumber = model_updatephase( fixPhyll,hasLastPrimordiumAppeared_t1,minFinalNumber,ignoreGrainMaturation,cumulTTFromZC_39,phyllochron,maxDL,grainCumulTT,vernaprog,cumulTT,dayLength,isMomentRegistredZC_39,sLDL,pFLLAnth,finalLeafNumber_t1,degfm,cumulTTFromZC_91,phase_t1,p,gAI,leafNumber_t1,dgf,choosePhyllUse,isVernalizable,dse,pHEADANTH,dcd)
    leafNumber = model_leafnumber( deltaTT,phyllochron_t1,hasFlagLeafLiguleAppeared,leafNumber_t1,phase)
    averageShootNumberPerPlant, leafTillerNumberArray, canopyShootNumber, numberTillerCohort, tilleringProfile = model_shootnumber( tilleringProfile_t1,sowingDensity,leafNumber,leafTillerNumberArray_t1,targetFertileShoot,canopyShootNumber_t1)
    calendarCumuls, calendarMoments, calendarDates, hasFlagLeafLiguleAppeared = model_updateleafflag( calendarCumuls,finalLeafNumber,calendarMoments,calendarDates,cumulTT,leafNumber,hasFlagLeafLiguleAppeared_t1,phase,currentdate)
    phyllochron = model_phyllochron( fixPhyll,lNeff,lARmin,lincr,B,pdecr,areaSS,sowingDensity,lARmax,gAImean,ptq,p,leafNumber,choosePhyllUse,areaSL,ldecr,pTQhf,pincr)
    calendarCumuls, currentZadokStage, calendarMoments, calendarDates, hasZadokStageChanged = model_registerzadok( calendarCumuls,finalLeafNumber,cumulTTFromZC_65,calendarMoments,cumulTT,calendarDates,intTSFLN,der,leafNumber,slopeTSFLN,currentZadokStage_t1,phase,currentdate)
    calendarCumuls, calendarMoments, calendarDates = model_updatecalendar( calendarCumuls,calendarMoments,cumulTT,calendarDates,phase,currentdate)
    return listGAITTWindowForPTQ, pastMaxAI, listTTShootWindowForPTQ1, gAImean, listTTShootWindowForPTQ, listPARTTWindowForPTQ, ptq, cumulTTFromZC_65, cumulTTFromZC_91, cumulTTFromZC_39, isMomentRegistredZC_39, minFinalNumber, calendarCumuls, vernaprog, calendarMoments, calendarDates, fixPhyll, phase, hasLastPrimordiumAppeared, finalLeafNumber, leafNumber, averageShootNumberPerPlant, leafTillerNumberArray, canopyShootNumber, numberTillerCohort, tilleringProfile, hasFlagLeafLiguleAppeared, currentZadokStage, hasZadokStageChanged, phyllochron