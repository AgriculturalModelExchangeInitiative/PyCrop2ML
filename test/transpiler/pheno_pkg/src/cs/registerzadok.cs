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
    //                          - min : -200
    //                          - default : 354.582294511779
    //                          - max : 10000
    //                          - uri : some url
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : 
    //            - name: phase
    //                          - min : 0
    //                          - default : 2
    //                          - max : 7
    //                          - uri : some url
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : instance of the phase class . You can get the name of the phase using phase.getPhaseAsString(PhaseValue) 
    //            - name: leafNumber
    //                          - min : 0
    //                          - default : 4.8854219661087575
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
    //            - name: cumulTTFromZC_65
    //                          - min : -200
    //                          - default : 0
    //                          - max : 10000
    //                          - uri : some url
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C d
    //                          - description : cumul of the thermal time (DeltaTT) since the moment ZC_65
    //            - name: currentdate
    //                          - min : 
    //                          - default : 9/4/2007
    //                          - max : 
    //                          - uri : some url
    //                          - variablecategory : auxiliary
    //                          - datatype : DATE
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : current date
    //            - name: der
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - uri : some url
    //                          - default : 300.0
    //                          - inputtype : parameter
    //                          - unit : °C d
    //                          - description : Duration of the endosperm endoreduplication phase
    //            - name: slopeTSFLN
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - uri : some url
    //                          - default : 0.9
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : used to calculate Terminal spikelet
    //            - name: intTSFLN
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - uri : some url
    //                          - default : 0.9
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : used to calculate Terminal spikelet
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
    //            - name: currentZadokStage
    //                          - min : 
    //                          - datatype : STRING
    //                          - max : 
    //                          - uri : some url
    //                          - default : MainShootPlus1Tiller
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : current zadok stage
    //            - name: hasZadokStageChanged
    //                          - min : 0
    //                          - default : 0
    //                          - max : 1
    //                          - uri : some url
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description : true if the zadok stage has changed this time step
        //- outputs:
    //            - name: hasZadokStageChanged
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 1
    //                          - uri : some url
    //                          - datatype : INT
    //                          - unit : 
    //                          - description : true if the zadok stage has changed this time step
    //            - name: currentZadokStage
    //                          - datatype : STRING
    //                          - variablecategory : auxiliary
    //                          - uri : some url
    //                          - unit :  
    //                          - description : current zadok stage
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