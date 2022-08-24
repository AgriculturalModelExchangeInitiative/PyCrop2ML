import numpy 
from math import *
def model_shootnumber(float leafNumber,
                      int numberTillerCohort_t1,
                      float canopyShootNumber_t1,
                      intlist leafTillerNumberArray_t1,
                      floatlist tilleringProfile_t1,
                      float sowingDensity,
                      float targetFertileShoot):
    """

    ShootNumber model
    Author: Pierre MARTRE
    Reference: ('',)
    Institution: INRA/LEPSE Montpellier
    ExtendedDescription: 
    ShortDescription: 

    """
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef intlist leafTillerNumberArray
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
    cdef int emergedLeaves 
    cdef int shoots 
    cdef int i 
    cdef intlist  lNumberArray_rate
    tilleringProfile = copy(tilleringProfile_t1)
    emergedLeaves = max(1, ceil(leafNumber - 1.0))
    shoots = fibonacci(emergedLeaves)
    canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
    averageShootNumberPerPlant = canopyShootNumber / sowingDensity
    if canopyShootNumber != canopyShootNumber_t1:
        tilleringProfile.append(canopyShootNumber - canopyShootNumber_t1)
    numberTillerCohort = len(tilleringProfile)
    for i in range(len(leafTillerNumberArray_t1) , ceil(leafNumber) , 1):
        lNumberArray_rate.append(numberTillerCohort)
    leafTillerNumberArray = copy(leafTillerNumberArray_t1)
    leafTillerNumberArray.extend(lNumberArray_rate)
    return  averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort
from math import *
from array import array

def fibonacci(int n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)