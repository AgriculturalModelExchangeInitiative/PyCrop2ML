package SoilTemperature.src.java2.SoilTemperature;
import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;

public class SoiltemperatureAuxiliary
{
    private double SnowIsolationIndex;
    
    public SoiltemperatureAuxiliary() { }
    
    public SoiltemperatureAuxiliary(SoiltemperatureAuxiliary toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SnowIsolationIndex = toCopy.getSnowIsolationIndex();
        }
    }
    public double getSnowIsolationIndex()
    { return SnowIsolationIndex; }

    public void setSnowIsolationIndex(double _SnowIsolationIndex)
    { this.SnowIsolationIndex= _SnowIsolationIndex; } 
    
}