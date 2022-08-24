# coding: utf8
from copy import copy
from array import array
from math import *

import numpy
from datetime import datetime

def model_updatecalendar(calendarCumuls,
         calendarDates,
         calendarMoments,
         phase,
         cumulTT,
         currentdate):
    """
     - Name: UpdateCalendar -Version: 001, -Time step: 1
     - Description:
                 * Title: UpdateCalendar model
                 * Author: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: calendarCumuls
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
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
                 * name: calendarCumuls
                               ** datatype : DOUBLELIST
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
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
    return (calendarCumuls, calendarDates, calendarMoments)