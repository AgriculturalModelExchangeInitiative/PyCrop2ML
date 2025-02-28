import numpy 
from math import *
def model_shootnumber(floatlist tilleringProfile_t1,
                      float sowingDensity,
                      float leafNumber,
                      intlist leafTillerNumberArray_t1,
                      float targetFertileShoot,
                      float canopyShootNumber_t1):
    """

    ShootNumber model
    Author: Pierre MARTRE
    Reference: ('',)
    Institution: INRA/LEPSE Montpellier
    ExtendedDescription: calculate the shoot number and update the related variables if needed
    ShortDescription: None

    """
    cdef float averageShootNumberPerPlant
    cdef intlist leafTillerNumberArray
    cdef float canopyShootNumber
    cdef int numberTillerCohort
    cdef floatlist tilleringProfile
    cdef int emergedLeaves 
    cdef int shoots 
    cdef int i 
    cdef intlist  lNumberArray_rate
    leafTillerNumberArray=[]
    tilleringProfile=[]
    lNumberArray_rate=[]
    tilleringProfile=copy(tilleringProfile_t1)
    emergedLeaves=max(1, ceil(leafNumber - 1.0))
    shoots=fibonacci(emergedLeaves)
    canopyShootNumber=min(shoots * sowingDensity, targetFertileShoot)
    averageShootNumberPerPlant=canopyShootNumber / sowingDensity
    if canopyShootNumber != canopyShootNumber_t1:
        tilleringProfile.append(canopyShootNumber - canopyShootNumber_t1)
    numberTillerCohort=len(tilleringProfile)
    for i in range(len(leafTillerNumberArray_t1) , ceil(leafNumber) , 1):
        lNumberArray_rate.append(numberTillerCohort)
    leafTillerNumberArray=copy(leafTillerNumberArray_t1)
    leafTillerNumberArray.extend(lNumberArray_rate)
    return  averageShootNumberPerPlant, leafTillerNumberArray, canopyShootNumber, numberTillerCohort, tilleringProfile


def fibonacci(int n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def init_shootnumber(float sowingDensity,
                     float targetFertileShoot):
    cdef floatlist tilleringProfile_t1
    cdef float leafNumber=0.0
    cdef intlist leafTillerNumberArray_t1
    cdef float canopyShootNumber_t1=288.0
    tilleringProfile_t1 = []
    leafTillerNumberArray_t1 = []
    canopyShootNumber_t1=sowingDensity
    tilleringProfile_t1.append(sowingDensity)
    return  tilleringProfile_t1, leafNumber, leafTillerNumberArray_t1, canopyShootNumber_t1
