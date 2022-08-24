import numpy 
from math import *
def model_ptq(floatlist listGAITTWindowForPTQ,
              floatlist listTTShootWindowForPTQ_t1,
              floatlist listPARTTWindowForPTQ_t1,
              float pAR,
              float deltaTT,
              float tTWindowForPTQ,
              float kl):
    """

    PTQ model
    Author: Pierre Martre
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: 
    ShortDescription: 

    """
    cdef floatlist listPARTTWindowForPTQ
    cdef floatlist listTTShootWindowForPTQ
    cdef float ptq
    cdef floatlist  TTList
    cdef floatlist  PARList
    cdef int i 
    cdef int count 
    cdef float SumTT 
    cdef float parInt = 0.0
    cdef float TTShoot 
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
    return  listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq
