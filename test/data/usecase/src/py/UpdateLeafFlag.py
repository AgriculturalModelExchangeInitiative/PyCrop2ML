if (phase >= 1 and phase< 4):
    if (LeafNumber > 0):
        if (HasFlagLeafLiguleAppeared == 0 and (FinalLeafNumber > 0 and LeafNumber >= FinalLeafNumber)):
            HasFlagLeafLiguleAppeared = 1
            if  "FlagLeafLiguleJustVisible" not in calendarMoments:
                calendarMoments.append("FlagLeafLiguleJustVisible")
                calendarCumuls.append(cumulTT)
                calendarDates.append(currentdate)


    else:
        HasFlagLeafLiguleAppeared = 0


    
