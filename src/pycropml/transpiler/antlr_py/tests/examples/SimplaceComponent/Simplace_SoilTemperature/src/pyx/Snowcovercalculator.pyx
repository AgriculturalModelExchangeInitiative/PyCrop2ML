import numpy 
from math import *
def model_snowcovercalculator(float cCarbonContent,
                              float iTempMax,
                              float iTempMin,
                              float iRadiation,
                              float iRAIN,
                              float iCropResidues,
                              float iPotentialSoilEvaporation,
                              float iLeafAreaIndex,
                              float iSoilTempArray[],
                              float Albedo,
                              float SnowWaterContent,
                              float SoilSurfaceTemperature,
                              int AgeOfSnow):
    """

    SnowCoverCalculator model
    Author: Gunther Krauss
    Reference: ('http://www.simplace.net/doc/simplace_modules/',)
    Institution: INRES Pflanzenbau, Uni Bonn
    ExtendedDescription: as given in the documentation
    ShortDescription: None

    """
    cdef float SnowIsolationIndex
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
    #b'/ convert from g/m^2 to kg/ha'
    tiCropResidues=iCropResidues * 10.0
    tiSoilTempArray=iSoilTempArray[0]
    #b'/TMEAN = Mean daily air temperature at 2 m (\xc3\x82\xc2\xb0C)'
    TMEAN=0.5 * (iTempMax + iTempMin)
    #b'/TAMPL = Amplitude of daily air temperature at 2 m (\xc3\x82\xc2\xb0C)'
    TAMPL=0.5 * (iTempMax - iTempMin)
    #b'/DST = Bare soil surface temperature (\xc3\x82\xc2\xb0C)'
    DST=TMEAN + (TAMPL * (iRadiation * (1 - Albedo) - 14) / 20)
    #b'/adding new precipitation to snow cover'
    if iRAIN > float(0) and (tiSoilTempArray < float(1) or SnowWaterContent > float(3) or SoilSurfaceTemperature < float(0)):
        SnowWaterContent=SnowWaterContent + iRAIN
    tSnowIsolationIndex=1.0
    if tiCropResidues < float(10):
        tSnowIsolationIndex=tiCropResidues / (tiCropResidues + exp(5.34 - (2.4 * tiCropResidues)))
    if SnowWaterContent < 1E-10:
        #b'/factor for no snow and crop cover'
        tSnowIsolationIndex=tSnowIsolationIndex * 0.85
        #b"/SoilSurfaceTemperature = Actual soil surface temperature (\xc3\x82\xc2\xb0C), iSoilTempArray = Yesterday's temperature in the first layer (\xc3\x82\xc2\xb0C)"
        tSoilSurfaceTemperature=0.5 * (DST + ((1 - tSnowIsolationIndex) * DST) + (tSnowIsolationIndex * tiSoilTempArray))
    else:
        #b'/coefficients based on EPIC SCRP(17) values from PARM0509.file'
        tSnowIsolationIndex=max(SnowWaterContent / (SnowWaterContent + exp(0.47 - (0.62 * SnowWaterContent))), tSnowIsolationIndex)
        #b"/SoilSurfaceTemperature = Actual soil surface temperature (\xc3\x82\xc2\xb0C), iSoilTempArray = Yesterday's temperature in the first layer (\xc3\x82\xc2\xb0C)"
        tSoilSurfaceTemperature=(1 - tSnowIsolationIndex) * DST + (tSnowIsolationIndex * tiSoilTempArray)
    if SnowWaterContent == float(0) and not (iRAIN > float(0) and tiSoilTempArray < float(1)):
        #b'/ no snow cover possible}'
        SnowWaterContent=float(0)
    else:
        #b'/EAJ = Soil cover index'
        EAJ=.5
        #b'/Equation from EPIC documentation'
        if SnowWaterContent < float(5):
            EAJ=exp(-max((0.4 * iLeafAreaIndex), (0.1 * (tiCropResidues + 0.1))))
        SNOWEVAPORATION=iPotentialSoilEvaporation * EAJ
        ageOfSnowFactor=AgeOfSnow / (AgeOfSnow + exp(5.34 - (2.395 * AgeOfSnow)))
        #b'/SNPKT is the snow pack temperature (\xc3\x82\xc2\xb0C)'
        SNPKT=.3333 * (2 * min(tSoilSurfaceTemperature, tiSoilTempArray) + iTempMax)
        if TMEAN > float(0):
            SNOWMELT=max(0, sqrt(iTempMax * iRadiation) * (1.52 + (.54 * ageOfSnowFactor * SNPKT)))
        else:
            SNOWMELT=float(0)
        if SNOWMELT + SNOWEVAPORATION > SnowWaterContent:
            SNOWMELT=SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
            SNOWEVAPORATION=SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent
        SnowWaterContent=SnowWaterContent - (SNOWMELT + SNOWEVAPORATION)
        #b'/no snow is minimum'
        if SnowWaterContent < float(0):
            SnowWaterContent=float(0)
        if SnowWaterContent < float(5):
            AgeOfSnow=0
        else:
            AgeOfSnow=AgeOfSnow + 1
    SnowIsolationIndex=tSnowIsolationIndex
    SoilSurfaceTemperature=tSoilSurfaceTemperature
    return  SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow, SnowIsolationIndex


def init_snowcovercalculator(float cCarbonContent,
                             float iTempMax,
                             float iTempMin,
                             float iRadiation,
                             float iRAIN,
                             float iCropResidues,
                             float iPotentialSoilEvaporation,
                             float iLeafAreaIndex,
                             float iSoilTempArray[]):
    cdef float Albedo
    cdef float SnowWaterContent=0.0
    cdef float SoilSurfaceTemperature=0.0
    cdef int AgeOfSnow=0
    Albedo = 0.0
    #b'/taken from experimental fit from Thomas Gaiser, 2000, n=35, R2=0.97'
    Albedo=0.0226 * log(cCarbonContent, 10) + 0.1502
    return  Albedo, SnowWaterContent, SoilSurfaceTemperature, AgeOfSnow
