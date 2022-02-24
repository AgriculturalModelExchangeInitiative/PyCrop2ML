def STEMP(SOILPROP, SRAD, SW, TAVG, TMAX, XLAT, TAV, TAMP,NL, SRFTEMP, ST) :                                

      #USE ModuleDefs     #Definitions of constructed variable types, 
                         # which contain control information, soil
                         # parameters, hourly weather data.


      TMA = [None]*5
      BD =[None]*5
      DLAYR =[None]*5
      DLI =[None]*5
      DS=[None]*5, 
      DSI=[None]*5
      DSMID =[None]*5, 
      DUL =[None]*5, 
      LL =[None]*5
      ST =[None]*5
      SW =[None]*5
      SWI =[None]*5

      BD     = SOILPROP.BD     
      DLAYR  = SOILPROP.DLAYR  
      DS     = SOILPROP.DS     
      DUL    = SOILPROP.DUL     
      LL     = SOILPROP.LL     
      NLAYR  = SOILPROP.NLAYR  
      MSALB  = SOILPROP.MSALB   


#***********************************************************************
#***********************************************************************
#     Run initialization - run once per simulation
#***********************************************************************
#      IF (DYNAMIC .EQ. RUNINIT) THEN
#-----------------------------------------------------------------------
#***********************************************************************
#***********************************************************************
#     Seasonal initialization - run once per season
#***********************************************************************
#      ELSEIF (DYNAMIC .EQ. SEASINIT) THEN
      IF (DYNAMIC .EQ. SEASINIT) THEN
#-----------------------------------------------------------------------
      FILEIO  = CONTROL % FILEIO    
      LUNIO   = CONTROL % LUNIO    
      RUN     = CONTROL % RUN    
      RNMODE  = CONTROL % RNMODE

      IF (RUN .EQ. 1 .OR. INDEX('QF',RNMODE) .LE. 0) THEN

#        IF (ISWWAT .NE. 'N') THEN
##         Read inital soil water values from FILEIO 
##         (not yet done in WATBAL, so need to do here)
#          OPEN (LUNIO, FILE = FILEIO, STATUS = 'OLD', IOSTAT=ERRNUM)
#          IF (ERRNUM .NE. 0) CALL ERROR(ERRKEY,ERRNUM,FILEIO,0)
#          SECTION = '*INITI'
#          CALL FIND(LUNIO, SECTION, LNUM, FOUND) 
#          IF (FOUND .EQ. 0) CALL ERROR(SECTION, 42, FILEIO, LNUM)
#
##         Initial depth to water table (not currently used)
#          READ(LUNIO,'(40X,F6.0)',IOSTAT=ERRNUM) ICWD ; LNUM = LNUM + 1
#          IF (ERRNUM .NE. 0) CALL ERROR(ERRKEY,ERRNUM,FILEIO,LNUM)
#
##         These have not yet been initialized in SOILDYN, so do it here.
#          DO L = 1, NLAYR
#            READ(LUNIO,'(2X,2F6.0)',IOSTAT=ERRNUM) DSI(L), SWI(L)
#            LNUM = LNUM + 1
#            IF (ERRNUM .NE. 0) CALL ERROR(ERRKEY,ERRNUM,FILEIO,LNUM)
#            IF (SWI(L) .LT. LL(L)) SWI(L) = LL(L)
#          ENDDO
#
#          CLOSE (LUNIO)
#        ELSE
#          SWI = DUL
#          DSI = SOILPROP % DS
#        ENDIF

        SWI = SW
        DSI = SOILPROP % DS

        IF (XLAT .LT. 0.0) THEN
          HDAY =  20.0           #DOY (hottest) for southern hemisphere
        ELSE
          HDAY = 200.0           #DOY (hottest) for northern hemisphere
        ENDIF

        TBD = 0.0
        TLL = 0.0
        TSW = 0.0
        TDL = 0.0
        CUMDPT = 0.0
        DO L = 1, NLAYR
          IF (L .EQ. 1) THEN
            DLI(L) = DSI(L)
          ELSE
            DLI(L) = DSI(L) - DSI(L-1)
          ENDIF
          DSMID(L) = CUMDPT + DLI(L)* 5.0   #mm depth to midpt of lyr
          CUMDPT   = CUMDPT + DLI(L)*10.0   #mm profile depth 
          TBD = TBD + BD(L)  * DLI(L)       #CHP
          TLL = TLL + LL(L)  * DLI(L)
          TSW = TSW + SWI(L) * DLI(L)
          TDL = TDL + DUL(L) * DLI(L)
        END DO

        IF (ISWWAT .EQ. 'Y') THEN
          PESW = AMAX1(0.0, TSW - TLL)      #cm
        ELSE
          #If water not being simulated, use DUL as water content
          PESW = AMAX1(0.0, TDL - TLL)
        ENDIF

        ABD    = TBD / DSI(NLAYR)                   #CHP
        FX     = ABD/(ABD+686.0*EXP(-5.63*ABD))
        DP     = 1000.0 + 2500.0*FX
        WW     = 0.356  - 0.144*ABD
        B      = ALOG(500.0/DP)
        ALBEDO = MSALB

