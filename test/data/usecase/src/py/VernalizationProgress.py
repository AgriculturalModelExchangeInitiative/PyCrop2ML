if (IsVernalizable==1 and Vernaprog < 1):
    TT = DeltaTT
        
    if (TT >= MinTvern and TT <= IntTvern):
        Vernaprog = Vernaprog + VAI * TT + VBEE
          
    if (TT > IntTvern):
        maxVernaProg = VAI * IntTvern + VBEE
        DLverna = max(MinDL, min(MaxDL, DayLength))
        Vernaprog += max(0, maxVernaProg * (1 + ((IntTvern - TT) / (MaxTvern - IntTvern)) * ((DLverna - MinDL) / (MaxDL - MinDL))))
            
    primordno = 2.0 * LeafNumber + PNini
        
    minLeafNumber = MinFinalNumber
    if (Vernaprog >= 1.0 or primordno >= AMXLFNO):
            
            
        MinFinalNumber = max(primordno, MinFinalNumber)
        calendarMoments.append("EndVernalisation")
        calendarCumuls.append(cumulTT) 
        calendarDates.append(currentdate)        
        Vernaprog = max(1, Vernaprog)
            
            
    else:
            
        potlfno = AMXLFNO - (AMXLFNO - minLeafNumber) * Vernaprog
        if (primordno >= potlfno):
                
                
            MinFinalNumber = max((potlfno + primordno) / 2.0, MinFinalNumber)
            Vernaprog = max(1, Vernaprog)
            calendarMoments.append("EndVernalisation")
            calendarCumuls.append(cumulTT) 
            calendarDates.append(currentdate)

             

