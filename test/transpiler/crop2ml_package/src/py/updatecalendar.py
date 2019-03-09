import numpy
from math import *

def updatecalendar_(cumulTT,calendarMoments,calendarDates,calendarCumuls,currentdate,phase):
    #- Description:
    #            - Model Name: Calendar Model
    #            - Author: Pierre Martre
    #            - Reference: Modeling development phase in the 
    #                Wheat Simulation Model SiriusQuality.
    #                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    #            - Institution: INRA Montpellier
    #            - Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
    #- inputs:
    #            - name: cumulTT
    #                          - description : cumul thermal times at current date
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLE
    #                          - min : -200
    #                          - max : 10000
    #                          - default : 741.510096671757
    #                          - unit : °C d
    #                          - inputtype : variable
    #            - name: calendarMoments
    #                          - description : List containing apparition of each stage
    #                          - variablecategory : auxiliary
    #                          - datatype : STRINGLIST
    #                          - default : ['Sowing']
    #                          - unit : 
    #                          - inputtype : variable
    #            - name: calendarDates
    #                          - description : List containing  the dates of the wheat developmental phases
    #                          - variablecategory : auxiliary
    #                          - datatype : DATELIST
    #                          - default : ['21/3/2007']
    #                          - unit : 
    #                          - inputtype : variable
    #            - name: calendarCumuls
    #                          - description : list containing for each stage occured its cumulated thermal times
    #                          - variablecategory : auxiliary
    #                          - datatype : DOUBLELIST
    #                          - default : [0.0]
    #                          - unit : °C d
    #                          - inputtype : variable
    #            - name: currentdate
    #                          - description : current date
    #                          - variablecategory : auxiliary
    #                          - datatype : DATE
    #                          - default : 27/3/2007
    #                          - unit : 
    #                          - inputtype : variable
    #            - name: phase
    #                          - description :  the name of the phase
    #                          - variablecategory : state
    #                          - datatype : DOUBLE
    #                          - min : 0
    #                          - max : 7
    #                          - default : 1
    #                          - unit : 
    #                          - inputtype : variable
    #- outputs:
    #            - name: calendarMoments
    #                          - description :  List containing apparition of each stage
    #                          - variablecategory : auxiliary
    #                          - datatype : STRINGLIST
    #                          - unit : 
    #            - name: calendarDates
    #                          - description :  List containing  the dates of the wheat developmental phases
    #                          - variablecategory : auxiliary
    #                          - datatype : DATELIST 
    #                          - unit : 
    #            - name: calendarCumuls
    #                          - description :  list containing for each stage occured its cumulated thermal times
    #                          - datatype : DOUBLELIST
    #                          - unit : °C d
    if (phase >= 1.0) and (phase < 2.0) and "Emergence" not in calendarMoments:
        calendarMoments.append("Emergence")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif (phase >= 2.0) and (phase < 3.0) and "FloralInitiation" not in calendarMoments:
        calendarMoments.append("FloralInitiation")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif (phase >= 3.0) and (phase < 4.0) and "Heading" not in calendarMoments:
        calendarMoments.append("Heading")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif (phase == 4.0) and "Anthesis" not in calendarMoments:
        calendarMoments.append("Anthesis")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif (phase == 4.5) and "EndCellDivision" not in calendarMoments:
        calendarMoments.append("EndCellDivision")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif (phase >= 5.0) and (phase < 6.0) and "EndGrainFilling" not in calendarMoments:
        calendarMoments.append("EndGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    elif (phase >= 6.0) and (phase < 7.0) and "Maturity" not in calendarMoments:
        calendarMoments.append("Maturity")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
    return (calendarMoments, calendarDates, calendarCumuls)