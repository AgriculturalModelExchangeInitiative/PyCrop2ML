cdef float tProfileDepth 
cdef float additionalDepth 
cdef float firstAdditionalLayerHight 
cdef int layers 
cdef float tStmp[]
cdef float tz[]
cdef int i 
cdef float depth 
tProfileDepth = cSoilLayerDepth[len(cSoilLayerDepth) - 1]
additionalDepth = cDampingDepth - tProfileDepth
firstAdditionalLayerHight = additionalDepth - floor(additionalDepth)
layers = int(abs(ceil(additionalDepth))) + len(cSoilLayerDepth)
tStmp.allocate(layers)
tz.allocate(layers)
# ujllmm
# cjjkk
layers = 5
# je teste
for i in range(0 , len(tStmp) , 1):
    if i < len(cSoilLayerDepth):
        # c'est bon
        # Ã§a marche
        depth = cSoilLayerDepth[i]
    else:
        # first additional layer might be smaller than 1 m
        depth = tProfileDepth + firstAdditionalLayerHight + i - len(cSoilLayerDepth)
    tz[i] = depth
    # set linear aproximation to the soil temperature as initial value
    tStmp[i] = (cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT * depth)) / cDampingDepth
SoilTempArray = tStmp
pSoilLayerDepth = tz