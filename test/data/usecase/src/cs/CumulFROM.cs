
double cumulTTFromZC_65 = 0;
double cumulTTFromZC_39 = 0;
double cumulTTFromZC_91 = 0;
        
if calendarMoments.Contains("Anthesis"){
    if (SwitchMaize == 0)
        cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.IndexOf("Anthesis")];
}    
if calendarMoments.Contains("FlagLeafLiguleJustVisible"){
    if (SwitchMaize == 0)
        cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.IndexOf("FlagLeafLiguleJustVisible")];
}   
if calendarMoments.Contains("EndGrainFilling"){
    if (SwitchMaize == 0)
        cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.IndexOf("FlagLeafLiguleJustVisible")];
}