using System;
using System.Collections.Generic;
public class Updatecalendar_
{
    public static Tuple<List<string>,List<string>,List<double>>  updatecalendar_(double cumulTT,List<string> calendarMoments,List<string> calendarDates,List<double> calendarCumuls,string currentdate,double phase)
    {
        //- Description:
    //            - Model Name: Calendar Model
    //            - Author: Pierre Martre
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: Lists containing for each stage the date it occurs as well as a copy of all types of cumulated thermal times 
        //- inputs:
    //            - name: cumulTT
    //                          - min : -200
    //                          - default : 741.510096671757
    //                          - max : 10000
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : cumul thermal times at current date
    //            - name: calendarMoments
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - default : ['Sowing']
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : List containing apparition of each stage
    //            - name: calendarDates
    //                          - variablecategory : auxiliary
    //                          - datatype : DATELIST
    //                          - default : ['21/3/2007']
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : List containing  the dates of the wheat developmental phases
    //            - name: calendarCumuls
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - default : [0.0]
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : list containing for each stage occured its cumulated thermal times
    //            - name: currentdate
    //                          - variablecategory : auxiliary
    //                          - datatype : DATE
    //                          - default : 27/3/2007
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : current date
    //            - name: phase
    //                          - min : 0
    //                          - default : 1
    //                          - max : 7
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description :  the name of the phase
        //- outputs:
    //            - name: calendarMoments
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - unit : 
    //                          - description :  List containing apparition of each stage
    //            - name: calendarDates
    //                          - variablecategory : auxiliary
    //                          - datatype : DATELIST 
    //                          - unit : 
    //                          - description :  List containing  the dates of the wheat developmental phases
    //            - name: calendarCumuls
    //                          - datatype : DOUBLELIST
    //                          - unit : °C d
    //                          - description :  list containing for each stage occured its cumulated thermal times
        if (phase >= 1.0d && phase < 2.0d && !calendarMoments.Contains("Emergence"))
        {
            calendarMoments.Add("Emergence");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 2.0d && phase < 3.0d && !calendarMoments.Contains("FloralInitiation"))
        {
            calendarMoments.Add("FloralInitiation");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 3.0d && phase < 4.0d && !calendarMoments.Contains("Heading"))
        {
            calendarMoments.Add("Heading");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase == 4.0d && !calendarMoments.Contains("Anthesis"))
        {
            calendarMoments.Add("Anthesis");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase == 4.5d && !calendarMoments.Contains("EndCellDivision"))
        {
            calendarMoments.Add("EndCellDivision");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 5.0d && phase < 6.0d && !calendarMoments.Contains("EndGrainFilling"))
        {
            calendarMoments.Add("EndGrainFilling");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        else if ( phase >= 6.0d && phase < 7.0d && !calendarMoments.Contains("Maturity"))
        {
            calendarMoments.Add("Maturity");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
        }
        return Tuple.Create(calendarMoments, calendarDates, calendarCumuls);
    }
}