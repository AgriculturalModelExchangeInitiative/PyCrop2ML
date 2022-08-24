import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;

public class SoiltempExogenous
{
    private double DEPIR;
    private double BIOMAS;
    private double TAMP;
    private double MULCHMASS;
    private double TMAX;
    private double SNOW;
    private double RAIN;
    private double TAV;
    private double TAVG;
    private double TMIN;
    
    public SoiltempExogenous() { }
    
    public SoiltempExogenous(SoiltempExogenous toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.DEPIR = toCopy.getDEPIR();
            this.BIOMAS = toCopy.getBIOMAS();
            this.TAMP = toCopy.getTAMP();
            this.MULCHMASS = toCopy.getMULCHMASS();
            this.TMAX = toCopy.getTMAX();
            this.SNOW = toCopy.getSNOW();
            this.RAIN = toCopy.getRAIN();
            this.TAV = toCopy.getTAV();
            this.TAVG = toCopy.getTAVG();
            this.TMIN = toCopy.getTMIN();
        }
    }
    public double getDEPIR()
    { return DEPIR; }

    public void setDEPIR(double _DEPIR)
    { this.DEPIR= _DEPIR; } 
    
    public double getBIOMAS()
    { return BIOMAS; }

    public void setBIOMAS(double _BIOMAS)
    { this.BIOMAS= _BIOMAS; } 
    
    public double getTAMP()
    { return TAMP; }

    public void setTAMP(double _TAMP)
    { this.TAMP= _TAMP; } 
    
    public double getMULCHMASS()
    { return MULCHMASS; }

    public void setMULCHMASS(double _MULCHMASS)
    { this.MULCHMASS= _MULCHMASS; } 
    
    public double getTMAX()
    { return TMAX; }

    public void setTMAX(double _TMAX)
    { this.TMAX= _TMAX; } 
    
    public double getSNOW()
    { return SNOW; }

    public void setSNOW(double _SNOW)
    { this.SNOW= _SNOW; } 
    
    public double getRAIN()
    { return RAIN; }

    public void setRAIN(double _RAIN)
    { this.RAIN= _RAIN; } 
    
    public double getTAV()
    { return TAV; }

    public void setTAV(double _TAV)
    { this.TAV= _TAV; } 
    
    public double getTAVG()
    { return TAVG; }

    public void setTAVG(double _TAVG)
    { this.TAVG= _TAVG; } 
    
    public double getTMIN()
    { return TMIN; }

    public void setTMIN(double _TMIN)
    { this.TMIN= _TMIN; } 
    
}