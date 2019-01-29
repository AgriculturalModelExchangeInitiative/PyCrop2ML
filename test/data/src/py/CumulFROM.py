   
cumulTTFromZC_65 = 0
cumulTTFromZC_39 = 0
cumulTTFromZC_91 = 0     
if "Anthesis" in calendarMoments:
    if (switchMaize == 0): cumulTTFromZC_65 = cumulTT-calendarCumuls[calendarMoments.index("Anthesis")]    
if "FlagLeafLiguleJustVisible" in calendarMoments:
    if (switchMaize == 0): cumulTTFromZC_39 = cumulTT-calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]  
if "EndGrainFilling"in calendarMoments:
    if (switchMaize == 0): cumulTTFromZC_91 = cumulTT-calendarCumuls[calendarMoments.index("FlagLeafLiguleJustVisible")]
