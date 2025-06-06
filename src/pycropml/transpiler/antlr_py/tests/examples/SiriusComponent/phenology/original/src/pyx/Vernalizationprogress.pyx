import numpy 
from math import *
from datetime import datetime

def model_vernalizationprogress(float intTvern,
                                float minTvern,
                                float vBEE,
                                datelist calendarDates_t1,
                                float deltaTT,
                                float maxDL,
                                float pNini,
                                float dayLength,
                                float cumulTT,
                                stringlist calendarMoments_t1,
                                float vernaprog_t1,
                                float aMXLFNO,
                                float maxTvern,
                                floatlist calendarCumuls_t1,
                                float vAI,
                                float leafNumber_t1,
                                int isVernalizable,
                                float minDL,
                                float minFinalNumber_t1,
                                datetime currentdate):
    """

    VernalizationProgress model
    Author: Pierre MARTRE
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: Calculate progress (VernaProg) towards vernalization, but there         			is no vernalization below minTvern         			and above maxTvern . The maximum value of VernaProg is 1.        			Progress towards full vernalization is a linear function of shoot         			temperature (soil temperature until leaf # reach MaxLeafSoil and then        			 canopy temperature)    	
    ShortDescription: None

    """
    cdef float minFinalNumber
    cdef floatlist calendarCumuls
    cdef float vernaprog
    cdef stringlist calendarMoments
    cdef datelist calendarDates
    cdef float maxVernaProg 
    cdef float dLverna 
    cdef float primordno 
    cdef float minLeafNumber 
    cdef float potlfno 
    cdef float tt 
    calendarMoments=[]
    calendarDates=[]
    calendarCumuls=[]
    calendarMoments=copy(calendarMoments_t1)
    calendarCumuls=copy(calendarCumuls_t1)
    calendarDates=copy(calendarDates_t1)
    minFinalNumber=minFinalNumber_t1
    vernaprog=vernaprog_t1
    if isVernalizable == 1 and vernaprog_t1 < 1.0:
        tt=deltaTT
        if tt >= minTvern and tt <= intTvern:
            vernaprog=vernaprog_t1 + (vAI * tt) + vBEE
        else:
            vernaprog=vernaprog_t1
        if tt > intTvern:
            maxVernaProg=vAI * intTvern + vBEE
            dLverna=max(minDL, min(maxDL, dayLength))
            vernaprog=vernaprog + max(0.0, maxVernaProg * (1.0 + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))))
        primordno=2.0 * leafNumber_t1 + pNini
        minLeafNumber=minFinalNumber_t1
        if vernaprog >= 1.0 or primordno >= aMXLFNO:
            minFinalNumber=max(primordno, minFinalNumber_t1)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT)
            calendarDates.append(currentdate)
            vernaprog=max(1.0, vernaprog)
        else:
            potlfno=aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog)
            if primordno >= potlfno:
                minFinalNumber=max((potlfno + primordno) / 2.0, minFinalNumber_t1)
                vernaprog=max(1.0, vernaprog)
                calendarMoments.append("EndVernalisation")
                calendarCumuls.append(cumulTT)
                calendarDates.append(currentdate)
    return  minFinalNumber, calendarCumuls, vernaprog, calendarMoments, calendarDates


