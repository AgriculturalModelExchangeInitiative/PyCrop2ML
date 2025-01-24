# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_shootnumber(tilleringProfile_t1:List[float],
         sowingDensity:float,
         leafNumber:float,
         leafTillerNumberArray_t1:List[int],
         targetFertileShoot:float,
         canopyShootNumber_t1:float):
    """
     - Name: ShootNumber -Version: 001, -Time step: 1
     - Description:
                 * Title: ShootNumber model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA/LEPSE Montpellier
                 * ExtendedDescription: calculate the shoot number and update the related variables if needed
                 * ShortDescription: None
     - inputs:
                 * name: tilleringProfile_t1
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: sowingDensity
                               ** description : number of plant /mÂ²
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 500
                               ** min : 0
                               ** default : 288.0
                               ** unit : plant m-2
                 * name: leafNumber
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: leafTillerNumberArray_t1
                               ** description : store the number of tiller for each leaf layer
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INTLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : leaf
                 * name: targetFertileShoot
                               ** description : max value of shoot number for the canopy
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 280
                               ** default : 600.0
                               ** unit : shoot
                 * name: canopyShootNumber_t1
                               ** description : shoot number for the whole canopy
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 288.0
                               ** unit : shoot m-2
     - outputs:
                 * name: averageShootNumberPerPlant
                               ** description : average shoot number per plant in the canopy
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                 * name: leafTillerNumberArray
                               ** description : store the number of tiller for each leaf layer
                               ** datatype : INTLIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : leaf
                 * name: canopyShootNumber
                               ** description : shoot number for the whole canopy
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                 * name: numberTillerCohort
                               ** description : Number of tiller which appears
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : dimensionless
                 * name: tilleringProfile
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
    """

    averageShootNumberPerPlant:float
    leafTillerNumberArray:List[int] = []
    canopyShootNumber:float
    numberTillerCohort:int
    tilleringProfile:List[float] = []
    emergedLeaves:int
    shoots:int
    i:int
    lNumberArray_rate:List[int] = []
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
    return (averageShootNumberPerPlant, leafTillerNumberArray, canopyShootNumber, numberTillerCohort, tilleringProfile)
#%%CyML Model End%%

def fibonacci(n:int):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#%%CyML Init Begin%%
def init_shootnumber(sowingDensity:float,
         targetFertileShoot:float):
    tilleringProfile_t1:List[float] = []
    leafNumber:float = 0.0
    leafTillerNumberArray_t1:List[int] = []
    canopyShootNumber_t1:float = 288.0
    tilleringProfile_t1 = []
    leafTillerNumberArray_t1 = []
    canopyShootNumber_t1 = sowingDensity
    tilleringProfile_t1.append(sowingDensity)
    return (tilleringProfile_t1, leafNumber, leafTillerNumberArray_t1, canopyShootNumber_t1)
#%%CyML Init End%%