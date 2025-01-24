# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_updatecalendar(calendarCumuls:List[float],
         calendarMoments:List[str],
         cumulTT:float,
         calendarDates:List[datetime],
         phase:float,
         currentdate:datetime):
    """
     - Name: UpdateCalendar -Version: 001, -Time step: 1
     - Description:
                 * Title: UpdateCalendar model
                 * Authors: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
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
                 * name: calendarMoments
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRINGLIST
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
                 * name: calendarDates
                               ** description : List containing  the dates of the wheat developmental phases
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** max : 
                               ** min : 
                               ** default : 
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
    """

    if phase >= 1.0 and (phase < 2.0 and "Emergence" not in calendarMoments):
        calendarMoments.append("Emergence")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 2.0 and (phase < 3.0 and "FloralInitiation" not in calendarMoments):
        calendarMoments.append("FloralInitiation")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 3.0 and (phase < 4.0 and "Heading" not in calendarMoments):
        calendarMoments.append("Heading")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase == 4.0 and "Anthesis" not in calendarMoments:
        calendarMoments.append("Anthesis")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase == 4.5 and "EndCellDivision" not in calendarMoments:
        calendarMoments.append("EndCellDivision")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 5.0 and (phase < 6.0 and "EndGrainFilling" not in calendarMoments):
        calendarMoments.append("EndGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif phase >= 6.0 and (phase < 7.0 and "Maturity" not in calendarMoments):
        calendarMoments.append("Maturity")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    return (calendarCumuls, calendarMoments, calendarDates)
#%%CyML Model End%%