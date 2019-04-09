using System;
using System.Collections.Generic;
public class Leafnumber_
{
    public static double leafnumber_(double deltaTT,double phyllochron,int hasFlagLeafLiguleAppeared,double leafNumber,double cumulTT,double phase)
    {
        //- Description:
    //            - Model Name: CalculateLeafNumber Model
    //            - Author: Pierre MARTRE
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day
        //- inputs:
    //            - name: deltaTT
    //                          - min : -20
    //                          - default : 23.5895677277199
    //                          - max : 100
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : daily delta TT 
    //            - name: phyllochron
    //                          - min : 0
    //                          - default : 0
    //                          - max : 1000
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C d leaf-1
    //                          - description : phyllochron
    //            - name: hasFlagLeafLiguleAppeared
    //                          - min : 0
    //                          - default : 0
    //                          - max : 1
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
    //            - name: leafNumber
    //                          - min : 0
    //                          - default : 0
    //                          - max : 25
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : leaf
    //                          - description :  Actual number of phytomers
    //            - name: cumulTT
    //                          - min : -200
    //                          - default : 402.042720581446
    //                          - max : 10000
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C
    //                          - description : cumul thermal times at current time 
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
    //            - name: leafNumber
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - uri : some url
    //                          - unit : leaf
    //                          - description : Actual number of phytomers
        double phyllochron_;
        if (phase >= 1.0d && phase < 4.0d)
        {
            if (hasFlagLeafLiguleAppeared == 0)
            {
                if (phyllochron == 0.0d)
                {
                    phyllochron_ = 0.0000001d;
                }
                else
                {
                    phyllochron_ = phyllochron;
                }
                leafNumber = leafNumber + Math.Min(deltaTT / phyllochron_, 0.999d);
            }
        }
        return leafNumber;
    }
}