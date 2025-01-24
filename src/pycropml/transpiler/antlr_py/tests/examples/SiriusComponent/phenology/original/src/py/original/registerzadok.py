# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_registerzadok(calendarCumuls:List[float],
         finalLeafNumber:float,
         cumulTTFromZC_65:float,
         calendarMoments:List[str],
         cumulTT:float,
         calendarDates:List[datetime],
         intTSFLN:float,
         der:float,
         leafNumber:float,
         slopeTSFLN:float,
         currentZadokStage_t1:str,
         phase:float,
         currentdate:datetime):
    """
     - Name: RegisterZadok -Version: 001, -Time step: 1
     - Description:
                 * Title: RegisterZadok model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA/LEPSE Montpellier
                 * ExtendedDescription: Record the zadok stage in the calendar    	
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
                 * name: cumulTTFromZC_65
                               ** description :  cumul TT from Anthesis to current date 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : -5000
                               ** min : 0
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
                 * name: intTSFLN
                               ** description : Intercept of the relationship between Haun stage at terminal spikelet and final leaf number
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 2.6
                               ** unit : 
                 * name: der
                               ** description : Duration of the endosperm endoreduplication phase
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 300.0
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
                 * name: slopeTSFLN
                               ** description : Slope of the relationship between Haun stage at terminal spikelet and final leaf number
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 0.9
                               ** unit : 
                 * name: currentZadokStage_t1
                               ** description : zadok stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRING
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
                 * name: currentZadokStage
                               ** description : zadok stage
                               ** datatype : STRING
                               ** variablecategory : state
                               ** max : 
                               ** min : 
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
                 * name: hasZadokStageChanged
                               ** description : true if the zadok stage has changed this time step
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
    """

    currentZadokStage:str
    hasZadokStageChanged:int
    roundedFinalLeafNumber:int
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
    elif finalLeafNumber > 0.0 and (leafNumber >= (slopeTSFLN * finalLeafNumber - intTSFLN) and "TerminalSpikelet" not in calendarMoments):
        calendarMoments.append("TerminalSpikelet")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "TerminalSpikelet"
    elif leafNumber >= (roundedFinalLeafNumber - 4.0) and (roundedFinalLeafNumber - 4 > 0 and "PseudoStemErection" not in calendarMoments):
        calendarMoments.append("PseudoStemErection")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "PseudoStemErection"
    elif leafNumber >= (roundedFinalLeafNumber - 3.0) and (roundedFinalLeafNumber - 3 > 0 and "1stNodeDetectable" not in calendarMoments):
        calendarMoments.append("1stNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "1stNodeDetectable"
    elif leafNumber >= (roundedFinalLeafNumber - 2.0) and (roundedFinalLeafNumber - 2 > 0 and "2ndNodeDetectable" not in calendarMoments):
        calendarMoments.append("2ndNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "2ndNodeDetectable"
    elif leafNumber >= (roundedFinalLeafNumber - 1.0) and (roundedFinalLeafNumber - 1 > 0 and "FlagLeafJustVisible" not in calendarMoments):
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
    return (calendarCumuls, currentZadokStage, calendarMoments, calendarDates, hasZadokStageChanged)
#%%CyML Model End%%