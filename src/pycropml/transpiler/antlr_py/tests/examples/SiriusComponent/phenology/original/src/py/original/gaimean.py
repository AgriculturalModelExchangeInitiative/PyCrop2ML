# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_gaimean(deltaTT:float,
         gAI:float,
         tTWindowForPTQ:float,
         listTTShootWindowForPTQ1_t1:List[float],
         pastMaxAI_t1:float,
         listGAITTWindowForPTQ_t1:List[float]):
    """
     - Name: GAImean -Version: 001, -Time step: 1
     - Description:
                 * Title: GAImean model
                 * Authors: LoÃ¯c Manceau
                 * Reference: ('',)
                 * Institution: INRA
                 * ExtendedDescription: -
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
                 * name: gAI
                               ** description : Green Area Index of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 500.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: tTWindowForPTQ
                               ** description : Thermal Time window for average
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 5000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d
                 * name: listTTShootWindowForPTQ1_t1
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: pastMaxAI_t1
                               ** description : Maximum Leaf Area Index reached the current day
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 5000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: listGAITTWindowForPTQ_t1
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : m2 leaf m-2 ground
     - outputs:
                 * name: listGAITTWindowForPTQ
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : m2 leaf m-2 ground
                 * name: pastMaxAI
                               ** description : Maximum Leaf Area Index reached the current day
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 5000.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: listTTShootWindowForPTQ1
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                 * name: gAImean
                               ** description : Mean Green Area Index
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 500.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
    """

    listGAITTWindowForPTQ:List[float] = []
    pastMaxAI:float
    listTTShootWindowForPTQ1:List[float] = []
    gAImean:float
    TTList:List[float] = []
    GAIList:List[float] = []
    SumTT:float
    count:int
    gai_:float
    gaiMean_:float
    countGaiMean:int
    i:int
    listTTShootWindowForPTQ1 = []
    listGAITTWindowForPTQ = []
    TTList = []
    GAIList = []
    count = 0
    gai_ = 0.0
    gaiMean_ = 0.0
    countGaiMean = 0
    for i in range(0 , len(listTTShootWindowForPTQ1_t1) , 1):
        TTList.append(listTTShootWindowForPTQ1_t1[i])
        GAIList.append(listGAITTWindowForPTQ_t1[i])
    TTList.append(deltaTT)
    GAIList.append(gAI)
    SumTT = sum(TTList)
    while SumTT > tTWindowForPTQ:
        SumTT = SumTT - TTList[count]
        count = count + 1
    for i in range(count , len(TTList) , 1):
        listTTShootWindowForPTQ1.append(TTList[i])
        listGAITTWindowForPTQ.append(GAIList[i])
    for i in range(0 , len(listGAITTWindowForPTQ) , 1):
        gaiMean_ = gaiMean_ + listGAITTWindowForPTQ[i]
        countGaiMean = countGaiMean + 1
    gaiMean_ = gaiMean_ / countGaiMean
    gai_ = max(pastMaxAI_t1, gaiMean_)
    pastMaxAI = gai_
    gAImean = gai_
    return (listGAITTWindowForPTQ, pastMaxAI, listTTShootWindowForPTQ1, gAImean)
#%%CyML Model End%%