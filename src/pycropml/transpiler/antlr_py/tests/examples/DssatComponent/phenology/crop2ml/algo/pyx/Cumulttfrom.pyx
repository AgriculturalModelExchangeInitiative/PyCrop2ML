cdef int a 
cumulTTFromZC_65 = 0.0
cumulTTFromZC_39 = 0.0
cumulTTFromZC_91 = 0.0
if "Anthesis" in calendarMoments_t1:
    cumulTTFromZC_65 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("Anthesis") - 1]
if "FlagLeafLiguleJustVisible" in calendarMoments_t1:
    cumulTTFromZC_39 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("FlagLeafLiguleJustVisible") - 1]
if "EndGrainFilling" in calendarMoments_t1:
    cumulTTFromZC_91 = cumulTT - calendarCumuls_t1[calendarMoments_t1.index("EndGrainFilling") - 1]
return (cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91)