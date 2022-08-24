cdef int I , L 
cdef int NWetDays 
cdef float ABD , B 
cdef float DP , FX , PESW 
cdef float TBD , WW 
cdef float TLL , TSW 
cdef float X2_AVG 
cdef float WFT , BCV 
cdef float CV , BCV1 , BCV2 , X2_PREV 
TBD = 0.0
TLL = 0.0
TSW = 0.0
X2_PREV = 0.0
for L in range(1 , NLAYR + 1 , 1):
    TBD = TBD + (BD[(L - 1)] * DLAYR[(L - 1)])
    TDL = TDL + (DUL[(L - 1)] * DLAYR[(L - 1)])
    TLL = TLL + (LL[(L - 1)] * DLAYR[(L - 1)])
    TSW = TSW + (SW[(L - 1)] * DLAYR[(L - 1)])
#CHP
ABD = TBD / DS[(NLAYR - 1)]
FX = ABD / (ABD + (686.0 * exp(-(5.63 * ABD))))
#DP in mm
DP = 1000.0 + (2500.0 * FX)
#vol. fraction
WW = 0.356 - (0.144 * ABD)
B = log(500.0 / DP)
if ISWWAT == "Y":
    #cm
    PESW = max(0.0, TSW - TLL)
else:
    #If water not being simulated, use DUL as water content
    #cm
    PESW = max(0.0, TDL - TLL)
#     Save 30 day memory of:
#     WFT = fraction of wet days (rainfall + irrigation)
if NDays == 30:
    for I in range(1 , 29 + 1 , 1):
        WetDay[I - 1] = WetDay[I + 1 - 1]
else:
    NDays = NDays + 1
if RAIN + DEPIR > 1.E-6:
    WetDay[NDays - 1] = 1
else:
    WetDay[NDays - 1] = 0
NWetDays = sum(WetDay)
WFT = float(NWetDays) / float(NDays)
#     Soil cover function
#t/ha
CV = (BIOMAS + MULCHMASS) / 1000.
BCV1 = CV / (CV + exp(5.3396 - (2.3951 * CV)))
BCV2 = SNOW / (SNOW + exp(2.303 - (0.2197 * SNOW)))
BCV = max(BCV1, BCV2)
(TMA, X2_PREV, ST, SRFTEMP, X2_AVG) = SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, WetDay[NDays - 1], WFT, WW, TMA, X2_PREV, ST)
