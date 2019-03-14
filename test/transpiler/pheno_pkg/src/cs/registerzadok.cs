using System;
using System.Collections.Generic;
public class Registerzadok_
{
    public static Tuple<int,string,List<string>,List<string>,List<double>>  registerzadok_(double cumulTT,double phase,double leafNumber,List<string> calendarMoments,List<string> calendarDates,List<double> calendarCumuls,double cumulTTFromZC_65,string currentdate,double der,double slopeTSFLN,double intTSFLN,double finalLeafNumber,string currentZadokStage,int hasZadokStageChanged)
    {
        //- Description:
    //            - Model Name: RegisterZadok Model
    //            - Author: Pierre MARTRE
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: Record the zadok stage in the calendar
    //    	
        //- inputs:
    //            - name: cumulTT
    //                          - description : cumul TT at current date
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -200
    //                          - max : 10000
    //                          - default : 354.582294511779
    //                          - unit : °C d
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: phase
    //                          - description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    //                          - variablecategory : state
    //                          - inputtype : variable
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 7
    //                          - default : 2
    //                          - unit : 
    //                          - uri : some url
    //            - name: leafNumber
    //                          - description : Actual number of phytomers
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 25
    //                          - default : 4.8854219661087575
    //                          - unit : leaf
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: calendarMoments
    //                          - description : List containing apparition of each stage
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - default : ['Sowing']
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: calendarDates
    //                          - description : List containing  the dates of the wheat developmental phases
    //                          - variablecategory : auxiliary
    //                          - datatype : DATELIST
    //                          - default : ['21/3/2007']
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: calendarCumuls
    //                          - description : list containing for each stage occured its cumulated thermal times
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - default : [0.0]
    //                          - unit : °C d
    //                          - inputtype : variable
    //            - name: cumulTTFromZC_65
    //                          - description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -200
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : °C d
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: currentdate
    //                          - description : current date
    //                          - variablecategory : auxiliary
    //                          - datatype : DATE
    //                          - min : 
    //                          - max : 
    //                          - default : 9/4/2007
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: der
    //                          - description : Duration of the endosperm endoreduplication phase
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 300.0
    //                          - unit : °C d
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: slopeTSFLN
    //                          - description : used to calculate Terminal spikelet
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0.9
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: intTSFLN
    //                          - description : used to calculate Terminal spikelet
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0.9
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: finalLeafNumber
    //                          - description : final leaf number
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 8.797582013199484
    //                          - unit : leaf
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: currentZadokStage
    //                          - description : current zadok stage
    //                          - datatype : STRING
    //                          - min : 
    //                          - max : 
    //                          - default : MainShootPlus1Tiller
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: hasZadokStageChanged
    //                          - description : true if the zadok stage has changed this time step
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : variable
        //- outputs:
    //            - name: hasZadokStageChanged
    //                          - description : true if the zadok stage has changed this time step
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : some url
    //            - name: currentZadokStage
    //                          - description : current zadok stage
    //                          - variablecategory : auxiliary
    //                          - datatype : STRING
    //                          - unit : m2 m-2
    //                          - uri : some url
    //            - name: calendarMoments
    //                          - description :  List containing apparition of each stage
    //                          - variablecategory : auxiliary
    //                          - datatype : STRINGLIST
    //                          - unit : 
    //            - name: calendarDates
    //                          - description :  List containing  the dates of the wheat developmental phases
    //                          - variablecategory : auxiliary
    //                          - datatype : DATELIST
    //                          - unit : 
    //            - name: calendarCumuls
    //                          - description :  list containing for each stage occured its cumulated thermal times
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - unit : °C d
        int roundedFinalLeafNumber;
        roundedFinalLeafNumber = (int)(finalLeafNumber + 0.5d);
        if (leafNumber >= 4.0d && !calendarMoments.Contains("MainShootPlus1Tiller"))
        {
            calendarMoments.Add("MainShootPlus1Tiller");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus1Tiller";
        }
        else if ( leafNumber >= 5.0d && !calendarMoments.Contains("MainShootPlus2Tiller"))
        {
            calendarMoments.Add("MainShootPlus2Tiller");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus2Tiller";
        }
        else if ( leafNumber >= 6.0d && !calendarMoments.Contains("MainShootPlus3Tiller"))
        {
            calendarMoments.Add("MainShootPlus3Tiller");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MainShootPlus3Tiller";
        }
        else if ( finalLeafNumber > 0.0d && leafNumber >= slopeTSFLN * finalLeafNumber - intTSFLN && !calendarMoments.Contains("TerminalSpikelet"))
        {
            calendarMoments.Add("TerminalSpikelet");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "TerminalSpikelet";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 4.0d && roundedFinalLeafNumber - 4 > 0 && !calendarMoments.Contains("PseudoStemErection"))
        {
            calendarMoments.Add("PseudoStemErection");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "PseudoStemErection";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 3.0d && roundedFinalLeafNumber - 3 > 0 && !calendarMoments.Contains("1stNodeDetectable"))
        {
            calendarMoments.Add("1stNodeDetectable");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "1stNodeDetectable";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 2.0d && roundedFinalLeafNumber - 2 > 0 && !calendarMoments.Contains("2ndNodeDetectable"))
        {
            calendarMoments.Add("2ndNodeDetectable");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "2ndNodeDetectable";
        }
        else if ( leafNumber >= roundedFinalLeafNumber - 1.0d && roundedFinalLeafNumber - 1 > 0 && !calendarMoments.Contains("FlagLeafJustVisible"))
        {
            calendarMoments.Add("FlagLeafJustVisible");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "FlagLeafJustVisible";
        }
        else if ( !calendarMoments.Contains("MidGrainFilling") && phase == 4.5d && cumulTTFromZC_65 >= der)
        {
            calendarMoments.Add("MidGrainFilling");
            calendarCumuls.Add(cumulTT);
            calendarDates.Add(currentdate);
            hasZadokStageChanged = 1;
            currentZadokStage = "MidGrainFilling";
        }
        else
        {
            hasZadokStageChanged = 0;
        }
        return Tuple.Create(hasZadokStageChanged, currentZadokStage, calendarMoments, calendarDates, calendarCumuls);
    }
}