
cumulTTFromZC_65 = 0.0D;
cumulTTFromZC_39 = 0.0D;
cumulTTFromZC_91 = 0.0D;
if (calendarMoments.contains("Anthesis")){
    if (switchMaize == 0)
        cumulTTFromZC_65 = cumulTT-calendarCumuls.get(calendarMoments.indexOf("Anthesis"));
}    
if (calendarMoments.contains("FlagLeafLiguleJustVisible")){
    if (switchMaize == 0)
        cumulTTFromZC_39 = cumulTT-calendarCumuls.get(calendarMoments.indexOf("FlagLeafLiguleJustVisible"));
}   
if (calendarMoments.contains("EndGrainFilling")){
    if (switchMaize == 0)
        cumulTTFromZC_91 = cumulTT-calendarCumuls.get(calendarMoments.indexOf("FlagLeafLiguleJustVisible"));
}