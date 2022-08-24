# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_ptq(listGAITTWindowForPTQ,
         listTTShootWindowForPTQ_t1,
         listPARTTWindowForPTQ_t1,
         pAR,
         deltaTT,
         tTWindowForPTQ,
         kl):
    """
     - Name: PTQ -Version: 001, -Time step: 1
     - Description:
                 * Title: PTQ model
                 * Author: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: listGAITTWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
                 * name: listTTShootWindowForPTQ_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: listPARTTWindowForPTQ_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : MJ m2 d
                               ** variablecategory : state
                 * name: pAR
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Daily Photosyntetically Active Radiation
                               ** inputtype : variable
                               ** max : 10000.0
                               ** min : 0.0
                               ** unit : MJ mÂ² d
                               ** variablecategory : auxiliary
                 * name: deltaTT
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** max : 100.0
                               ** min : 0.0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: tTWindowForPTQ
                               ** datatype : DOUBLE
                               ** default : 70.0
                               ** description : Thermal time window in which averages are computed
                               ** inputtype : parameter
                               ** max : 70000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : Â°C d
                 * name: kl
                               ** datatype : DOUBLE
                               ** default : 0.45
                               ** description : Exctinction Coefficient
                               ** inputtype : parameter
                               ** max : 50.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : 
     - outputs:
                 * name: listPARTTWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** max : 
                               ** min : 
                               ** unit : MJ m2 d
                               ** variablecategory : state
                 * name: listTTShootWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: ptq
                               ** datatype : DOUBLE
                               ** description : Photothermal quotient 
                               ** max : 10000.0
                               ** min : 0.0
                               ** unit : MJ Â°C-1 d-1 m-2)
                               ** variablecategory : state
    """

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
    return (listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq)