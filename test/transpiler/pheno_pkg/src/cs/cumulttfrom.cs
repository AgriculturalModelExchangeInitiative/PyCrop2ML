using System;
using System.Collections.Generic;
public class Cumulttfrom_
{
    public static Tuple<double,double,double>  cumulttfrom_(List<string> calendarMoments,List<double> calendarCumuls,double cumulTT)
    {
        //- Description:
    //            - Model Name: CumulTTFrom Model
    //            - Author: Pierre Martre
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: Calculate CumulTT 
        //- inputs:
    //            - name: calendarMoments
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - default : ['Sowing']
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : List containing appearance of each stage
    //            - name: calendarCumuls
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - default : [0.0]
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : list containing for each stage occured its cumulated thermal times
    //            - name: cumulTT
    //                          - min : -200
    //                          - default : 8
    //                          - max : 10000
    //                          - datatype : DOUBLE
    //                          - variablecategory : auxiliary
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : cumul TT at current date
        //- outputs:
    //            - name: cumulTTFromZC_65
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - variablecategory : auxiliary
    //                          - max : 5000
    //                          - unit : °C d
    //                          - description :  cumul TT from Anthesis to current date 
    //            - name: cumulTTFromZC_39
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - variablecategory : auxiliary
    //                          - max : 5000
    //                          - unit : °C d
    //                          - description :  cumul TT from FlagLeafLiguleJustVisible to current date 
    //            - name: cumulTTFromZC_91
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - variablecategory : auxiliary
    //                          - max : 5000
    //                          - unit : °C d
    //                          - description :  cumul TT from EndGrainFilling to current date 
        double cumulTTFromZC_65;
        double cumulTTFromZC_39;
        double cumulTTFromZC_91;
        cumulTTFromZC_65 = 0.0d;
        cumulTTFromZC_39 = 0.0d;
        cumulTTFromZC_91 = 0.0d;
        if (calendarMoments.Contains("Anthesis"))
        {
            cumulTTFromZC_65 = cumulTT - calendarCumuls[calendarMoments.IndexOf("Anthesis")];
        }
        if (calendarMoments.Contains("FlagLeafLiguleJustVisible"))
        {
            cumulTTFromZC_39 = cumulTT - calendarCumuls[calendarMoments.IndexOf("FlagLeafLiguleJustVisible")];
        }
        if (calendarMoments.Contains("EndGrainFilling"))
        {
            cumulTTFromZC_91 = cumulTT - calendarCumuls[calendarMoments.IndexOf("EndGrainFilling")];
        }
        return Tuple.Create(cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91);
    }
}