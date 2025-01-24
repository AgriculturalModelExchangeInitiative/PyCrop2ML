cdef float tiCropResidues 
cdef float tiSoilTempArray 
cdef float TMEAN 
cdef float TAMPL 
cdef float DST 
cdef float tSoilSurfaceTemperature 
cdef float tSnowIsolationIndex 
cdef float SNOWEVAPORATION 
cdef float SNOWMELT 
cdef float EAJ 
cdef float ageOfSnowFactor 
cdef float SNPKT 
#/ convert from g/m^2 to kg/ha
tiCropResidues=iCropResidues * 10.0
tiSoilTempArray=iSoilTempArray[0]
#/TMEAN = Mean daily air temperature at 2 m (Â°C)
TMEAN=0.5 * (iTempMax + iTempMin)
#/TAMPL = Amplitude of daily air temperature at 2 m (Â°C)
TAMPL=0.5 * (iTempMax - iTempMin)
#/DST = Bare soil surface temperature (Â°C)
DST=TMEAN + (TAMPL * (iRadiation * (1 - Albedo) - 14) / 20)
#/adding new precipitation to snow cover
if iRAIN > float(0) and (tiSoilTempArray < float(1) or SnowWaterContent > float(3) or SoilSurfaceTemperature < float(0)):
    SnowWaterContent=SnowWaterContent + iRAIN
tSnowIsolationIndex=1.0
if tiCropResidues < float(10):
    tSnowIsolationIndex=tiCropResidues / (tiCropResidues + exp(5.34 - (2.4 * tiCropResidues)))
if SnowWaterContent < 1E-10:
    #/factor for no snow and crop cover
    tSnowIsolationIndex=tSnowIsolationIndex * 0.85
    #/SoilSurfaceTemperature = Actual soil surface temperature (Â°C), iSoilTempArray = Yesterday's temperature in the first layer (Â°C)
    tSoilSurfaceTemperature=0.5 * (DST + ((1 - tSnowIsolationIndex) * DST) + (tSnowIsolationIndex * tiSoilTempArray))
else:
    #/coefficients based on EPIC SCRP(17) values from PARM0509.file
    tSnowIsolationIndex=max(SnowWaterContent / (SnowWaterContent + exp(0.47 - (0.62 * SnowWaterContent))), tSnowIsolationIndex)
    #/SoilSurfaceTemperature = Actual soil surface temperature (Â°C), iSoilTempArray = Yesterday's temperature in the first layer (Â°C)
    tSoilSurfaceTemperature=(1 - tSnowIsolationIndex) * DST + (tSnowIsolationIndex * tiSoilTempArray)
if SnowWaterContent == float(0) and not (iRAIN > float(0) and tiSoilTempArray < float(1)):
    #/ no snow cover possible}
    SnowWaterContent=float(0)
else:
    #/EAJ = Soil cover index
    EAJ=.5
    #/Equation from EPIC documentation
    if SnowWaterContent < float(5):
        EAJ=exp(-max((0.4 * iLeafAreaIndex), (0.1 * (tiCropResidues + 0.1))))
    SNOWEVAPORATION=iPotentialSoilEvaporation * EAJ
    ageOfSnowFactor=AgeOfSnow / (AgeOfSnow + exp(5.34 - (2.395 * AgeOfSnow)))
    #/SNPKT is the snow pack temperature (Â°C)
    SNPKT=.3333 * (2 * min(tSoilSurfaceTemperature, tiSoilTempArray) + iTempMax)
    if TMEAN > float(0):
        SNOWMELT=max(0, sqrt(iTempMax * iRadiation) * (1.52 + (.54 * ageOfSnowFactor * SNPKT)))
    else:
        SNOWMELT=float(0)
    if SNOWMELT + SNOWEVAPORATION > SnowWaterContent:
        SNOWMELT=SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
        SNOWEVAPORATION=SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
    SnowWaterContent=SnowWaterContent - (SNOWMELT + SNOWEVAPORATION)
    #/no snow is minimum
    if SnowWaterContent < float(0):
        SnowWaterContent=float(0)
    if SnowWaterContent < float(5):
        AgeOfSnow=0
    else:
        AgeOfSnow=AgeOfSnow + 1
SnowIsolationIndex=tSnowIsolationIndex
SoilSurfaceTemperature=tSoilSurfaceTemperature