# CVF: difference in soil temperatures occur between different optimization
#     levels in compiled versions.
# Keep only 4 decimals. chp 06/03/03
#     Prevents differences between release & debug modes:
        DO I = 1, 5
          TMA(I) = NINT(TAVG*10000.)/10000.   #chp
        END DO
        ATOT = TMA(1) * 5.0

        DO L = 1, NLAYR
          ST(L) = TAVG
        END DO

        DO I = 1, 8
          CALL SOILT (
     &        ALBEDO, B, CUMDPT, DOY, DP, HDAY, NLAYR,    #Input
     &        PESW, SRAD, TAMP, TAV, TAVG, TMAX, WW, DSMID,#Input
     &        ATOT, TMA, SRFTEMP, ST)                     #Output
        END DO
      ENDIF

#     Print soil temperature data in STEMP.OUT
      CALL OPSTEMP(CONTROL, ISWITCH, DOY, SRFTEMP, ST, TAV, TAMP)
      
#***********************************************************************
#***********************************************************************
#     Daily rate calculations
#***********************************************************************
   
   
C  Determines soil temperature by layer
C-----------------------------------------------------------------------
C  Revision history
C  02/09/1933 PWW Header revision and minor changes.
C  12/09/1999 CHP Revisions for modular format.
C  01/01/2000 AJG Added surface temperature for the CENTURY-based
C                SOM/soil-N module.
C  01/14/2005 CHP Added METMP = 3: Corrected water content in temp. eqn.
#  12/07/2008 CHP Removed METMP -- use only corrected water content
C-----------------------------------------------------------------------
C  Called : STEMP
C  Calls  : None
C=======================================================================

      SUBROUTINE SOILT (
     &    ALBEDO, B, CUMDPT, DOY, DP, HDAY, NLAYR,    #Input
     &    PESW, SRAD, TAMP, TAV, TAVG, TMAX, WW, DSMID,#Input
     &    ATOT, TMA, SRFTEMP, ST)                     #Output
      
#     ------------------------------------------------------------------
      USE ModuleDefs     #Definitions of constructed variable types, 
                         # which contain control information, soil
                         # parameters, hourly weather data.
#     NL defined in ModuleDefs.for

      IMPLICIT  NONE
      SAVE

      INTEGER  K, L, DOY, NLAYR

      REAL ALBEDO, ALX, ATOT, B, CUMDPT, DD, DP, DT, FX
      REAL HDAY, PESW, SRAD, SRFTEMP, TA, TAMP, TAV, TAVG, TMAX
      REAL WC, WW, ZD
      REAL TMA(5)
      REAL DSMID(NL) 
      REAL ST(NL)

#-----------------------------------------------------------------------
      ALX    = (FLOAT(DOY) - HDAY) * 0.0174
      ATOT   = ATOT - TMA(5)

      DO K = 5, 2, -1
        TMA(K) = TMA(K-1)
      END DO

      TMA(1) = (1.0 - ALBEDO) * (TAVG + (TMAX - TAVG) * 
     &      SQRT(SRAD * 0.03)) + ALBEDO * TMA(1)

#     Prevents differences between release & debug modes:
#       Keep only 4 decimals. chp 06/03/03
      TMA(1) = NINT(TMA(1)*10000.)/10000.  #chp 
      ATOT = ATOT + TMA(1)

#-----------------------------------------------------------------------
#      #Water content function - compare old and new
#      SELECT CASE (METMP)
#      CASE ('O')  #Old, uncorrected equation
#        #OLD EQUATION (used in DSSAT v3.5 CROPGRO, SUBSTOR, CERES-Maize
#         WC = AMAX1(0.01, PESW) / (WW * CUMDPT * 10.0) 
#
#      CASE ('E')  #Corrected method (EPIC)
#        #NEW (CORRECTED) EQUATION
#        #chp 11/24/2003 per GH and LAH
        WC = AMAX1(0.01, PESW) / (WW * CUMDPT) * 10.0
#     frac =              cm   / (    mm     ) * mm/cm
        #WC (ratio)
        #PESW (cm)
        #WW (dimensionless)
        #CUMDPT (mm)
#      END SELECT
#-----------------------------------------------------------------------

      FX = EXP(B * ((1.0 - WC) / (1.0 + WC))**2)

      DD = FX * DP                                  #DD in mm
