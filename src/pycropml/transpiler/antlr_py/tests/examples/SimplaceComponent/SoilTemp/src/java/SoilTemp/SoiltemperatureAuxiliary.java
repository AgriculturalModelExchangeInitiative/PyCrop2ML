import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;

public class SoiltemperatureAuxiliary
{
    private Double SnowIsolationIndex;
    
    public SoiltemperatureAuxiliary() { }
    
    public SoiltemperatureAuxiliary(SoiltemperatureAuxiliary toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SnowIsolationIndex = toCopy.getSnowIsolationIndex();
        }
    }
    public Double getSnowIsolationIndex()
    { return SnowIsolationIndex; }

    public void setSnowIsolationIndex(Double _SnowIsolationIndex)
    { this.SnowIsolationIndex= _SnowIsolationIndex; } 
    
}