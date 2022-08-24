# coding: utf8
from copy import copy
from array import array
from math import *

import numpy

def model_phyllochron(leafNumber,
         gAImean,
         ptq,
         fixPhyll,
         lincr,
         ldecr,
         pdecr,
         pincr,
         kl,
         pTQhf,
         B,
         p,
         choosePhyllUse,
         areaSL,
         areaSS,
         lARmin,
         lARmax,
         sowingDensity,
         lNeff):
    """
     - Name: Phyllochron -Version: 001, -Time step: 1
     - Description:
                 * Title: Phyllochron model
                 * Author: Pierre Martre
                 * Reference: ('',)
                 * Institution: INRA Montpellier
                 * ExtendedDescription: 
                 * ShortDescription: 
     - inputs:
                 * name: leafNumber
                               ** datatype : DOUBLE
                               ** default : 0
                               ** description : Actual number of phytomers
                               ** inputtype : variable
                               ** max : 25
                               ** min : 0
                               ** unit : leaf
                               ** variablecategory : state
                 * name: gAImean
                               ** datatype : DOUBLE
                               ** default : 
                               ** description : Mean Green Area Index
                               ** inputtype : variable
                               ** max : 500.0
                               ** min : 0.0
                               ** unit : m2 leaf m-2 ground
                               ** variablecategory : state
                 * name: ptq
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Photothermal quotient 
                               ** inputtype : variable
                               ** max : 10000.0
                               ** min : 0.0
                               ** unit : MJ Â°C-1 d-1 m-2)
                               ** variablecategory : state
                 * name: fixPhyll
                               ** datatype : DOUBLE
                               ** default : 
                               ** description :  Phyllochron Varietal parameter 
                               ** inputtype : variable
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                               ** variablecategory : auxiliary
                 * name: lincr
                               ** datatype : DOUBLE
                               ** default : 8.0
                               ** description : Leaf number above which the phyllochron is increased by Pincr
                               ** inputtype : parameter
                               ** max : 30.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : leaf
                 * name: ldecr
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Leaf number up to which the phyllochron is decreased by Pdecr
                               ** inputtype : parameter
                               ** max : 100.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : leaf
                 * name: pdecr
                               ** datatype : DOUBLE
                               ** default : 0.4
                               ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
                               ** inputtype : parameter
                               ** max : 10.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : -
                 * name: pincr
                               ** datatype : DOUBLE
                               ** default : 1.5
                               ** description : Factor increasing the phyllochron for leaf number higher than Lincr
                               ** inputtype : parameter
                               ** max : 10.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : -
                 * name: kl
                               ** datatype : DOUBLE
                               ** default : 0.45
                               ** description : Exctinction Coefficient
                               ** inputtype : parameter
                               ** max : 50.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : -
                 * name: pTQhf
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : Â°C d leaf-1
                 * name: B
                               ** datatype : DOUBLE
                               ** default : 20.0
                               ** description : Phyllochron at PTQ equal 1
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : Â°C d leaf-1
                 * name: p
                               ** datatype : DOUBLE
                               ** default : 120.0
                               ** description : Phyllochron (Varietal parameter)
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : Â°C d leaf-1
                 * name: choosePhyllUse
                               ** datatype : STRING
                               ** default : 
                               ** description : Switch to choose the type of phyllochron calculation to be used
                               ** inputtype : parameter
                               ** max : 
                               ** min : 
                               ** parametercategory : constant
                               ** unit : -
                 * name: areaSL
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description :  Area Leaf
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : cm2
                 * name: areaSS
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Area Sheath
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : cm2
                 * name: lARmin
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : LAR minimum
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : leaf-1 Â°C
                 * name: lARmax
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : LAR maximum
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : leaf-1 Â°C
                 * name: sowingDensity
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Sowing Density
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : plant m-2
                 * name: lNeff
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** description : Leaf Number efficace
                               ** inputtype : parameter
                               ** max : 1000.0
                               ** min : 0.0
                               ** parametercategory : constant
                               ** unit : leaf
     - outputs:
                 * name: phyllochron
                               ** datatype : DOUBLE
                               ** description : phyllochron
                               ** max : 1000
                               ** min : 0
                               ** unit : Â°C d leaf-1
                               ** variablecategory : state
    """

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