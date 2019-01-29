if (phase >= 1 && phase< 4)
{
    if (LeafNumber > 0)
    {
        if (HasFlagLeafLiguleAppeared == 0 && (FinalLeafNumber > 0 && LeafNumber >= FinalLeafNumber))
        {
            HasFlagLeafLiguleAppeared = 1;
            if  (calendarMoments.Contains("FlagLeafLiguleJustVisible")==false)
            {
                calendarMoments.add("FlagLeafLiguleJustVisible");
                calendarCumuls.add(cumulTT);
                calendarDates.add(currentdate);
            }
        }
    }
    else:
        HasFlagLeafLiguleAppeared = 0;
}


    
