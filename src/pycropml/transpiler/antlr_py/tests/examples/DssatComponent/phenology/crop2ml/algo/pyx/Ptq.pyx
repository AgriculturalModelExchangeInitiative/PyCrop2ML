cdef floatlist  TTList
cdef floatlist  PARList
cdef int i 
cdef int count 
cdef float SumTT 
cdef float parInt 
cdef float TTShoot 
parInt = 0.0
for i in range(0 , len(listTTShootWindowForPTQ_t1) - 1 + 1 , 1):
    TTList.append(listTTShootWindowForPTQ_t1[i + 1 - 1])
    PARList.append(listPARTTWindowForPTQ_t1[i + 1 - 1])
TTList.append(deltaTT)
PARList.append(pAR)
SumTT = sum(TTList)
count = 0
while SumTT > tTWindowForPTQ:
    SumTT = SumTT - TTList[count + 1 - 1]
    count = count + 1
for i in range(count , len(TTList) - 1 + 1 , 1):
    listTTShootWindowForPTQ.append(TTList[i + 1 - 1])
    listPARTTWindowForPTQ.append(PARList[i + 1 - 1])
for i in range(0 , len(listTTShootWindowForPTQ) - 1 + 1 , 1):
    parInt = parInt + (listPARTTWindowForPTQ[(i + 1 - 1)] * (1 - exp(-kl * listGAITTWindowForPTQ[(i + 1 - 1)])))
TTShoot = sum(listTTShootWindowForPTQ)
ptq = parInt / TTShoot
return (listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq)