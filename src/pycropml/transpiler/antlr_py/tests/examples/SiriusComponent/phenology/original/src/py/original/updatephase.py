# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_updatephase(fixPhyll:float,
         hasLastPrimordiumAppeared_t1:int,
         minFinalNumber:float,
         ignoreGrainMaturation:int,
         cumulTTFromZC_39:float,
         phyllochron:float,
         maxDL:float,
         grainCumulTT:float,
         vernaprog:float,
         cumulTT:float,
         dayLength:float,
         isMomentRegistredZC_39:int,
         sLDL:float,
         pFLLAnth:float,
         finalLeafNumber_t1:float,
         degfm:float,
         cumulTTFromZC_91:float,
         phase_t1:float,
         p:float,
         gAI:float,
         leafNumber_t1:float,
         dgf:float,
         choosePhyllUse:str,
         isVernalizable:int,
         dse:float,
         pHEADANTH:float,
         dcd:float):
    """
     - Name: UpdatePhase -Version: 001, -Time step: 1
     - Description:
                 * Title: UpdatePhase model
                 * Authors: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: This strategy advances the phase and calculate the final leaf number    	
                 * ShortDescription: None
     - inputs:
                 * name: fixPhyll
                               ** description :  Phyllochron Varietal parameter 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 
                               ** unit : Â°C d leaf-1
                 * name: hasLastPrimordiumAppeared_t1
                               ** description : if Last Primordium has Appeared
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 0
                               ** unit : 
                 * name: minFinalNumber
                               ** description : minimum final leaf number
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 5.5
                               ** unit : leaf
                 * name: ignoreGrainMaturation
                               ** description : true to ignore grain maturation
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 0
                               ** min : 0
                               ** default : 0
                               ** unit : 
                 * name: cumulTTFromZC_39
                               ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 5000
                               ** min : 0
                               ** default : 
                               ** unit : Â°C d
                 * name: phyllochron
                               ** description : phyllochron
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0
                               ** unit : Â°C d leaf-1
                 * name: maxDL
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 24
                               ** min : 0
                               ** default : 15
                               ** unit : h
                 * name: grainCumulTT
                               ** description : cumulTT used for the grain developpment
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 0
                               ** unit : Â°C d
                 * name: vernaprog
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.5517254187376879
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
                 * name: dayLength
                               ** description : day length
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 12.3037621834005
                               ** unit : mm2 m-2
                 * name: isMomentRegistredZC_39
                               ** description :  if Flag leaf ligule has already appeared 
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 
                               ** unit : 
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
                 * name: cumulTTFromZC_91
                               ** description :  cumul TT from EndGrainFilling to current date 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 4000
                               ** min : 0
                               ** default : 
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
                 * name: p
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 120
                               ** unit : Â°C d leaf-1
                 * name: gAI
                               ** description : Green Area Index of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 500.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : m2 leaf m-2 ground
                 * name: leafNumber_t1
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
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
                 * name: isVernalizable
                               ** description : true if the plant is vernalizable
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
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
     - outputs:
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
    """

    phase:float
    hasLastPrimordiumAppeared:int
    finalLeafNumber:float
    ttFromLastLeafToHeading:float
    appFLN:float
    localDegfm:float
    ttFromLastLeafToAnthesis:float
    hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1
    finalLeafNumber = finalLeafNumber_t1
    phase = phase_t1
    if phase_t1 >= 0.0 and phase_t1 < 1.0:
        if cumulTT >= dse:
            phase = 1.0
        else:
            phase = phase_t1
    elif phase_t1 >= 1.0 and phase_t1 < 2.0:
        if isVernalizable == 1 and vernaprog >= 1.0 or isVernalizable == 0:
            if dayLength > maxDL:
                finalLeafNumber = minFinalNumber
                hasLastPrimordiumAppeared = 1
            else:
                appFLN = minFinalNumber + (sLDL * (maxDL - dayLength))
                if appFLN / 2.0 <= leafNumber_t1:
                    finalLeafNumber = appFLN
                    hasLastPrimordiumAppeared = 1
                else:
                    phase = phase_t1
            if hasLastPrimordiumAppeared == 1:
                phase = 2.0
        else:
            phase = phase_t1
    elif phase_t1 >= 2.0 and phase_t1 < 4.0:
        if isMomentRegistredZC_39 == 1:
            if phase_t1 < 3.0:
                ttFromLastLeafToHeading = 0.0
                if choosePhyllUse == "Default":
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll
                elif choosePhyllUse == "PTQ":
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
                elif choosePhyllUse == "Test":
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                if cumulTTFromZC_39 >= ttFromLastLeafToHeading:
                    phase = 3.0
                else:
                    phase = phase_t1
            else:
                phase = phase_t1
            ttFromLastLeafToAnthesis = 0.0
            if choosePhyllUse == "Default":
                ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
            elif choosePhyllUse == "PTQ":
                ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
            elif choosePhyllUse == "Test":
                ttFromLastLeafToAnthesis = pFLLAnth * p
            if cumulTTFromZC_39 >= ttFromLastLeafToAnthesis:
                phase = 4.0
        else:
            phase = phase_t1
    elif phase_t1 == 4.0:
        if grainCumulTT >= dcd:
            phase = 4.5
        else:
            phase = phase_t1
    elif phase_t1 == 4.5:
        if grainCumulTT >= dgf or gAI <= 0.0:
            phase = 5.0
        else:
            phase = phase_t1
    elif phase_t1 >= 5.0 and phase_t1 < 6.0:
        localDegfm = degfm
        if ignoreGrainMaturation:
            localDegfm = -1.0
        if cumulTTFromZC_91 >= localDegfm:
            phase = 6.0
        else:
            phase = phase_t1
    elif phase_t1 >= 6.0 and phase_t1 < 7.0:
        phase = phase_t1
    return (phase, hasLastPrimordiumAppeared, finalLeafNumber)
#%%CyML Model End%%