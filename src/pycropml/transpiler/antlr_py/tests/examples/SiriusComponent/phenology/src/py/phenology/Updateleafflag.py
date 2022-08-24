# coding: utf8
from copy import copy
from array import array
from math import *

import numpy
from datetime import datetime

def model_updateleafflag(calendarDates,
         calendarMoments,
         phase,
         calendarCumuls,
         leafNumber,
         finalLeafNumber,
         hasFlagLeafLiguleAppeared_t1,
         cumulTT,
         currentdate):
    """
     - Name: UpdateLeafFlag -Version: 001, -Time step: 1
     - Description:
                 * Title: UpdateLeafFlag model
                 * Author: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: calendarDates
                               ** datatype : DATELIST
                               ** default : 
                               ** description : List containing  the dates of the wheat developmental phases
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarMoments
                               ** datatype : STRINGLIST
                               ** default : 
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: phase
                               ** datatype : DOUBLE
                               ** default : 1
                               ** description :  the name of the phase
                               ** inputtype : variable
                               ** max : 7
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarCumuls
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: leafNumber
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: finalLeafNumber
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : final leaf number
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: hasFlagLeafLiguleAppeared_t1
                               ** datatype : INT
                               ** default : 1
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** inputtype : variable
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
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
     - outputs:
                 * name: calendarDates
                               ** datatype : DATELIST
                               ** description : List containing  the dates of the wheat developmental phases
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: calendarMoments
                               ** datatype : STRINGLIST
                               ** description : List containing appearance of each stage
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
                 * name: hasFlagLeafLiguleAppeared
                               ** datatype : INT
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
    """

    hasFlagLeafLiguleAppeared = hasFlagLeafLiguleAppeared_t1
    if phase >= 1.0 and phase < 4.0:
        if leafNumber > 0.0:
            if hasFlagLeafLiguleAppeared_t1 == 0 and (finalLeafNumber > 0.0 and leafNumber >= finalLeafNumber):
                hasFlagLeafLiguleAppeared = 1
                if "FlagLeafLiguleJustVisible" not in calendarMoments:
                    calendarMoments.append("FlagLeafLiguleJustVisible")
                    calendarCumuls.append(cumulTT)
                    calendarDates.append(currentdate)
        else:
            hasFlagLeafLiguleAppeared = 0
    return (calendarDates, calendarMoments, calendarCumuls, hasFlagLeafLiguleAppeared)