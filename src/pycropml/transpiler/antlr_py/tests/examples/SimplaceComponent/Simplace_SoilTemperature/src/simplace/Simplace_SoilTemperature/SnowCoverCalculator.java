package net.simplace.sim.components.Simplace_SoilTemperature;
import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import net.simplace.sim.model.FWSimComponent;
import net.simplace.sim.util.FWSimVarMap;
import net.simplace.sim.util.FWSimVariable;
import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;
import net.simplace.sim.util.FWSimVariable.DATA_TYPE;
import org.jdom2.Element;


public class SnowCoverCalculator extends FWSimComponent
{
    private FWSimVariable<Double> cCarbonContent;
    private FWSimVariable<Double> iTempMax;
    private FWSimVariable<Double> iTempMin;
    private FWSimVariable<Double> iRadiation;
    private FWSimVariable<Double> iRAIN;
    private FWSimVariable<Double> iCropResidues;
    private FWSimVariable<Double> iPotentialSoilEvaporation;
    private FWSimVariable<Double> iLeafAreaIndex;
    private FWSimVariable<Double[]> iSoilTempArray;
    private FWSimVariable<Double> Albedo;
    private FWSimVariable<Double> SnowWaterContent;
    private FWSimVariable<Double> SoilSurfaceTemperature;
    private FWSimVariable<Integer> AgeOfSnow;
    private FWSimVariable<Double> SnowIsolationIndex;

    public SnowCoverCalculator(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public SnowCoverCalculator(){
        super();
    }
    @Override
    protected void process()
    {
        Double t_cCarbonContent = cCarbonContent.getValue();
        Double t_iTempMax = iTempMax.getValue();
        Double t_iTempMin = iTempMin.getValue();
        Double t_iRadiation = iRadiation.getValue();
        Double t_iRAIN = iRAIN.getValue();
        Double t_iCropResidues = iCropResidues.getValue();
        Double t_iPotentialSoilEvaporation = iPotentialSoilEvaporation.getValue();
        Double t_iLeafAreaIndex = iLeafAreaIndex.getValue();
        Double [] t_iSoilTempArray = iSoilTempArray.getValue();
        Double t_Albedo = Albedo.getValue();
        Double t_SnowWaterContent = SnowWaterContent.getValue();
        Double t_SoilSurfaceTemperature = SoilSurfaceTemperature.getValue();
        Integer t_AgeOfSnow = AgeOfSnow.getValue();
        Double t_SnowIsolationIndex;
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
        tiCropResidues = t_iCropResidues * 10.0d;
        tiSoilTempArray = t_iSoilTempArray[0];
        TMEAN = 0.5d * (t_iTempMax + t_iTempMin);
        TAMPL = 0.5d * (t_iTempMax - t_iTempMin);
        DST = TMEAN + (TAMPL * (t_iRadiation * (1 - t_Albedo) - 14) / 20);
        if (t_iRAIN > (double)(0) && (tiSoilTempArray < (double)(1) || (t_SnowWaterContent > (double)(3) || t_SoilSurfaceTemperature < (double)(0))))
        {
            t_SnowWaterContent = t_SnowWaterContent + t_iRAIN;
        }
        tSnowIsolationIndex = 1.0d;
        if (tiCropResidues < (double)(10))
        {
            tSnowIsolationIndex = tiCropResidues / (tiCropResidues + Math.exp(5.34d - (2.4d * tiCropResidues)));
        }
        if (t_SnowWaterContent < 1E-10d)
        {
            tSnowIsolationIndex = tSnowIsolationIndex * 0.85d;
            tSoilSurfaceTemperature = 0.5d * (DST + ((1 - tSnowIsolationIndex) * DST) + (tSnowIsolationIndex * tiSoilTempArray));
        }
        else
        {
            tSnowIsolationIndex = Math.max(t_SnowWaterContent / (t_SnowWaterContent + Math.exp(0.47d - (0.62d * t_SnowWaterContent))), tSnowIsolationIndex);
            tSoilSurfaceTemperature = (1 - tSnowIsolationIndex) * DST + (tSnowIsolationIndex * tiSoilTempArray);
        }
        if (t_SnowWaterContent == (double)(0) && !(t_iRAIN > (double)(0) && tiSoilTempArray < (double)(1)))
        {
            t_SnowWaterContent = (double)(0);
        }
        else
        {
            EAJ = .5d;
            if (t_SnowWaterContent < (double)(5))
            {
                EAJ = Math.exp(-Math.max((0.4d * t_iLeafAreaIndex), (0.1d * (tiCropResidues + 0.1d))));
            }
            SNOWEVAPORATION = t_iPotentialSoilEvaporation * EAJ;
            ageOfSnowFactor = t_AgeOfSnow / (t_AgeOfSnow + Math.exp(5.34d - (2.395d * t_AgeOfSnow)));
            SNPKT = .3333d * (2 * Math.min(tSoilSurfaceTemperature, tiSoilTempArray) + t_iTempMax);
            if (TMEAN > (double)(0))
            {
                SNOWMELT = Math.max(0, Math.sqrt(t_iTempMax * t_iRadiation) * (1.52d + (.54d * ageOfSnowFactor * SNPKT)));
            }
            else
            {
                SNOWMELT = (double)(0);
            }
            if (SNOWMELT + SNOWEVAPORATION > t_SnowWaterContent)
            {
                SNOWMELT = SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * t_SnowWaterContent;
                SNOWEVAPORATION = SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * t_SnowWaterContent;
            }
            t_SnowWaterContent = t_SnowWaterContent - (SNOWMELT + SNOWEVAPORATION);
            if (t_SnowWaterContent < (double)(0))
            {
                t_SnowWaterContent = (double)(0);
            }
            if (t_SnowWaterContent < (double)(5))
            {
                t_AgeOfSnow = 0;
            }
            else
            {
                t_AgeOfSnow = t_AgeOfSnow + 1;
            }
        }
        t_SnowIsolationIndex = tSnowIsolationIndex;
        t_SoilSurfaceTemperature = tSoilSurfaceTemperature;
        SnowWaterContent.setValue(t_SnowWaterContent, this);
        SoilSurfaceTemperature.setValue(t_SoilSurfaceTemperature, this);
        AgeOfSnow.setValue(t_AgeOfSnow, this);
        SnowIsolationIndex.setValue(t_SnowIsolationIndex, this);
    }
    @Override
    protected void init()
    {
        Double t_cCarbonContent = cCarbonContent.getValue();
        Double t_iTempMax = iTempMax.getValue();
        Double t_iTempMin = iTempMin.getValue();
        Double t_iRadiation = iRadiation.getValue();
        Double t_iRAIN = iRAIN.getValue();
        Double t_iCropResidues = iCropResidues.getValue();
        Double t_iPotentialSoilEvaporation = iPotentialSoilEvaporation.getValue();
        Double t_iLeafAreaIndex = iLeafAreaIndex.getValue();
        Double [] t_iSoilTempArray = iSoilTempArray.getValue();
        Double t_Albedo = Albedo.getDefault();
        Double t_SnowWaterContent = SnowWaterContent.getDefault();
        Double t_SoilSurfaceTemperature = SoilSurfaceTemperature.getDefault();
        Integer t_AgeOfSnow = AgeOfSnow.getDefault();
        t_Albedo = 0.0d;
        t_Albedo = 0.0226d * Math.log10(t_cCarbonContent) + 0.1502d;
        Albedo.setValue(t_Albedo, this);
        SnowWaterContent.setValue(t_SnowWaterContent, this);
        SoilSurfaceTemperature.setValue(t_SoilSurfaceTemperature, this);
        AgeOfSnow.setValue(t_AgeOfSnow, this);
    }

    public HashMap<String, FWSimVariable<?>> fillTestVariables(int aParamIndex, TEST_STATE aDefineOrCheck)
    {
        if(aParamIndex == 0 && aDefineOrCheck == TEST_STATE.DEFINE) //before process
        {
            FWSimVariable.setValue(10.0, iFieldMap.get("SnowCoverCalculator.cCarbonContent"), this);
            FWSimVariable.setValue(3.0, iFieldMap.get("SnowCoverCalculator.iTempMax"), this);
            FWSimVariable.setValue(-9.0, iFieldMap.get("SnowCoverCalculator.iTempMin"), this);
            FWSimVariable.setValue(1.4, iFieldMap.get("SnowCoverCalculator.iRadiation"), this);
            FWSimVariable.setValue(6.0, iFieldMap.get("SnowCoverCalculator.iRAIN"), this);
            FWSimVariable.setValue(30.0, iFieldMap.get("SnowCoverCalculator.iCropResidues"), this);
            FWSimVariable.setValue(0.6, iFieldMap.get("SnowCoverCalculator.iPotentialSoilEvaporation"), this);
            FWSimVariable.setValue(0.1, iFieldMap.get("SnowCoverCalculator.iLeafAreaIndex"), this);
            FWSimVariable.setValue(new Double[] {2.6,5.4,8.6,12.2,11.4,10.6,9.8,9.0}, iFieldMap.get("SnowCoverCalculator.iSoilTempArray"), this);
            FWSimVariable.setValue(5.0, iFieldMap.get("SnowCoverCalculator.SnowWaterContent"), this);
            FWSimVariable.setValue(5, iFieldMap.get("SnowCoverCalculator.AgeOfSnow"), this);
            FWSimVariable.setValue(1.8397688, iFieldMap.get("SnowCoverCalculator.SoilSurfaceTemperature"), this);
        }
        else if(aParamIndex ==  0 && aDefineOrCheck == TEST_STATE.CHECK) //after process
        {
            FWSimVariable.setValue(10.7, iFieldMap.get("SnowCoverCalculator.SnowWaterContent"), this);
            FWSimVariable.setValue(6, iFieldMap.get("SnowCoverCalculator.AgeOfSnow"), this);
            FWSimVariable.setValue(1.0, iFieldMap.get("SnowCoverCalculator.SnowIsolationIndex"), this);
            FWSimVariable.setValue(2.6, iFieldMap.get("SnowCoverCalculator.SoilSurfaceTemperature"), this);
        }
        else return null;
        return iFieldMap;
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new SnowCoverCalculator(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cCarbonContent", "Carbon content of upper soil layer", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", 0.0, 20.0, 0.5, this));
        addVariable(FWSimVariable.createSimVariable("iTempMax", "Daily maximum temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", -40.0, 50.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iTempMin", "Daily minimum temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", -40.0, 50.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iRadiation", "Solar radiation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 0.0, 2000.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iRAIN", "Rain amount", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 0.0, 60.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iCropResidues", "Crop residues plus above ground biomass", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 0.0, 20000.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iPotentialSoilEvaporation", "Potenial Evaporation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 0.0, 12.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iLeafAreaIndex", "Leaf area index", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 0.0, 10.0, null, this));
        addVariable(FWSimVariable.createSimVariable("iSoilTempArray", "Soil Temp array of last day", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.input,"", -15.0, 35.0, null, this));
        addVariable(FWSimVariable.createSimVariable("Albedo", "Albedo", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", 0.0, 1.0, null, this));
        addVariable(FWSimVariable.createSimVariable("SnowWaterContent", "Snow water content", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", 0.0, 1500.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("SoilSurfaceTemperature", "Soil surface temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", -40.0, 70.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("AgeOfSnow", "Age of snow", DATA_TYPE.INT, CONTENT_TYPE.state,"", 0, null, 0, this));
        addVariable(FWSimVariable.createSimVariable("SnowIsolationIndex", "Snow isolation index", DATA_TYPE.DOUBLE, CONTENT_TYPE.out,"", 0.0, 1.0, null, this));

        return iFieldMap;
    }
}