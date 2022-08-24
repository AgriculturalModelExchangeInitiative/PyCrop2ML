# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_gaimean(listTTShootWindowForPTQ1_t1,
         pastMaxAI_t1,
         listGAITTWindowForPTQ_t1,
         gAI,
         deltaTT,
         tTWindowForPTQ):
    """
     - Name: GAImean -Version: 001, -Time step: 1
     - Description:
                 * Title: GAImean model
                 * Author: LoÃ¯c Manceau
                 * Reference: ('',)
                 * Institution: INRA
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: listTTShootWindowForPTQ1_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: pastMaxAI_t1
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Maximum Leaf Area Index reached the current day
                               ** inputtype : variable
                               ** max : 5000.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
                 * name: listGAITTWindowForPTQ_t1
                               ** datatype : DOUBLELIST
                               ** default : 
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** inputtype : variable
                               ** max : 
                               ** min : 
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
                 * name: gAI
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Green Area Index of the day
                               ** inputtype : variable
                               ** max : 500.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
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
                               ** default : 0.0
                               ** description : Thermal Time window for average
                               ** inputtype : parameter
                               ** max : 5000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : Â°C d
     - outputs:
                 * name: gAImean
                               ** datatype : DOUBLE
                               ** description : Mean Green Area Index
                               ** max : 500.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
                 * name: pastMaxAI
                               ** datatype : DOUBLE
                               ** description : Maximum Leaf Area Index reached the current day
                               ** max : 5000.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
                 * name: listTTShootWindowForPTQ1
                               ** datatype : DOUBLELIST
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                               ** variablecategory : state
                 * name: listGAITTWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** max : 
                               ** min : 
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
    """

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
    return (gAImean, pastMaxAI, listTTShootWindowForPTQ1, listGAITTWindowForPTQ)