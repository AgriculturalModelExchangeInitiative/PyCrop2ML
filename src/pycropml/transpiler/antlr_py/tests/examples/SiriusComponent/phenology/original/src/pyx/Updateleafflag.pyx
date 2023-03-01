import numpy 
from math import *
from datetime import datetime

def model_updateleafflag(floatlist calendarCumuls,
                         float finalLeafNumber,
                         stringlist calendarMoments,
                         datelist calendarDates,
                         float cumulTT,
                         float leafNumber,
                         int hasFlagLeafLiguleAppeared_t1,
                         float phase,
                         datetime currentdate):
    """

    UpdateLeafFlag model
    Author: Pierre MARTRE
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: tells if flag leaf has appeared and update the calendar if so    	
    ShortDescription: None

    """
    cdef int hasFlagLeafLiguleAppeared
    hasFlagLeafLiguleAppeared=hasFlagLeafLiguleAppeared_t1
    if phase >= 1.0 and phase < 4.0:
        if leafNumber > 0.0:
            if hasFlagLeafLiguleAppeared_t1 == 0 and finalLeafNumber > 0.0 and leafNumber >= finalLeafNumber:
                hasFlagLeafLiguleAppeared=1
                if "FlagLeafLiguleJustVisible" not in calendarMoments:
                    calendarMoments.append("FlagLeafLiguleJustVisible")
                    calendarCumuls.append(cumulTT)
                    calendarDates.append(currentdate)
        else:
            hasFlagLeafLiguleAppeared=0
    return  calendarCumuls, calendarMoments, calendarDates, hasFlagLeafLiguleAppeared


