# coding: utf8
from copy import copy
from array import array
from math import *

import numpy
from datetime import datetime

def model_vernalizationprogress(calendarDates_t1,
         calendarMoments_t1,
         minFinalNumber_t1,
         calendarCumuls_t1,
         leafNumber_t1,
         vernaprog_t1,
         dayLength,
         deltaTT,
         cumulTT,
         currentdate,
         minTvern,
         intTvern,
         vAI,
         vBEE,
         minDL,
         maxDL,
         maxTvern,
         pNini,
         aMXLFNO,
         isVernalizable):
    """
     - Name: VernalizationProgress -Version: 001, -Time step: 1
     - Description:
                 * Title: VernalizationProgress model
                 * Author: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: calendarDates_t1
                               ** datatype : DATELIST
                               ** default : 
                               ** description : List containing  the dates of the wheat developmental phases
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarMoments_t1
                               ** datatype : STRINGLIST
                               ** default : 
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: minFinalNumber_t1
                               ** datatype : DOUBLE
                               ** default : 5.5
                               ** description : minimum final leaf number
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: calendarCumuls_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: leafNumber_t1
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: vernaprog_t1
                               ** datatype : DOUBLE
                               ** default : 0.5517254187376879
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** inputtype : variable
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: dayLength
                               ** datatype : DOUBLE
                               ** default : 12.3037621834005
                               ** description : day length
                               ** inputtype : variable
                               ** max : 10000
                               ** min : 0
                               ** unit : mm2 m-2
                               ** variablecategory : auxiliary
                 * name: deltaTT
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** max : 100.0
                               ** min : 0.0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: cumulTT
                               ** datatype : DOUBLE
                               ** default : 112.330110409888
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** max : 10000
                               ** min : -200
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: currentdate
                               ** datatype : DATE
                               ** default : 
                               ** description : current date 
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : auxiliary
                 * name: minTvern
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Minimum temperature for vernalization to occur
                               ** inputtype : parameter
                               ** max : 60
                               ** min : -20
                               ** parametercategory : constant
                               ** unit : Â°C
                 * name: intTvern
                               ** datatype : DOUBLE
                               ** default : 11.0
                               ** description : Intermediate temperature for vernalization to occur
                               ** inputtype : parameter
                               ** max : 60
                               ** min : -20
                               ** parametercategory : constant
                               ** unit : Â°C
                 * name: vAI
                               ** datatype : DOUBLE
                               ** default : 0.015
                               ** description : Response of vernalization rate to temperature
                               ** inputtype : parameter
                               ** max : 1
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : d-1 Â°C-1
                 * name: vBEE
                               ** datatype : DOUBLE
                               ** default : 0.01
                               ** description : Vernalization rate at 0Â°C
                               ** inputtype : parameter
                               ** max : 1
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : d-1
                 * name: minDL
                               ** datatype : DOUBLE
                               ** default : 8.0
                               ** description : Threshold daylength below which it does influence vernalization rate
                               ** inputtype : parameter
                               ** max : 24
                               ** min : 12
                               ** parametercategory : constant
                               ** unit : h
                 * name: maxDL
                               ** datatype : DOUBLE
                               ** default : 15.0
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                               ** inputtype : parameter
                               ** max : 24
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : h
                 * name: maxTvern
                               ** datatype : DOUBLE
                               ** default : 23.0
                               ** description : Maximum temperature for vernalization to occur
                               ** inputtype : parameter
                               ** max : 60
                               ** min : -20
                               ** parametercategory : constant
                               ** unit : Â°C
                 * name: pNini
                               ** datatype : DOUBLE
                               ** default : 4.0
                               ** description : Number of primorida in the apex at emergence
                               ** inputtype : parameter
                               ** max : 24
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : primordia
                 * name: aMXLFNO
                               ** datatype : DOUBLE
                               ** default : 24.0
                               ** description : Absolute maximum leaf number
                               ** inputtype : parameter
                               ** max : 25
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : leaf
                 * name: isVernalizable
                               ** datatype : INT
                               ** default : 1
                               ** description : true if the plant is vernalizable
                               ** inputtype : parameter
                               ** max : 1
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
     - outputs:
                 * name: vernaprog
                               ** datatype : DOUBLE
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: minFinalNumber
                               ** datatype : DOUBLE
                               ** description : minimum final leaf number
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: calendarMoments
                               ** datatype : STRINGLIST
                               ** description : List containing appearance of each stage
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarDates
                               ** datatype : DATELIST
                               ** description : List containing  the dates of the wheat developmental phases
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarCumuls
                               ** datatype : DOUBLELIST
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
    """

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
    return (vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls)