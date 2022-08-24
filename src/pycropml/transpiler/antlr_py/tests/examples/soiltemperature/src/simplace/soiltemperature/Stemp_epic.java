import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.LocalDateTime;
import net.simplace.sim.model.FWSimComponent;
import net.simplace.sim.util.FWSimVarMap;
import net.simplace.sim.util.FWSimVariable;
import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;
import net.simplace.sim.util.FWSimVariable.DATA_TYPE;
import org.jdom.Element;


public class Stemp_epic extends FWSimComponent
{
    private FWSimVariable<Integer> NL;
    private FWSimVariable<String> ISWWAT;
    private FWSimVariable<Double[]> BD;
    private FWSimVariable<Double[]> DLAYR;
    private FWSimVariable<Double[]> DS;
    private FWSimVariable<Double[]> DUL;
    private FWSimVariable<Double[]> LL;
    private FWSimVariable<Integer> NLAYR;
    private FWSimVariable<Double[]> SW;
    private FWSimVariable<Double> CUMDPT;
    private FWSimVariable<Double[]> DSMID;
    private FWSimVariable<Double> SRFTEMP;
    private FWSimVariable<Integer> NDays;
    private FWSimVariable<Double> TDL;
    private FWSimVariable<Integer[]> WetDay;
    private FWSimVariable<Double[]> ST;
    private FWSimVariable<Double[]> TMA;

