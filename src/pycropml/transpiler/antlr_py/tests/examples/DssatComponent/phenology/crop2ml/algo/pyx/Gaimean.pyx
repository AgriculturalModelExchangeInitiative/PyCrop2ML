cdef floatlist TTList
cdef floatlist GAIList
cdef float SumTT 
cdef int count 
cdef float gai_ 
cdef float gaiMean_ 
cdef int countGaiMean 
cdef int i 
count = 0
gai_ = 0.0
gaiMean_ = 0.0
countGaiMean = 0
for i in range(0 , len(listTTShootWindowForPTQ1_t1) - 1 , 1):
    TTList.append(listTTShootWindowForPTQ1_t1[i + 1])
    GAIList.append(listGAITTWindowForPTQ_t1[i + 1])
TTList.append(deltaTT)
GAIList.append(gAI)
SumTT = sum(TTList)
while SumTT > tTWindowForPTQ:
    SumTT = SumTT - TTList[count + 1]
    count = count + 1
for i in range(count , len(TTList) - 1 , 1):
    listTTShootWindowForPTQ1.append(TTList[i + 1])
    listGAITTWindowForPTQ.append(GAIList[i + 1])
for i in range(0 , len(listGAITTWindowForPTQ) - 1 , 1):
    gaiMean_ = gaiMean_ + listGAITTWindowForPTQ[i + 1]
    countGaiMean = countGaiMean + 1
gaiMean_ = gaiMean_ / countGaiMean
gai_ = max(pastMaxAI_t1, gaiMean_)
pastMaxAI = gai_
gAImean = gai_