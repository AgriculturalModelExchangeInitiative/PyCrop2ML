import numpy as np 
from math import *

def vernalizationprogress_(float dayLength=12.3037621834005,
                           float deltaTT=20.3429985011972,
                           float cumulTT=112.330110409888,
                           float leafNumber=0.0,
                           list calendarMoments=['Sowing'],
                           list calendarDates=['21/3/2007'],
                           list calendarCumuls=[0.0],
                           float minTvern=0.0,
                           float intTvern=11.0,
                           float vAI=0.015,
                           float vBEE=0.01,
                           float minDL=8.0,
                           float maxDL=15.0,
                           float maxTvern=23.0,
                           float pNini=4.0,
                           float aMXLFNO=24.0,
                           float vernaprog=0.5517254187376879,
                           str currentdate='27/3/2007',
                           int isVernalizable=1,
                           float minFinalNumber=5.5):
    """


    VernalizationProgress Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: Calculate progress (VernaProg) towards vernalization, but there 
        			is no vernalization below minTvern 
        			and above maxTvern . The maximum value of VernaProg is 1.
        			Progress towards full vernalization is a linear function of shoot 
        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
        			 canopy temperature)
    	

    """
    cdef float maxVernaProg, dLverna, primordno, minLeafNumber, potlfno, tt
    if (isVernalizable==1 and vernaprog < 1.0):
        tt = deltaTT       
        if (tt >= minTvern and tt <= intTvern):
            vernaprog = vernaprog + vAI * tt + vBEE      
        if (tt > intTvern):
            maxVernaProg = vAI * intTvern + vBEE
            dLverna = max(minDL, min(maxDL, dayLength))
            vernaprog += max(0.0, maxVernaProg * (1.0 + ((intTvern - tt) / (maxTvern - intTvern)) * ((dLverna - minDL) / (maxDL - minDL))))      
        primordno = 2.0 * leafNumber + pNini     
        minLeafNumber = minFinalNumber
        if (vernaprog >= 1.0 or primordno >= aMXLFNO):      
            minFinalNumber = max(primordno, minFinalNumber)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT) 
            calendarDates.append(currentdate)        
            vernaprog = max(1.0, vernaprog)      
        else:    
            potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog
            if (primordno >= potlfno):    
                minFinalNumber = max((potlfno + primordno) / 2.0, minFinalNumber)
                vernaprog = max(1.0, vernaprog)
                calendarMoments.append("EndVernalisation")
                calendarCumuls.append(cumulTT) 
                calendarDates.append(currentdate)
    return  vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls
