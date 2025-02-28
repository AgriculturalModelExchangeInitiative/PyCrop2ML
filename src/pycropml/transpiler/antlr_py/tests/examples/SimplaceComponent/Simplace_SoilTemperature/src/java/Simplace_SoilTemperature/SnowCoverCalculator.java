import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
public class SnowCoverCalculator
{
    private Double cCarbonContent;
    public Double getcCarbonContent()
    { return cCarbonContent; }

    public void setcCarbonContent(Double _cCarbonContent)
    { this.cCarbonContent= _cCarbonContent; } 
    
    public SnowCoverCalculator() { }
    public void  Calculate_snowcovercalculator(SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a,  SoilTemperatureExogenous ex)
    {
        //- Name: SnowCoverCalculator -Version: 001, -Time step: 1
        //- Description:
    //            * Title: SnowCoverCalculator model
    //            * Authors: Gunther Krauss
    //            * Reference: ('http://www.simplace.net/doc/simplace_modules/',)
    //            * Institution: INRES Pflanzenbau, Uni Bonn
    //            * ExtendedDescription: as given in the documentation
    //            * ShortDescription: None
        //- inputs:
    //            * name: cCarbonContent
    //                          ** description : Carbon content of upper soil layer
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 20.0
    //                          ** min : 0.0
    //                          ** default : 0.5
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/percent
    //            * name: iTempMax
    //                          ** description : Daily maximum temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 50.0
    //                          ** min : -40.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: iTempMin
    //                          ** description : Daily minimum temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 50.0
    //                          ** min : -40.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: iRadiation
    //                          ** description : Solar radiation
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 2000.0
    //                          ** min : 0.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/megajoule_per_square_metre
    //            * name: iRAIN
    //                          ** description : Rain amount
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 60.0
    //                          ** min : 0.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    //            * name: iCropResidues
    //                          ** description : Crop residues plus above ground biomass
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 20000.0
    //                          ** min : 0.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/gram_per_square_metre
    //            * name: iPotentialSoilEvaporation
    //                          ** description : Potenial Evaporation
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 12.0
    //                          ** min : 0.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    //            * name: iLeafAreaIndex
    //                          ** description : Leaf area index
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLE
    //                          ** max : 10.0
    //                          ** min : 0.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/square_metre_per_square_metre
    //            * name: iSoilTempArray
    //                          ** description : Soil Temp array of last day
    //                          ** inputtype : variable
    //                          ** variablecategory : exogenous
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : 
    //                          ** max : 35.0
    //                          ** min : -15.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: Albedo
    //                          ** description : Albedo
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 1.0
    //                          ** min : 0.0
    //                          ** default : 
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    //            * name: SnowWaterContent
    //                          ** description : Snow water content
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 1500.0
    //                          ** min : 0.0
    //                          ** default : 0.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    //            * name: SoilSurfaceTemperature
    //                          ** description : Soil surface temperature
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 70.0
    //                          ** min : -40.0
    //                          ** default : 0.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: AgeOfSnow
    //                          ** description : Age of snow
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** max : null
    //                          ** min : 0
    //                          ** default : 0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
        //- outputs:
    //            * name: SnowWaterContent
    //                          ** description : Snow water content
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** max : 1500.0
    //                          ** min : 0.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    //            * name: SoilSurfaceTemperature
    //                          ** description : Soil surface temperature
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** max : 70.0
    //                          ** min : -40.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    //            * name: AgeOfSnow
    //                          ** description : Age of snow
    //                          ** datatype : INT
    //                          ** variablecategory : state
    //                          ** max : null
    //                          ** min : 0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
    //            * name: SnowIsolationIndex
    //                          ** description : Snow isolation index
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** max : 1.0
    //                          ** min : 0.0
    //                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/one
        Double iTempMax = ex.getiTempMax();
        Double iTempMin = ex.getiTempMin();
        Double iRadiation = ex.getiRadiation();
        Double iRAIN = ex.getiRAIN();
        Double iCropResidues = ex.getiCropResidues();
        Double iPotentialSoilEvaporation = ex.getiPotentialSoilEvaporation();
        Double iLeafAreaIndex = ex.getiLeafAreaIndex();
        Double [] iSoilTempArray = ex.getiSoilTempArray();
        Double Albedo = s.getAlbedo();
        Double SnowWaterContent = s.getSnowWaterContent();
        Double SoilSurfaceTemperature = s.getSoilSurfaceTemperature();
        Integer AgeOfSnow = s.getAgeOfSnow();
        Double SnowIsolationIndex;
        Double tiCropResidues;
        Double tiSoilTempArray;
        Double TMEAN;
        Double TAMPL;
        Double DST;
        Double tSoilSurfaceTemperature;
        Double tSnowIsolationIndex;
        Double SNOWEVAPORATION;
        Double SNOWMELT;
        Double EAJ;
        Double ageOfSnowFactor;
        Double SNPKT;
        tiCropResidues = iCropResidues * 10.0d;
        tiSoilTempArray = iSoilTempArray[0];
        TMEAN = 0.5d * (iTempMax + iTempMin);
        TAMPL = 0.5d * (iTempMax - iTempMin);
        DST = TMEAN + (TAMPL * (iRadiation * (1 - Albedo) - 14) / 20);
        if (iRAIN > (double)(0) && (tiSoilTempArray < (double)(1) || (SnowWaterContent > (double)(3) || SoilSurfaceTemperature < (double)(0))))
        {
            SnowWaterContent = SnowWaterContent + iRAIN;
        }
        tSnowIsolationIndex = 1.0d;
        if (tiCropResidues < (double)(10))
        {
            tSnowIsolationIndex = tiCropResidues / (tiCropResidues + Math.exp(5.34d - (2.4d * tiCropResidues)));
        }
        if (SnowWaterContent < 1E-10d)
        {
            tSnowIsolationIndex = tSnowIsolationIndex * 0.85d;
            tSoilSurfaceTemperature = 0.5d * (DST + ((1 - tSnowIsolationIndex) * DST) + (tSnowIsolationIndex * tiSoilTempArray));
        }
        else
        {
            tSnowIsolationIndex = Math.max(SnowWaterContent / (SnowWaterContent + Math.exp(0.47d - (0.62d * SnowWaterContent))), tSnowIsolationIndex);
            tSoilSurfaceTemperature = (1 - tSnowIsolationIndex) * DST + (tSnowIsolationIndex * tiSoilTempArray);
        }
        if (SnowWaterContent == (double)(0) && !(iRAIN > (double)(0) && tiSoilTempArray < (double)(1)))
        {
            SnowWaterContent = (double)(0);
        }
        else
        {
            EAJ = .5d;
            if (SnowWaterContent < (double)(5))
            {
                EAJ = Math.exp(-Math.max((0.4d * iLeafAreaIndex), (0.1d * (tiCropResidues + 0.1d))));
            }
            SNOWEVAPORATION = iPotentialSoilEvaporation * EAJ;
            ageOfSnowFactor = AgeOfSnow / (AgeOfSnow + Math.exp(5.34d - (2.395d * AgeOfSnow)));
            SNPKT = .3333d * (2 * Math.min(tSoilSurfaceTemperature, tiSoilTempArray) + iTempMax);
            if (TMEAN > (double)(0))
            {
                SNOWMELT = Math.max(0, Math.sqrt(iTempMax * iRadiation) * (1.52d + (.54d * ageOfSnowFactor * SNPKT)));
            }
            else
            {
                SNOWMELT = (double)(0);
            }
            if (SNOWMELT + SNOWEVAPORATION > SnowWaterContent)
            {
                SNOWMELT = SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent;
                SNOWEVAPORATION = SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * SnowWaterContent;
            }
            SnowWaterContent = SnowWaterContent - (SNOWMELT + SNOWEVAPORATION);
            if (SnowWaterContent < (double)(0))
            {
                SnowWaterContent = (double)(0);
            }
            if (SnowWaterContent < (double)(5))
            {
                AgeOfSnow = 0;
            }
            else
            {
                AgeOfSnow = AgeOfSnow + 1;
            }
        }
        SnowIsolationIndex = tSnowIsolationIndex;
        SoilSurfaceTemperature = tSoilSurfaceTemperature;
        s.setSnowWaterContent(SnowWaterContent);
        s.setSoilSurfaceTemperature(SoilSurfaceTemperature);
        s.setAgeOfSnow(AgeOfSnow);
        a.setSnowIsolationIndex(SnowIsolationIndex);
    }
    public void Init(SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a,  SoilTemperatureExogenous ex)
    {
        Double iTempMax = ex.getiTempMax();
        Double iTempMin = ex.getiTempMin();
        Double iRadiation = ex.getiRadiation();
        Double iRAIN = ex.getiRAIN();
        Double iCropResidues = ex.getiCropResidues();
        Double iPotentialSoilEvaporation = ex.getiPotentialSoilEvaporation();
        Double iLeafAreaIndex = ex.getiLeafAreaIndex();
        Double [] iSoilTempArray = ex.getiSoilTempArray();
        Double Albedo;
        Double SnowWaterContent = 0.0;
        Double SoilSurfaceTemperature = 0.0;
        Integer AgeOfSnow = 0;
        Albedo = 0.0d;
        Albedo = 0.0226d * Math.log10(cCarbonContent) + 0.1502d;
        s.setAlbedo(Albedo);
        s.setSnowWaterContent(SnowWaterContent);
        s.setSoilSurfaceTemperature(SoilSurfaceTemperature);
        s.setAgeOfSnow(AgeOfSnow);
    }
}