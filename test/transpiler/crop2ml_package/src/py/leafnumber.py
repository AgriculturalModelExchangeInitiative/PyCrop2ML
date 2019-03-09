import numpy
from math import *

def leafnumber_(deltaTT,phyllochron,hasFlagLeafLiguleAppeared,switchMaize,atip,leaf_tip_emerg,k_bl,nlim,leafNumber,cumulTTPhenoMaizeAtEmergence,cumulTT,phase):
    #- Description:
    #            - Model Name: CalculateLeafNumber Model
    #            - Author: Pierre MARTRE
    #            - Reference: Modeling development phase in the 
    #                Wheat Simulation Model SiriusQuality.
    #                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #            - Institution: INRA Montpellier
    #            - Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
    #- inputs:
    #            - name: deltaTT
    #                          - description : daily delta TT 
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : -20
    #                          - max : 100
    #                          - default : 23.5895677277199
    #                          - unit : °C d
    #                          - inputtype : variable
    #            - name: phyllochron
    #                          - description : phyllochron
    #                          - variablecategory : state
    #                          - inputtype : variable
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 1000
    #                          - default : 0
    #                          - unit : °C d leaf-1
    #            - name: hasFlagLeafLiguleAppeared
    #                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    #                          - variablecategory : state
    #                          - datatype : INT
    #                          - min : 0
    #                          - max : 1
    #                          - default : 0
    #                          - unit : 
    #                          - inputtype : variable
    #            - name: switchMaize
    #                          - description : true if maize
    #                          - parametercategory : constant
    #                          - datatype : INT
    #                          - min : 0
    #                          - max : 1
    #                          - default : 0
    #                          - unit : 
    #                          - inputtype : parameter
    #            - name: atip
    #                          - description : slope of leaf initiation
    #                          - parametercategory : species
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 1000
    #                          - default : 10
    #                          - unit : leaf °C-1 d-2
    #                          - inputtype : parameter
    #            - name: leaf_tip_emerg
    #                          - description : parameter for maize number of tip emerged
    #                          - parametercategory : species
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 1000
    #                          - default : 10
    #                          - unit : 
    #                          - inputtype : parameter
    #            - name: k_bl
    #                          - description : 
    #                          - parametercategory : constant
    #                          - inputtype : parameter
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 100
    #                          - default : 1.412
    #                          - unit : 
    #            - name: nlim
    #                          - description : 
    #                          - parametercategory : constant
    #                          - datatype : DOUBLE
    #                          - default : 6.617
    #                          - min : 0
    #                          - max : 1000
    #                          - unit : 
    #                          - inputtype : parameter
    #            - name: leafNumber
    #                          - description :  Actual number of phytomers
    #                          - variablecategory : state
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 25
    #                          - default : 0
    #                          - unit : leaf
    #                          - inputtype : variable
    #            - name: cumulTTPhenoMaizeAtEmergence
    #                          - description : cumulTTPhenoMaizeAtEmergence
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 10000
    #                          - default : 300
    #                          - unit : °C
    #                          - inputtype : variable
    #            - name: cumulTT
    #                          - description : cumul thermal times at current time 
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : -200
    #                          - max : 10000
    #                          - unit : °C
    #                          - default : 402.042720581446
    #                          - inputtype : variable
    #            - name: phase
    #                          - description :  the name of the phase
    #                          - variablecategory : state
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 7
    #                          - default : 1
    #                          - unit :  
    #                          - uri : some url
    #                          - inputtype : variable
    #- outputs:
    #            - name: leafNumber
    #                          - description : Actual number of phytomers
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 10000
    #                          - unit : leaf
    #                          - uri : some url
    #            - name: ntip
    #                          - description : Maize number of tip
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 10000
    #                          - unit : leaf
    #                          - uri : some url
    #            - name: cumulTTPhenoMaizeAtEmergence
    #                          - description : cumulTTPhenoMaizeAtEmergence
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 10000
    #                          - unit : °C
    leafNumber1 = leafNumber
    ntip = 0.0
    if (phase == 1.0) and (cumulTTPhenoMaizeAtEmergence == 0.0):
        cumulTTPhenoMaizeAtEmergence = cumulTT
    if (phase >= 1.0) and (phase < 4.0):
        if (hasFlagLeafLiguleAppeared == 0):
            if (switchMaize == 0):
                if (phyllochron == 0.0):
                    phyllochron = 0.0000001
                leafNumber = leafNumber1 + min(deltaTT / phyllochron, 0.999)
                ntip = 0.0
            else:
                if (leafNumber1 < leaf_tip_emerg):
                    leafNumber = leaf_tip_emerg
                else:
                    nextstartExpTT = 0.0
                    nexttipTT = (leafNumber1 + 1 - leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence
                    abl = k_bl * atip
                    tt_lim_lip = (nlim - leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence
                    bbl = nlim - abl * tt_lim_lip
                    tt_bl = (leafNumber1 + 1 - bbl) / abl
                    if (tt_bl > nexttipTT):
                        nextstartExpTT = nexttipTT
                    else:
                        nextstartExpTT = tt_bl
                    if (cumulTT >= nextstartExpTT):
                        leafNumber = leafNumber1 + 1
                    else:
                        leafNumber = leafNumber1
                ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) + leaf_tip_emerg
    return (leafNumber, ntip, cumulTTPhenoMaizeAtEmergence)