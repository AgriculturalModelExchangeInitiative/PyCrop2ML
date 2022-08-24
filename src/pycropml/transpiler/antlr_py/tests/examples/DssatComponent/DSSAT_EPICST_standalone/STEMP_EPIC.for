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
C  @ShortDescription
C  Determines soil temperature by layer
C
C  @ExtendedDescription
C
C  @Timestep 1day
C  @Version 1.0
C-----------------------------------------------------------------------
C  @Author
C  Kenneth N. Potter (USDA-ARS)
C  @Author
C  Jimmy R. Williams (USDA-ARS)
C  
C  @Reference
C  https://doi.org/10.2134/agronj1994.00021962008600060014x
C------------------------------------------------------------------------
C
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
     &    SOILPROP,CUMDPT,DSMID, SW,   !Input
     &    TAVG, TMAX, TMIN, TAV, WEATHER,   !Input
     &    SRFTEMP, NDays, TDL, WetDay, ST,TMA)         !InOut

C-----------------------------------------------------------------------
      USE ModuleDefs
      USE ModuleData

      IMPLICIT  NONE
      SAVE
!%%CyML Ignore Begin%%
      CHARACTER*1  RNMODE
      INTEGER DYNAMIC
      INTEGER RUN, YRDOY, YEAR
      INTEGER LUNIO
      CHARACTER*6, PARAMETER :: ERRKEY = "EPIC STEMP"
      CHARACTER*30 FILEIO
      CHARACTER*78 MSG(3)
!%%CyML Ignore End%%

      CHARACTER*1 ISWWAT
      INTEGER DOY, I, L, NLAYR
      INTEGER WetDay(30), NDays, NWetDays
      REAL ABD, B, CUMDPT 
      REAL DP, FX, PESW, SRFTEMP 
      REAL TAV, TAMP, TAVG, TBD, TMAX, TMIN, WW
      REAL TDL, TLL, TSW
      REAL TMA(5), X2_AVG
      REAL DEPIR, WFT, BCV, RAIN, BIOMAS, MULCHMASS
      REAL SNOW, CV, BCV1, BCV2, X2_PREV
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
        X2_PREV = 0.0
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
     &    TMA,X2_PREV, ST, SRFTEMP, X2_AVG)                       !Output
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
      X2_PREV = 0.0
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
        DO I = 1, 29
          WetDay(I) = WetDay(I+1)
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
     &    TMA,X2_PREV, ST, SRFTEMP, X2_AVG)                       !Output
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
     &    TMA,X2_PREV,ST,                                             !InOut
     &    SRFTEMP, X2_AVG)                      !Output
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
!%%CyML Description Begin%%
! ABD      Average bulk density for soil profile (g [soil] / cm3 [soil]) 
!            () auxiliary variable
! B        Exponential decay factor (Parton and Logan) (in subroutine 
!            HTEMP) 
! BIOMAS    Biomass  (kg/ha) () exogenous variable
! BD(NL)    Bulk density, soil layer NL (g [soil] / cm3 [soil]) () soil parameter
! CONTROL  Composite variable containing variables related to control 
!            and/or timing of simulation.    See Appendix A. 
! CUMDPT   Cumulative depth of soil profile (mm) () state variable
! DD        
! DLAYR(NL) Thickness of soil layer NL (cm) () constant parameter
! DEPIR    Depth of irrigation  () exogenous variable
! DP        
! DS(NL)    Cumulative depth in soil layer NL (cm) () soil parameter
! DSMID(NL)    Depth to midpoint of soil layer NL (cm) () state variable
! DUL(NL)   Volumetric soil water content at Drained Upper Limit in soil 
!            layer L (cm3[water]/cm3[soil]) () soil parameter
! ERRNUM   Error number for input 
! FILEIO   Filename for input file (e.g., IBSNAT35.INP) 
! FOUND    Indicator that good data was read from file by subroutine FIND 
!            (0 - End-of-file encountered, 1 - NAME was found) 
! FX        
! ICWD     Initial water table depth (cm)
! ISWITCH  Composite variable containing switches which control flow of 
!            execution for model.  The structure of the variable 
!            (SwitchType) is defined in ModuleDefs.for. 
! ISWWAT   Water simulation control switch (Y or N) (dimensionless) (Y) constant parameter
! LINC     Line number of input file 
! LL(NL)    Volumetric soil water content in soil layer NL at lower limit
!           (cm3 [water] / cm3 [soil]) () soil parameter
! LNUM     Current line number of input file 
! LUNIO    Logical unit number for FILEIO 
! MSG      Text array containing information to be written to WARNING.OUT 
!            file. 
! NLAYER    Number of soil layers (dimensionless) () constant parameter
! MSGCOUNT Number of lines of message text to be sent to WARNING.OUT 
! MULCHMASS  Mass of surface mulch layer (kg/ha) () exogenous variable
! NLAYR    Actual number of soil layers (dimensionless) () constant parameter
! NDays    Number of days ... (day) () state variable
! NL       Maximum number of soil layers  (dimensionless) () constant parameter
! PESW     Potential extractable soil water (= SW - LL) summed over root 
!            depth (cm)
! RNMODE    Simulation run mode (I=Interactive, A=All treatments, 
!             B=Batch mode, E=Sensitivity, D=Debug, N=Seasonal, Q=Sequence)
! RUN      Change in date between two observations for linear interpolation
! RAIN     daily rainfall (mm) () exogenous variable 
! SECTION  Section name in input file 
! SNOW     Snow cover (mm)  () exogenous variable
! SOILPROP Composite variable containing soil properties including bulk 
!            density, drained upper limit, lower limit, pH, saturation 
!            water content.  Structure defined in ModuleDefs. 
! SRFTEMP  Temperature of soil surface litter (degC) () state variable
! ST(NL)    Soil temperature in soil layer NL (degC) ()  state variable
! SW(NL)    Volumetric soil water content in layer NL
!           (cm3 [water] / cm3 [soil]) () soil parameter
! SWI(NL)   Initial soil water content (cm3[water]/cm3[soil])
! TAV      Average annual soil temperature, used with TAMP to calculate 
!            soil temperature. (degC) () exogenous variable
! TAVG     Average daily temperature (degC) () exogenous variable
! TAMP     Annual amplitude of the average air temperature (degC) () exogenous variable
! TMAX     Maximum Temperature (degC) () exogenous variable
! TMIN     Minimum Temperature (degC) () exogenous variable
! TBD      Sum of bulk density over soil profile 
! TDL      Total water content of soil at drained upper limit (cm) () state variable
! TLL      Total soil water in the profile at the lower limit of 
!            plant-extractable water (cm)
! TMA(5)   Array of previous 5 days of average soil temperatures. (degC) () state variable
! TMAX     Maximum daily temperature (degC) () exogenous variable
! TSW      Total soil water in profile (cm)
! WC        
! WW        
! YEAR     Year of current date of simulation 
! YRDOY    Current day of simulation (YYYYDDD)
! WetDay(30)   Wet Days (day) () state variable
! ZD
!%%CyML Description End%%
!=======================================================================
!<CyML Parametersets Start> 

