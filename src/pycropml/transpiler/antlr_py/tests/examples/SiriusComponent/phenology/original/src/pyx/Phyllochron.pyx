import numpy 
from math import *
def model_phyllochron(float fixPhyll,
                      float lNeff,
                      float lARmin,
                      float lincr,
                      float B,
                      float pdecr,
                      float areaSS,
                      float sowingDensity,
                      float lARmax,
                      float gAImean,
                      float ptq,
                      float p,
                      float leafNumber,
                      str choosePhyllUse,
                      float areaSL,
                      float ldecr,
                      float pTQhf,
                      float pincr):
    """

    Phyllochron model
    Author: Pierre Martre
    Reference: ('',)
    Institution: INRA Montpellier
    ExtendedDescription: Calculate different types of phyllochron 
    ShortDescription: None

    """
    cdef float phyllochron
    cdef float gaiLim 
    cdef float LAR 
    phyllochron=0.0
    LAR=0.0
    gaiLim=lNeff * ((areaSL + areaSS) / 10000.0) * sowingDensity
    if choosePhyllUse == "Default":
        if leafNumber < ldecr:
            phyllochron=fixPhyll * pdecr
        elif leafNumber >= ldecr and leafNumber < lincr:
            phyllochron=fixPhyll
        else:
            phyllochron=fixPhyll * pincr
    if choosePhyllUse == "PTQ":
        if gAImean > gaiLim:
            LAR=(lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gAImean)
        else:
            LAR=(lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gaiLim)
        phyllochron=1.0 / LAR
    if choosePhyllUse == "Test":
        if leafNumber < ldecr:
            phyllochron=p * pdecr
        elif leafNumber >= ldecr and leafNumber < lincr:
            phyllochron=p
        else:
            phyllochron=p * pincr
    return  phyllochron


