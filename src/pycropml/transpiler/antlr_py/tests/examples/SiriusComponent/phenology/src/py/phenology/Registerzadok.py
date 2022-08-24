# coding: utf8
from copy import copy
from array import array
from math import *

import numpy
from datetime import datetime

def model_registerzadok(calendarDates,
         calendarMoments,
         phase,
         calendarCumuls,
         leafNumber,
         finalLeafNumber,
         currentZadokStage_t1,
         hasZadokStageChanged_t1,
         cumulTT,
         cumulTTFromZC_65,
         currentdate,
         der,
         slopeTSFLN,
         intTSFLN):
    """
     - Name: RegisterZadok -Version: 001, -Time step: 1
     - Description:
                 * Title: RegisterZadok model
                 * Author: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA/LEPSE Montpellier
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
                 * name: currentZadokStage_t1
                               ** datatype : STRING
                               ** default : 
                               ** description : zadok stage
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: hasZadokStageChanged_t1
                               ** datatype : INT
                               ** default : 0
                               ** description : true if the zadok stage has changed this time step
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
                 * name: cumulTTFromZC_65
                               ** datatype : DOUBLE
                               ** default : 
                               ** description :  cumul TT from Anthesis to current date 
                               ** inputtype : variable
                               ** max : -5000D
                               ** min : 0
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
                 * name: der
                               ** datatype : DOUBLE
                               ** default : 300.0
                               ** description : Duration of the endosperm endoreduplication phase
                               ** inputtype : parameter
                               ** max : 10000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d
                 * name: slopeTSFLN
                               ** datatype : DOUBLE
                               ** default : 0.9
                               ** description : Slope of the relationship between Haun stage at terminal spikelet and final leaf number
                               ** inputtype : parameter
                               ** max : 10000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
                 * name: intTSFLN
                               ** datatype : DOUBLE
                               ** default : 2.6
                               ** description : Intercept of the relationship between Haun stage at terminal spikelet and final leaf number
                               ** inputtype : parameter
                               ** max : 10000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
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
                 * name: hasZadokStageChanged
                               ** datatype : INT
                               ** description : true if the zadok stage has changed this time step
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: currentZadokStage
                               ** datatype : STRING
                               ** description : zadok stage
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
    """

    currentZadokStage = currentZadokStage_t1
    roundedFinalLeafNumber = int(finalLeafNumber + 0.5)
    if leafNumber >= 4.0 and "MainShootPlus1Tiller" not in calendarMoments:
        calendarMoments.append("MainShootPlus1Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus1Tiller"
    elif leafNumber >= 5.0 and "MainShootPlus2Tiller" not in calendarMoments:
        calendarMoments.append("MainShootPlus2Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus2Tiller"
    elif leafNumber >= 6.0 and "MainShootPlus3Tiller" not in calendarMoments:
        calendarMoments.append("MainShootPlus3Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus3Tiller"
    elif finalLeafNumber > 0.0 and (leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN and "TerminalSpikelet" not in calendarMoments):
        calendarMoments.append("TerminalSpikelet")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "TerminalSpikelet"
    elif leafNumber >= roundedFinalLeafNumber - 4.0 and (roundedFinalLeafNumber - 4 > 0 and "PseudoStemErection" not in calendarMoments):
        calendarMoments.append("PseudoStemErection")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "PseudoStemErection"
    elif leafNumber >= roundedFinalLeafNumber - 3.0 and (roundedFinalLeafNumber - 3 > 0 and "1stNodeDetectable" not in calendarMoments):
        calendarMoments.append("1stNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "1stNodeDetectable"
    elif leafNumber >= roundedFinalLeafNumber - 2.0 and (roundedFinalLeafNumber - 2 > 0 and "2ndNodeDetectable" not in calendarMoments):
        calendarMoments.append("2ndNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "2ndNodeDetectable"
    elif leafNumber >= roundedFinalLeafNumber - 1.0 and (roundedFinalLeafNumber - 1 > 0 and "FlagLeafJustVisible" not in calendarMoments):
        calendarMoments.append("FlagLeafJustVisible")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "FlagLeafJustVisible"
    elif "MidGrainFilling" not in calendarMoments and (phase == 4.5 and cumulTTFromZC_65 >= der):
        calendarMoments.append("MidGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MidGrainFilling"
    else:
        hasZadokStageChanged = 0
    return (calendarDates, calendarMoments, calendarCumuls, hasZadokStageChanged, currentZadokStage)