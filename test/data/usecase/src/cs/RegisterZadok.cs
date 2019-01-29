
int roundedFinalLeafNumber = (int)(FinalLeafNumber+0.5);
if (LeafNumber>=4 && calendarMoments.contains("MainShootPlus1Tiller")==false):
    calendarMoments.add("MainShootPlus1Tiller");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus1Tiller";

else if (LeafNumber>=5 && calendarMoments.contains("MainShootPlus2Tiller")==false):
    calendarMoments.add("MainShootPlus2Tiller");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MainShootPlus2Tiller";

else if (LeafNumber>=6 && calendarMoments.contains("MainShootPlus3Tiller")==false):
    calendarMoments.add("MainShootPlus3Tiller");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1
    currentZadokStage = "MainShootPlus3Tiller";
        
else if (FinalLeafNumber > 0 && LeafNumber>=(slopeTSFLN * FinalLeafNumber - intTSFLN) &&  calendarMoments.contains("TerminalSpikelet")==false):
    calendarMoments.add("TerminalSpikelet");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "TerminalSpikelet";
        
        
else if ((LeafNumber >= (roundedFinalLeafNumber-4) && (roundedFinalLeafNumber-4) > 0) && calendarMoments.contains("PseudoStemErection")==false):
    calendarMoments.add("PseudoStemErection");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "PseudoStemErection";

else if ((LeafNumber >= (roundedFinalLeafNumber-3) && (roundedFinalLeafNumber-3) > 0) && calendarMoments.contains("1stNodeDetectable")==false):
    calendarMoments.add("1stNodeDetectable");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1
    currentZadokStage = "1stNodeDetectable";


else if ((LeafNumber >= (roundedFinalLeafNumber-2) && (roundedFinalLeafNumber-2) > 0) &&  calendarMoments.contains("2ndNodeDetectable")==false):
    calendarMoments.add("2ndNodeDetectable");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1
    currentZadokStage = "2ndNodeDetectable";
     
else if ((LeafNumber >= (roundedFinalLeafNumber-1) && (roundedFinalLeafNumber-1) > 0) && calendarMoments.contains("FlagLeafJustVisible")==false):
    calendarMoments.add("FlagLeafJustVisible");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "FlagLeafJustVisible";
     
else if ((calendarMoments.contains("MidGrainFilling")==false) && phase == 4.5 && cumulTTFromZC_65 >= Der):
    calendarMoments.add("MidGrainFilling");
    calendarCumuls.add(cumulTT);
    calendarDates.add(currentdate);
    hasZadokStageChanged = 1;
    currentZadokStage = "MidGrainFilling" ;                

else:
    hasZadokStageChanged = 0;

