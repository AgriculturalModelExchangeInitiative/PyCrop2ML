# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_updatephase(vernaprog,
         phyllochron,
         isMomentRegistredZC_39,
         minFinalNumber,
         leafNumber_t1,
         finalLeafNumber_t1,
         hasLastPrimordiumAppeared_t1,
         phase_t1,
         cumulTT,
         cumulTTFromZC_39,
         gAI,
         grainCumulTT,
         dayLength,
         fixPhyll,
         cumulTTFromZC_91,
         isVernalizable,
         dse,
         pFLLAnth,
         dcd,
         dgf,
         degfm,
         maxDL,
         sLDL,
         ignoreGrainMaturation,
         pHEADANTH,
         choosePhyllUse,
         p):
    """
     - Name: UpdatePhase -Version: 001, -Time step: 1
     - Description:
                 * Title: UpdatePhase model
                 * Author: Pierre MARTRE
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: vernaprog
                               ** datatype : DOUBLE
                               ** default : 0.5517254187376879
                               ** description : progression on a 0  to 1 scale of the vernalization
                               ** inputtype : variable
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: phyllochron
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : phyllochron
                               ** inputtype : variable
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                               ** variablecategory : state
                 * name: isMomentRegistredZC_39
                               ** datatype : INT
                               ** default : 
                               ** description :  if Flag leaf ligule has already appeared 
                               ** inputtype : variable
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: minFinalNumber
                               ** datatype : DOUBLE
                               ** default : 5.5
                               ** description : minimum final leaf number
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: leafNumber_t1
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: finalLeafNumber_t1
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : final leaf number
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: hasLastPrimordiumAppeared_t1
                               ** datatype : INT
                               ** default : 0
                               ** description : if Last Primordium has Appeared
                               ** inputtype : variable
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: phase_t1
                               ** datatype : DOUBLE
                               ** default : 1
                               ** description :  the name of the phase
                               ** inputtype : variable
                               ** max : 7
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: cumulTT
                               ** datatype : DOUBLE
                               ** default : 112.330110409888
                               ** description : cumul thermal times at currentdate
                               ** inputtype : variable
                               ** max : 10000
                               ** min : -200
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: cumulTTFromZC_39
                               ** datatype : DOUBLE
                               ** default : 
                               ** description :  cumul TT from FlagLeafLiguleJustVisible to current date 
                               ** inputtype : variable
                               ** max : 5000
                               ** min : 0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: gAI
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Green Area Index of the day
                               ** inputtype : variable
                               ** max : 500.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : auxiliary
                 * name: grainCumulTT
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : cumulTT used for the grain developpment
                               ** inputtype : variable
                               ** max : 10000
                               ** min : 0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: dayLength
                               ** datatype : DOUBLE
                               ** default : 12.3037621834005
                               ** description : day length
                               ** inputtype : variable
                               ** max : 10000
                               ** min : 0
                               ** unit : mm2 m-2
                               ** variablecategory : auxiliary
                 * name: fixPhyll
                               ** datatype : DOUBLE
                               ** default : 
                               ** description :  Phyllochron Varietal parameter 
                               ** inputtype : variable
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                               ** variablecategory : auxiliary
                 * name: cumulTTFromZC_91
                               ** datatype : DOUBLE
                               ** default : 
                               ** description :  cumul TT from EndGrainFilling to current date 
                               ** inputtype : variable
                               ** max : 4000D
                               ** min : 0
                               ** unit : Â°C d
                               ** variablecategory : auxiliary
                 * name: isVernalizable
                               ** datatype : INT
                               ** default : 1
                               ** description : true if the plant is vernalizable
                               ** inputtype : parameter
                               ** max : 1
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
                 * name: dse
                               ** datatype : DOUBLE
                               ** default : 105
                               ** description : Thermal time from sowing to emergence
                               ** inputtype : parameter
                               ** max : 1000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d
                 * name: pFLLAnth
                               ** datatype : DOUBLE
                               ** default : 2.22
                               ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
                               ** inputtype : parameter
                               ** max : 1000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
                 * name: dcd
                               ** datatype : DOUBLE
                               ** default : 100
                               ** description : Duration of the endosperm cell division phase
                               ** inputtype : parameter
                               ** max : 10000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d
                 * name: dgf
                               ** datatype : DOUBLE
                               ** default : 450
                               ** description : Grain filling duration (from anthesis to physiological maturity)
                               ** inputtype : parameter
                               ** max : 10000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d
                 * name: degfm
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
                               ** inputtype : parameter
                               ** max : 50
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d
                 * name: maxDL
                               ** datatype : DOUBLE
                               ** default : 15
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                               ** inputtype : parameter
                               ** max : 24
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : h
                 * name: sLDL
                               ** datatype : DOUBLE
                               ** default : 0.85
                               ** description : Daylength response of leaf production
                               ** inputtype : parameter
                               ** max : 1
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : leaf h-1
                 * name: ignoreGrainMaturation
                               ** datatype : INT
                               ** default : 0
                               ** description : true to ignore grain maturation
                               ** inputtype : parameter
                               ** max : 0
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
                 * name: pHEADANTH
                               ** datatype : DOUBLE
                               ** default : 1
                               ** description : Number of phyllochron between heading and anthesiss
                               ** inputtype : parameter
                               ** max : 1000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : 
                 * name: choosePhyllUse
                               ** datatype : STRING
                               ** default : 
                               ** description : Switch to choose the type of phyllochron calculation to be used
                               ** inputtype : parameter
                               ** max : 
                               ** min : 
                               ** parametercategory : constant
                               ** unit : 
                 * name: p
                               ** datatype : DOUBLE
                               ** default : 120
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** max : 1000
                               ** min : 0
                               ** parametercategory : constant
                               ** unit : Â°C d leaf-1
     - outputs:
                 * name: finalLeafNumber
                               ** datatype : DOUBLE
                               ** description : final leaf number
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: phase
                               ** datatype : DOUBLE
                               ** description :  the name of the phase
                               ** max : 7
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
                 * name: hasLastPrimordiumAppeared
                               ** datatype : INT
                               ** description : if Last Primordium has Appeared
                               ** max : 1
                               ** min : 0
                               ** unit : 
                               ** variablecategory : state
    """

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
    return (finalLeafNumber, phase, hasLastPrimordiumAppeared)