# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_vernalizationprogress(intTvern:float,
         minTvern:float,
         vBEE:float,
         calendarDates_t1:List[datetime],
         deltaTT:float,
         maxDL:float,
         pNini:float,
         dayLength:float,
         cumulTT:float,
         calendarMoments_t1:List[str],
         vernaprog_t1:float,
         aMXLFNO:float,
         maxTvern:float,
         calendarCumuls_t1:List[float],
         vAI:float,
         leafNumber_t1:float,
         isVernalizable:int,
         minDL:float,
         minFinalNumber_t1:float,
         currentdate:datetime):
    """
     - Name: VernalizationProgress -Version: 001, -Time step: 1
     - Description:
                 * Title: VernalizationProgress model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: Calculate progress (VernaProg) towards vernalization, but there         			is no vernalization below minTvern         			and above maxTvern . The maximum value of VernaProg is 1.        			Progress towards full vernalization is a linear function of shoot         			temperature (soil temperature until leaf # reach MaxLeafSoil and then        			 canopy temperature)    	
                 * ShortDescription: None
     - inputs:
                 * name: intTvern
                               ** description : Intermediate temperature for vernalization to occur
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 60
                               ** min : -20
                               ** default : 11.0
                               ** unit : Â°C
                 * name: minTvern
                               ** description : Minimum temperature for vernalization to occur
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 60
                               ** min : -20
                               ** default : 0.0
                               ** unit : Â°C
                 * name: vBEE
                               ** description : Vernalization rate at 0Â°C
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.01
                               ** unit : d-1
                 * name: calendarDates_t1
                               ** description : List containing  the dates of the wheat developmental phases
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: deltaTT
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 100.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d
                 * name: maxDL
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 0
                               ** default : 15.0
                               ** unit : h
                 * name: pNini
                               ** description : Number of primorida in the apex at emergence
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 0
                               ** default : 4.0
                               ** unit : primordia
                 * name: dayLength
                               ** description : day length
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 12.3037621834005
                               ** unit : mm2 m-2
                 * name: cumulTT
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : -200
                               ** default : 112.330110409888
                               ** unit : Â°C d
                 * name: calendarMoments_t1
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: vernaprog_t1
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.5517254187376879
                               ** unit : 
                 * name: aMXLFNO
                               ** description : Absolute maximum leaf number
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 24.0
                               ** unit : leaf
                 * name: maxTvern
                               ** description : Maximum temperature for vernalization to occur
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 60
                               ** min : -20
                               ** default : 23.0
                               ** unit : Â°C
                 * name: calendarCumuls_t1
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: vAI
                               ** description : Response of vernalization rate to temperature
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.015
                               ** unit : d-1 Â°C-1
                 * name: leafNumber_t1
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: isVernalizable
                               ** description : true if the plant is vernalizable
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: minDL
                               ** description : Threshold daylength below which it does influence vernalization rate
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 12
                               ** default : 8.0
                               ** unit : h
                 * name: minFinalNumber_t1
                               ** description : minimum final leaf number
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 5.5
                               ** unit : leaf
                 * name: currentdate
                               ** description : current date 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
     - outputs:
                 * name: minFinalNumber
                               ** description : minimum final leaf number
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                 * name: calendarCumuls
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                 * name: vernaprog
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
                 * name: calendarMoments
                               ** description : List containing appearance of each stage
                               ** datatype : STRINGLIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
                 * name: calendarDates
                               ** description : List containing  the dates of the wheat developmental phases
                               ** datatype : DATELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
    """

    minFinalNumber:float
    calendarCumuls:List[float] = []
    vernaprog:float
    calendarMoments:List[str] = []
    calendarDates:List[datetime] = []
    maxVernaProg:float
    dLverna:float
    primordno:float
    minLeafNumber:float
    potlfno:float
    tt:float
    calendarMoments = []
    calendarDates = []
    calendarCumuls = []
    calendarMoments = copy(calendarMoments_t1)
    calendarCumuls = copy(calendarCumuls_t1)
    calendarDates = copy(calendarDates_t1)
    minFinalNumber = minFinalNumber_t1
    vernaprog = vernaprog_t1
    if isVernalizable == 1 and vernaprog_t1 < 1.0:
        tt = deltaTT
        if tt >= minTvern and tt <= intTvern:
            vernaprog = vernaprog_t1 + (vAI * tt) + vBEE
        else:
            vernaprog = vernaprog_t1
        if tt > intTvern:
            maxVernaProg = vAI * intTvern + vBEE
            dLverna = max(minDL, min(maxDL, dayLength))
            vernaprog = vernaprog + max(0.0, maxVernaProg * (1.0 + ((intTvern - tt) / (maxTvern - intTvern) * ((dLverna - minDL) / (maxDL - minDL)))))
        primordno = 2.0 * leafNumber_t1 + pNini
        minLeafNumber = minFinalNumber_t1
        if vernaprog >= 1.0 or primordno >= aMXLFNO:
            minFinalNumber = max(primordno, minFinalNumber_t1)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT)
            calendarDates.append(currentdate)
            vernaprog = max(1.0, vernaprog)
        else:
            potlfno = aMXLFNO - ((aMXLFNO - minLeafNumber) * vernaprog)
            if primordno >= potlfno:
                minFinalNumber = max((potlfno + primordno) / 2.0, minFinalNumber_t1)
                vernaprog = max(1.0, vernaprog)
                calendarMoments.append("EndVernalisation")
                calendarCumuls.append(cumulTT)
                calendarDates.append(currentdate)
    return (minFinalNumber, calendarCumuls, vernaprog, calendarMoments, calendarDates)
#%%CyML Model End%%