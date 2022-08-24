C=======================================================================
C  COPYRIGHT 1998-2010 The University of Georgia, Griffin, Georgia
C                      University of Florida, Gainesville, Florida
C                      Iowa State University, Ames, Iowa
C                      International Center for Soil Fertility and 
C                       Agricultural Development, Muscle Shoals, Alabama
C                      University of Guelph, Guelph, Ontario
C  ALL RIGHTS RESERVED
C=======================================================================
C=======================================================================
C  STEMP_EPIC, Subroutine
C
C  Determines soil temperature by layer
C-----------------------------------------------------------------------
C  Revision history
C  12/01/1980     Originally based on EPIC soil temperature routines
!  09/16/2010 CHP / MSC modified for EPIC soil temperature method.
!     Cite Potter & Williams here
C-----------------------------------------------------------------------
C  Called : Main
C  Calls  : SOILT
C=======================================================================
!%%CyML Model Begin%%
      SUBROUTINE STEMP_EPIC(CONTROL, ISWITCH,  
     &    SOILPROP, SW, TAVG, TMAX, TMIN, TAV, WEATHER,   !Input
     &    SRFTEMP, ST)                                    !Output

C-----------------------------------------------------------------------
      USE ModuleDefs
      USE ModuleData

      IMPLICIT  NONE
      SAVE
!%%CyML Ignore Begin%%
      CHARACTER*1  RNMODE
      INTEGER DYNAMIC
      INTEGER RUN, YRDOY, YEAR
      INTEGER ERRNUM, FOUND, LNUM, LUNIO
      CHARACTER*6  SECTION
      CHARACTER*6, PARAMETER :: ERRKEY = "EPIC STEMP"
      CHARACTER*30 FILEIO
      CHARACTER*78 MSG(3)
!%%CyML Ignore End%%

      CHARACTER*1 ISWWAT
      INTEGER DOY, I, L, NLAYR
      INTEGER WetDay(30), NDays, NWetDays
      REAL ABD, B, CUMDPT 
      REAL DP, FX, ICWD, PESW, SRFTEMP 
      REAL TAV, TAMP, TAVG, TBD, TMAX, TMIN, WW
      REAL TDL, TLL, TSW
      REAL TMA(5), X2_AVG
      REAL DEPIR, WFT, BCV, RAIN, BIOMAS, MULCHMASS
      REAL SNOW, CV, BCV1, BCV2
      REAL, DIMENSION(NL) :: BD, DLAYR, DS, DUL, LL, ST, SW, SWI, DSMID

!-----------------------------------------------------------------------
!%%CyML Ignore Begin%%
      TYPE (ControlType) CONTROL
!%%CyML Ignore End%%

      TYPE (SoilType)    SOILPROP
      TYPE (SwitchType)  ISWITCH
      TYPE (WeatherType) WEATHER

!     Transfer values from constructed data types into local variables.
!%%CyML Ignore Begin%%
      DYNAMIC = CONTROL % DYNAMIC  
      YRDOY   = CONTROL % YRDOY  
!%%CyML Ignore End%%  


      ISWWAT = ISWITCH % ISWWAT
!      METMP  = ISWITCH % METMP
      BD     = SOILPROP % BD     
      DLAYR  = SOILPROP % DLAYR  
      DS     = SOILPROP % DS     
      DUL    = SOILPROP % DUL     
      LL     = SOILPROP % LL     
      NLAYR  = SOILPROP % NLAYR  

      TAMP = WEATHER % TAMP

!-----------------------------------------------------------------------
!%%CyML Ignore Begin%%
      CALL YR_DOY(YRDOY, YEAR, DOY)
!%%CyML Ignore End%%

!***********************************************************************
!***********************************************************************
!     Run initialization - run once per simulation
!***********************************************************************
!      IF (DYNAMIC .EQ. RUNINIT) THEN
!-----------------------------------------------------------------------
!***********************************************************************
!***********************************************************************
!     Seasonal initialization - run once per season
!***********************************************************************
!      ELSEIF (DYNAMIC .EQ. SEASINIT) THEN
      IF (DYNAMIC .EQ. SEASINIT) THEN
!-----------------------------------------------------------------------
      FILEIO  = CONTROL % FILEIO    
      LUNIO   = CONTROL % LUNIO    
      RUN     = CONTROL % RUN    
      RNMODE  = CONTROL % RNMODE

      IF (RUN .EQ. 1 .OR. INDEX('QF',RNMODE) .LE. 0) THEN

!        IF (ISWWAT .NE. 'N') THEN
!!         Read inital soil water values from FILEIO 
!!         (not yet done in WATBAL, so need to do here)
!          OPEN (LUNIO, FILE = FILEIO, STATUS = 'OLD', IOSTAT=ERRNUM)
!          IF (ERRNUM .NE. 0) CALL ERROR(ERRKEY,ERRNUM,FILEIO,0)
!          SECTION = '*INITI'
!          CALL FIND(LUNIO, SECTION, LNUM, FOUND) 
!          IF (FOUND .EQ. 0) CALL ERROR(SECTION, 42, FILEIO, LNUM)
!
!!         Initial depth to water table (not currently used)
!          READ(LUNIO,'(40X,F6.0)',IOSTAT=ERRNUM) ICWD ; LNUM = LNUM + 1
!          IF (ERRNUM .NE. 0) CALL ERROR(ERRKEY,ERRNUM,FILEIO,LNUM)
!
!          DO L = 1, NLAYR
!            READ(LUNIO,'(9X,F5.3)',IOSTAT=ERRNUM) SWI(L)
!            LNUM = LNUM + 1
!            IF (ERRNUM .NE. 0) CALL ERROR(ERRKEY,ERRNUM,FILEIO,LNUM)
!            IF (SWI(L) .LT. LL(L)) SWI(L) = LL(L)
!          ENDDO
!
!          CLOSE (LUNIO)
!        ELSE
!          SWI = DUL
!        ENDIF
!%%CyML Init Begin%%
        SWI = SW
        
        TBD = 0.0
        TLL = 0.0
        TSW = 0.0
        TDL = 0.0
        CUMDPT = 0.0
        DO L = 1, NLAYR
          DSMID(L) = CUMDPT + DLAYR(L)* 5.0   !mm depth to midpt of lyr
          CUMDPT   = CUMDPT + DLAYR(L)*10.0   !mm profile depth 
          TBD = TBD + BD(L)  * DLAYR(L)       
          TLL = TLL + LL(L)  * DLAYR(L)
          TSW = TSW + SWI(L) * DLAYR(L)
          TDL = TDL + DUL(L) * DLAYR(L)
        END DO

        IF (ISWWAT .EQ. 'Y') THEN
          PESW = AMAX1(0.0, TSW - TLL)      !cm
        ELSE
          !If water not being simulated, use DUL as water content
          PESW = AMAX1(0.0, TDL - TLL)
        ENDIF

        ABD    = TBD / DS(NLAYR)                   !CHP
        FX     = ABD/(ABD+686.0*EXP(-5.63*ABD))
        DP     = 1000.0 + 2500.0*FX
        WW     = 0.356  - 0.144*ABD
        B      = ALOG(500.0/DP)

        DO I = 1, 5
          TMA(I) = NINT(TAVG*10000.)/10000.   !chp
        END DO
        X2_AVG = TMA(1) * 5.0

        DO L = 1, NLAYR
          ST(L) = TAVG
        END DO

!       Save 30 day memory of:
!       WFT = fraction of wet days (rainfall + irrigation)
        WFT = 0.1
        WetDay = 0
        NDays = 0
      
!       Soil cover function
!%%CyML Ignore Begin%%
        CALL GET('ORGC' ,'MULCHMASS',MULCHMASS)   !kg/ha
        CALL GET('WATER','SNOW'     , SNOW)       !mm
!%%CyML Ignore End%%
      
        CV = (MULCHMASS) / 1000.         !t/ha
        BCV1 = CV / (CV + EXP(5.3396 - 2.3951 * CV))
        BCV2 = SNOW / (SNOW + EXP(2.303 - 0.2197 * SNOW))
        BCV = MAX(BCV1, BCV2)

        DO I = 1, 8
          CALL SOILT_EPIC (
     &    B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV,    !Input
     &    TAVG, TMAX, TMIN, 0, WFT, WW,                   !Input
     &    TMA, SRFTEMP, ST, X2_AVG)                       !Output
        END DO
!%%CyML Init End%%
      ENDIF

!%%CyML Ignore Begin%%
!     Print soil temperature data in STEMP.OUT
      CALL OPSTEMP(CONTROL, ISWITCH, DOY, SRFTEMP, ST, TAV, TAMP)

      MSG(1) = "Running EPIC soil temperature routine."
      MSG(2) = "Start simulation at least 30 days early to initialize"
      MSG(3) = "  soil temperature parameters."
!%%CyML Ignore End%%


! - ASKE ORIGINAL START      
!      CALL WARNING(3,ERRKEY,MSG)
! - ASKE ORIGINAL END
!***********************************************************************
!***********************************************************************
!     Daily rate calculations
!***********************************************************************
      ELSEIF (DYNAMIC .EQ. RATE) THEN
