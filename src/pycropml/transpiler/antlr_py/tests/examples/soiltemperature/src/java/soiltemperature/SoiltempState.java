import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;
public class SoiltempState
{
    private double SRFTEMP;
    private Double [] TMA;
    private double TDL;
    private Double [] ST;
    private double CUMDPT;
    private int NDays;
    private Integer [] WetDay;
    private Double [] DSMID;
    
    public SoiltempState() { }
    
    public SoiltempState(SoiltempState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SRFTEMP = toCopy.getSRFTEMP();
            TMA = new Double[5];
        for (int i = 0; i < 5; i++)
        {
            TMA[i] = toCopy.getTMA()[i];
        }
            this.TDL = toCopy.getTDL();
            ST = new Double[toCopy.getST().length];
        for (int i = 0; i < toCopy.getST().length; i++)
        {
            ST[i] = toCopy.getST()[i];
        }
            this.CUMDPT = toCopy.getCUMDPT();
            this.NDays = toCopy.getNDays();
            WetDay = new Integer[toCopy.getWetDay().length];
        for (int i = 0; i < toCopy.getWetDay().length; i++)
        {
            WetDay[i] = toCopy.getWetDay()[i];
        }
            DSMID = new Double[toCopy.getDSMID().length];
        for (int i = 0; i < toCopy.getDSMID().length; i++)
        {
            DSMID[i] = toCopy.getDSMID()[i];
        }
        }
    }
    public double getSRFTEMP()
    { return SRFTEMP; }

    public void setSRFTEMP(double _SRFTEMP)
    { this.SRFTEMP= _SRFTEMP; } 
    
    public Double [] getTMA()
    { return TMA; }

    public void setTMA(Double [] _TMA)
    { this.TMA= _TMA; } 
    
    public double getTDL()
    { return TDL; }

    public void setTDL(double _TDL)
    { this.TDL= _TDL; } 
    
    public Double [] getST()
    { return ST; }

    public void setST(Double [] _ST)
    { this.ST= _ST; } 
    
    public double getCUMDPT()
    { return CUMDPT; }

    public void setCUMDPT(double _CUMDPT)
    { this.CUMDPT= _CUMDPT; } 
    
    public int getNDays()
    { return NDays; }

    public void setNDays(int _NDays)
    { this.NDays= _NDays; } 
    
    public Integer [] getWetDay()
    { return WetDay; }

    public void setWetDay(Integer [] _WetDay)
    { this.WetDay= _WetDay; } 
    
    public Double [] getDSMID()
    { return DSMID; }

    public void setDSMID(Double [] _DSMID)
    { this.DSMID= _DSMID; } 
    
}