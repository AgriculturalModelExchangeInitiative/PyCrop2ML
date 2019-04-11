import numpy as np 
from math import *

def phyllochron_(float fixPhyll=5.0,
                 float leafNumber=0.0,
                 float lincr=8.0,
                 float ldecr=10.0,
                 float pdecr=0.4,
                 float pincr=1.5,
                 float ptq=0.0,
                 float gai=0.0,
                 float pastMaxAI=0.0,
                 float kl=0.45,
                 float aPTQ=0.842934,
                 float phylPTQ1=20.0,
                 float p=120.0,
                 str choosePhyllUse='Default'):
    """


    Phyllochron Model
    Author: Pierre Martre
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: Calculate different types of phyllochron 

    """
    cdef float phyllochron
    cdef float gai_
    if choosePhyllUse =="Default":
        if (leafNumber < ldecr): phyllochron = fixPhyll * pdecr
        elif (leafNumber >= ldecr and leafNumber < lincr): phyllochron = fixPhyll
        else: phyllochron = fixPhyll * pincr
    if choosePhyllUse =="PTQ":
        gai_ = max(pastMaxAI,gai)
        pastMaxAI = gai_
        if (gai_ > 0.0): phyllochron = phylPTQ1 * ((gai_ * kl) / (1 - exp(-kl * gai_))) / (ptq + aPTQ)
        else: phyllochron = phylPTQ1      
    if choosePhyllUse == "Test":
        if (leafNumber < ldecr): phyllochron = p * pdecr
        elif (leafNumber >= ldecr and leafNumber < lincr): phyllochron = p
        else: phyllochron = p * pincr
    return  phyllochron, pastMaxAI
