from datetime import datetime
from math import *
from soiltemperature.Stemp_epic import model_stemp_epic
def model_soiltemp(float BD[NL],
      float SRFTEMP,
      float TMA[5],
      float DEPIR,
      float BIOMAS,
      float TDL,
      int NL,
      float TAMP,
      float MULCHMASS,
      float TMAX,
      float SNOW,
      float RAIN,
      int NLAYR,
      float TAV,
      float TAVG,
      float TMIN,
      float SW[NL],
      float ST[NL],
      float DS[NL],
      float DLAYR[NL],
      float CUMDPT,
      int NDays,
      str ISWWAT,
      float DUL[NL],
      int WetDay[NL],
      float DSMID[NL],
      float LL[NL]):
    SRFTEMP, NDays, TDL, WetDay, ST, TMA = model_stemp_epic( NL,ISWWAT,BD,DLAYR,DS,DUL,LL,NLAYR,TAMP,RAIN,CUMDPT,DSMID,SW,TAVG,TMAX,TMIN,TAV,SRFTEMP,NDays,TDL,WetDay,ST,TMA,DEPIR,BIOMAS,MULCHMASS,SNOW)
    return SRFTEMP, NDays, TDL, WetDay, ST, TMA