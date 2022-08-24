#=======================================================================
#%%CyML Model End%%
#=======================================================================
#  SOILT_EPIC, Subroutine
#  Determines soil temperature by layer
#-----------------------------------------------------------------------
#  Revision history
#  02/09/1933 PWW Header revision and minor changes.
#  12/09/1999 CHP Revisions for modular format.
#  01/01/2000 AJG Added surface temperature for the CENTURY-based
#                SOM/soil-N module.
#  01/14/2005 CHP Added METMP = 3: Corrected water content in temp. eqn.
#  12/07/2008 CHP Removed METMP -- use only corrected water content
#  09/16/2010 CHP / MSC modified for EPIC soil temperature method.
#-----------------------------------------------------------------------
#  Called : STEMP
#  Calls  : None
#=======================================================================

def SOILT_EPIC(int NL,
         float B,
         float BCV,
         float CUMDPT,
         float DP,
         float DSMID[NL],
         int NLAYR,
         float PESW,
         float TAV,
         float TAVG,
         float TMAX,
         float TMIN,
         int WetDay,
         float WFT,
         float WW,
         float TMA[5],
         float X2_PREV,
         float ST[NL]):
    cdef int K , L 
    cdef float DD , FX 
    cdef float SRFTEMP 
    cdef float WC , ZD 
    cdef float X1 , X2 , X3 , F , X2_AVG 
    cdef float LAG 
    LAG = 0.5
    #-----------------------------------------------------------------------
    WC = max(0.01, PESW) / (WW * CUMDPT) * 10.0
    #     frac =              cm   / (    mm     ) * mm/cm
    #WC (ratio)
    #PESW (cm)
    #WW (dimensionless)
    #CUMDPT (mm)
    FX = exp(B * pow((1.0 - WC) / (1.0 + WC), 2))
    #DD in mm
    DD = FX * DP
    #=========================================================================
    #     Below this point - EPIC soil temperature routine differs from
    #       DSSAT original routine.
    #=========================================================================
    if WetDay > 0:
        #       Potter & Williams, 1994, Eqn. 2
        #       X2=WFT(MO)*(TX-TMN)+TMN
        X2 = WFT * (TAVG - TMIN) + TMIN
    else:
        #       Eqn 1
        #       X2=WFT(MO)*(TMX-TX)+TX+2.*((ST0/15.)**2-1.)
        #       Removed ST0 factor for now.
        X2 = WFT * (TMAX - TAVG) + TAVG + 2.
    TMA[1 - 1] = X2
    for K in range(5 , 2 - 1 , -1):
        TMA[K - 1] = TMA[K - 1 - 1]
    #Eqn 
    X2_AVG = sum(TMA) / 5.0
    #     Eqn 4
    #     X3=(1.-BCV)*X2+BCV*T(LID(2))
    X3 = (1. - BCV) * X2_AVG + (BCV * X2_PREV)
    #     DST0=AMIN1(X2,X3)
    SRFTEMP = min(X2_AVG, X3)
    #     Eqn 6 (partial)
    #     X1=AVT-X3
    X1 = TAV - X3
    for L in range(1 , NLAYR + 1 , 1):
        #Eqn 8
        ZD = DSMID[(L - 1)] / DD
        #       Eqn 7
        F = ZD / (ZD + exp(-.8669 - (2.0775 * ZD)))
        #       Eqn 6
        #       T(L)=PARM(15)*T(L)+XLG1*(F*X1+X3)
        ST[L - 1] = LAG * ST[(L - 1)] + ((1. - LAG) * (F * X1 + X3))
    X2_PREV = X2_AVG
    #=========================================================================
    #     old CSM code:
    #=========================================================================
    #
    #      TA = TAV + TAMP * COS(ALX) / 2.0
    #      DT = ATOT / 5.0 - TA
    #
    #      DO L = 1, NLAYR
    #        ZD    = -DSMID(L) / DD
    #        ST(L) = TAV + (TAMP / 2.0 * COS(ALX + ZD) + DT) * EXP(ZD)
    #        ST(L) = NINT(ST(L) * 1000.) / 1000.   !debug vs release fix
    #      END DO
    #
    #-----------------------------------------------------------------------
    return (TMA, X2_PREV, ST, SRFTEMP, X2_AVG)
