public class SoiltempComponent
{
    
    public SoiltempComponent() { }

    Stemp_epic _Stemp_epic = new Stemp_epic();

    public Double [] getBD()
    { return _Stemp_epic.getBD(); }
    public void setBD(Double [] BD)
    { _Stemp_epic.setBD(BD); } 

    public int getNL()
    { return _Stemp_epic.getNL(); }
    public void setNL(int NL)
    { _Stemp_epic.setNL(NL); } 

    public int getNLAYR()
    { return _Stemp_epic.getNLAYR(); }
    public void setNLAYR(int NLAYR)
    { _Stemp_epic.setNLAYR(NLAYR); } 

    public Double [] getSW()
    { return _Stemp_epic.getSW(); }
    public void setSW(Double [] SW)
    { _Stemp_epic.setSW(SW); } 

    public Double [] getDS()
    { return _Stemp_epic.getDS(); }
    public void setDS(Double [] DS)
    { _Stemp_epic.setDS(DS); } 

    public Double [] getDLAYR()
    { return _Stemp_epic.getDLAYR(); }
    public void setDLAYR(Double [] DLAYR)
    { _Stemp_epic.setDLAYR(DLAYR); } 

    public String getISWWAT()
    { return _Stemp_epic.getISWWAT(); }
    public void setISWWAT(String ISWWAT)
    { _Stemp_epic.setISWWAT(ISWWAT); } 

    public Double [] getDUL()
    { return _Stemp_epic.getDUL(); }
    public void setDUL(Double [] DUL)
    { _Stemp_epic.setDUL(DUL); } 

    public Double [] getLL()
    { return _Stemp_epic.getLL(); }
    public void setLL(Double [] LL)
    { _Stemp_epic.setLL(LL); } 
    public void  Calculate_soiltemp(SoiltempState s, SoiltempState s1, SoiltempRate r, SoiltempAuxiliary a, SoiltempExogenous ex)
    {
        _Stemp_epic.Calculate_stemp_epic(s, s1, r, a);
    }
    private Double [] BD;
    private int NL;
    private int NLAYR;
    private Double [] SW;
    private Double [] DS;
    private Double [] DLAYR;
    private String ISWWAT;
    private Double [] DUL;
    private Double [] LL;
    public SoiltempComponent(SoiltempComponent toCopy) // copy constructor 
    {
        
        for (int i = 0; i < toCopy.getBD.length; i++)
        {
            BD[i] = toCopy.getBD()[i];
        }
        this.NL = toCopy.getNL();
        this.NLAYR = toCopy.getNLAYR();
        
        for (int i = 0; i < toCopy.getSW.length; i++)
        {
            SW[i] = toCopy.getSW()[i];
        }
        
        for (int i = 0; i < toCopy.getDS.length; i++)
        {
            DS[i] = toCopy.getDS()[i];
        }
        
        for (int i = 0; i < toCopy.getDLAYR.length; i++)
        {
            DLAYR[i] = toCopy.getDLAYR()[i];
        }
        this.ISWWAT = toCopy.getISWWAT();
        
        for (int i = 0; i < toCopy.getDUL.length; i++)
        {
            DUL[i] = toCopy.getDUL()[i];
        }
        
        for (int i = 0; i < toCopy.getLL.length; i++)
        {
            LL[i] = toCopy.getLL()[i];
        }

    }
}