!-----------------------------------------------------------------------
!%%CyML Rate Begin%%
      TBD = 0.0
      TLL = 0.0
      TSW = 0.0
      DO L = 1, NLAYR
        TBD = TBD + BD(L) * DLAYR(L) 
        TDL = TDL + DUL(L)* DLAYR(L)
        TLL = TLL + LL(L) * DLAYR(L)
        TSW = TSW + SW(L) * DLAYR(L)
      ENDDO

      ABD    = TBD / DS(NLAYR)                    !CHP
      FX     = ABD/(ABD+686.0*EXP(-5.63*ABD))
      DP     = 1000.0 + 2500.0*FX   !DP in mm
      WW     = 0.356  - 0.144*ABD   !vol. fraction
      B      = ALOG(500.0/DP)

      IF (ISWWAT .EQ. 'Y') THEN
        PESW = MAX(0.0, TSW - TLL)      !cm
      ELSE
        !If water not being simulated, use DUL as water content
        PESW = AMAX1(0.0, TDL - TLL)    !cm
      ENDIF

!     Save 30 day memory of:
!     WFT = fraction of wet days (rainfall + irrigation)
      RAIN = WEATHER % RAIN
!%%CyML Ignore Begin%%
      CALL GET('MGMT','DEPIR',DEPIR)
!%%CyML Ignore End%%
      IF (NDays == 30) THEN
        DO i = 1, 29
          WetDay(i) = WetDay(i+1)
        ENDDO
      ELSE
        NDays = NDays + 1
      ENDIF
      IF (RAIN + DEPIR > 1.E-6) THEN
        WetDay(NDays) = 1
      ELSE
        WetDay(NDays) = 0 
      ENDIF
      NWetDays = SUM(WetDay)
      WFT = Float(NWetDays) / float(NDays)

!     Soil cover function
!%%CyML Ignore Begin%%
      CALL GET('PLANT','BIOMAS'   ,BIOMAS)      !kg/ha
      CALL GET('ORGC' ,'MULCHMASS',MULCHMASS)   !kg/ha
      CALL GET('WATER','SNOW'     , SNOW)       !mm
!%%CyML Ignore End%%

      CV = (BIOMAS + MULCHMASS) / 1000.         !t/ha
      BCV1 = CV / (CV + EXP(5.3396 - 2.3951 * CV))
      BCV2 = SNOW / (SNOW + EXP(2.303 - 0.2197 * SNOW))
      BCV = MAX(BCV1, BCV2)

      CALL SOILT_EPIC (
     &    B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV,    !Input
     &    TAVG, TMAX, TMIN, WetDay(NDays), WFT, WW,       !Input
     &    TMA, SRFTEMP, ST, X2_AVG)                       !Output
!%%CyML Rate End%%

!***********************************************************************
!***********************************************************************
!     Output & Seasonal summary
!***********************************************************************
!%%CyML Ignore Begin%%
      ELSEIF (DYNAMIC .EQ. OUTPUT .OR. DYNAMIC .EQ. SEASEND) THEN
!-----------------------------------------------------------------------
      CALL OPSTEMP(CONTROL, ISWITCH, DOY, SRFTEMP, ST, TAV, TAMP)

!***********************************************************************
!***********************************************************************
!     END OF DYNAMIC IF CONSTRUCT
!%%CyML Ignore End%%
!***********************************************************************
      ENDIF
!***********************************************************************
      RETURN
      END SUBROUTINE STEMP_EPIC
!=======================================================================
!%%CyML Model End%%

C=======================================================================
C  SOILT_EPIC, Subroutine
C  Determines soil temperature by layer
C-----------------------------------------------------------------------
C  Revision history
C  02/09/1933 PWW Header revision and minor changes.
C  12/09/1999 CHP Revisions for modular format.
C  01/01/2000 AJG Added surface temperature for the CENTURY-based
C                SOM/soil-N module.
C  01/14/2005 CHP Added METMP = 3: Corrected water content in temp. eqn.
!  12/07/2008 CHP Removed METMP -- use only corrected water content
!  09/16/2010 CHP / MSC modified for EPIC soil temperature method.
C-----------------------------------------------------------------------
C  Called : STEMP
C  Calls  : None
C=======================================================================

      SUBROUTINE SOILT_EPIC (
     &    B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV,    !Input
     &    TAVG, TMAX, TMIN, WetDay, WFT, WW,              !Input
     &    TMA, SRFTEMP, ST, X2_AVG)                       !Output
      
!     ------------------------------------------------------------------
      USE ModuleDefs
      IMPLICIT  NONE
      SAVE

      INTEGER  K, L, NLAYR, WetDay

      REAL B, CUMDPT, DD, DP, FX
      REAL PESW, SRFTEMP, TAV, TAVG, TMAX
      REAL WC, WW, ZD
      REAL TMA(5)
      REAL DSMID(NL) 
      REAL ST(NL)
      REAL X1, X2, X3, F, WFT, BCV, TMIN, X2_AVG, X2_PREV
      REAL LAG
      PARAMETER (LAG=0.5)

!-----------------------------------------------------------------------
      WC = AMAX1(0.01, PESW) / (WW * CUMDPT) * 10.0
!     frac =              cm   / (    mm     ) * mm/cm
        !WC (ratio)
        !PESW (cm)
        !WW (dimensionless)
        !CUMDPT (mm)

      FX = EXP(B * ((1.0 - WC) / (1.0 + WC))**2)
      DD = FX * DP                                  !DD in mm

!=========================================================================
!     Below this point - EPIC soil temperature routine differs from
!       DSSAT original routine.
!=========================================================================

      IF (WetDay > 0) THEN
!       Potter & Williams, 1994, Eqn. 2
!       X2=WFT(MO)*(TX-TMN)+TMN
        X2=WFT*(TAVG-TMIN)+TMIN
      ELSE
!       Eqn 1
!       X2=WFT(MO)*(TMX-TX)+TX+2.*((ST0/15.)**2-1.)
!       Removed ST0 factor for now.
        X2=WFT*(TMAX-TAVG)+TAVG+2.
      ENDIF

      TMA(1) = X2
      DO K = 5, 2, -1
        TMA(K) = TMA(K-1)
      END DO
      X2_AVG = SUM(TMA) / 5.0     !Eqn 

!     Eqn 4
!     X3=(1.-BCV)*X2+BCV*T(LID(2))
      X3=(1.-BCV)*X2_AVG+BCV*X2_PREV

!     DST0=AMIN1(X2,X3)
      SRFTEMP=AMIN1(X2_AVG,X3)

!     Eqn 6 (partial)
!     X1=AVT-X3
      X1=TAV-X3

      DO L = 1, NLAYR
        ZD    = DSMID(L) / DD  !Eqn 8
!       Eqn 7
        F=ZD/(ZD+EXP(-.8669-2.0775*ZD))
!       Eqn 6
!       T(L)=PARM(15)*T(L)+XLG1*(F*X1+X3)
        ST(L)=LAG*ST(L)+(1.-LAG)*(F*X1+X3)
      END DO

      X2_PREV = X2_AVG

!=========================================================================
!     old CSM code:
!=========================================================================
!
!      TA = TAV + TAMP * COS(ALX) / 2.0
!      DT = ATOT / 5.0 - TA
!
!      DO L = 1, NLAYR
!        ZD    = -DSMID(L) / DD
!        ST(L) = TAV + (TAMP / 2.0 * COS(ALX + ZD) + DT) * EXP(ZD)
!        ST(L) = NINT(ST(L) * 1000.) / 1000.   !debug vs release fix
!      END DO
!
!-----------------------------------------------------------------------

      RETURN
      END SUBROUTINE SOILT_EPIC
C=======================================================================