#     JWJ, GH 12/9/2008
#     Checked damping depths against values from literature and 
#       values are reasonable (after fix to WC equation).
#     Hillel, D. 2004. Introduction to Environmental Soil Physics.
#       Academic Press, San Diego, CA, USA.

      TA = TAV + TAMP * COS(ALX) / 2.0
      DT = ATOT / 5.0 - TA

      DO L = 1, NLAYR
        ZD    = -DSMID(L) / DD
        ST(L) = TAV + (TAMP / 2.0 * COS(ALX + ZD) + DT) * EXP(ZD)
        ST(L) = NINT(ST(L) * 1000.) / 1000.   #debug vs release fix
      END DO

#     Added: soil T for surface litter layer.
#     NB: this should be done by adding array element 0 to ST(L). Now
#     temporarily done differently.
      SRFTEMP = TAV + (TAMP / 2. * COS(ALX) + DT)
#     Note: ETPHOT calculates TSRF(3), which is surface temperature by 
#     canopy zone.  1=sunlit leaves.  2=shaded leaves.  3= soil.  Should
#     we combine these variables?  At this time, only SRFTEMP is used
#     elsewhere. - chp 11/27/01

#-----------------------------------------------------------------------
      RETURN
      END SUBROUTINE SOILT
C=======================================================================


#=======================================================================
# STEMP and SOILT Variable definitions - updated 2/15/2004
#=======================================================================
# ABD      Average bulk density for soil profile (g [soil] / cm3 [soil])
# ALBEDO   Reflectance of soil-crop surface (fraction)
# ALX       
# ATOT     Sum of TMA array (last 5 days soil temperature) (�C)
# B        Exponential decay factor (Parton and Logan) (in subroutine 
#            HTEMP) 
# BD(L)    Bulk density, soil layer L (g [soil] / cm3 [soil])
# CONTROL  Composite variable containing variables related to control 
#            and/or timing of simulation.    See Appendix A. 
# CUMDPT   Cumulative depth of soil profile (mm)
# DD        
# DLAYR(L) Thickness of soil layer L (cm)
# DOY      Current day of simulation (d)
# DP        
# DS(L)    Cumulative depth in soil layer L (cm)
# DSMID    Depth to midpoint of soil layer L (cm)
# DT        
# DUL(L)   Volumetric soil water content at Drained Upper Limit in soil 
#            layer L (cm3[water]/cm3[soil])
# ERRNUM   Error number for input 
# FILEIO   Filename for input file (e.g., IBSNAT35.INP) 
# FOUND    Indicator that good data was read from file by subroutine FIND 
#            (0 - End-of-file encountered, 1 - NAME was found) 
# FX        
# HDAY      
# ICWD     Initial water table depth (cm)
# ISWITCH  Composite variable containing switches which control flow of 
#            execution for model.  The structure of the variable 
#            (SwitchType) is defined in ModuleDefs.for. 
# ISWWAT   Water simulation control switch (Y or N) 
# LINC     Line number of input file 
# LL(L)    Volumetric soil water content in soil layer L at lower limit
#           (cm3 [water] / cm3 [soil])
# LNUM     Current line number of input file 
# LUNIO    Logical unit number for FILEIO 
# MSG      Text array containing information to be written to WARNING.OUT 
#            file. 
# MSGCOUNT Number of lines of message text to be sent to WARNING.OUT 
# NLAYR    Actual number of soil layers 
# PESW     Potential extractable soil water (= SW - LL) summed over root 
#            depth (cm)
# RNMODE    Simulation run mode (I=Interactive, A=All treatments, 
#             B=Batch mode, E=Sensitivity, D=Debug, N=Seasonal, Q=Sequence)
# RUN      Change in date between two observations for linear interpolation
# MSALB    Soil albedo with mulch and soil water effects (fraction)
# SECTION  Section name in input file 
# SOILPROP Composite variable containing soil properties including bulk 
#            density, drained upper limit, lower limit, pH, saturation 
#            water content.  Structure defined in ModuleDefs. 
# SRAD     Solar radiation (MJ/m2-d)
# SRFTEMP  Temperature of soil surface litter (�C)
# ST(L)    Soil temperature in soil layer L (�C)
# SW(L)    Volumetric soil water content in layer L
#           (cm3 [water] / cm3 [soil])
# SWI(L)   Initial soil water content (cm3[water]/cm3[soil])
# TA       Daily normal temperature (�C)
# TAMP     Amplitude of temperature function used to calculate soil 
#            temperatures (�C)
# TAV      Average annual soil temperature, used with TAMP to calculate 
#            soil temperature. (�C)
# TAVG     Average daily temperature (�C)
# TBD      Sum of bulk density over soil profile 
# TDL      Total water content of soil at drained upper limit (cm)
# TLL      Total soil water in the profile at the lower limit of 
#            plant-extractable water (cm)
# TMA(I)   Array of previous 5 days of average soil temperatures. (�C)
# TMAX     Maximum daily temperature (�C)
# TSW      Total soil water in profile (cm)
# WC        
# WW        
# XLAT     Latitude (deg.)
# YEAR     Year of current date of simulation 
# YRDOY    Current day of simulation (YYYYDDD)
# ZD        
#=======================================================================