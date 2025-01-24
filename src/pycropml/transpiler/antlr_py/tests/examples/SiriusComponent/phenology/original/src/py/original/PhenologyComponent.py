# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

from original.Gaimean import model_gaimean
from original.Ptq import model_ptq
from original.Cumulttfrom import model_cumulttfrom
from original.Ismomentregistredzc_39 import model_ismomentregistredzc_39
from original.Vernalizationprogress import model_vernalizationprogress
from original.Phylsowingdatecorrection import model_phylsowingdatecorrection
from original.Updatephase import model_updatephase
from original.Leafnumber import model_leafnumber
from original.Shootnumber import model_shootnumber
from original.Updateleafflag import model_updateleafflag
from original.Registerzadok import model_registerzadok
from original.Updatecalendar import model_updatecalendar
from original.Phyllochron import model_phyllochron

#%%CyML Model Begin%%
def model_phenology(deltaTT:float,
         gAI:float,
         tTWindowForPTQ:float,
         listTTShootWindowForPTQ1_t1:List[float],
         pastMaxAI_t1:float,
         listGAITTWindowForPTQ_t1:List[float],
         listPARTTWindowForPTQ_t1:List[float],
         pAR:float,
         listTTShootWindowForPTQ_t1:List[float],
         kl:float,
         cumulTT:float,
         calendarCumuls_t1:List[float],
         calendarMoments_t1:List[str],
         intTvern:float,
         minTvern:float,
         vBEE:float,
         calendarDates_t1:List[datetime],
         maxDL:float,
         pNini:float,
         dayLength:float,
         vernaprog_t1:float,
         aMXLFNO:float,
         maxTvern:float,
         vAI:float,
         leafNumber_t1:float,
         isVernalizable:int,
         minDL:float,
         minFinalNumber_t1:float,
         currentdate:datetime,
         p:float,
         sDsa_nh:float,
         sowingDay:int,
         sDsa_sh:float,
         latitude:float,
         rp:float,
         sDws:int,
         hasLastPrimordiumAppeared_t1:int,
         ignoreGrainMaturation:int,
         grainCumulTT:float,
         sLDL:float,
         pFLLAnth:float,
         finalLeafNumber_t1:float,
         degfm:float,
         phase_t1:float,
         dgf:float,
         choosePhyllUse:str,
         dse:float,
         pHEADANTH:float,
         dcd:float,
         phyllochron_t1:float,
         tilleringProfile_t1:List[float],
         sowingDensity:float,
         leafTillerNumberArray_t1:List[int],
         targetFertileShoot:float,
         canopyShootNumber_t1:float,
         hasFlagLeafLiguleAppeared_t1:int,
         intTSFLN:float,
         der:float,
         slopeTSFLN:float,
         currentZadokStage_t1:str,
         lNeff:float,
         B:float,
         lARmin:float,
         lincr:float,
         lARmax:float,
         areaSL:float,
         pdecr:float,
         ldecr:float,
         pTQhf:float,
         pincr:float,
         areaSS:float):
    """
     - Name: Phenology -Version: 001, -Time step: 1
     - Description:
                 * Title: Phenology model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA/LEPSE
                 * ExtendedDescription: see documentation
                 * ShortDescription: None
     - inputs:
                 * name: deltaTT
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 100.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d
                 * name: gAI
                               ** description : Green Area Index of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 500.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: tTWindowForPTQ
                               ** description : Thermal Time window for average
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 5000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d
                 * name: listTTShootWindowForPTQ1_t1
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: pastMaxAI_t1
                               ** description : Maximum Leaf Area Index reached the current day
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 5000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: listGAITTWindowForPTQ_t1
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : m2 leaf m-2 ground
                 * name: listPARTTWindowForPTQ_t1
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : MJ m2 d
                 * name: pAR
                               ** description : Daily Photosyntetically Active Radiation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : MJ mÂ² d
                 * name: listTTShootWindowForPTQ_t1
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: kl
                               ** description : Exctinction Coefficient
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** min : 0.0
                               ** default : 0.45
                               ** unit : 
                 * name: cumulTT
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : -200
                               ** default : 112.330110409888
                               ** unit : Â°C d
                 * name: calendarCumuls_t1
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : Â°C d
                 * name: calendarMoments_t1
                               ** description : List containing appearance of each stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: intTvern
                               ** description : Intermediate temperature for vernalization to occur
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 60
                               ** min : -20
                               ** default : 11.0
                               ** unit : Â°C
                 * name: minTvern
                               ** description : Minimum temperature for vernalization to occur
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 60
                               ** min : -20
                               ** default : 0.0
                               ** unit : Â°C
                 * name: vBEE
                               ** description : Vernalization rate at 0Â°C
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.01
                               ** unit : d-1
                 * name: calendarDates_t1
                               ** description : List containing  the dates of the wheat developmental phases
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: maxDL
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 0
                               ** default : 15.0
                               ** unit : h
                 * name: pNini
                               ** description : Number of primorida in the apex at emergence
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 0
                               ** default : 4.0
                               ** unit : primordia
                 * name: dayLength
                               ** description : day length
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 12.3037621834005
                               ** unit : mm2 m-2
                 * name: vernaprog_t1
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.5517254187376879
                               ** unit : 
                 * name: aMXLFNO
                               ** description : Absolute maximum leaf number
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 24.0
                               ** unit : leaf
                 * name: maxTvern
                               ** description : Maximum temperature for vernalization to occur
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 60
                               ** min : -20
                               ** default : 23.0
                               ** unit : Â°C
                 * name: vAI
                               ** description : Response of vernalization rate to temperature
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.015
                               ** unit : d-1 Â°C-1
                 * name: leafNumber_t1
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: isVernalizable
                               ** description : true if the plant is vernalizable
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: minDL
                               ** description : Threshold daylength below which it does influence vernalization rate
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 12
                               ** default : 8.0
                               ** unit : h
                 * name: minFinalNumber_t1
                               ** description : minimum final leaf number
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 5.5
                               ** unit : leaf
                 * name: currentdate
                               ** description : current date 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: p
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 120
                               ** unit : Â°C d leaf-1
                 * name: sDsa_nh
                               ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 365
                               ** min : 1
                               ** default : 1.0
                               ** unit : d
                 * name: sowingDay
                               ** description : Day of Year at sowing
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 365
                               ** min : 1
                               ** default : 1
                               ** unit : d
                 * name: sDsa_sh
                               ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 365
                               ** min : 1
                               ** default : 1.0
                               ** unit : d
                 * name: latitude
                               ** description : Latitude
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 90
                               ** min : -90
                               ** default : 0.0
                               ** unit : Â°
                 * name: rp
                               ** description : Rate of change of Phyllochrone with sowing date
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 365
                               ** min : 0
                               ** default : 0
                               ** unit : d-1
                 * name: sDws
                               ** description : Sowing date at which Phyllochrone is minimum
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 365
                               ** min : 1
                               ** default : 1
                               ** unit : d
                 * name: hasLastPrimordiumAppeared_t1
                               ** description : if Last Primordium has Appeared
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 0
                               ** unit : 
                 * name: ignoreGrainMaturation
                               ** description : true to ignore grain maturation
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 0
                               ** min : 0
                               ** default : 0
                               ** unit : 
                 * name: grainCumulTT
                               ** description : cumulTT used for the grain developpment
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 0
                               ** unit : Â°C d
                 * name: sLDL
                               ** description : Daylength response of leaf production
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.85
                               ** unit : leaf h-1
                 * name: pFLLAnth
                               ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 2.22
                               ** unit : 
                 * name: finalLeafNumber_t1
                               ** description : final leaf number
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: degfm
                               ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 50
                               ** min : 0
                               ** default : 0
                               ** unit : Â°C d
                 * name: phase_t1
                               ** description :  the name of the phase
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 7
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: dgf
                               ** description : Grain filling duration (from anthesis to physiological maturity)
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 450
                               ** unit : Â°C d
                 * name: choosePhyllUse
                               ** description : Switch to choose the type of phyllochron calculation to be used
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : STRING
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: dse
                               ** description : Thermal time from sowing to emergence
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 105
                               ** unit : Â°C d
                 * name: pHEADANTH
                               ** description : Number of phyllochron between heading and anthesiss
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: dcd
                               ** description : Duration of the endosperm cell division phase
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 100
                               ** unit : Â°C d
                 * name: phyllochron_t1
                               ** description : phyllochron
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0
                               ** unit : Â°C d leaf-1
                 * name: tilleringProfile_t1
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: sowingDensity
                               ** description : number of plant /mÂ²
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 500
                               ** min : 0
                               ** default : 288.0
                               ** unit : plant m-2
                 * name: leafTillerNumberArray_t1
                               ** description : store the number of tiller for each leaf layer
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INTLIST
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : leaf
                 * name: targetFertileShoot
                               ** description : max value of shoot number for the canopy
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 280
                               ** default : 600.0
                               ** unit : shoot
                 * name: canopyShootNumber_t1
                               ** description : shoot number for the whole canopy
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 288.0
                               ** unit : shoot m-2
                 * name: hasFlagLeafLiguleAppeared_t1
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
                 * name: intTSFLN
                               ** description : Intercept of the relationship between Haun stage at terminal spikelet and final leaf number
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 2.6
                               ** unit : 
                 * name: der
                               ** description : Duration of the endosperm endoreduplication phase
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 300.0
                               ** unit : Â°C d
                 * name: slopeTSFLN
                               ** description : Slope of the relationship between Haun stage at terminal spikelet and final leaf number
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 0.9
                               ** unit : 
                 * name: currentZadokStage_t1
                               ** description : zadok stage
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : STRING
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : 
                 * name: lNeff
                               ** description : Leaf Number efficace
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : leaf
                 * name: B
                               ** description : Phyllochron at PTQ equal 1
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 20.0
                               ** unit : Â°C d leaf-1
                 * name: lARmin
                               ** description : LAR minimum
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : leaf-1 Â°C
                 * name: lincr
                               ** description : Leaf number above which the phyllochron is increased by Pincr
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 30.0
                               ** min : 0.0
                               ** default : 8.0
                               ** unit : leaf
                 * name: lARmax
                               ** description : LAR maximum
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : leaf-1 Â°C
                 * name: areaSL
                               ** description :  Area Leaf
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : cm2
                 * name: pdecr
                               ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10.0
                               ** min : 0.0
                               ** default : 0.4
                               ** unit : -
                 * name: ldecr
                               ** description : Leaf number up to which the phyllochron is decreased by Pdecr
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : leaf
                 * name: pTQhf
                               ** description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : Â°C d leaf-1
                 * name: pincr
                               ** description : Factor increasing the phyllochron for leaf number higher than Lincr
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10.0
                               ** min : 0.0
                               ** default : 1.5
                               ** unit : -
                 * name: areaSS
                               ** description : Area Sheath
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : cm2
     - outputs:
                 * name: listGAITTWindowForPTQ
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : m2 leaf m-2 ground
                 * name: pastMaxAI
                               ** description : Maximum Leaf Area Index reached the current day
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 5000.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: listTTShootWindowForPTQ1
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                 * name: gAImean
                               ** description : Mean Green Area Index
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 500.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: listTTShootWindowForPTQ
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                 * name: listPARTTWindowForPTQ
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : MJ m2 d
                 * name: ptq
                               ** description : Photothermal quotient 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000.0
                               ** min : 0.0
                               ** unit : MJ Â°C-1 d-1 m-2)
                 * name: cumulTTFromZC_65
                               ** description :  cumul TT from Anthesis to current date 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : -5000
                               ** min : 0
                               ** unit : Â°C d
                 * name: cumulTTFromZC_91
                               ** description :  cumul TT from EndGrainFilling to current date 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 4000
                               ** min : 0
                               ** unit : Â°C d
                 * name: cumulTTFromZC_39
                               ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : Â°C d
                 * name: isMomentRegistredZC_39
                               ** description :  if Flag leaf ligule has already appeared 
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
                 * name: minFinalNumber
                               ** description : minimum final leaf number
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                 * name: calendarCumuls
                               ** description : list containing for each stage occured its cumulated thermal times
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : Â°C d
                 * name: vernaprog
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
                 * name: calendarMoments
                               ** description : List containing appearance of each stage
                               ** datatype : STRINGLIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
                 * name: calendarDates
                               ** description : List containing  the dates of the wheat developmental phases
                               ** datatype : DATELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
                 * name: fixPhyll
                               ** description :  Phyllochron Varietal parameter 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                 * name: phase
                               ** description :  the name of the phase
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 7
                               ** min : 0
                               ** unit : 
                 * name: hasLastPrimordiumAppeared
                               ** description : if Last Primordium has Appeared
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
                 * name: finalLeafNumber
                               ** description : final leaf number
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                 * name: leafNumber
                               ** description : Actual number of phytomers
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                 * name: averageShootNumberPerPlant
                               ** description : average shoot number per plant in the canopy
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                 * name: leafTillerNumberArray
                               ** description : store the number of tiller for each leaf layer
                               ** datatype : INTLIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : leaf
                 * name: canopyShootNumber
                               ** description : shoot number for the whole canopy
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : shoot m-2
                 * name: numberTillerCohort
                               ** description : Number of tiller which appears
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : dimensionless
                 * name: tilleringProfile
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                               ** datatype : DOUBLELIST
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
                 * name: hasFlagLeafLiguleAppeared
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
                 * name: currentZadokStage
                               ** description : zadok stage
                               ** datatype : STRING
                               ** variablecategory : state
                               ** max : 
                               ** min : 
                               ** unit : 
                 * name: hasZadokStageChanged
                               ** description : true if the zadok stage has changed this time step
                               ** datatype : INT
                               ** variablecategory : state
                               ** max : 1
                               ** min : 0
                               ** unit : 
                 * name: phyllochron
                               ** description : phyllochron
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
    """

    listGAITTWindowForPTQ:List[float] = []
    pastMaxAI:float
    listTTShootWindowForPTQ1:List[float] = []
    gAImean:float
    listTTShootWindowForPTQ:List[float] = []
    listPARTTWindowForPTQ:List[float] = []
    ptq:float
    cumulTTFromZC_65:float
    cumulTTFromZC_91:float
    cumulTTFromZC_39:float
    isMomentRegistredZC_39:int
    minFinalNumber:float
    calendarCumuls:List[float] = []
    vernaprog:float
    calendarMoments:List[str] = []
    calendarDates:List[datetime] = []
    fixPhyll:float
    phyllochron:float
    phase:float
    hasLastPrimordiumAppeared:int
    finalLeafNumber:float
    hasFlagLeafLiguleAppeared:int
    leafNumber:float
    averageShootNumberPerPlant:float
    leafTillerNumberArray:List[int] = []
    canopyShootNumber:float
    numberTillerCohort:int
    tilleringProfile:List[float] = []
    currentZadokStage:str
    hasZadokStageChanged:int
    (listGAITTWindowForPTQ, pastMaxAI, listTTShootWindowForPTQ1, gAImean) = model_gaimean(deltaTT, gAI, tTWindowForPTQ, listTTShootWindowForPTQ1_t1, pastMaxAI_t1, listGAITTWindowForPTQ_t1)
    (cumulTTFromZC_65, cumulTTFromZC_91, cumulTTFromZC_39) = model_cumulttfrom(cumulTT, calendarMoments_t1, calendarCumuls_t1)
    isMomentRegistredZC_39 = model_ismomentregistredzc_39(calendarMoments_t1)
    (minFinalNumber, calendarCumuls, vernaprog, calendarMoments, calendarDates) = model_vernalizationprogress(intTvern, minTvern, vBEE, calendarDates_t1, deltaTT, maxDL, pNini, dayLength, cumulTT, calendarMoments_t1, vernaprog_t1, aMXLFNO, maxTvern, calendarCumuls_t1, vAI, leafNumber_t1, isVernalizable, minDL, minFinalNumber_t1, currentdate)
    fixPhyll = model_phylsowingdatecorrection(p, sDsa_nh, sowingDay, sDsa_sh, latitude, rp, sDws)
    (listTTShootWindowForPTQ, listPARTTWindowForPTQ, ptq) = model_ptq(deltaTT, listPARTTWindowForPTQ_t1, listGAITTWindowForPTQ, pAR, listTTShootWindowForPTQ_t1, kl, tTWindowForPTQ)
    (phase, hasLastPrimordiumAppeared, finalLeafNumber) = model_updatephase(fixPhyll, hasLastPrimordiumAppeared_t1, minFinalNumber, ignoreGrainMaturation, cumulTTFromZC_39, phyllochron, maxDL, grainCumulTT, vernaprog, cumulTT, dayLength, isMomentRegistredZC_39, sLDL, pFLLAnth, finalLeafNumber_t1, degfm, cumulTTFromZC_91, phase_t1, p, gAI, leafNumber_t1, dgf, choosePhyllUse, isVernalizable, dse, pHEADANTH, dcd)
    leafNumber = model_leafnumber(deltaTT, phyllochron_t1, hasFlagLeafLiguleAppeared, leafNumber_t1, phase)
    (averageShootNumberPerPlant, leafTillerNumberArray, canopyShootNumber, numberTillerCohort, tilleringProfile) = model_shootnumber(tilleringProfile_t1, sowingDensity, leafNumber, leafTillerNumberArray_t1, targetFertileShoot, canopyShootNumber_t1)
    (calendarCumuls, calendarMoments, calendarDates, hasFlagLeafLiguleAppeared) = model_updateleafflag(calendarCumuls, finalLeafNumber, calendarMoments, calendarDates, cumulTT, leafNumber, hasFlagLeafLiguleAppeared_t1, phase, currentdate)
    phyllochron = model_phyllochron(fixPhyll, lNeff, lARmin, lincr, B, pdecr, areaSS, sowingDensity, lARmax, gAImean, ptq, p, leafNumber, choosePhyllUse, areaSL, ldecr, pTQhf, pincr)
    (calendarCumuls, currentZadokStage, calendarMoments, calendarDates, hasZadokStageChanged) = model_registerzadok(calendarCumuls, finalLeafNumber, cumulTTFromZC_65, calendarMoments, cumulTT, calendarDates, intTSFLN, der, leafNumber, slopeTSFLN, currentZadokStage_t1, phase, currentdate)
    (calendarCumuls, calendarMoments, calendarDates) = model_updatecalendar(calendarCumuls, calendarMoments, cumulTT, calendarDates, phase, currentdate)
    return (listGAITTWindowForPTQ, pastMaxAI, listTTShootWindowForPTQ1, gAImean, listTTShootWindowForPTQ, listPARTTWindowForPTQ, ptq, cumulTTFromZC_65, cumulTTFromZC_91, cumulTTFromZC_39, isMomentRegistredZC_39, minFinalNumber, calendarCumuls, vernaprog, calendarMoments, calendarDates, fixPhyll, phase, hasLastPrimordiumAppeared, finalLeafNumber, leafNumber, averageShootNumberPerPlant, leafTillerNumberArray, canopyShootNumber, numberTillerCohort, tilleringProfile, hasFlagLeafLiguleAppeared, currentZadokStage, hasZadokStageChanged, phyllochron)
#%%CyML Model End%%