# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_updateleafflag(calendarCumuls:List[float],
         finalLeafNumber:float,
         calendarMoments:List[str],
         calendarDates:List[datetime],
         cumulTT:float,
         leafNumber:float,
         hasFlagLeafLiguleAppeared_t1:int,
         phase:float,
         currentdate:datetime):
    """
     - Name: UpdateLeafFlag -Version: 001, -Time step: 1
     - Description:
                 * Title: UpdateLeafFlag model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: tells if flag leaf has appeared and update the calendar if so    	
                 * ShortDescription: None
     - inputs:
                 * name: calendarCumuls
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: finalLeafNumber
                               ** description : final leaf number
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: calendarMoments
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: calendarDates
                               ** description : List containing  the dates of the wheat developmental phases
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: cumulTT
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : -200
                               ** default : 112.330110409888
                               ** unit : Â°C d
                 * name: leafNumber
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: hasFlagLeafLiguleAppeared_t1
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: phase
                               ** description :  the name of the phase
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 7
                               ** min : 0
                               ** default : 1
                               ** unit : 
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
                 * name: calendarCumuls
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
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
                 * name: hasFlagLeafLiguleAppeared
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
    """

    hasFlagLeafLiguleAppeared:int
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
    return (calendarCumuls, calendarMoments, calendarDates, hasFlagLeafLiguleAppeared)
#%%CyML Model End%%