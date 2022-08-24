cdef int I , L 
cdef float ABD , B 
cdef float DP , FX , PESW 
cdef float TBD , WW 
cdef float TLL , TSW 
cdef float X2_AVG 
cdef float WFT , BCV 
cdef float CV , BCV1 , BCV2 , X2_PREV 
cdef float SWI[NL]
SWI = SW
TBD = 0.0
TLL = 0.0
TSW = 0.0
TDL = 0.0
CUMDPT = 0.0
X2_PREV = 0.0
for L in range(1 , NLAYR + 1 , 1):
    #mm depth to midpt of lyr
    DSMID[L - 1] = CUMDPT + (DLAYR[(L - 1)] * 5.0)
    #mm profile depth 
    CUMDPT = CUMDPT + (DLAYR[(L - 1)] * 10.0)
    TBD = TBD + (BD[(L - 1)] * DLAYR[(L - 1)])
    TLL = TLL + (LL[(L - 1)] * DLAYR[(L - 1)])
    TSW = TSW + (SWI[(L - 1)] * DLAYR[(L - 1)])
    TDL = TDL + (DUL[(L - 1)] * DLAYR[(L - 1)])
if ISWWAT == "Y":
    #cm
    PESW = max(0.0, TSW - TLL)
else:
    #If water not being simulated, use DUL as water content
    PESW = max(0.0, TDL - TLL)
#CHP
ABD = TBD / DS[(NLAYR - 1)]
FX = ABD / (ABD + (686.0 * exp(-(5.63 * ABD))))
DP = 1000.0 + (2500.0 * FX)
WW = 0.356 - (0.144 * ABD)
B = log(500.0 / DP)
for I in range(1 , 5 + 1 , 1):
    #chp
    TMA[I - 1] = int(TAVG * 10000.) / 10000.
X2_AVG = TMA[(1 - 1)] * 5.0
for L in range(1 , NLAYR + 1 , 1):
    ST[L - 1] = TAVG
#       Save 30 day memory of:
#       WFT = fraction of wet days (rainfall + irrigation)
WFT = 0.1
WetDay = array('i', [0]*30)
NDays = 0
#       Soil cover function
#t/ha
CV = MULCHMASS / 1000.
BCV1 = CV / (CV + exp(5.3396 - (2.3951 * CV)))
BCV2 = SNOW / (SNOW + exp(2.303 - (0.2197 * SNOW)))
BCV = max(BCV1, BCV2)
for I in range(1 , 8 + 1 , 1):
    (TMA, X2_PREV, ST, SRFTEMP, X2_AVG) = SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, 0, WFT, WW, TMA, X2_PREV, ST)