!=======================================================================
! STEMP and SOILT Variable definitions - updated 2/15/2004
!=======================================================================
! ABD      Average bulk density for soil profile (g [soil] / cm3 [soil])
! B        Exponential decay factor (Parton and Logan) (in subroutine 
!            HTEMP) 
! BD(L)    Bulk density, soil layer L (g [soil] / cm3 [soil])
! CONTROL  Composite variable containing variables related to control 
!            and/or timing of simulation.    See Appendix A. 
! CUMDPT   Cumulative depth of soil profile (mm)
! DD        
! DLAYR(L) Thickness of soil layer L (cm)
! DP        
! DS(L)    Cumulative depth in soil layer L (cm)
! DSMID    Depth to midpoint of soil layer L (cm)
! DUL(L)   Volumetric soil water content at Drained Upper Limit in soil 
!            layer L (cm3[water]/cm3[soil])
! ERRNUM   Error number for input 
! FILEIO   Filename for input file (e.g., IBSNAT35.INP) 
! FOUND    Indicator that good data was read from file by subroutine FIND 
!            (0 - End-of-file encountered, 1 - NAME was found) 
! FX        
! ICWD     Initial water table depth (cm)
! ISWITCH  Composite variable containing switches which control flow of 
!            execution for model.  The structure of the variable 
!            (SwitchType) is defined in ModuleDefs.for. 
! ISWWAT   Water simulation control switch (Y or N) 
! LINC     Line number of input file 
! LL(L)    Volumetric soil water content in soil layer L at lower limit
!           (cm3 [water] / cm3 [soil])
! LNUM     Current line number of input file 
! LUNIO    Logical unit number for FILEIO 
! MSG      Text array containing information to be written to WARNING.OUT 
!            file. 
! MSGCOUNT Number of lines of message text to be sent to WARNING.OUT 
! NLAYR    Actual number of soil layers 
! PESW     Potential extractable soil water (= SW - LL) summed over root 
!            depth (cm)
! RNMODE    Simulation run mode (I=Interactive, A=All treatments, 
!             B=Batch mode, E=Sensitivity, D=Debug, N=Seasonal, Q=Sequence)
! RUN      Change in date between two observations for linear interpolation
! SECTION  Section name in input file 
! SOILPROP Composite variable containing soil properties including bulk 
!            density, drained upper limit, lower limit, pH, saturation 
!            water content.  Structure defined in ModuleDefs. 
! SRFTEMP  Temperature of soil surface litter (�C)
! ST(L)    Soil temperature in soil layer L (�C)
! SW(L)    Volumetric soil water content in layer L
!           (cm3 [water] / cm3 [soil])
! SWI(L)   Initial soil water content (cm3[water]/cm3[soil])
! TAV      Average annual soil temperature, used with TAMP to calculate 
!            soil temperature. (�C)
! TAVG     Average daily temperature (�C)
! TBD      Sum of bulk density over soil profile 
! TDL      Total water content of soil at drained upper limit (cm)
! TLL      Total soil water in the profile at the lower limit of 
!            plant-extractable water (cm)
! TMA(I)   Array of previous 5 days of average soil temperatures. (�C)
! TMAX     Maximum daily temperature (�C)
! TSW      Total soil water in profile (cm)
! WC        
! WW        
! YEAR     Year of current date of simulation 
! YRDOY    Current day of simulation (YYYYDDD)
! ZD        
!=======================================================================

      PROGRAM ASKEE

      USE ModuleDefs
      USE ModuleData

      IMPLICIT NONE
C-----------------------------------------------------------------------
      CHARACTER*1   ANS,RNMODE,BLANK,UPCASE,ISWWAT
      CHARACTER*6   ERRKEY,FINDCH,TRNARG
      CHARACTER*30  FILEIO
      
      REAL ABD, ALBEDO, ATOT, B, CUMDPT 
      REAL DP, FX, HDAY, ICWD, PESW, MSALB, SRAD, SRFTEMP 
      REAL TAMP, TAV, TAVG, TBD, TMAX, TMIN, XLAT, WW
      REAL TDL, TLL, TSW
      REAL TMA(5)
      REAL BIOMAS,DEPIR,MULCHMASS,SNOW
      REAL, DIMENSION(NL) :: BD, DLAYR, DLI, DS, DSI, DSMID, DUL, LL, 
     &      ST, SW, SWI
     
      INTEGER DOY, DYNAMIC, I, L, NLAYR

      PARAMETER (ERRKEY = 'ASKEE ')      
      PARAMETER (BLANK  = ' ')

C     Define constructed variable types based on definitions in
C     ModuleDefs.for.

C     The variable "CONTROL" is of type "ControlType".
      TYPE (ControlType) CONTROL

C     The variable "ISWITCH" is of type "SwitchType".
      TYPE (SwitchType) ISWITCH
      
      TYPE (SoilType) SOILPROP
      
      TYPE (WeatherType) WEATHER
      

C*********************************************************************** 
C*********************************************************************** 
C     RUN INITIALIZATION
C***********************************************************************

      CONTROL % FILEIO  = FILEIO
      CONTROL % ERRCODE = 0
      CONTROL % DYNAMIC = 1
      CONTROL % RUN     = 1
      CONTROL % RNMODE  = 'B'
      CONTROL % YRDOY   = 2021100
      
      ISWITCH % ISWWAT = 'Y'
      
      SOILPROP % BD    = 1.6
      SOILPROP % DLAYR = 10.0
      SOILPROP % DS(1) = 10.0
      SOILPROP % DS(2) = 20.0 
      SOILPROP % DS(3) = 30.0 
      SOILPROP % DS(4) = 40.0 
      SOILPROP % DUL   = 0.3 
      SOILPROP % LL    = 0.2 
      SOILPROP % NLAYR = 4 
      SOILPROP % MSALB = 0.13
      
      
      
      SRAD    = 20.0 
      SW      = 0.2
      TAVG    = 25.0
      TMAX    = 30.0
      TMIN    = 20.0
      XLAT    = 28.0
      TAV     = 20.0
      !TAMP    = 10.0
      
      WEATHER % TAMP = 10.0
      WEATHER % RAIN = 0.0
      
      MULCHMASS = 0.0
      CALL PUT('ORGC' ,'MULCHMASS',MULCHMASS)   !kg/ha
      
      SNOW = 0.0
      CALL PUT('WATER','SNOW'     , SNOW)       !mm
      
      DEPIR = 0.0
      CALL PUT('MGMT','DEPIR',DEPIR)
      
      BIOMAS = 0.0
!     Soil cover function
      CALL PUT('PLANT','BIOMAS'   ,BIOMAS)      !kg/ha

C*********************************************************************** 
C*********************************************************************** 
C     CALL SOIL TEMPERATURE SUBROUTINE
C***********************************************************************
      DO WHILE (CONTROL % DYNAMIC .LE. SEASEND)
        
          CALL STEMP_EPIC(CONTROL, ISWITCH,  
     &         SOILPROP, SW, TAVG, TMAX, TMIN, TAV, WEATHER,   !Input
     &         SRFTEMP, ST)                                    !Output
      
      
        CONTROL % DYNAMIC = CONTROL % DYNAMIC + 1
      ENDDO


      END PROGRAM ASKEE

!===========================================================================
! Variable listing
! ---------------------------------
! BLANK   Blank character 
! CONTROL Composite variable containing variables related to control and/or 
!           timing of simulation.  The structure of the variable 
!           (ControlType) is defined in ModuleDefs.for. 
!===========================================================================

!=======================================================================
C  MODULE ModuleDefs
C  11/01/2001 CHP Written
C  06/15/2002 CHP Added flood-related data constructs 
C  03/12/2003 CHP Added residue data construct
C  05/08/2003 CHP Added version information
C  09/03/2004 CHP Modified GetPut_Control routine to store entire
C                   CONTROL variable. 
C             CHP Added GETPUT_ISWITCH routine to store ISWITCH.
C             CHP Added TRTNUM to CONTROL variable.
!  06/14/2005 CHP Added FILEX to CONTROL variable.
!  10/24/2005 CHP Put weather variables in constructed variable. 
!             CHP Added PlantStres environmental stress variable
!  11/07/2005 CHP Added KG2PPM conversion variable to SoilType
!  03/03/2006 CHP Tillage variables added to SOILPROP
!                 Added N_ELEMS to CONTROL variable.
!  03/06/2006 CHP Added mulch variable
!  07/13/2006 CHP Add P variables to SwitchType and SoilType TYPES
!  07/14/2006 CHP Added Fertilizer type, Organic Matter Application type
!  07/24/2006 CHP Added mulch/soil albedo (MSALB) and canopy/mulch/soil
!                   albedo (CMSALB) to SOILPROP variable
!  01/12/2007 CHP Changed TRTNO to TRTNUM to avoid conflict with same
!                 variable name (but different meaning) in input module.
!  01/24/2007 CHP Changed GET & PUT routines to more extensible format.
!  01/22/2008 CHP Moved data exchange (GET & PUT routines) to ModuleData
!  04/28/2008 CHP Added option to read CO2 from file 
!  08/08/2008 CHP Use OPSYS to define variables dependant on operating system
!  08/08/2008 CHP Compiler directives for system call library
!  08/21/2008 CHP Add ROTNUM to CONTROL variable
!  11/25/2008 CHP Mauna Loa CO2 is default
!  12/09/2008 CHP Remove METMP
!  11/19/2010 CHP Added "branch" to version to keep track of non-release branches
!  08/08/2017 WP  Version identification moved to CSMVersion.for
!  08/08/2017 WP  Definitions related with OS platform moved to OSDefinitions.for
!=======================================================================

      MODULE ModuleDefs
!     Contains defintion of derived data types and constants which are 
!     used throughout the model.

!=======================================================================
!      USE CSMVersion
!      USE OSDefinitions
      SAVE
!=======================================================================
!     Global constants
      INTEGER, PARAMETER :: 
     &    NL       = 20,  !Maximum number of soil layers 
     &    TS       = 24,  !Number of hourly time steps per day
     &    NAPPL    = 9000,!Maximum number of applications or operations
     &    NCOHORTS = 300, !Maximum number of cohorts
     &    NELEM    = 3,   !Number of elements modeled (currently N & P)
