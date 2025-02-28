# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_ptq(deltaTT:float,
         listPARTTWindowForPTQ_t1:List[float],
         listGAITTWindowForPTQ:List[float],
         pAR:float,
         listTTShootWindowForPTQ_t1:List[float],
         kl:float,
         tTWindowForPTQ:float):
    """
     - Name: PTQ -Version: 001, -Time step: 1
     - Description:
                 * Title: PTQ model
                 * Authors: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: Calculate Photothermal Quaotient 
                 * ShortDescription: None
     - inputs:
                 * name: deltaTT
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 100.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d
                 * name: listPARTTWindowForPTQ_t1
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : MJ m2 d
                 * name: listGAITTWindowForPTQ
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : m2 leaf m-2 ground
                 * name: pAR
                               ** description : Daily Photosyntetically Active Radiation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : MJ mÂ² d
                 * name: listTTShootWindowForPTQ_t1
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: kl
                               ** description : Exctinction Coefficient
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : 0.0
                               ** default : 0.45
                               ** unit : 
                 * name: tTWindowForPTQ
                               ** description : Thermal time window in which averages are computed
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 70000.0
                               ** min : 0.0
                               ** default : 70.0
                               ** unit : Â°C d
     - outputs:
                 * name: listTTShootWindowForPTQ
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                 * name: listPARTTWindowForPTQ
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : MJ m2 d
                 * name: ptq
                               ** description : Photothermal quotient 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000.0
                               ** min : 0.0
                               ** unit : MJ Â°C-1 d-1 m-2)
    """

    listTTShootWindowForPTQ:List[float] = []
    listPARTTWindowForPTQ:List[float] = []
    ptq:float
    TTList:List[float] = []
    PARList:List[float] = []
    i:int
    count:int
    SumTT:float
    parInt:float
    TTShoot:float
    listPARTTWindowForPTQ = []
    listTTShootWindowForPTQ = []
    TTList = []
    PARList = []
    parInt = 0.0
    for i in range(0 , len(listTTShootWindowForPTQ_t1) , 1):
        TTList.append(listTTShootWindowForPTQ_t1[i])
        PARList.append(listPARTTWindowForPTQ_t1[i])
    TTList.append(deltaTT)
    PARList.append(pAR)
    SumTT = sum(TTList)
    count = 0
    while SumTT > tTWindowForPTQ:
        SumTT = SumTT - TTList[count]
        count = count + 1
    for i in range(count , len(TTList) , 1):
        listTTShootWindowForPTQ.append(TTList[i])
        listPARTTWindowForPTQ.append(PARList[i])
    for i in range(0 , len(listTTShootWindowForPTQ) , 1):
        parInt = parInt + (listPARTTWindowForPTQ[i] * (1 - exp(-kl * listGAITTWindowForPTQ[i])))
    TTShoot = sum(listTTShootWindowForPTQ)
    ptq = parInt / TTShoot
    return (listTTShootWindowForPTQ, listPARTTWindowForPTQ, ptq)
#%%CyML Model End%%