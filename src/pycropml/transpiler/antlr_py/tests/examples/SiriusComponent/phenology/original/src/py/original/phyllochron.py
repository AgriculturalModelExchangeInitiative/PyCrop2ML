# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

import numpy

#%%CyML Model Begin%%
def model_phyllochron(fixPhyll:float,
         lNeff:float,
         lARmin:float,
         lincr:float,
         B:float,
         pdecr:float,
         areaSS:float,
         sowingDensity:float,
         lARmax:float,
         gAImean:float,
         ptq:float,
         p:float,
         leafNumber:float,
         choosePhyllUse:str,
         areaSL:float,
         ldecr:float,
         pTQhf:float,
         pincr:float):
    """
     - Name: Phyllochron -Version: 001, -Time step: 1
     - Description:
                 * Title: Phyllochron model
                 * Authors: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: Calculate different types of phyllochron 
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
                 * name: lNeff
                               ** description : Leaf Number efficace
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : leaf
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
                 * name: B
                               ** description : Phyllochron at PTQ equal 1
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 20.0
                               ** unit : Â°C d leaf-1
                 * name: pdecr
                               ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10.0
                               ** min : 0.0
                               ** default : 0.4
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
                 * name: sowingDensity
                               ** description : Sowing Density
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : plant m-2
                 * name: lARmax
                               ** description : LAR maximum
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : leaf-1 Â°C
                 * name: gAImean
                               ** description : Mean Green Area Index
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 500.0
                               ** min : 0.0
                               ** default : 
                               ** unit : m2 leaf m-2 ground
                 * name: ptq
                               ** description : Photothermal quotient 
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 10000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : MJ Â°C-1 d-1 m-2)
                 * name: p
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 120.0
                               ** unit : Â°C d leaf-1
                 * name: leafNumber
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** max : 25
                               ** min : 0
                               ** default : 0
                               ** unit : leaf
                 * name: choosePhyllUse
                               ** description : Switch to choose the type of phyllochron calculation to be used
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : STRING
                               ** max : 
                               ** min : 
                               ** default : 
                               ** unit : -
                 * name: areaSL
                               ** description :  Area Leaf
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** min : 0.0
                               ** default : 0.0
                               ** unit : cm2
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
     - outputs:
                 * name: phyllochron
                               ** description : phyllochron
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
    """

    phyllochron:float
    gaiLim:float
    LAR:float
    phyllochron = 0.0
    LAR = 0.0
    gaiLim = lNeff * ((areaSL + areaSS) / 10000.0) * sowingDensity
    if choosePhyllUse == "Default":
        if leafNumber < ldecr:
            phyllochron = fixPhyll * pdecr
        elif leafNumber >= ldecr and leafNumber < lincr:
            phyllochron = fixPhyll
        else:
            phyllochron = fixPhyll * pincr
    if choosePhyllUse == "PTQ":
        if gAImean > gaiLim:
            LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gAImean)
        else:
            LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gaiLim)
        phyllochron = 1.0 / LAR
    if choosePhyllUse == "Test":
        if leafNumber < ldecr:
            phyllochron = p * pdecr
        elif leafNumber >= ldecr and leafNumber < lincr:
            phyllochron = p
        else:
            phyllochron = p * pincr
    return phyllochron
#%%CyML Model End%%