!            Note: set NELEM to 3 for now so Century arrays will match
     &    NumOfDays = 1000, !Maximum days in sugarcane run (FSR)
     &    NumOfStalks = 42, !Maximum stalks per sugarcane stubble (FSR)
     &    EvaluateNum = 40, !Number of evaluation variables
     &    MaxFiles = 500,   !Maximum number of output files
     &    MaxPest = 500    !Maximum number of pest operations

      REAL, PARAMETER :: 
     &    PI = 3.14159265,
     &    RAD=PI/180.0

      INTEGER, PARAMETER :: 
         !Dynamic variable values
     &    RUNINIT  = 1, 
     &    INIT     = 2,  !Will take the place of RUNINIT & SEASINIT
                         !     (not fully implemented)
     &    SEASINIT = 2, 
     &    RATE     = 3,
     &    EMERG    = 3,  !Used for some plant processes.  
     &    INTEGR   = 4,  
     &    OUTPUT   = 5,  
     &    SEASEND  = 6,
     &    ENDRUN   = 7 

      INTEGER, PARAMETER :: 
         !Nutrient array positions:
     &    N = 1,          !Nitrogen
     &    P = 2,          !Phosphorus
     &    Kel = 3         !Potassium

      CHARACTER(LEN=3)  ModelVerTxt
      CHARACTER(LEN=6)  LIBRARY    !library required for system calls

      CHARACTER*3 MonthTxt(12)
      DATA MonthTxt /'JAN','FEB','MAR','APR','MAY','JUN',
     &               'JUL','AUG','SEP','OCT','NOV','DEC'/

!     MAKEFILEW VARIABLES 
      INTEGER:: FirstWeatherDate = -99
      INTEGER:: NEWSDATE = -99
!=======================================================================
!     Data construct for control variables
      TYPE ControlType
        CHARACTER (len=1)  MESIC, RNMODE
        CHARACTER (len=2)  CROP
        CHARACTER (len=8)  MODEL, ENAME
        CHARACTER (len=12) FILEX
        CHARACTER (len=30) FILEIO
        CHARACTER (len=102)DSSATP
        CHARACTER (len=120) :: SimControl = 
     &  "                                                            "//
     &  "                                                            "
        INTEGER   DAS, DYNAMIC, FROP, ErrCode, LUNIO, MULTI, N_ELEMS
        INTEGER   NYRS, REPNO, ROTNUM, RUN, TRTNUM
        INTEGER   YRDIF, YRDOY, YRSIM
        INTEGER   FODAT, ENDYRS  !Forecast start date and ensemble #
      END TYPE ControlType

!=======================================================================
!     Data construct for control switches
      TYPE SwitchType
        CHARACTER (len=1) FNAME
        CHARACTER (len=1) IDETC, IDETD, IDETG, IDETH, IDETL, IDETN
        CHARACTER (len=1) IDETO, IDETP, IDETR, IDETS, IDETW
        CHARACTER (len=1) IHARI, IPLTI, IIRRI, ISIMI
        CHARACTER (len=1) ISWCHE, ISWDIS, ISWNIT
        CHARACTER (len=1) ISWPHO, ISWPOT, ISWSYM, ISWTIL, ISWWAT
        CHARACTER (len=1) MEEVP, MEGHG, MEHYD, MEINF, MELI, MEPHO
        CHARACTER (len=1) MESOM, MESOL, MESEV, MEWTH
        CHARACTER (len=1) METMP !Temperature, EPIC
        CHARACTER (len=1) IFERI, IRESI, ICO2, FMOPT
        INTEGER NSWI
      END TYPE SwitchType

!Other switches and methods used by model:
! MELI, IOX - not used
! IDETH - only used in MgmtOps
! MEWTH - only used in WEATHR

!=======================================================================
!     Data construct for weather variables
      TYPE WeatherType
        SEQUENCE

!       Weather station information
        REAL REFHT, WINDHT, XLAT, XLONG, XELEV

!       Daily weather data.
        REAL CLOUDS, CO2, DAYL, DCO2, PAR, RAIN, RHUM, SNDN, SNUP, 
     &    SRAD, TAMP, TA, TAV, TAVG, TDAY, TDEW, TGROAV, TGRODY,      
     &    TMAX, TMIN, TWILEN, VAPR, WINDRUN, WINDSP, VPDF, VPD_TRANSP,
     &    OZON7

!       Hourly weather data
        REAL, DIMENSION(TS) :: AMTRH, AZZON, BETA, FRDIFP, FRDIFR, PARHR
        REAL, DIMENSION(TS) :: RADHR, RHUMHR, TAIRHR, TGRO, WINDHR

      END TYPE WeatherType

!=======================================================================
!     Data construct for soil variables
      TYPE SoilType
        INTEGER NLAYR
        CHARACTER (len=5) SMPX
        CHARACTER (len=10) SLNO
        CHARACTER (len=12) TEXTURE(NL)
        CHARACTER (len=17) SOILLAYERTYPE(NL)
        CHARACTER*50 SLDESC, TAXON
        
        LOGICAL COARSE(NL)
        
        REAL ALES, DMOD, SLPF         !DMOD was SLNF
        REAL CMSALB, MSALB, SWALB, SALB      !Albedo 
        REAL, DIMENSION(NL) :: BD, CEC, CLAY, DLAYR, DS, DUL
        REAL, DIMENSION(NL) :: KG2PPM, LL, OC, PH, PHKCL, POROS
        REAL, DIMENSION(NL) :: SAND, SAT, SILT, STONES, SWCN
        
      !Residual water content
        REAL, DIMENSION(NL) :: WCR

      !vanGenuchten parameters
        REAL, DIMENSION(NL) :: alphaVG, mVG, nVG

      !Second tier soils data:
        REAL, DIMENSION(NL) :: CACO3, EXTP, ORGP, PTERMA, PTERMB
        REAL, DIMENSION(NL) :: TOTP, TOTBAS, EXCA, EXK, EXNA

      !Soil analysis data 
        REAL, DIMENSION(NL) :: SASC   !stable organic C

      !Variables added with new soil format:
        REAL ETDR, PONDMAX, SLDN, SLOPE
!       REAL, DIMENSION(NL) :: RCLPF, RGIMPF

      !Variables deleted with new soil format:
      !Still needed for Ritchie hydrology
        REAL CN, SWCON, U
        REAL, DIMENSION(NL) :: ADCOEF, TOTN, TotOrgN, WR

      !Text describing soil layer depth data
      !1-9 describe depths for layers 1-9
      !10 depths for layers 10 thru NLAYR (if NLAYR > 9)
      !11 depths for layers 5 thru NLAYR (if NLAYR > 4)
        CHARACTER*8 LayerText(11)

      !These variables could be made available if needed elsewhere.
      !  They are currently read by SOILDYN module.
      !  CHARACTER*5 SLTXS
      !  CHARACTER*11 SLSOUR
      !  CHARACTER*50 SLDESC, TAXON

      !Second tier soils data that could be used:
!        REAL, DIMENSION(NL) :: EXTAL, EXTFE, EXTMN, 
!        REAL, DIMENSION(NL) :: EXMG, EXTS, SLEC

      END TYPE SoilType