    public Stemp_epic(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Stemp_epic(){
        super();
    }
    @Override
    protected void process()
    {
        int tNL = NL.getValue();
        String tISWWAT = ISWWAT.getValue();
        Double [] tBD = BD.getValue();
        Double [] tDLAYR = DLAYR.getValue();
        Double [] tDS = DS.getValue();
        Double [] tDUL = DUL.getValue();
        Double [] tLL = LL.getValue();
        int tNLAYR = NLAYR.getValue();
        double tTAMP = TAMP.getValue();
        double tRAIN = RAIN.getValue();
        double tCUMDPT = CUMDPT.getValue();
        Double [] tDSMID = DSMID.getValue();
        Double [] tSW = SW.getValue();
        double tTAVG = TAVG.getValue();
        double tTMAX = TMAX.getValue();
        double tTMIN = TMIN.getValue();
        double tTAV = TAV.getValue();
        double tDEPIR = DEPIR.getValue();
        double tBIOMAS = BIOMAS.getValue();
        double tMULCHMASS = MULCHMASS.getValue();
        double tSNOW = SNOW.getValue();
        int I;
        int L;
        int NWetDays;
        double ABD;
        double B;
        double DP;
        double FX;
        double PESW;
        double TBD;
        double WW;
        double TLL;
        double TSW;
        double X2_AVG;
        double WFT;
        double BCV;
        double CV;
        double BCV1;
        double BCV2;
        double X2_PREV;
        TBD = 0.0d;
        TLL = 0.0d;
        TSW = 0.0d;
        X2_PREV = 0.0d;
        for (L=1 ; L!=tNLAYR + 1 ; L+=1)
        {
            TBD = TBD + (tBD[(L - 1)] * tDLAYR[(L - 1)]);
            tTDL = tTDL + (tDUL[(L - 1)] * tDLAYR[(L - 1)]);
            TLL = TLL + (tLL[(L - 1)] * tDLAYR[(L - 1)]);
            TSW = TSW + (tSW[(L - 1)] * tDLAYR[(L - 1)]);
        }
        ABD = TBD / tDS[(tNLAYR - 1)];
        FX = ABD / (ABD + (686.0d * Math.exp(-(5.63d * ABD))));
        DP = 1000.0d + (2500.0d * FX);
        WW = 0.356d - (0.144d * ABD);
        B = Math.log(500.0d / DP);
        if (tISWWAT == "Y")
        {
            PESW = Math.max(0.0d, TSW - TLL);
        }
        else
        {
            PESW = Math.max(0.0d, tTDL - TLL);
        }
        if (tNDays == 30)
        {
            for (I=1 ; I!=29 + 1 ; I+=1)
            {
                tWetDay[I - 1] = tWetDay[I + 1 - 1];
            }
        }
        else
        {
            tNDays = tNDays + 1;
        }
        if (tRAIN + tDEPIR > 1.E-6d)
        {
            tWetDay[tNDays - 1] = 1;
        }
        else
        {
            tWetDay[tNDays - 1] = 0;
        }
        NWetDays = tWetDay.stream().mapToInt(Integer::intValue).sum();
        WFT = (double)(NWetDays) / (double)(tNDays);
        CV = (tBIOMAS + tMULCHMASS) / 1000.d;
        BCV1 = CV / (CV + Math.exp(5.3396d - (2.3951d * CV)));
        BCV2 = tSNOW / (tSNOW + Math.exp(2.303d - (0.2197d * tSNOW)));
        BCV = Math.max(BCV1, BCV2);
        new Pair[]{new Pair<>("TMA", TMA),new Pair<>("X2_PREV", X2_PREV),new Pair<>("ST", ST),new Pair<>("SRFTEMP", SRFTEMP),new Pair<>("X2_AVG", X2_AVG)} = SOILT_EPIC(tNL, B, BCV, tCUMDPT, DP, tDSMID, tNLAYR, PESW, tTAV, tTAVG, tTMAX, tTMIN, tWetDay[tNDays - 1], WFT, WW, tTMA, X2_PREV, tST);
        
        SRFTEMP.setValue(tSRFTEMP, this);
        NDays.setValue(tNDays, this);
        TDL.setValue(tTDL, this);
        WetDay.setValue(tWetDay, this);
        ST.setValue(tST, this);
        TMA.setValue(tTMA, this);
    }
    public static Pair[] SOILT_EPIC(int NL, double B, double BCV, double CUMDPT, double DP, Double [] DSMID, int NLAYR, double PESW, double TAV, double TAVG, double TMAX, double TMIN, int WetDay, double WFT, double WW, Double [] TMA, double X2_PREV, Double [] ST)
    {
    int K;
    int L;
    double DD;
    double FX;
    double WC;
    double ZD;
    double X1;
    double X2;
    double X3;
    double F;
    double X2_AVG;
    double LAG;
    double SRFTEMP;
    LAG = 0.5d;
    WC = Math.max(0.01d, PESW) / (WW * tCUMDPT) * 10.0d;
    FX = Math.exp(B * Math.pow((1.0d - WC) / (1.0d + WC), 2));
    DD = FX * DP;
    if (tWetDay > 0)
    {
        X2 = WFT * (tTAVG - tTMIN) + tTMIN;
    }
    else
    {
        X2 = WFT * (tTMAX - tTAVG) + tTAVG + 2.d;
    }
    tTMA[1 - 1] = X2;
    for (K=5 ; K!=2 - 1 ; K+=-1)
    {
        tTMA[K - 1] = tTMA[K - 1 - 1];
    }
    X2_AVG = tTMA.stream().mapToDouble(Double::doubleValue).sum() / 5.0d;
    X3 = (1.d - BCV) * X2_AVG + (BCV * X2_PREV);
    tSRFTEMP = Math.min(X2_AVG, X3);
    X1 = tTAV - X3;
    for (L=1 ; L!=tNLAYR + 1 ; L+=1)
    {
        ZD = tDSMID[(L - 1)] / DD;
        F = ZD / (ZD + Math.exp(-.8669d - (2.0775d * ZD)));
        tST[L - 1] = LAG * tST[(L - 1)] + ((1.d - LAG) * (F * X1 + X3));
    }
    X2_PREV = X2_AVG;
    return new Pair[]{new Pair<>("TMA", TMA),new Pair<>("X2_PREV", X2_PREV),new Pair<>("ST", ST),new Pair<>("SRFTEMP", SRFTEMP),new Pair<>("X2_AVG", X2_AVG)};
}
@Override
protected void init()
{
    int tNL = NL.getValue();
    String tISWWAT = ISWWAT.getValue();
    Double [] tBD = BD.getValue();
    Double [] tDLAYR = DLAYR.getValue();
    Double [] tDS = DS.getValue();
    Double [] tDUL = DUL.getValue();
    Double [] tLL = LL.getValue();
    int tNLAYR = NLAYR.getValue();
    double tTAMP = TAMP.getValue();
    double tRAIN = RAIN.getValue();
    Double [] tSW = SW.getValue();
    double tTAVG = TAVG.getValue();
    double tTMAX = TMAX.getValue();
    double tTMIN = TMIN.getValue();
    double tTAV = TAV.getValue();
    double tDEPIR = DEPIR.getValue();
    double tBIOMAS = BIOMAS.getValue();
    double tMULCHMASS = MULCHMASS.getValue();
    double tSNOW = SNOW.getValue();
    double tCUMDPT;
    Double [] tDSMID;
    double tSRFTEMP;
    int tNDays;
    double tTDL;
    Integer [] tWetDay;
    Double [] tST;
    Double [] tTMA;
    int I;
    int L;
    double ABD;
    double B;
    double DP;
    double FX;
    double PESW;
    double TBD;
    double WW;
    double TLL;
    double TSW;
    double X2_AVG;
    double WFT;
    double BCV;
    double CV;
    double BCV1;
    double BCV2;
    double X2_PREV;
    Double[] SWI = Double[tNL];
    SWI = tSW;
    TBD = 0.0d;
    TLL = 0.0d;
    TSW = 0.0d;
    tTDL = 0.0d;
    tCUMDPT = 0.0d;
    X2_PREV = 0.0d;
    for (L=1 ; L!=tNLAYR + 1 ; L+=1)
    {
        tDSMID[L - 1] = tCUMDPT + (tDLAYR[(L - 1)] * 5.0d);
        tCUMDPT = tCUMDPT + (tDLAYR[(L - 1)] * 10.0d);
        TBD = TBD + (tBD[(L - 1)] * tDLAYR[(L - 1)]);
        TLL = TLL + (tLL[(L - 1)] * tDLAYR[(L - 1)]);
        TSW = TSW + (SWI[(L - 1)] * tDLAYR[(L - 1)]);
        tTDL = tTDL + (tDUL[(L - 1)] * tDLAYR[(L - 1)]);
    }
    if (tISWWAT == "Y")
    {
        PESW = Math.max(0.0d, TSW - TLL);
    }
    else
    {
        PESW = Math.max(0.0d, tTDL - TLL);
    }
    ABD = TBD / tDS[(tNLAYR - 1)];
    FX = ABD / (ABD + (686.0d * Math.exp(-(5.63d * ABD))));
    DP = 1000.0d + (2500.0d * FX);
    WW = 0.356d - (0.144d * ABD);
    B = Math.log(500.0d / DP);
    for (I=1 ; I!=5 + 1 ; I+=1)
    {
        tTMA[I - 1] = (int)(tTAVG * 10000.d) / 10000.d;
    }
    X2_AVG = tTMA[(1 - 1)] * 5.0d;
    for (L=1 ; L!=tNLAYR + 1 ; L+=1)
    {
        tST[L - 1] = tTAVG;
    }
    WFT = 0.1d;
    tWetDay = new Integer[0];
    tNDays = 0;
    CV = tMULCHMASS / 1000.d;
    BCV1 = CV / (CV + Math.exp(5.3396d - (2.3951d * CV)));
    BCV2 = tSNOW / (tSNOW + Math.exp(2.303d - (0.2197d * tSNOW)));
    BCV = Math.max(BCV1, BCV2);
    for (I=1 ; I!=8 + 1 ; I+=1)
    {
        new Pair[]{new Pair<>("TMA", TMA),new Pair<>("X2_PREV", X2_PREV),new Pair<>("ST", ST),new Pair<>("SRFTEMP", SRFTEMP),new Pair<>("X2_AVG", X2_AVG)} = SOILT_EPIC(tNL, B, BCV, tCUMDPT, DP, tDSMID, tNLAYR, PESW, tTAV, tTAVG, tTMAX, tTMIN, 0, WFT, WW, tTMA, X2_PREV, tST);
    }
    CUMDPT.setValue(tCUMDPT, this);
    DSMID.setValue(tDSMID, this);
    SRFTEMP.setValue(tSRFTEMP, this);
    NDays.setValue(tNDays, this);
    TDL.setValue(tTDL, this);
    WetDay.setValue(tWetDay, this);
    ST.setValue(tST, this);
    TMA.setValue(tTMA, this);
}

@Override
protected FWSimComponent clone(FWSimVarMap aVarMap)
{
    return new Stemp_epic(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
}

@Override
public HashMap<String, FWSimVariable<?>> createVariables()
{
    addVariable(FWSimVariable.createSimVariable("cNL", "Number of soil layers", DATA_TYPE.INT, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cISWWAT", "Water simulation control switch (Y or N)", DATA_TYPE.CHAR, CONTENT_TYPE.constant,"", null, null, "Y", this));
    addVariable(FWSimVariable.createSimVariable("cBD", "Bulk density, soil layer NL", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cDLAYR", "Thickness of soil layer NL", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cDS", "Cumulative depth in soil layer NL", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cDUL", "Volumetric soil water content at Drained Upper Limit in soil layer L", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cLL", "Volumetric soil water content in soil layer NL at lower limit", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cNLAYR", "Actual number of soil layers", DATA_TYPE.INT, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("cSW", "Volumetric soil water content in layer NL", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sCUMDPT", "Cumulative depth of soil profile", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sDSMID", "Depth to midpoint of soil layer NL", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sSRFTEMP", "Temperature of soil surface litter", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sNDays", "Number of days ...", DATA_TYPE.INT, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sTDL", "Total water content of soil at drained upper limit", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sWetDay", "Wet Days", DATA_TYPE.INTARRAY, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sST", "Soil temperature in soil layer NL", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"", null, null, "", this));
    addVariable(FWSimVariable.createSimVariable("sTMA", "Array of previous 5 days of average soil temperatures.", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"", null, null,"" , this));

    return iFieldMap;
}
}