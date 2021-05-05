import numpy as np 
from math import *

def initshootnumber_(float sowingDensity=288.0):
    """

    Initialize ShootNumber Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA/LEPSE Montpellier
    Abstract: calculate the shoot number and update the related variables if needed

    """
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef list tilleringProfile
    cdef int tillerNumber
    canopyShootNumber = sowingDensity
    averageShootNumberPerPlant = 1.0
    tilleringProfile.append(sowingDensity)
    tillerNumber = 1
    return  averageShootNumberPerPlant, canopyShootNumber, tilleringProfile, tillerNumber