!=======================================================================
!     Data construct for mulch layer
      TYPE MulchType
        REAL MULCHMASS    !Mass of surface mulch layer (kg[dry mat.]/ha)
        REAL MULCHALB     !Albedo of mulch layer
        REAL MULCHCOVER   !Coverage of mulch layer (frac. of surface)
        REAL MULCHTHICK   !Thickness of mulch layer (mm)
        REAL MULCHWAT     !Water content of mulch (mm3/mm3)
        REAL MULCHEVAP    !Evaporation from mulch layer (mm/d)
        REAL MULCHSAT     !Saturation water content of mulch (mm3/mm3)
        REAL MULCHN       !N content of mulch layer (kg[N]/ha)
        REAL MULCHP       !P content of mulch layer (kg[P]/ha)
        REAL NEWMULCH     !Mass of new surface mulch (kg[dry mat.]/ha)
        REAL NEWMULCHWAT  !Water content of new mulch ((mm3/mm3)
        REAL MULCH_AM     !Area covered / dry weight of residue (ha/kg)
        REAL MUL_EXTFAC   !Light extinction coef. for mulch layer
        REAL MUL_WATFAC   !Saturation water content (mm[water] ha kg-1)
      END TYPE MulchType

!=======================================================================
!     Data construct for tillage operations
      TYPE TillType
        INTEGER NTIL      !Total number of tillage events in FILEX
        INTEGER TILDATE   !Date of current tillage event

!       Maximum values for multiple events in a single day
        REAL TILDEP, TILMIX, TILRESINC

!       Irrigation amount which affects tilled soil properties 
!          expressed in units of equivalent rainfall depth
        REAL TIL_IRR   

!       Allows multiple tillage passes in a day
        INTEGER NTil_today !number of tillage events today (max 3)
        INTEGER, DIMENSION(NAPPL) :: NLYRS
        REAL, DIMENSION(NAPPL) :: CNP, TDEP
        REAL, DIMENSION(NAPPL,NL) :: BDP, DEP, SWCNP
      END TYPE TillType

!=======================================================================
!     Data construct for oxidation layer
      TYPE OxLayerType
        INTEGER IBP
        REAL    OXU, OXH4, OXN3   
        REAL    OXLT, OXMIN4, OXMIN3
        REAL    DLTOXU, DLTOXH4, DLTOXN3
        REAL    ALGACT
        LOGICAL DailyCalc
      END TYPE OxLayerType

!======================================================================
!     Fertilizer application data
      TYPE FertType
        CHARACTER*7 AppType != 'UNIFORM', 'BANDED ' or 'HILL   '
        INTEGER FERTDAY, FERTYPE
        INTEGER, DIMENSION(NELEM) :: NAPFER
        REAL FERDEPTH, FERMIXPERC
        REAL ADDFNH4, ADDFNO3, ADDFUREA
        REAL ADDOXU, ADDOXH4, ADDOXN3
        REAL, DIMENSION(NELEM) :: AMTFER
        REAL, DIMENSION(NL) :: ADDSNH4, ADDSNO3, ADDUREA
        REAL, DIMENSION(NL) :: ADDSPi
        REAL, DIMENSION(NL) :: ADDSKi
        LOGICAL UNINCO
      END TYPE FertType

!=======================================================================
!   Data construct for residue (harvest residue, senesced matter, etc.)
      TYPE ResidueType
        REAL, DIMENSION(0:NL) :: ResWt        !kg[dry matter]/ha/d
        REAL, DIMENSION(0:NL) :: ResLig       !kg[lignin]/ha/d
        REAL, DIMENSION(0:NL,NELEM) :: ResE   !kg[E]/ha/d (E=N,P,K,..)
        REAL  CumResWt                        !cumul. kg[dry matter]/ha
        REAL, DIMENSION(NELEM) :: CumResE     !cumulative kg[E]/ha
      END TYPE ResidueType

!======================================================================
!     Organic Matter Application data
      TYPE OrgMatAppType
        INTEGER NAPRes, ResDat, ResDepth
        CHARACTER (len=5) RESTYPE
        REAL ResMixPerc   !Percent mixing rate for SOM module

        REAL, DIMENSION(0:NL) :: ResWt        !kg[dry matter]/ha/d
        REAL, DIMENSION(0:NL) :: ResLig       !kg[lignin]/ha/d
        REAL, DIMENSION(0:NL,NELEM) :: ResE   !kg[E]/ha/d (E=N, P, ..)
        REAL  CumResWt                        !cumul. kg[dry matter]/ha
        REAL, DIMENSION(NELEM) :: CumResE     !cumulative kg[E]/ha
      END TYPE OrgMatAppType

!======================================================================
!     Plant stresses for environmental stress summary
      Type PlStresType
        INTEGER NSTAGES   !# of stages (max 5)
        CHARACTER(len=23) StageName(0:5)
        REAL W_grow, W_phot, N_grow, N_phot
        REAL P_grow, P_phot
        LOGICAL ACTIVE(0:5)
      End Type PlStresType

!======================================================================
!     Array of output files, aliases, unit numbers, etc.
      Type OutputType
        INTEGER NumFiles
        CHARACTER*16, DIMENSION(MaxFiles) :: FileName
        CHARACTER*2,  DIMENSION(MaxFiles) :: OPCODE
        CHARACTER*50, DIMENSION(MaxFiles) :: Description
        CHARACTER*10, DIMENSION(MaxFiles) :: ALIAS
        INTEGER, DIMENSION(MaxFiles) :: LUN
      End Type


!======================================================================
!      CONTAINS
!
!!----------------------------------------------------------------------
!      SUBROUTINE SETOP ()
!      IMPLICIT NONE
!
!      WRITE(ModelVerTxt,'(I2.2,I1)') Version%Major, Version%Minor
!
!      END SUBROUTINE SETOP

!======================================================================
      END MODULE ModuleDefs
!======================================================================


! - ASKE ORIGINAL START
!!======================================================================
!!     Paddy Managment routines.
!!======================================================================
!      MODULE FloodModule
!!=======================================================================
!!     Data construct for flood data. 
!      Type FloodWatType
!        !From IRRIG
!        LOGICAL BUNDED        
!        INTEGER NBUND         
!        REAL ABUND            
!        REAL PUDPERC, PERC
!        REAL PLOWPAN    !Depth of puddling (m) (ORYZA)
!
!        !From Paddy_Mgmt
!        INTEGER YRDRY, YRWET  
!        REAL FLOOD, FRUNOFF   
!        REAL TOTBUNDRO        
!        LOGICAL PUDDLED       
!
!        REAL CEF, EF          !From SPAM
!        REAL INFILT, RUNOFF   !From WATBAL
!      End Type FloodWatType
!
!      Type FloodNType
!        INTEGER NDAT
!        REAL    ALGFON                        !Algae kill or dry-up
!        REAL    FLDH4C, FLDN3C                !Flood N concentrations
!        REAL    FLDU, FLDN3, FLDH4            !Flood N mass (kg/ha)
!        REAL    FRNH4U, FRNO3U                !Flood N uptake (kg/ha)
!        REAL    DLTFUREA, DLTFNH4, DLTFNO3    !Flood N flux (kg/ha)
!      End Type FloodNType
!
!      END MODULE FloodModule
!!======================================================================
! - ASKE ORIGINAL END

!=======================================================================
!  MODULE ModuleData
!  01/22/2008 CHP Written
!=======================================================================

      MODULE ModuleData
!     Data storage and retrieval module.
!     Defines data structures that hold information that can be 
!       stored or accessed by query.  

!     A call to the GET routine will return the value of variable 
!       requested.  The procedure is "overloaded", i.e., the procedure 
!       executed will depend on the type of variable(s) in the argument 
!       list.  A request for a "real" data type will invoke the GET_Real
!       procedure, for example.  

!     Similarly, a call to the PUT routine will store the data sent.
!       It is also an overloaded procedure including several different
!       types of data which can be stored.

!     The SAVE_data variable is used to store all information.

!     To add a variable for storage and retrieval: 
!     1.  Add the variable to one of the Type constructs based on the 
!         module that "owns" the variable, for example SPAMType, Planttype 
!         or MgmtType.
!     2.  For a real data type, add a line of code in both the GET_Real and
!         PUT_Real subroutines.  
!     3.  For an integer data type, add a line of code in both the 
!         GET_Integer and PUT_Integer subroutines.  
!     4.  All routines accessing GET or PUT procedures must include a 
!         "USE ModuleData" statement.
!     5.  A call to the PUT routine must be used to store data prior to
!         a call to the GET routine to retrive the data.

      USE ModuleDefs
      SAVE

!======================================================================
!     Data transferred from hourly energy balance 
      Type SPAMType
        REAL AGEFAC, PG                   !photosynthese
        REAL CEF, CEM, CEO, CEP, CES      !Cumulative ET - mm
        REAL CET, CEVAP                   !Cumulative ET - mm
        REAL  EF,  EM,  EO,  EP,  ES,  ET !Daily ET - mm/d
        REAL  EOP, EVAP                   !Daily mm/d
        REAL, DIMENSION(NL) :: UH2O       !Root water uptake
        !ASCE reference ET with FAO-56 dual crop coefficient (KRT)
        REAL REFET, SKC, KCBMIN, KCBMAX, KCB, KE, KC
      End Type SPAMType

!     Data transferred from CROPGRO routine 
      TYPE PlantType
        REAL CANHT, CANWH, DXR57, EXCESS,
     &    PLTPOP, RNITP, SLAAD, XPOD
        REAL BIOMAS
        INTEGER NR5, iSTAGE, iSTGDOY
        CHARACTER*10 iSTNAME
      END TYPE PlantType

!     Data transferred from management routine 
      Type MgmtType
        REAL DEPIR, EFFIRR, FERNIT, IRRAMT, TOTIR, TOTEFFIRR
        REAL V_AVWAT(20) !Create vectors for growth stage based irrig
        REAL V_IMDEP(20)
        REAL V_ITHRL(20)
        REAL V_ITHRU(20)
        INTEGER V_IRON(20)
        REAL V_IRAMT(20)
        REAL V_IREFF(20)
        INTEGER V_IFREQ(20)
        INTEGER GSIRRIG
        CHARACTER*5 V_IRONC(20)
      End Type MgmtType

!     Data transferred from Soil water routine
      Type WatType
        REAL DRAIN, RUNOFF, SNOW
      End Type WatType

!     Data transferred from Soil Inorganic Nitrogen routine
      Type NiType
        REAL TNOXD, TLeachD    !, TN2OD     ! added N2O PG
      End Type NiType

!     Data transferred from Organic C routines
      Type OrgCType
        REAL TOMINFOM, TOMINSOM, TOMINSOM1, TOMINSOM2
        REAL TOMINSOM3, TNIMBSOM
        REAL MULCHMASS
      End Type OrgCType

!     Data from weather
      Type WeathType
        INTEGER WYEAR
        Character*8 WSTAT
      End Type WeathType

      TYPE PDLABETATYPE
        REAL PDLA
        REAL BETALS
      END TYPE

!     Data which can be transferred between modules
      Type TransferType
        Type (ControlType) CONTROL
        Type (SwitchType)  ISWITCH
        Type (OutputType)  OUTPUT
        Type (PlantType)   PLANT
        Type (MgmtType)    MGMT
        Type (NiType)      NITR
        Type (OrgCType)    ORGC
        Type (SoilType)    SOILPROP
        Type (SPAMType)    SPAM
        Type (WatType)     WATER
        Type (WeathType)   WEATHER
        TYPE (PDLABETATYPE) PDLABETA
      End Type TransferType

!     The variable SAVE_data contains all of the components to be 
!     stored and retrieved.
      Type (TransferType) SAVE_data

!======================================================================
!     GET and PUT routines are differentiated by argument type.  All of 
!       these procedures can be accessed with a CALL GET(...)
      INTERFACE GET
         MODULE PROCEDURE GET_Control
     &                  , GET_ISWITCH 
     &                  , GET_Output 
     &                  , GET_SOILPROP
!     &                  , GET_Weather
     &                  , GET_Real 
! - ASKE ORIGINAL START
!     &                  , GET_Real_Array_NL
!     &                  , GET_Integer
!     &                  , GET_Char
! - ASKE ORIGINAL END
      END INTERFACE

      INTERFACE PUT
         MODULE PROCEDURE PUT_Control
     &                  , PUT_ISWITCH 
     &                  , PUT_Output 
     &                  , PUT_SOILPROP
!     &                  , PUT_Weather
     &                  , PUT_Real 
! - ASKE ORIGINAL START     
!     &                  , PUT_Real_Array_NL
!     &                  , PUT_Integer
!     &                  , PUT_Char
! - ASKE ORIGINAL END
      END INTERFACE

      CONTAINS

!----------------------------------------------------------------------
      Subroutine Get_CONTROL (CONTROL_arg)
!     Retrieves CONTROL variable
      IMPLICIT NONE
      Type (ControlType) Control_arg
      Control_arg = SAVE_data % Control
      Return
      End Subroutine Get_CONTROL

!----------------------------------------------------------------------
      Subroutine Put_CONTROL (CONTROL_arg)
!     Stores CONTROL variable
      IMPLICIT NONE
      Type (ControlType) Control_arg
      SAVE_data % Control = Control_arg
      Return
      End Subroutine Put_CONTROL

!----------------------------------------------------------------------
      Subroutine Get_ISWITCH (ISWITCH_arg)
!     Retrieves ISWITCH variable
      IMPLICIT NONE
      Type (SwitchType) ISWITCH_arg
      ISWITCH_arg = SAVE_data % ISWITCH
      Return
      End Subroutine Get_ISWITCH

!----------------------------------------------------------------------
      Subroutine Put_ISWITCH (ISWITCH_arg)
!     Stores ISWITCH variable
      IMPLICIT NONE
      Type (SwitchType) ISWITCH_arg
      SAVE_data % ISWITCH = ISWITCH_arg
      Return
      End Subroutine Put_ISWITCH

!----------------------------------------------------------------------
      SUBROUTINE GET_OUTPUT(OUTPUT_ARG)
!     Retrieves OUTPUT variable as needed
      IMPLICIT NONE
      TYPE (OutputType) OUTPUT_ARG
      OUTPUT_ARG = SAVE_data % OUTPUT
      RETURN
      END SUBROUTINE GET_OUTPUT

!----------------------------------------------------------------------
      SUBROUTINE PUT_OUTPUT(OUTPUT_ARG)
!     Stores OUTPUT variable 
      IMPLICIT NONE
      TYPE (OutputType) OUTPUT_ARG
      SAVE_data % OUTPUT = OUTPUT_ARG
      RETURN
      END SUBROUTINE PUT_OUTPUT

!----------------------------------------------------------------------
      SUBROUTINE GET_SOILPROP(SOIL_ARG)
!     Retrieves SOILPROP variable as needed
      IMPLICIT NONE
      TYPE (SoilType) SOIL_ARG
      SOIL_ARG = SAVE_data % SOILPROP
      RETURN
      END SUBROUTINE GET_SOILPROP

!----------------------------------------------------------------------
      SUBROUTINE PUT_SOILPROP(SOIL_ARG)
!     Stores SOILPROP variable 
      IMPLICIT NONE
      TYPE (SoilType) SOIL_ARG
      SAVE_data % SOILPROP = SOIL_ARG
      RETURN
      END SUBROUTINE PUT_SOILPROP

!!----------------------------------------------------------------------
!      SUBROUTINE GET_WEATHER(WEATHER_ARG)
!!     Retrieves WEATHER variable as needed
!      IMPLICIT NONE
!      TYPE (WeathType) WEATHER_ARG
!      WEATHER_ARG = SAVE_data % WEATHER
!      RETURN
!      END SUBROUTINE GET_WEATHER
!
!!----------------------------------------------------------------------
!      SUBROUTINE PUT_WEATHER(WEATHER_ARG)
!!     Stores WEATHER variable 
!      IMPLICIT NONE
!      TYPE (WeathType) WEATHER_ARG
!      SAVE_data % WEATHER = WEATHER_ARG
!      RETURN
!      END SUBROUTINE PUT_WEATHER

!----------------------------------------------------------------------
      Subroutine GET_Real(ModuleName, VarName, Value)
!     Retrieves real variable from SAVE_data.  Variable must be
!         included as a component of SAVE_data. 
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
      Character*78 MSG(2)
      Real Value
      Logical ERROR

      Value = 0.0
      ERROR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('SPAM')
        SELECT CASE (VarName)
        Case ('AGEFAC')
            Value = SAVE_data % SPAM % AGEFAC
        Case ('PG')
            Value = SAVE_data % SPAM % PG
        Case ('CEF')
            Value = SAVE_data % SPAM % CEF
        Case ('CEM')
            Value = SAVE_data % SPAM % CEM
        Case ('CEO')
            Value = SAVE_data % SPAM % CEO
        Case ('CEP')
            Value = SAVE_data % SPAM % CEP
        Case ('CES')
            Value = SAVE_data % SPAM % CES
        Case ('CET')
            Value = SAVE_data % SPAM % CET
        Case ('CEVAP')
            Value = SAVE_data % SPAM % CEVAP
        Case ('EF')
            Value = SAVE_data % SPAM % EF
        Case ('EM')
            Value = SAVE_data % SPAM % EM
        Case ('EO')
            Value = SAVE_data % SPAM % EO
        Case ('EP')
            Value = SAVE_data % SPAM % EP
        Case ('ES')
            Value = SAVE_data % SPAM % ES
        Case ('ET')
            Value = SAVE_data % SPAM % ET
        Case ('EOP')
            Value = SAVE_data % SPAM % EOP
        Case ('EVAP')
            Value = SAVE_data % SPAM % EVAP
        Case ('REFET')
            Value = SAVE_data % SPAM % REFET
        Case ('SKC')
            Value = SAVE_data % SPAM % SKC
        Case ('KCBMIN')
            Value = SAVE_data % SPAM % KCBMIN
        Case ('KCBMAX')
            Value = SAVE_data % SPAM % KCBMAX
        Case ('KCB')
            Value = SAVE_data % SPAM % KCB
        Case ('KE')
            Value = SAVE_data % SPAM % KE
        Case ('KC')
            Value = SAVE_data % SPAM % KC
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('PLANT')
        SELECT CASE (VarName)
        Case ('BIOMAS')
            Value = SAVE_data % PLANT % BIOMAS
        Case ('CANHT')
            Value = SAVE_data % PLANT % CANHT
        Case ('CANWH')
            Value = SAVE_data % PLANT % CANWH
        Case ('DXR57')
            Value = SAVE_data % PLANT % DXR57
        Case ('EXCESS')
            Value = SAVE_data % PLANT % EXCESS
        Case ('PLTPOP')
            Value = SAVE_data % PLANT % PLTPOP
        Case ('RNITP')
            Value = SAVE_data % PLANT % RNITP
        Case ('SLAAD')
            Value = SAVE_data % PLANT % SLAAD
        Case ('XPOD')
            Value = SAVE_data % PLANT % XPOD
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('MGMT')
        SELECT CASE (VarName)
        Case ('EFFIRR')
            Value = SAVE_data % MGMT % EFFIRR
        Case ('TOTIR')
            Value = SAVE_data % MGMT % TOTIR
        Case ('TOTEFFIRR')
            Value=SAVE_data % MGMT % TOTEFFIRR
        Case ('DEPIR')
            Value = SAVE_data % MGMT % DEPIR
        Case ('IRRAMT')
            Value = SAVE_data % MGMT % IRRAMT
        Case ('FERNIT')
            Value = SAVE_data % MGMT % FERNIT
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('WATER')
        SELECT CASE (VarName)
        Case ('DRAIN')
            Value = SAVE_data % WATER % DRAIN
        Case ('RUNOFF')
            Value = SAVE_data % WATER % RUNOFF
        Case ('SNOW')
            Value = SAVE_data % WATER % SNOW
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('NITR')
        SELECT CASE (VarName)
        Case ('TNOXD')
            Value = SAVE_data % NITR % TNOXD
       Case ('TLCHD')
            Value = SAVE_data % NITR % TLeachD
!       Case ('TN2OD') Value = SAVE_data % NITR % TN2OD
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('ORGC')
        SELECT CASE (VarName)
        Case ('MULCHMASS')
            Value = SAVE_data % ORGC % MULCHMASS
        Case ('TOMINFOM')
            Value = SAVE_data % ORGC % TOMINFOM
        Case ('TOMINSOM')
            Value = SAVE_data % ORGC % TOMINSOM
        Case ('TOMINSOM1')
            Value = SAVE_data % ORGC % TOMINSOM1
        Case ('TOMINSOM2')
            Value = SAVE_data % ORGC % TOMINSOM2
        Case ('TOMINSOM3')
            Value = SAVE_data % ORGC % TOMINSOM3
        Case ('TNIMBSOM')
            Value = SAVE_data % ORGC % TNIMBSOM
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('SOIL')
        SELECT CASE (VarName)
        Case ('TOMINFOM')
            Value = SAVE_data % ORGC % TOMINFOM
        Case ('TOMINSOM')
            Value = SAVE_data % ORGC % TOMINSOM
        Case ('TOMINSOM1')
            Value = SAVE_data % ORGC % TOMINSOM1
        Case ('TOMINSOM2')
            Value = SAVE_data % ORGC % TOMINSOM2
        Case ('TOMINSOM3')
            Value = SAVE_data % ORGC % TOMINSOM3
        Case ('TNIMBSOM')
            Value = SAVE_data % ORGC % TNIMBSOM
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      CASE ('PDLABETA')
        SELECT CASE(VarName)
        CASE('PDLA')
            Value = SAVE_data % PDLABETA % PDLA
        CASE('BETA')
            Value = SAVE_data % PDLABETA % BETALS
        CASE DEFAULT
            ERROR = .TRUE.
        END SELECT
            
      Case DEFAULT
            ERROR = .TRUE.
      END SELECT

      IF (ERROR) THEN
        WRITE(MSG(1),'("Error transferring variable: ",A, " in ",A)') 
     &      Trim(VarName), Trim(ModuleName)
        MSG(2) = 'Value set to zero.'
! - ASKE ORIGINAL START        
!        CALL WARNING(2,'GET_REAL',MSG)
! - ASKE ORIGINAL START        
      ENDIF

      RETURN
      END SUBROUTINE GET_Real

!----------------------------------------------------------------------
      SUBROUTINE PUT_Real(ModuleName, VarName, Value)
!     Stores real variable SAVE_data.  
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
      Character*78 MSG(2)
      Real Value
      Logical ERROR

      ERROR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('SPAM')
        SELECT CASE (VarName)
        Case ('AGEFAC')
            SAVE_data % SPAM % AGEFAC = Value
        Case ('PG')
            SAVE_data % SPAM % PG     = Value
        Case ('CEF')
            SAVE_data % SPAM % CEF    = Value
        Case ('CEM')
            SAVE_data % SPAM % CEM    = Value
        Case ('CEO')
            SAVE_data % SPAM % CEO    = Value
        Case ('CEP')
            SAVE_data % SPAM % CEP    = Value
        Case ('CES')
            SAVE_data % SPAM % CES    = Value
        Case ('CET')
            SAVE_data % SPAM % CET    = Value
        Case ('CEVAP')
            SAVE_data % SPAM % CEVAP  = Value
        Case ('EF')
            SAVE_data % SPAM % EF     = Value
        Case ('EM')
            SAVE_data % SPAM % EM     = Value
        Case ('EO')
            SAVE_data % SPAM % EO     = Value
        Case ('EP')
            SAVE_data % SPAM % EP     = Value
        Case ('ES')
            SAVE_data % SPAM % ES     = Value
        Case ('ET')
            SAVE_data % SPAM % ET     = Value
        Case ('EOP')
            SAVE_data % SPAM % EOP    = Value
        Case ('EVAP')
            SAVE_data % SPAM % EVAP   = Value
        Case ('REFET')
            SAVE_data % SPAM % REFET  = Value
        Case ('SKC')
            SAVE_data % SPAM % SKC    = Value
        Case ('KCBMIN')
            SAVE_data % SPAM % KCBMIN = Value
        Case ('KCBMAX')
            SAVE_data % SPAM % KCBMAX = Value
        Case ('KCB')
            SAVE_data % SPAM % KCB    = Value
        Case ('KE')
            SAVE_data % SPAM % KE     = Value
        Case ('KC')
            SAVE_data % SPAM % KC     = Value
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('PLANT')
        SELECT CASE (VarName)
        Case ('BIOMAS')
            SAVE_data % PLANT % BIOMAS = Value
        Case ('CANHT')
            SAVE_data % PLANT % CANHT  = Value
        Case ('CANWH')
            SAVE_data % PLANT % CANWH  = Value
        Case ('DXR57')
            SAVE_data % PLANT % DXR57  = Value
        Case ('EXCESS')
            SAVE_data % PLANT % EXCESS = Value
        Case ('PLTPOP')
            SAVE_data % PLANT % PLTPOP = Value
        Case ('RNITP')
            SAVE_data % PLANT % RNITP  = Value
        Case ('SLAAD')
            SAVE_data % PLANT % SLAAD  = Value
        Case ('XPOD')
            SAVE_data % PLANT % XPOD   = Value
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('MGMT')
        SELECT CASE (VarName)
        Case ('EFFIRR')
            SAVE_data % MGMT % EFFIRR = Value
        Case ('TOTIR')
            SAVE_data % MGMT % TOTIR  = Value
        Case ('TOTEFFIRR')
            SAVE_data%MGMT % TOTEFFIRR=Value
        Case ('DEPIR')
            SAVE_data % MGMT % DEPIR  = Value
        Case ('IRRAMT')
            SAVE_data % MGMT % IRRAMT = Value
        Case ('FERNIT')
            SAVE_data % MGMT % FERNIT = Value
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('WATER')
        SELECT CASE (VarName)
        Case ('DRAIN')
            SAVE_data % WATER % DRAIN  = Value
        Case ('RUNOFF')
            SAVE_data % WATER % RUNOFF = Value
        Case ('SNOW')
            SAVE_data % WATER % SNOW   = Value
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('NITR')
        SELECT CASE (VarName)
        Case ('TNOXD')
            SAVE_data % NITR % TNOXD = Value
        Case ('TLCHD')
            SAVE_data % NITR % TLeachD = Value
!       Case ('TN2OD') SAVE_data % NITR % TN2OD = Value
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      Case ('ORGC')
        SELECT CASE (VarName)
        Case ('MULCHMASS')
            SAVE_data % ORGC % MULCHMASS = Value
        Case ('TOMINFOM')
            SAVE_data % ORGC % TOMINFOM  = Value
        Case ('TOMINSOM')
            SAVE_data % ORGC % TOMINSOM  = Value
        Case ('TOMINSOM1')
            SAVE_data % ORGC % TOMINSOM1 = Value
        Case ('TOMINSOM2')
            SAVE_data % ORGC % TOMINSOM2 = Value
        Case ('TOMINSOM3')
            SAVE_data % ORGC % TOMINSOM3 = Value
        Case ('TNIMBSOM')
            SAVE_data % ORGC % TNIMBSOM  = Value
        Case DEFAULT
            ERROR = .TRUE.
        END SELECT

      CASE ('PDLABETA')
        SELECT CASE(VarName)
        CASE('PDLA')
            SAVE_data % PDLABETA % PDLA = Value
        CASE('BETA')
            SAVE_data % PDLABETA % BETALS = Value
        CASE DEFAULT
            ERROR = .TRUE.
        END SELECT
            
      Case DEFAULT
            ERROR = .TRUE.
      END SELECT

      IF (ERROR) THEN
        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
     &      Trim(VarName), Trim(ModuleName)
        MSG(2) = 'Value not saved! Errors may result.'
! - ASKE ORIGINAL START        
!        CALL WARNING(2,'PUT_REAL',MSG)
! - ASKE ORIGINAL END        
      ENDIF

      RETURN
      END SUBROUTINE PUT_Real
      
! - ASKE ORIGINAL START
!!----------------------------------------------------------------------
!      SUBROUTINE GET_Real_Array_NL(ModuleName, VarName, Value)
!!     Retrieves array of dimension(NL) 
!      IMPLICIT NONE
!      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
!      REAL, DIMENSION(NL) :: Value
!      Logical ERROR
!
!      Value = 0.0
!      ERROR = .FALSE.
!
!      SELECT CASE (ModuleName)
!
!      CASE ('SPAM')
!        SELECT CASE (VarName)
!          CASE ('UH2O')  Value = SAVE_data % SPAM % UH2O
!          CASE DEFAULT ERROR = .TRUE.
!        END SELECT
!
!        CASE DEFAULT ERROR = .TRUE.
!      END SELECT
!
!      IF (ERROR) THEN
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_Real_Array_NL',MSG)
!      ENDIF
!
!      RETURN
!      END SUBROUTINE GET_Real_Array_NL
!
!!----------------------------------------------------------------------
!      SUBROUTINE PUT_Real_Array_NL(ModuleName, VarName, Value)
!!     Stores array of dimension NL
!      IMPLICIT NONE
!      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
!      REAL, DIMENSION(NL) :: Value
!      Logical ERROR
!
!      ERROR = .FALSE.
!
!      SELECT CASE (ModuleName)
!      Case ('SPAM')
!        SELECT CASE (VarName)
!        Case ('UH2O') SAVE_data % SPAM % UH2O = Value
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case DEFAULT ERROR = .TRUE.
!      END SELECT
!
!      IF (ERROR) THEN
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_Real_Array_NL',MSG)
!      ENDIF
!
!      RETURN
!      END SUBROUTINE PUT_Real_Array_NL
!
!!----------------------------------------------------------------------
!      Subroutine GET_Integer(ModuleName, VarName, Value)
!!     Retrieves Integer variable as needed
!      IMPLICIT NONE
!      Character*(*) ModuleName, VarName
!      Character*78  MSG(2)
!      Integer Value
!      Logical ERROR
!
!      Value = 0
!      ERROR = .FALSE.
!
!      SELECT CASE (ModuleName)
!      Case ('PLANT')
!        SELECT CASE (VarName)
!        Case ('NR5')  Value = SAVE_data % PLANT % NR5
!        Case ('iSTAGE')  Value = SAVE_data % PLANT % iSTAGE
!        Case ('iSTGDOY') Value = SAVE_data % PLANT % iSTGDOY
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case ('WEATHER')
!        SELECT CASE (VarName)
!        Case ('WYEAR') Value = SAVE_data % WEATHER % WYEAR
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case Default ERROR = .TRUE.
!      END SELECT
!
!      IF (ERROR) THEN
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_INTEGER',MSG)
!      ENDIF
!
!      RETURN
!      END SUBROUTINE GET_Integer
!
!!----------------------------------------------------------------------
!      SUBROUTINE PUT_Integer(ModuleName, VarName, Value)
!!     Stores Integer variable
!      IMPLICIT NONE
!      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
!      Integer Value
!      Logical ERROR
!
!      ERROR = .FALSE.
!
!      SELECT CASE (ModuleName)
!      Case ('PLANT')
!        SELECT CASE (VarName)
!        Case ('NR5')  SAVE_data % PLANT % NR5  = Value
!        Case ('iSTAGE')  SAVE_data % PLANT % iSTAGE  = Value
!        Case ('iSTGDOY') SAVE_data % PLANT % iSTGDOY = Value
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case ('WEATHER')
!        SELECT CASE (VarName)
!        Case ('WYEAR') SAVE_data % WEATHER % WYEAR = Value
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case DEFAULT ERROR = .TRUE.
!      END SELECT
!
!      IF (ERROR) THEN
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_Integer',MSG)
!      ENDIF
!
!      RETURN
!      END SUBROUTINE PUT_Integer
!
!!----------------------------------------------------------------------
!      Subroutine GET_Char(ModuleName, VarName, Value)
!!     Retrieves Integer variable as needed
!      IMPLICIT NONE
!      Character*(*) ModuleName, VarName, Value
!      Character*78  MSG(2)
!      Logical ERROR
!
!      Value = ' '
!      ERROR = .FALSE.
!
!      SELECT CASE (ModuleName)
!      Case ('WEATHER')
!        SELECT CASE (VarName)
!        Case ('WSTA')  Value = SAVE_data % WEATHER % WSTAT
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case ('PLANT')
!        SELECT CASE (VarName)
!        Case ('iSTNAME')  Value = SAVE_data % PLANT % iSTNAME
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case Default ERROR = .TRUE.
!      END SELECT
!
!      IF (ERROR) THEN
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_INTEGER',MSG)
!      ENDIF
!
!      RETURN
!      END SUBROUTINE GET_Char
!
!!----------------------------------------------------------------------
!      SUBROUTINE PUT_Char(ModuleName, VarName, Value)
!!     Stores Character variable
!      IMPLICIT NONE
!      Character*(*) ModuleName, VarName, Value
!      Character*78 MSG(2)
!      Logical ERROR
!
!      ERROR = .FALSE.
!
!      SELECT CASE (ModuleName)
!      Case ('WEATHER')
!        SELECT CASE (VarName)
!        Case ('WSTA')  SAVE_data % WEATHER % WSTAT  = Value
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case ('PLANT')
!        SELECT CASE (VarName)
!        Case ('iSTNAME')  SAVE_data % PLANT % iSTNAME = Value
!        Case DEFAULT ERROR = .TRUE.
!        END SELECT
!
!      Case DEFAULT ERROR = .TRUE.
!      END SELECT
!
!      IF (ERROR) THEN
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)') 
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_Integer',MSG)
!      ENDIF
!
!      RETURN
!      END SUBROUTINE PUT_Char
! - ASKE ORIGINAL END
!======================================================================
      END MODULE ModuleData
