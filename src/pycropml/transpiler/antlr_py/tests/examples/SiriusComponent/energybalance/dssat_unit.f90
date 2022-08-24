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
     &    SOILPROP,CUMDPT, ...)         !InOut

      USE ModuleDefs

      REAL ABD, B, CUMDPT 
      REAL, DIMENSION(NL) :: BD, DLAYR, DS

      TYPE (SoilType)    SOILPROP

      DS   = SOILPROP % DS     
      !!!!!!!....
      RETURN
      END SUBROUTINE STEMP_EPIC

      !%%CyML Description Begin%%

      ! CUMDPT   Cumulative depth of soil profile (mm) () state variable       
      ! DS(NL)    Cumulative depth in soil layer NL (cm) () soil parameter
      ! SOILPROP Composite variable containing soil properties 
      !
      ! %%CyML Description End%%
      








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
! MULCHMASS  Mulch Mass (kg/ha) () exogenous variable
! NLAYR    Actual number of soil layers (dimensionless) () constant parameter
! NDays    Number of days ... (day) () state variable
! NL       Number of soil layers (dimensionless) () constant parameter
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
!
! wetParam description of this set of parameters
!  NL = 4 
!  ISWWAT = 'Y'
!  BD    = 1.6
!  DLAYR = 10.2
!  DS = (/10.0,20.0 ,30.0, 40.0/)
!  DUL   = 0.3 
!  LL    = 0.2 
!  NLAYR = 4 
!  MSALB = 0.13
!  SRAD    = 20.0
!  SW      = 0.2
!  TAVG    = 25.0
!  TMAX    = 30.0
!  TMIN    = 20.0
!  XLAT    = 28.0
!  TAV     = 20.0
!  TAMP    = 10.0
!  TAMP = 10.0
!  RAIN = 0.0
!  MULCHMASS = 0.0
!  SNOW = 0.0
!  DEPIR = 0.0
!  BIOMAS = 0.0
!  TMA = (/27.5, 27.5, 27.5, 27.5/)
!  CUMDPT = 400.0
!  DSMID = (/50.0, 150.0, 250.0, 350.0, 0.0/)
!  SRFTEMP = 27.5
!  NDays = 0
!  TDL = 12.0
!  WetDay = (/0, 0, 0, 0/)
!  ST = (/25.8049, 23.2596, 21.7681, 20.9658/)

!!<CyML Parametersets End> 

!<CyML Testsets Start> 
!<CyML Testset Start>

!<CyML Testset End>
!<CyML Testsets End> 