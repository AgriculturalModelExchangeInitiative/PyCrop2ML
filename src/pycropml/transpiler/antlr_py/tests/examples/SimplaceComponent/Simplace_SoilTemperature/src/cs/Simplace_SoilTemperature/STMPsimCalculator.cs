using System;
using System.Collections.Generic;
using System.Linq;
public class STMPsimCalculator
{
    private double[] _cSoilLayerDepth;
    public double[] cSoilLayerDepth
        {
            get { return this._cSoilLayerDepth; }
            set { this._cSoilLayerDepth= value; } 
        }
    private double _cFirstDayMeanTemp;
    public double cFirstDayMeanTemp
        {
            get { return this._cFirstDayMeanTemp; }
            set { this._cFirstDayMeanTemp= value; } 
        }
    private double _cAVT;
    public double cAVT
        {
            get { return this._cAVT; }
            set { this._cAVT= value; } 
        }
    private double _cABD;
    public double cABD
        {
            get { return this._cABD; }
            set { this._cABD= value; } 
        }
    private double _cDampingDepth;
    public double cDampingDepth
        {
            get { return this._cDampingDepth; }
            set { this._cDampingDepth= value; } 
        }
    public STMPsimCalculator() { }
    
    public void  CalculateModel(SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex)
    {
        //- Name: STMPsimCalculator -Version: 001, -Time step: 1
        //- Description:
    //            * Title: STMPsimCalculator model
    //            * Authors: Gunther Krauss
    //            * Reference: ('http://www.simplace.net/doc/simplace_modules/',)
    //            * Institution: INRES Pflanzenbau, Uni Bonn
    //            * ExtendedDescription: as given in the documentation
    //            * ShortDescription: None
        //- inputs:
    //            * name: cSoilLayerDepth
    //                          ** description : Depth of soil layer
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : 
    //                          ** max : 20.0
    //                          ** min : 0.03
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    //            * name: cFirstDayMeanTemp
    //                          ** description : Mean temperature on first day
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 50.0
    //                          ** min : -40.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: cAVT
    //                          ** description : Constant Temperature of deepest soil layer
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 20.0
    //                          ** min : -10.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: cABD
    //                          ** description : Mean bulk density
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 4.0
    //                          ** min : 1.0
    //                          ** default : 2.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre
    //            * name: cDampingDepth
    //                          ** description : Initial value for damping depth of soil
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 20.0
    //                          ** min : 1.5
    //                          ** default : 6.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    //            * name: iSoilWaterContent
    //                          ** description : Content of water in Soil
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 20.0
    //                          ** min : 1.5
    //                          ** default : 5.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    //            * name: iSoilSurfaceTemperature
    //                          ** description : Temperature at soil surface
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 20.0
    //                          ** min : 1.5
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: SoilTempArray
    //                          ** description : Array of temperature 
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : 
    //                          ** max : 40
    //                          ** min : -20
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: pSoilLayerDepth
    //                          ** description : Depth of soil layer plus additional depth
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : 
    //                          ** max : 20.0
    //                          ** min : 0.03
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
        //- outputs:
    //            * name: SoilTempArray
    //                          ** description : Array of temperature 
    //                          ** datatype : DOUBLEARRAY
    //                          ** variablecategory : state
    //                          ** len : 
    //                          ** max : 40
    //                          ** min : -20
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
        double iSoilWaterContent = ex.iSoilWaterContent;
        double iSoilSurfaceTemperature = ex.iSoilSurfaceTemperature;
        double[] SoilTempArray = s.SoilTempArray;
        double[] pSoilLayerDepth = s.pSoilLayerDepth;
        double XLAG;
        double XLG1;
        double DP;
        double WC;
        double DD;
        double Z1;
        int i;
        double ZD;
        double RATE;
        XLAG = .8d;
        XLG1 = 1 - XLAG;
        DP = 1 + (2.5d * cABD / (cABD + Math.Exp(6.53d - (5.63d * cABD))));
        WC = 0.001d * iSoilWaterContent / ((.356d - (.144d * cABD)) * cSoilLayerDepth[(cSoilLayerDepth.Length - 1)]);
        DD = Math.Exp(Math.Log(0.5d / DP) * ((1 - WC) / (1 + WC)) * 2) * DP;
        Z1 = (double)(0);
        for (i=0 ; i!=SoilTempArray.Length ; i+=1)
        {
            ZD = 0.5d * (Z1 + pSoilLayerDepth[i]) / DD;
            RATE = ZD / (ZD + Math.Exp(-.8669d - (2.0775d * ZD))) * (cAVT - iSoilSurfaceTemperature);
            SoilTempArray[i] = XLAG * SoilTempArray[i] + (XLG1 * (RATE + iSoilSurfaceTemperature));
            Z1 = pSoilLayerDepth[i];
        }
        s.SoilTempArray= SoilTempArray;
    }
    public void Init(SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex)
    {
        double iSoilWaterContent;
        double iSoilSurfaceTemperature;
        double[] SoilTempArray ;
        double[] pSoilLayerDepth ;
        double tProfileDepth;
        double additionalDepth;
        double firstAdditionalLayerHight;
        int layers;
        double[] tStmp ;
        double[] tz ;
        int i;
        double depth;
        tProfileDepth = cSoilLayerDepth[cSoilLayerDepth.Length - 1];
        additionalDepth = cDampingDepth - tProfileDepth;
        firstAdditionalLayerHight = additionalDepth - (double)(Math.Floor(additionalDepth));
        layers = (int)(Math.Abs((double)((int) Math.Ceiling(additionalDepth)))) + cSoilLayerDepth.Length;
        tStmp = new double[ layers];
        tz = new double[ layers];
        for (i=0 ; i!=tStmp.Length ; i+=1)
        {
            if (i < cSoilLayerDepth.Length)
            {
                depth = cSoilLayerDepth[i];
            }
            else
            {
                depth = tProfileDepth + firstAdditionalLayerHight + i - cSoilLayerDepth.Length;
            }
            tz[i] = depth;
            tStmp[i] = (cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT * depth)) / cDampingDepth;
        }
        SoilTempArray = tStmp;
        pSoilLayerDepth = tz;
        s.SoilTempArray= SoilTempArray;
        s.pSoilLayerDepth= pSoilLayerDepth;
    }
}