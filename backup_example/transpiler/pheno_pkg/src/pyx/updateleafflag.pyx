import numpy as np 
from math import *

def updateleafflag_(float cumulTT=741.510096671757,
                    float leafNumber=8.919453833361189,
                    list calendarMoments=['Sowing'],
                    list calendarDates=['21/3/2007'],
                    list calendarCumuls=[0.0],
                    str currentdate='29/4/2007',
                    float finalLeafNumber=8.797582013199484,
                    int hasFlagLeafLiguleAppeared=1,
                    float phase=1.0):
    """

    UpdateLeafFlag Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: tells if flag leaf has appeared and update the calendar if so
    	

    """
    if (phase >= 1.0 and phase< 4.0):
        if (leafNumber > 0.0):
            if (hasFlagLeafLiguleAppeared == 0 and (finalLeafNumber > 0.0 and leafNumber >= finalLeafNumber)):
                hasFlagLeafLiguleAppeared = 1
                if  "FlagLeafLiguleJustVisible" not in calendarMoments:
                    calendarMoments.append("FlagLeafLiguleJustVisible")
                    calendarCumuls.append(cumulTT)
                    calendarDates.append(currentdate)
        else:
            hasFlagLeafLiguleAppeared = 0
    return  hasFlagLeafLiguleAppeared, calendarMoments, calendarDates, calendarCumuls
