import numpy 
from math import *
def model_stmpsimcalculator(float cSoilLayerDepth[],
                            float cFirstDayMeanTemp,
                            float cAVT,
                            float cABD,
                            float cDampingDepth,
                            float iSoilWaterContent,
                            float iSoilSurfaceTemperature,
                            float SoilTempArray[],
                            float pSoilLayerDepth[]):
    """

    STMPsimCalculator model
    Author: Gunther Krauss
    Reference: ('http://www.simplace.net/doc/simplace_modules/',)
    Institution: INRES Pflanzenbau, Uni Bonn
    ExtendedDescription: as given in the documentation
    ShortDescription: None

    """
    cdef float XLAG 
    cdef float XLG1 
    cdef float DP 
    cdef float WC 
    cdef float DD 
    cdef float Z1 
    cdef int i 
    cdef float ZD 
    cdef float RATE 
    #b"/XLAG = LAG = Coefficient for weighting yesterday's soil temperature"
    XLAG=.8
    #b"/XLG1 = Inverse of coefficient for weighting yesterday's soil temperature"
    XLG1=1 - XLAG
    #b'/DP= Maximum damping depth (m)'
    DP=1 + (2.5 * cABD / (cABD + exp(6.53 - (5.63 * cABD))))
    #b'/WC seems to be a water content related factor [cm3/g] to modify the damping depth ?'
    WC=0.001 * iSoilWaterContent / ((.356 - (.144 * cABD)) * cSoilLayerDepth[(len(cSoilLayerDepth) - 1)])
    #b'/DD(t)= Damping depth (m), multiplied by 2 (20110628 TG) to increase damping depth'
    DD=exp(log(0.5 / DP) * ((1 - WC) / (1 + WC)) * 2) * DP
    #b'/ DD could be also calculated from d = (2Dh /w )^0.5 (easy soilT, Nofziger et al.), where w = 2Pi/365 (d^-1)'
    #b'/and Dh is the thermal diffusivity (m^2 s^-l) with  ( Dh= K/Cs, Cs = volumetric heat capacity in J m^-3 K^-1, K=??)'
    #b'/Z1=Depth of the bottom of the previous soil layer, initialized with 0 (m)'
    Z1=float(0)
    for i in range(0 , len(SoilTempArray) , 1):
        ZD=0.5 * (Z1 + pSoilLayerDepth[i]) / DD
        #b'/Factor of the depth in soil: Middle of depth of layer divided by damping depth'
        RATE=ZD / (ZD + exp(-.8669 - (2.0775 * ZD))) * (cAVT - iSoilSurfaceTemperature)
        #b'/RATE = Rate of change of STMP(ISL) (\xc3\x83\xe2\x80\x9a\xc3\x82\xc2\xb0C)'
        SoilTempArray[i]=XLAG * SoilTempArray[i] + (XLG1 * (RATE + iSoilSurfaceTemperature))
        Z1=pSoilLayerDepth[i]
    return  SoilTempArray


def init_stmpsimcalculator(float cSoilLayerDepth[],
                           float cFirstDayMeanTemp,
                           float cAVT,
                           float cABD,
                           float cDampingDepth,
                           float iSoilWaterContent,
                           float iSoilSurfaceTemperature):
    cdef float SoilTempArray[]
    cdef float pSoilLayerDepth[]
    SoilTempArray = None
    pSoilLayerDepth = None
    cdef float tProfileDepth 
    cdef float additionalDepth 
    cdef float firstAdditionalLayerHight 
    cdef int layers 
    cdef float tStmp[]
    cdef float tz[]
    cdef int i 
    cdef float depth 
    tProfileDepth=cSoilLayerDepth[len(cSoilLayerDepth) - 1]
    additionalDepth=cDampingDepth - tProfileDepth
    firstAdditionalLayerHight=additionalDepth - float(floor(additionalDepth))
    layers=int(abs(float(ceil(additionalDepth)))) + len(cSoilLayerDepth)
    tStmp.allocate(layers)
    tz.allocate(layers)
    for i in range(0 , len(tStmp) , 1):
        if i < len(cSoilLayerDepth):
            depth=cSoilLayerDepth[i]
        else:
            #b'/first additional layer might be smaller than 1 m'
            depth=tProfileDepth + firstAdditionalLayerHight + i - len(cSoilLayerDepth)
        tz[i]=depth
        #b'/set linear aproximation to the soil temperature as initial value'
        tStmp[i]=(cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT * depth)) / cDampingDepth
    SoilTempArray=tStmp
    pSoilLayerDepth=tz
    return  SoilTempArray, pSoilLayerDepth
