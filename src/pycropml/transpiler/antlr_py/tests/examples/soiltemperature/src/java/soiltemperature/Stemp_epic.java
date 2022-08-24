import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
public class Stemp_epic
{
    private int NL;
    public int getNL()
    { return NL; }

    public void setNL(int _NL)
    { this.NL= _NL; } 
    
    private String ISWWAT;
    public String getISWWAT()
    { return ISWWAT; }

    public void setISWWAT(String _ISWWAT)
    { this.ISWWAT= _ISWWAT; } 
    
    private Double [] BD;
    public Double [] getBD()
    { return BD; }

    public void setBD(Double [] _BD)
    { this.BD= _BD; } 
    
    private Double [] DLAYR;
    public Double [] getDLAYR()
    { return DLAYR; }

    public void setDLAYR(Double [] _DLAYR)
    { this.DLAYR= _DLAYR; } 
    
    private Double [] DS;
    public Double [] getDS()
    { return DS; }

    public void setDS(Double [] _DS)
    { this.DS= _DS; } 
    
    private Double [] DUL;
    public Double [] getDUL()
    { return DUL; }

    public void setDUL(Double [] _DUL)
    { this.DUL= _DUL; } 
    
    private Double [] LL;
    public Double [] getLL()
    { return LL; }

    public void setLL(Double [] _LL)
    { this.LL= _LL; } 
    
    private int NLAYR;
    public int getNLAYR()
    { return NLAYR; }

    public void setNLAYR(int _NLAYR)
    { this.NLAYR= _NLAYR; } 
    
    private Double [] SW;
    public Double [] getSW()
    { return SW; }

    public void setSW(Double [] _SW)
    { this.SW= _SW; } 
    
