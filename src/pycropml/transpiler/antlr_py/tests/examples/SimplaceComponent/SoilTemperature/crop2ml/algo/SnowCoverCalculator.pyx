cdef float tCV 
cdef float tTSOIL 
cdef float TMEAN 
cdef float TAMPL 
cdef float DST 
cdef float tDST0 
cdef float tBCV 
cdef float SNOWEVAPORATION 
cdef float SNOWMELT 
cdef float EAJ 
cdef float ageOfSnowFactor 
cdef float SNPKT 
#convert from g/m^2 to kg/ha
tCV = CV * 10.0
tTSOIL = TSOIL[0]
#MEAN = Mean daily air temperature at 2 m (Â°C)
TMEAN = 0.5 * (TMX + TMN)
#TAMPL = Amplitude of daily air temperature at 2 m (Â°C)
TAMPL = 0.5 * (TMX - TMN)
#DST = Bare soil surface temperature (Â°C)
DST = TMEAN + (TAMPL * (RA * (1 - Albedo) - 14) / 20)
#Adding new precipitation to snow cover
if PREC > 0 and (tTSOIL < 1 or SNOWC > 3 or DST0 < 0):
    SNOWC = SNOWC + PREC
tBCV = 1
if tCV < 10:
    tBCV = tCV / (tCV + exp(5.34 - (2.4 * tCV)))
if SNOWC < 1E-10:
    #Factor for no snow and crop cover
    tBCV = tBCV * 0.85
    #tDST0 = Actual soil surface temperature (Â°C), TSOIL = Yesterday's temperature in the first layer (Â°C)
    tDST0 = 0.5 * (DST + ((1 - tBCV) * DST) + (tBCV * tTSOIL))
else:
    #coefficients based on EPIC SCRP(17) values from PARM0509.file
    tBCV = max(SNOWC / (SNOWC + exp(0.47 - (0.62 * SNOWC))), tBCV)
    #DST0 = Actual soil surface temperature (Â°C), TSOIL = Yesterday's temperature in the first layer (Â°C)
    tDST0 = (1 - tBCV) * DST + (tBCV * tTSOIL)
if SNOWC == 0 and :
    #no snow cover possible}
    SNOWC = 0
else:
    #EAJ = Soil cover index
    EAJ = .5
    #Equation from EPIC documentation
    if SNOWC < 5:
        EAJ = exp(-max((0.4 * SLA), (0.1 * (tCV + 0.1))))
    SNOWEVAPORATION = PEVAP * EAJ
    ageOfSnowFactor = AgeOfSnow / (AgeOfSnow + exp(5.34 - (2.395 * AgeOfSnow)))
    #SNPKT is the snow pack temperature (Â°C)
    SNPKT = .3333 * (2 * min(tDST0, tTSOIL) + TMX)
    if TMEAN > 0:
        SNOWMELT = max(0, sqrt(TMX * RA) * (1.52 + (.54 * ageOfSnowFactor * SNPKT)))
    else:
        SNOWMELT = 0
    if SNOWMELT + SNOWEVAPORATION > SNOWC:
        SNOWMELT = SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * SNOWC
        SNOWEVAPORATION = SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * SNOWC
    SNOWC = SNOWC - SNOWMELT + SNOWEVAPORATION
    #No snow is minimum
    if SNOWC < 0:
        SNOWC = 0
    if SNOWC < 5:
        AgeOfSnow = 0
    else:
        AgeOfSnow = AgeOfSnow + 1
        SNOWC2 = SNOWC
BCV = tBCV
DST0 = tDST0