!======================================================================
C=======================================================================
C  OPSTEMP, Subroutine, C.H.Porter 
C  Generates output for daily soil temperature data
C-----------------------------------------------------------------------
C  REVISION HISTORY
C  11/01/2001 CHP Written
C  06/07/2002 GH  Modified for crop rotations
C-----------------------------------------------------------------------
C  Called from:   STEMP
C  Calls:         None
C=======================================================================
      SUBROUTINE OPSTEMP(CONTROL, ISWITCH, DOY, SRFTEMP, ST, TAV, TAMP)

!-----------------------------------------------------------------------
      USE ModuleDefs

      IMPLICIT NONE
      SAVE
!-----------------------------------------------------------------------
      CHARACTER*1  RNMODE
      CHARACTER*12 OUTT

      INTEGER DAS, DOY, DYNAMIC, ERRNUM, FROP, L, N_LYR
      INTEGER NOUTDT, RUN, YEAR, YRDOY, REPNO
      REAL ST(NL), SRFTEMP, TAV, TAMP

      LOGICAL FEXIST, DOPRINT

!-----------------------------------------------------------------------
!     The variable "CONTROL" is of constructed type "ControlType" as 
!     defined in ModuleDefs.for, and contains the following variables.
!     The components are copied into local variables for use here.
!-----------------------------------------------------------------------
      TYPE (ControlType) CONTROL
      TYPE (SwitchType)  ISWITCH
      TYPE (SoilType)    SOILPROP

      DAS     = CONTROL % DAS
      DYNAMIC = CONTROL % DYNAMIC
      FROP    = CONTROL % FROP
      YRDOY   = CONTROL % YRDOY
      