    public Stemp_epic() { }
    public void  Calculate_stemp_epic(SoiltempState s, SoiltempState s1, SoiltempRate r, SoiltempAuxiliary a,  SoiltempExogenous ex)
    {
        //- Name: STEMP_EPIC -Version: 001, -Time step: 1
        //- Description:
    //            * Title: model of soil
    //            * Author: Cyrille
    //            * Reference: None
    //            * Institution: INRAE
    //            * ExtendedDescription: None
    //            * ShortDescription: None
        //- inputs:
    //            * name: NL
    //                          ** description : Number of soil layers
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : INT
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : dimensionless
    //            * name: ISWWAT
    //                          ** description : Water simulation control switch (Y or N)
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : STRING
    //                          ** max : 
    //                          ** min : 
    //                          ** default : Y
    //                          ** unit : dimensionless
    //            * name: BD
    //                          ** description : Bulk density, soil layer NL
    //                          ** inputtype : parameter
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : g [soil] / cm3 [soil]
    //            * name: DLAYR
    //                          ** description : Thickness of soil layer NL
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm
    //            * name: DS
    //                          ** description : Cumulative depth in soil layer NL
    //                          ** inputtype : parameter
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm
    //            * name: DUL
    //                          ** description : Volumetric soil water content at Drained Upper Limit in soil layer L
    //                          ** inputtype : parameter
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm3[water]/cm3[soil]
    //            * name: LL
    //                          ** description : Volumetric soil water content in soil layer NL at lower limit
    //                          ** inputtype : parameter
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm3 [water] / cm3 [soil]
    //            * name: NLAYR
    //                          ** description : Actual number of soil layers
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : INT
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : dimensionless
    //            * name: TAMP
    //                          ** description : Annual amplitude of the average air temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: RAIN
    //                          ** description : daily rainfall
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : mm
    //            * name: CUMDPT
    //                          ** description : Cumulative depth of soil profile
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : mm
    //            * name: DSMID
    //                          ** description : Depth to midpoint of soil layer NL
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm
    //            * name: SW
    //                          ** description : Volumetric soil water content in layer NL
    //                          ** inputtype : parameter
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm3 [water] / cm3 [soil]
    //            * name: TAVG
    //                          ** description : Average daily temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: TMAX
    //                          ** description : Maximum daily temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: TMIN
    //                          ** description : Maximum Temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: TAV
    //                          ** description : Average annual soil temperature, used with TAMP to calculate soil temperature.
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: SRFTEMP
    //                          ** description : Temperature of soil surface litter
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: NDays
    //                          ** description : Number of days ...
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : day
    //            * name: TDL
    //                          ** description : Total water content of soil at drained upper limit
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : cm
    //            * name: WetDay
    //                          ** description : Wet Days
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : INTARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : day
    //            * name: ST
    //                          ** description : Soil temperature in soil layer NL
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: TMA
    //                          ** description : Array of previous 5 days of average soil temperatures.
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : 5
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : degC
    //            * name: DEPIR
    //                          ** description : Management variable
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : don't know
    //            * name: BIOMAS
    //                          ** description : Biomass
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : kg/ha
    //            * name: MULCHMASS
    //                          ** description : Mulch Mass
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : kg/ha
    //            * name: SNOW
    //                          ** description : Snow cover
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : mm
        //- outputs:
    //            * name: SRFTEMP
    //                          ** description : Temperature of soil surface litter
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : degC
    //            * name: NDays
    //                          ** description : Number of days ...
    //                          ** datatype : INT
    //                          ** variablecategory : state
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : day
    //            * name: TDL
    //                          ** description : Total water content of soil at drained upper limit
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : cm
    //            * name: WetDay
    //                          ** description : Wet Days
    //                          ** datatype : INTARRAY
    //                          ** variablecategory : state
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : day
    //            * name: ST
    //                          ** description : Soil temperature in soil layer NL
    //                          ** datatype : DOUBLEARRAY
    //                          ** variablecategory : state
    //                          ** len : NL
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : degC
    //            * name: TMA
    //                          ** description : Array of previous 5 days of average soil temperatures.
    //                          ** datatype : DOUBLEARRAY
    //                          ** variablecategory : state
    //                          ** len : 5
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : degC
        SOILT_EPIC zz_SOILT_EPIC;
        double TAMP = ex.getTAMP();
        double RAIN = ex.getRAIN();
        double CUMDPT = s.getCUMDPT();
        Double [] DSMID = s.getDSMID();
        double TAVG = ex.getTAVG();
        double TMAX = ex.getTMAX();
        double TMIN = ex.getTMIN();
        double TAV = ex.getTAV();
        double SRFTEMP = s.getSRFTEMP();
        int NDays = s.getNDays();
        double TDL = s.getTDL();
        Integer [] WetDay = s.getWetDay();
        Double [] ST = s.getST();
        Double [] TMA = s.getTMA();
        double DEPIR = ex.getDEPIR();
        double BIOMAS = ex.getBIOMAS();
        double MULCHMASS = ex.getMULCHMASS();
        double SNOW = ex.getSNOW();
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
        for (L=1 ; L!=NLAYR + 1 ; L+=1)
        {
            TBD = TBD + (BD[(L - 1)] * DLAYR[(L - 1)]);
            TDL = TDL + (DUL[(L - 1)] * DLAYR[(L - 1)]);
            TLL = TLL + (LL[(L - 1)] * DLAYR[(L - 1)]);
            TSW = TSW + (SW[(L - 1)] * DLAYR[(L - 1)]);
        }
        ABD = TBD / DS[(NLAYR - 1)];
        FX = ABD / (ABD + (686.0d * Math.exp(-(5.63d * ABD))));
        DP = 1000.0d + (2500.0d * FX);
        WW = 0.356d - (0.144d * ABD);
        B = Math.log(500.0d / DP);
        if (ISWWAT == "Y")
        {
            PESW = Math.max(0.0d, TSW - TLL);
        }
        else
        {
            PESW = Math.max(0.0d, TDL - TLL);
        }
        if (NDays == 30)
        {
            for (I=1 ; I!=29 + 1 ; I+=1)
            {
                WetDay[I - 1] = WetDay[I + 1 - 1];
            }
        }
        else
        {
            NDays = NDays + 1;
        }
        if (RAIN + DEPIR > 1.E-6d)
        {
            WetDay[NDays - 1] = 1;
        }
        else
        {
            WetDay[NDays - 1] = 0;
        }
        NWetDays = Arrays.stream(WetDay).mapToInt(Int::intValue).sum();
        WFT = (double)(NWetDays) / (double)(NDays);
        CV = (BIOMAS + MULCHMASS) / 1000.d;
        BCV1 = CV / (CV + Math.exp(5.3396d - (2.3951d * CV)));
        BCV2 = SNOW / (SNOW + Math.exp(2.303d - (0.2197d * SNOW)));
        BCV = Math.max(BCV1, BCV2);
        zz_SOILT_EPIC = Calculate_SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, WetDay[NDays - 1], WFT, WW, TMA, X2_PREV, ST);
        TMA = zz_SOILT_EPIC.getTMA();
        X2_PREV = zz_SOILT_EPIC.getX2_PREV();
        ST = zz_SOILT_EPIC.getST();
        SRFTEMP = zz_SOILT_EPIC.getSRFTEMP();
        X2_AVG = zz_SOILT_EPIC.getX2_AVG();
        s.setSRFTEMP(SRFTEMP);
        s.setNDays(NDays);
        s.setTDL(TDL);
        s.setWetDay(WetDay);
        s.setST(ST);
        s.setTMA(TMA);
    }
    public SOILT_EPIC Calculate_SOILT_EPIC (int NL, double B, double BCV, double CUMDPT, double DP, Double [] DSMID, int NLAYR, double PESW, double TAV, double TAVG, double TMAX, double TMIN, int WetDay, double WFT, double WW, Double [] TMA, double X2_PREV, Double [] ST)
    {
        int K;
        int L;
        double DD;
        double FX;
        double SRFTEMP;
        double WC;
        double ZD;
        double X1;
        double X2;
        double X3;
        double F;
        double X2_AVG;
        double LAG;
        LAG = 0.5d;
        WC = Math.max(0.01d, PESW) / (WW * CUMDPT) * 10.0d;
        FX = Math.exp(B * Math.pow((1.0d - WC) / (1.0d + WC), 2));
        DD = FX * DP;
        if (WetDay > 0)
        {
            X2 = WFT * (TAVG - TMIN) + TMIN;
        }
        else
        {
            X2 = WFT * (TMAX - TAVG) + TAVG + 2.d;
        }
        TMA[1 - 1] = X2;
        for (K=5 ; K!=2 - 1 ; K+=-1)
        {
            TMA[K - 1] = TMA[K - 1 - 1];
        }
        X2_AVG = Arrays.stream(TMA).mapToDouble(Double::doubleValue).sum() / 5.0d;
        X3 = (1.d - BCV) * X2_AVG + (BCV * X2_PREV);
        SRFTEMP = Math.min(X2_AVG, X3);
        X1 = TAV - X3;
        for (L=1 ; L!=NLAYR + 1 ; L+=1)
        {
            ZD = DSMID[(L - 1)] / DD;
            F = ZD / (ZD + Math.exp(-.8669d - (2.0775d * ZD)));
            ST[L - 1] = LAG * ST[(L - 1)] + ((1.d - LAG) * (F * X1 + X3));
        }
        X2_PREV = X2_AVG;
        return new SOILT_EPIC(TMA, X2_PREV, ST, SRFTEMP, X2_AVG);
    }
    public void Init(SoiltempState s, SoiltempState s1, SoiltempRate r, SoiltempAuxiliary a,  SoiltempExogenous ex)
    {
        SOILT_EPIC zz_SOILT_EPIC;
        double TAMP = ex.getTAMP();
        double RAIN = ex.getRAIN();
        double TAVG = ex.getTAVG();
        double TMAX = ex.getTMAX();
        double TMIN = ex.getTMIN();
        double TAV = ex.getTAV();
        double DEPIR = ex.getDEPIR();
        double BIOMAS = ex.getBIOMAS();
        double MULCHMASS = ex.getMULCHMASS();
        double SNOW = ex.getSNOW();
        double CUMDPT;
        Double[] DSMID =  new Double [NL];
        double SRFTEMP;
        int NDays;
        double TDL;
        Integer[] WetDay =  new Integer [NL];
        Double[] ST =  new Double [NL];
        Double[] TMA =  new Double [5];
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
        Double[] SWI =  new Double [NL];
        SWI = SW;
        TBD = 0.0d;
        TLL = 0.0d;
        TSW = 0.0d;
        TDL = 0.0d;
        CUMDPT = 0.0d;
        X2_PREV = 0.0d;
        for (L=1 ; L!=NLAYR + 1 ; L+=1)
        {
            DSMID[L - 1] = CUMDPT + (DLAYR[(L - 1)] * 5.0d);
            CUMDPT = CUMDPT + (DLAYR[(L - 1)] * 10.0d);
            TBD = TBD + (BD[(L - 1)] * DLAYR[(L - 1)]);
            TLL = TLL + (LL[(L - 1)] * DLAYR[(L - 1)]);
            TSW = TSW + (SWI[(L - 1)] * DLAYR[(L - 1)]);
            TDL = TDL + (DUL[(L - 1)] * DLAYR[(L - 1)]);
        }
        if (ISWWAT == "Y")
        {
            PESW = Math.max(0.0d, TSW - TLL);
        }
        else
        {
            PESW = Math.max(0.0d, TDL - TLL);
        }
        ABD = TBD / DS[(NLAYR - 1)];
        FX = ABD / (ABD + (686.0d * Math.exp(-(5.63d * ABD))));
        DP = 1000.0d + (2500.0d * FX);
        WW = 0.356d - (0.144d * ABD);
        B = Math.log(500.0d / DP);
        for (I=1 ; I!=5 + 1 ; I+=1)
        {
            TMA[I - 1] = (int)(TAVG * 10000.d) / 10000.d;
        }
        X2_AVG = TMA[(1 - 1)] * 5.0d;
        for (L=1 ; L!=NLAYR + 1 ; L+=1)
        {
            ST[L - 1] = TAVG;
        }
        WFT = 0.1d;
        Arrays.fill(WetDay, 0);
        NDays = 0;
        CV = MULCHMASS / 1000.d;
        BCV1 = CV / (CV + Math.exp(5.3396d - (2.3951d * CV)));
        BCV2 = SNOW / (SNOW + Math.exp(2.303d - (0.2197d * SNOW)));
        BCV = Math.max(BCV1, BCV2);
        for (I=1 ; I!=8 + 1 ; I+=1)
        {
            zz_SOILT_EPIC = Calculate_SOILT_EPIC(NL, B, BCV, CUMDPT, DP, DSMID, NLAYR, PESW, TAV, TAVG, TMAX, TMIN, 0, WFT, WW, TMA, X2_PREV, ST);
            TMA = zz_SOILT_EPIC.getTMA();
            X2_PREV = zz_SOILT_EPIC.getX2_PREV();
            ST = zz_SOILT_EPIC.getST();
            SRFTEMP = zz_SOILT_EPIC.getSRFTEMP();
            X2_AVG = zz_SOILT_EPIC.getX2_AVG();
        }
        s.setCUMDPT(CUMDPT);
        s.setDSMID(DSMID);
        s.setSRFTEMP(SRFTEMP);
        s.setNDays(NDays);
        s.setTDL(TDL);
        s.setWetDay(WetDay);
        s.setST(ST);
        s.setTMA(TMA);
    }
}
final class SOILT_EPIC {
    private Double [] TMA;
    public Double [] getTMA()
    { return TMA; }

    public void setTMA(Double [] _TMA)
    { this.TMA= _TMA; } 
    
    private double X2_PREV;
    public double getX2_PREV()
    { return X2_PREV; }

    public void setX2_PREV(double _X2_PREV)
    { this.X2_PREV= _X2_PREV; } 
    
    private Double [] ST;
    public Double [] getST()
    { return ST; }

    public void setST(Double [] _ST)
    { this.ST= _ST; } 
    
    private double SRFTEMP;
    public double getSRFTEMP()
    { return SRFTEMP; }

    public void setSRFTEMP(double _SRFTEMP)
    { this.SRFTEMP= _SRFTEMP; } 
    
    private double X2_AVG;
    public double getX2_AVG()
    { return X2_AVG; }

    public void setX2_AVG(double _X2_AVG)
    { this.X2_AVG= _X2_AVG; } 
    
    public SOILT_EPIC(Double [] TMA,double X2_PREV,Double [] ST,double SRFTEMP,double X2_AVG)
    {
        this.TMA = TMA;
        this.X2_PREV = X2_PREV;
        this.ST = ST;
        this.SRFTEMP = SRFTEMP;
        this.X2_AVG = X2_AVG;
    }
}