using System;
using System.Collections.Generic;
public class Ismomentregistredzc_39_
{
    public static int ismomentregistredzc_39_(List<string> calendarMoments)
    {
        //- Description:
    //            - Model Name: IsMomentRegistredZC39 Model
    //            - Author: Pierre Martre
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: if FlagLeafLiguleJustVisible is already Registred 
        //- inputs:
    //            - name: calendarMoments
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - default : ['Sowing']
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : List containing appearance of each stage
        //- outputs:
    //            - name: isMomentRegistredZC_39
    //                          - min : 0
    //                          - datatype : INT
    //                          - max : 1
    //                          - unit : 
    //                          - description :  if Flag leaf ligule has already appeared 
        int isMomentRegistredZC_39;
        isMomentRegistredZC_39 = calendarMoments.Contains("FlagLeafLiguleJustVisible") ? 1 : 0;
        return isMomentRegistredZC_39;
    }
}