!***********************************************************************
!***********************************************************************
!     Seasonal initialization - run once per season
!***********************************************************************
!      ELSEIF (DYNAMIC .EQ. SEASINIT) THEN
      IF (DYNAMIC .EQ. SEASINIT) THEN
!-----------------------------------------------------------------------
!       Open the output files
        OUTT = 'SoilTemp.OUT'
        OPEN (UNIT=NOUTDT, FILE=OUTT, STATUS='NEW',
     &      IOSTAT = ERRNUM)
 !        Write headers info to daily output file
          WRITE(NOUTDT,'("*SOIL TEMPERATURE OUTPUT FILE (DAILY)")')
C-----------------------------------------------------------------------
C     Variable heading for SoilTemp.OUT
C-----------------------------------------------------------------------                  
!        CALL GET(SOILPROP)
        N_LYR = MIN(10, MAX(4,SOILPROP%NLAYR))
          
          IF (N_LYR < 10) THEN
            WRITE (NOUTDT,120) ("TS",L,"D",L=1,N_LYR)
  120       FORMAT('@YEAR DOY   DAS    TS0D',10("    ",A2,I1,A1))

          ELSE
            WRITE (NOUTDT,122) ("TS",L,"D",L=1,9), "    TS10"
  122       FORMAT('@YEAR DOY   DAS    TS0D',9("    ",A2,I1,A1),A8)
          ENDIF

      ENDIF !DYNAMIC

