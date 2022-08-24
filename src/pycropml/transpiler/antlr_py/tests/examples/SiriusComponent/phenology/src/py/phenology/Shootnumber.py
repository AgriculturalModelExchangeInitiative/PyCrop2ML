# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_shootnumber(leafNumber,
         numberTillerCohort_t1,
         canopyShootNumber_t1,
         leafTillerNumberArray_t1,
         tilleringProfile_t1,
         sowingDensity,
         targetFertileShoot):
    """
     - Name: ShootNumber -Version: 001, -Time step: 1
     - Description:
                 * Title: ShootNumber model
                 * Author: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA/LEPSE Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: leafNumber
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: numberTillerCohort_t1
                               ** datatype : INT
                               ** default : 
                               ** description : Number of tiller which appears
                               ** inputtype : variable
                               ** max : 10000
                               ** min : 0
                               ** unit : dimensionless
                               ** variablecategory : state
                 * name: canopyShootNumber_t1
                               ** datatype : DOUBLE
                               ** default : 288.0
                               ** description : shoot number for the whole canopy
                               ** inputtype : variable
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                               ** variablecategory : state
                 * name: leafTillerNumberArray_t1
                               ** datatype : INTLIST
                               ** default : 
                               ** description : store the number of tiller for each leaf layer
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : leaf
                               ** variablecategory : state
                 * name: tilleringProfile_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: sowingDensity
                               ** datatype : DOUBLE
                               ** default : 288.0
                               ** description : number of plant /mÂ²
                               ** inputtype : parameter
                               ** max : 500
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : plant m-2
                 * name: targetFertileShoot
                               ** datatype : DOUBLE
                               ** default : 600.0
                               ** description : max value of shoot number for the canopy
                               ** inputtype : parameter
                               ** max : 1000
                               ** min : 280
                               ** parametercategory : constant
                               ** unit : shoot
     - outputs:
                 * name: averageShootNumberPerPlant
                               ** datatype : DOUBLE
                               ** description : average shoot number per plant in the canopy
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                               ** variablecategory : state
                 * name: canopyShootNumber
                               ** datatype : DOUBLE
                               ** description : shoot number for the whole canopy
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                               ** variablecategory : state
                 * name: leafTillerNumberArray
                               ** datatype : INTLIST
                               ** description : store the number of tiller for each leaf layer
                               ** max : 
                               ** min : 
                               ** unit : leaf
                               ** variablecategory : state
                 * name: tilleringProfile
                               ** datatype : DOUBLELIST
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                               ** max : 
                               ** min : 
                               ** unit : 
                               ** variablecategory : state
                 * name: numberTillerCohort
                               ** datatype : INT
                               ** description : Number of tiller which appears
                               ** max : 10000
                               ** min : 0
                               ** unit : dimensionless
                               ** variablecategory : state
    """

    leafTillerNumberArray = []
    tilleringProfile = []
    lNumberArray_rate = []
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
    return (averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)