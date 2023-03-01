import numpy 
from math import *
def model_ptq(float deltaTT,
              floatlist listPARTTWindowForPTQ_t1,
              floatlist listGAITTWindowForPTQ,
              float pAR,
              floatlist listTTShootWindowForPTQ_t1,
              float kl,
              float tTWindowForPTQ):
    """

    PTQ model
    Author: Pierre Martre
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: Calculate Photothermal Quaotient 
    ShortDescription: None

    """
    cdef floatlist listTTShootWindowForPTQ
    cdef floatlist listPARTTWindowForPTQ
    cdef float ptq
    cdef floatlist  TTList
    cdef floatlist  PARList
    cdef int i 
    cdef int count 
    cdef float SumTT 
    cdef float parInt 
    cdef float TTShoot 
    listPARTTWindowForPTQ=[]
    listTTShootWindowForPTQ=[]
    TTList=[]
    PARList=[]
    parInt=0.0
    for i in range(0 , len(listTTShootWindowForPTQ_t1) , 1):
        TTList.append(listTTShootWindowForPTQ_t1[i])
        PARList.append(listPARTTWindowForPTQ_t1[i])
    TTList.append(deltaTT)
    PARList.append(pAR)
    SumTT=sum(TTList)
    count=0
    while SumTT > tTWindowForPTQ:
        SumTT=SumTT - TTList[count]
        count=count + 1
    for i in range(count , len(TTList) , 1):
        listTTShootWindowForPTQ.append(TTList[i])
        listPARTTWindowForPTQ.append(PARList[i])
    for i in range(0 , len(listTTShootWindowForPTQ) , 1):
        parInt=parInt + (listPARTTWindowForPTQ[i] * (1 - exp(-kl * listGAITTWindowForPTQ[i])))
    TTShoot=sum(listTTShootWindowForPTQ)
    ptq=parInt / TTShoot
    return  listTTShootWindowForPTQ, listPARTTWindowForPTQ, ptq