!***********************************************************************
!***********************************************************************
!     Output
!***********************************************************************
      IF (DYNAMIC .EQ. OUTPUT) THEN
        CALL YR_DOY(YRDOY, YEAR, DOY)
!         Generate output for file SoilTemp.OUT
          WRITE (NOUTDT,300) YEAR, DOY, DAS, SRFTEMP, (ST(L),L=1,N_LYR)
  300     FORMAT(1X,I4,1X,I3.3,1X,I5,11F8.1)
      ENDIF
!***********************************************************************
!***********************************************************************
!     SEASEND
!***********************************************************************
      IF (DYNAMIC .EQ. SEASEND) THEN
!-----------------------------------------------------------------------
        CLOSE (NOUTDT)
!***********************************************************************
!***********************************************************************
!     END OF DYNAMIC IF CONSTRUCT
!***********************************************************************
      ENDIF
!***********************************************************************
      RETURN
      END SUBROUTINE OPSTEMP
!***********************************************************************

C=======================================================================
C  YR_DOY, Subroutine, N.B. Pickering, 09/13/91
C  Converts YRDOY to YR and DOY.
C-----------------------------------------------------------------------
C  Input : YRDOY
C  Output: YR,DOY
C=======================================================================

      SUBROUTINE YR_DOY(YRDOY,YR,DOY)

      IMPLICIT NONE

      INTEGER DOY,YR,YRDOY

      YR  = INT(YRDOY / 1000)
      DOY = YRDOY - YR * 1000

      END SUBROUTINE YR_DOY
