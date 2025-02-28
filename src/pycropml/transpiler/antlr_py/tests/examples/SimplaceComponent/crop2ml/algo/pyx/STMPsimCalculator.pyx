cdef float XLAG 
cdef float XLG1 
cdef float DP 
cdef float WC 
cdef float DD 
cdef float Z1 
cdef int i 
cdef float ZD 
cdef float RATE 
#/XLAG = LAG = Coefficient for weighting yesterday's soil temperature
XLAG=.8
#/XLG1 = Inverse of coefficient for weighting yesterday's soil temperature
XLG1=1 - XLAG
#/DP= Maximum damping depth (m)
DP=1 + (2.5 * cABD / (cABD + exp(6.53 - (5.63 * cABD))))
#/WC seems to be a water content related factor [cm3/g] to modify the damping depth ?
WC=0.001 * iSoilWaterContent / ((.356 - (.144 * cABD)) * cSoilLayerDepth[(len(cSoilLayerDepth) - 1)])
#/DD(t)= Damping depth (m), multiplied by 2 (20110628 TG) to increase damping depth
DD=exp(log(0.5 / DP) * ((1 - WC) / (1 + WC)) * 2) * DP
#/ DD could be also calculated from d = (2Dh /w )^0.5 (easy soilT, Nofziger et al.), where w = 2Pi/365 (d^-1)
#/and Dh is the thermal diffusivity (m^2 s^-l) with  ( Dh= K/Cs, Cs = volumetric heat capacity in J m^-3 K^-1, K=??)
#/Z1=Depth of the bottom of the previous soil layer, initialized with 0 (m)
Z1=float(0)
for i in range(0 , len(SoilTempArray) , 1):
    ZD=0.5 * (Z1 + pSoilLayerDepth[i]) / DD
    #/Factor of the depth in soil: Middle of depth of layer divided by damping depth
    RATE=ZD / (ZD + exp(-.8669 - (2.0775 * ZD))) * (cAVT - iSoilSurfaceTemperature)
    #/RATE = Rate of change of STMP(ISL) (Ã‚Â°C)
    SoilTempArray[i]=XLAG * SoilTempArray[i] + (XLG1 * (RATE + iSoilSurfaceTemperature))
    Z1=pSoilLayerDepth[i]