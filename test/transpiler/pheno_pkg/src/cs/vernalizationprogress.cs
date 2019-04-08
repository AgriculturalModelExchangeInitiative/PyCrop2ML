using System;
using System.Collections.Generic;
public class Vernalizationprogress_
{
    public static Tuple<double,double,List<string>,List<string>,List<double>>  vernalizationprogress_(double dayLength,double deltaTT,double cumulTT,double leafNumber,List<string> calendarMoments,List<string> calendarDates,List<double> calendarCumuls,double minTvern,double intTvern,double vAI,double vBEE,double minDL,double maxDL,double maxTvern,double pNini,double aMXLFNO,double vernaprog,string currentdate,int isVernalizable,double minFinalNumber)
    {
        //- Description:
    //            - Model Name: VernalizationProgress Model
    //            - Author: Pierre MARTRE
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: Calculate progress (VernaProg) towards vernalization, but there 
    //        			is no vernalization below minTvern 
    //        			and above maxTvern . The maximum value of VernaProg is 1.
    //        			Progress towards full vernalization is a linear function of shoot 
    //        			temperature (soil temperature until leaf # reach MaxLeafSoil and then
    //        			 canopy temperature)
    //    	
        //- inputs:
    //            - name: dayLength
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - default : 12.3037621834005
    //                          - inputtype : variable
    //                          - unit : mm2 m-2
    //                          - description : day length
    //            - name: deltaTT
    //                          - min : -20
    //                          - datatype : DOUBLE
    //                          - max : 100
    //                          - default : 20.3429985011972
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : difference cumul TT between j and j-1 day 
    //            - name: cumulTT
    //                          - min : -200
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - default : 112.330110409888
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : cumul thermal times at currentdate
    //            - name: leafNumber
    //                          - min : 0
    //                          - default : 0
    //                          - max : 25
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
    //                          - description : List containing appearance of each stage
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
    //                          - unit : 
    //                          - description : list containing for each stage occured its cumulated thermal times
    //            - name: minTvern
    //                          - parametercategory : species
    //                          - min : -20
    //                          - datatype : DOUBLE
    //                          - max : 60
    //                          - default : 0.0
    //                          - inputtype : parameter
    //                          - unit : °C
    //                          - description : Minimum temperature for vernalization to occur
    //            - name: intTvern
    //                          - parametercategory : species
    //                          - min : -20
    //                          - datatype : DOUBLE
    //                          - max : 60
    //                          - default :  11.0
    //                          - inputtype : parameter
    //                          - unit : °C
    //                          - description : Intermediate temperature for vernalization to occur
    //            - name: vAI
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - default :  0.015
    //                          - inputtype : parameter
    //                          - unit : d-1 °C-1
    //                          - description : Response of vernalization rate to temperature
    //            - name: vBEE
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - default : 0.01
    //                          - inputtype : parameter
    //                          - unit : d-1
    //                          - description : Vernalization rate at 0°C
    //            - name: minDL
    //                          - parametercategory : species
    //                          - min : 12
    //                          - datatype : DOUBLE
    //                          - max : 24
    //                          - default : 8.0
    //                          - inputtype : parameter
    //                          - unit : h
    //                          - description : Threshold daylength below which it does influence vernalization rate
    //            - name: maxDL
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 24
    //                          - default : 15.0
    //                          - inputtype : parameter
    //                          - unit : h
    //                          - description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //            - name: maxTvern
    //                          - parametercategory : species
    //                          - min : -20
    //                          - datatype : DOUBLE
    //                          - max : 60
    //                          - default :  23.0
    //                          - inputtype : parameter
    //                          - unit : °C
    //                          - description : Maximum temperature for vernalization to occur
    //            - name: pNini
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 24
    //                          - default : 4.0
    //                          - inputtype : parameter
    //                          - unit : primordia
    //                          - description : Number of primorida in the apex at emergence
    //            - name: aMXLFNO
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 25
    //                          - default : 24.0
    //                          - inputtype : parameter
    //                          - unit : leaf
    //                          - description : Absolute maximum leaf number
    //            - name: vernaprog
    //                          - min : 0
    //                          - default :  0.5517254187376879
    //                          - max : 1
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : progression on a 0  to 1 scale of the vernalization
    //            - name: currentdate
    //                          - variablecategory : auxiliary
    //                          - datatype : DATE
    //                          - default : 27/3/2007
    //                          - inputtype : variable
    //                          - description : current date 
    //            - name: isVernalizable
    //                          - min : 0
    //                          - datatype : INT
    //                          - max : 1
    //                          - default : 1
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : true if the plant is vernalizable
    //            - name: minFinalNumber
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 25
    //                          - default : 5.5
    //                          - variablecategory : state
    //                          - inputtype : variable
    //                          - unit : leaf
    //                          - description : minimum final leaf number
        //- outputs:
    //            - name: vernaprog
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - unit : 
    //                          - description : progression on a 0  to 1 scale of the vernalization
    //            - name: minFinalNumber
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - unit : leaf
    //                          - description : minimum final leaf number
    //            - name: calendarMoments
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - unit : 
    //                          - description : List containing appearance of each stage
    //            - name: calendarDates
    //                          - variablecategory : auxiliary
    //                          - datatype : DATELIST
    //                          - unit : 
    //                          - description : List containing  the dates of the wheat developmental phases
    //            - name: calendarCumuls
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - unit : 
    //                          - description : list containing for each stage occured its cumulated thermal times
        double maxVernaProg;
        double dLverna;
        double primordno;
        double minLeafNumber;
        double potlfno;
        double tt;
        if (isVernalizable == 1 && vernaprog < 1.0d)
        {
            tt = deltaTT;
            if (tt >= minTvern && tt <= intTvern)
            {
                vernaprog = vernaprog + vAI * tt + vBEE;
            }
            if (tt > intTvern)
            {
                maxVernaProg = vAI * intTvern + vBEE;
                dLverna = Math.Max(minDL, Math.Min(maxDL, dayLength));
                vernaprog = vernaprog + Math.Max(0.0d, maxVernaProg * (1.0d + (intTvern - tt) / (maxTvern - intTvern) * (dLverna - minDL) / (maxDL - minDL)));
            }
            primordno = 2.0d * leafNumber + pNini;
            minLeafNumber = minFinalNumber;
            if (vernaprog >= 1.0d || primordno >= aMXLFNO)
            {
                minFinalNumber = Math.Max(primordno, minFinalNumber);
                calendarMoments.Add("EndVernalisation");
                calendarCumuls.Add(cumulTT);
                calendarDates.Add(currentdate);
                vernaprog = Math.Max(1.0d, vernaprog);
            }
            else
            {
                potlfno = aMXLFNO - (aMXLFNO - minLeafNumber) * vernaprog;
                if (primordno >= potlfno)
                {
                    minFinalNumber = Math.Max((potlfno + primordno) / 2.0d, minFinalNumber);
                    vernaprog = Math.Max(1.0d, vernaprog);
                    calendarMoments.Add("EndVernalisation");
                    calendarCumuls.Add(cumulTT);
                    calendarDates.Add(currentdate);
                }
            }
        }
        return Tuple.Create(vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls);
    }
}