! <Paramset start>
! paramset1, wetParam description of this set of parameters
!  NL = 4 
!  ISWWAT = 'Y'
!  BD    = 1.6
!  DLAYR = 10.2
!  DS = (/10.0,20.0 ,30.0, 40.0/)
!  DUL   = 0.3 
!  LL    = 0.2 
!  NLAYR = 4 
!  MSALB = 0.13
!  TDL = 12.0
! <Paramset end>

!!<CyML Parametersets End> 

!<CyML Testsets Start> 
!<CyML Test Start>
! test1, paramset1, the first test

! <Inputs start>
! ST = (/25.8049, 23.2596, 21.7681, 20.9658/)
! WetDay = (/0, 0, 0, 0/)
!  NDays = 0
! !  TAVG    = 25.0
!  TMAX    = 30.0
!  TMIN    = 20.0
!  TAV     = 20.0
!  TAMP    = 10.0
!  TAMP = 10.0
!  RAIN = 0.0
!  MULCHMASS = 0.0
!  SNOW = 0.0
!  SW      = 0.2
!  DEPIR = 0.0
!  BIOMAS = 0.0
!  TMA = (/27.5, 27.5, 27.5, 27.5/)
!  CUMDPT = 400.0
!  DSMID = (/50.0, 150.0, 250.0, 350.0, 0.0/)
!  SRFTEMP = 27.5
!  <Inputs end>

! <Outputs start>
! ST = (/25.8049, 23.2596, 21.7681, 20.9658/)
!  TMA = (/27.5, 27.5, 27.5, 27.5/)
!  CUMDPT = 400.0
!  DSMID = (/50.0, 150.0, 250.0, 350.0, 0.0/)
!  SRFTEMP = 27.5
! <Outputs end>

!<CyML Test End>
!<CyML Testsets End> 