cdef floatlist  TTList
cdef floatlist  GAIList
cdef float SumTT 
cdef int count 
cdef float gai_ 
cdef float gaiMean_ 
cdef int countGaiMean 
cdef int i 
listTTShootWindowForPTQ1=[]
listGAITTWindowForPTQ=[]
TTList=[]
GAIList=[]
count=0
gai_=0.0
gaiMean_=0.0
countGaiMean=0
for i in range(0 , len(listTTShootWindowForPTQ1_t1) , 1):
    TTList.append(listTTShootWindowForPTQ1_t1[i])
    GAIList.append(listGAITTWindowForPTQ_t1[i])
TTList.append(deltaTT)
GAIList.append(gAI)
SumTT=sum(TTList)
while SumTT > tTWindowForPTQ:
    SumTT=SumTT - TTList[count]
    count=count + 1
for i in range(count , len(TTList) , 1):
    listTTShootWindowForPTQ1.append(TTList[i])
    listGAITTWindowForPTQ.append(GAIList[i])
for i in range(0 , len(listGAITTWindowForPTQ) , 1):
    gaiMean_=gaiMean_ + listGAITTWindowForPTQ[i]
    countGaiMean=countGaiMean + 1
gaiMean_=gaiMean_ / countGaiMean
gai_=max(pastMaxAI_t1, gaiMean_)
pastMaxAI=gai_
gAImean=gai_