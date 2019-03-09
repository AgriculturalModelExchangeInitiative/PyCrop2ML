import numpy
from math import *

def cumulttfrom_(calendarMoments,calendarCumuls,switchMaize,cumulTT):
    #- Description:
    #            - Model Name: CumulTTFrom Model
    #            - Author: Pierre Martre
    #            - Reference: Modeling development phase in the 
    #                Wheat Simulation Model SiriusQuality.
    #                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #            - Institution: INRA Montpellier
    #            - Abstract: Calculate CumulTT 
    #- inputs:
    #            - name: calendarMoments
    #                          - description : List containing appearance of each stage
    #                          - variablecategory : auxiliary
    #                          - datatype : STRINGLIST
    #                          - default : ['Sowing']
    #                          - unit : 
    #                          - inputtype : variable
    #            - name: calendarCumuls
    #                          - description : list containing for each stage occured its cumulated thermal times
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLELIST
    #                          - default : [0.0]
    #                          - unit : °C d
    #                          - inputtype : variable
    #            - name: switchMaize
    #                          - description : true if maize
    #                          - datatype : INT
    #                          - parametercategory : constant
    #                          - min : 0
    #                          - max : 1
    #                          - default : 0
    #                          - unit : 
    #                          - inputtype : parameter
    #            - name: cumulTT
    #                          - description : cumul TT at current date
    #                          - datatype : DOUBLE
    #                          - variablecategory : auxiliary
    #                          - min : -200
    #                          - max : 10000
    #                          - default : 8
    #                          - unit : °C d
    #                          - inputtype : variable
    #- outputs:
    #            - name: cumulTTFromZC_65
    #                          - description :  cumul TT from Anthesis to current date 
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 5000
    #                          - unit : °C d
    #            - name: cumulTTFromZC_39
    #                          - description :  cumul TT from FlagLeafLiguleJustVisible to current date 
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 5000
    #                          - unit : °C d
    #            - name: cumulTTFromZC_91
    #                          - description :  cumul TT from EndGrainFilling to current date 
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 5000
    #                          - unit : °C d
    cumulTTFromZC_65 = 0.0
    cumulTTFromZC_39 = 0.0
    cumulTTFromZC_91 = 0.0
    if "Anthesis" in calendarMoments:
        if (switchMaize == 0):
            cumulTTFromZC_65 = cumulTT - calendarCumuls[calendarMoments.index("Anthesis")]
    if "FlagLeafLiguleJustVisible" in calendarMoments:
        if (switchMaize == 0):
            cumulTTFromZC_39 = cumulTT - calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]
    if "EndGrainFilling" in calendarMoments:
        if (switchMaize == 0):
            cumulTTFromZC_91 = cumulTT - calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]
    return (cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91)