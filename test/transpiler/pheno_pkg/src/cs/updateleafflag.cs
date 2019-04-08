using System;
using System.Collections.Generic;
public class Updateleafflag_
{
    public static Tuple<int,List<string>,List<string>,List<double>>  updateleafflag_(double cumulTT,double leafNumber,List<string> calendarMoments,List<string> calendarDates,List<double> calendarCumuls,string currentdate,double finalLeafNumber,int hasFlagLeafLiguleAppeared,double phase)
    {
        //- Description:
    //            - Model Name: UpdateLeafFlag Model
    //            - Author: Pierre MARTRE
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: tells if flag leaf has appeared and update the calendar if so
    //    	
        //- inputs:
    //            - name: cumulTT
    //                          - min : -200
    //                          - default : 741.510096671757
    //                          - max : 10000
    //                          - uri : some url
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : cumul thermal times at current date
    //            - name: leafNumber
    //                          - min : 0
    //                          - default : 8.919453833361189
    //                          - max : 25
    //                          - uri : some url
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : leaf
    //                          - description : Actual number of phytomers
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
    //                          - default : 29/4/2007
    //                          - uri : some url
    //                          - variablecategory : auxiliary
    //                          - datatype : DATE
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description :  current date
    //            - name: finalLeafNumber
    //                          - min : 0
    //                          - default : 8.797582013199484
    //                          - max : 10000
    //                          - uri : some url
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : leaf
    //                          - description : final leaf number
    //            - name: hasFlagLeafLiguleAppeared
    //                          - min : 0
    //                          - default : 1
    //                          - max : 1
    //                          - uri : some url
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //            - name: phase
    //                          - min : 0
    //                          - default : 1
    //                          - max : 7
    //                          - uri : some url
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description :  the name of the phase
        //- outputs:
    //            - name: hasFlagLeafLiguleAppeared
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 1
    //                          - uri : some url
    //                          - datatype : INT
    //                          - unit : 
    //                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
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
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - unit : °C d
    //                          - description :  list containing for each stage occured its cumulated thermal times
        if (phase >= 1.0d && phase < 4.0d)
        {
            if (leafNumber > 0.0d)
            {
                if (hasFlagLeafLiguleAppeared == 0 && finalLeafNumber > 0.0d && leafNumber >= finalLeafNumber)
                {
                    hasFlagLeafLiguleAppeared = 1;
                    if (!calendarMoments.Contains("FlagLeafLiguleJustVisible"))
                    {
                        calendarMoments.Add("FlagLeafLiguleJustVisible");
                        calendarCumuls.Add(cumulTT);
                        calendarDates.Add(currentdate);
                    }
                }
            }
            else
            {
                hasFlagLeafLiguleAppeared = 0;
            }
        }
        return Tuple.Create(hasFlagLeafLiguleAppeared, calendarMoments, calendarDates, calendarCumuls);
    }
}