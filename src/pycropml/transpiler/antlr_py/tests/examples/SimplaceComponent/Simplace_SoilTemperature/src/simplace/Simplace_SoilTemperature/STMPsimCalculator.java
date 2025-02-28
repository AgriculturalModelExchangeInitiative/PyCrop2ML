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


public class STMPsimCalculator extends FWSimComponent
{
    private FWSimVariable<Double[]> cSoilLayerDepth;
    private FWSimVariable<Double> cFirstDayMeanTemp;
    private FWSimVariable<Double> cAVT;
    private FWSimVariable<Double> cABD;
    private FWSimVariable<Double> cDampingDepth;
    private FWSimVariable<Double> iSoilWaterContent;
    private FWSimVariable<Double> iSoilSurfaceTemperature;
    private FWSimVariable<Double[]> SoilTempArray;
    private FWSimVariable<Double[]> pSoilLayerDepth;

    public STMPsimCalculator(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public STMPsimCalculator(){
        super();
    }
    @Override
    protected void process()
    {
        Double [] t_cSoilLayerDepth = cSoilLayerDepth.getValue();
        Double t_cFirstDayMeanTemp = cFirstDayMeanTemp.getValue();
        Double t_cAVT = cAVT.getValue();
        Double t_cABD = cABD.getValue();
        Double t_cDampingDepth = cDampingDepth.getValue();
        Double t_iSoilWaterContent = iSoilWaterContent.getValue();
        Double t_iSoilSurfaceTemperature = iSoilSurfaceTemperature.getValue();
        Double [] t_SoilTempArray = SoilTempArray.getValue();
        Double [] t_pSoilLayerDepth = pSoilLayerDepth.getValue();
        Double XLAG;
        Double XLG1;
        Double DP;
        Double WC;
        Double DD;
        Double Z1;
        Integer i;
        Double ZD;
        Double RATE;
        XLAG = .8d;
        XLG1 = 1 - XLAG;
        DP = 1 + (2.5d * t_cABD / (t_cABD + Math.exp(6.53d - (5.63d * t_cABD))));
        WC = 0.001d * t_iSoilWaterContent / ((.356d - (.144d * t_cABD)) * t_cSoilLayerDepth[(t_cSoilLayerDepth.length - 1)]);
        DD = Math.exp(Math.log(0.5d / DP) * ((1 - WC) / (1 + WC)) * 2) * DP;
        Z1 = (double)(0);
        for (i=0 ; i!=t_SoilTempArray.length ; i+=1)
        {
            ZD = 0.5d * (Z1 + t_pSoilLayerDepth[i]) / DD;
            RATE = ZD / (ZD + Math.exp(-.8669d - (2.0775d * ZD))) * (t_cAVT - t_iSoilSurfaceTemperature);
            t_SoilTempArray[i] = XLAG * t_SoilTempArray[i] + (XLG1 * (RATE + t_iSoilSurfaceTemperature));
            Z1 = t_pSoilLayerDepth[i];
        }
        SoilTempArray.setValue(t_SoilTempArray, this);
    }
    @Override
    protected void init()
    {
        Double [] t_cSoilLayerDepth = cSoilLayerDepth.getValue();
        Double t_cFirstDayMeanTemp = cFirstDayMeanTemp.getValue();
        Double t_cAVT = cAVT.getValue();
        Double t_cABD = cABD.getValue();
        Double t_cDampingDepth = cDampingDepth.getValue();
        Double t_iSoilWaterContent = iSoilWaterContent.getValue();
        Double t_iSoilSurfaceTemperature = iSoilSurfaceTemperature.getValue();
        Double [] t_SoilTempArray = SoilTempArray.getDefault();
        Double [] t_pSoilLayerDepth = pSoilLayerDepth.getDefault();
        Double tProfileDepth;
        Double additionalDepth;
        Double firstAdditionalLayerHight;
        Integer layers;
        Double[] tStmp;
        Double[] tz;
        Integer i;
        Double depth;
        tProfileDepth = t_cSoilLayerDepth[t_cSoilLayerDepth.length - 1];
        additionalDepth = t_cDampingDepth - tProfileDepth;
        firstAdditionalLayerHight = additionalDepth - (double)(Math.floor(additionalDepth));
        layers = (int)(Math.abs((double)((int) Math.ceil(additionalDepth)))) + t_cSoilLayerDepth.length;
        tStmp = new Double [layers];
        tz = new Double [layers];
        for (i=0 ; i!=tStmp.length ; i+=1)
        {
            if (i < t_cSoilLayerDepth.length)
            {
                depth = t_cSoilLayerDepth[i];
            }
            else
            {
                depth = tProfileDepth + firstAdditionalLayerHight + i - t_cSoilLayerDepth.length;
            }
            tz[i] = depth;
            tStmp[i] = (t_cFirstDayMeanTemp * (t_cDampingDepth - depth) + (t_cAVT * depth)) / t_cDampingDepth;
        }
        t_SoilTempArray = tStmp;
        t_pSoilLayerDepth = tz;
        SoilTempArray.setValue(t_SoilTempArray, this);
        pSoilLayerDepth.setValue(t_pSoilLayerDepth, this);
    }

    public HashMap<String, FWSimVariable<?>> fillTestVariables(int aParamIndex, TEST_STATE aDefineOrCheck)
    {
        if(aParamIndex == 0 && aDefineOrCheck == TEST_STATE.DEFINE) //before process
        {
            FWSimVariable.setValue(new Double[] {0.1,0.5,1.5}, iFieldMap.get("STMPsimCalculator.cSoilLayerDepth"), this);
            FWSimVariable.setValue(15.0, iFieldMap.get("STMPsimCalculator.cFirstDayMeanTemp"), this);
            FWSimVariable.setValue(9.0, iFieldMap.get("STMPsimCalculator.cAVT"), this);
            FWSimVariable.setValue(1.4, iFieldMap.get("STMPsimCalculator.cABD"), this);
            FWSimVariable.setValue(6.0, iFieldMap.get("STMPsimCalculator.cDampingDepth"), this);
            FWSimVariable.setValue(0.3, iFieldMap.get("STMPsimCalculator.iSoilWaterContent"), this);
            FWSimVariable.setValue(6.0, iFieldMap.get("STMPsimCalculator.iSoilSurfaceTemperature"), this);
        }
        else if(aParamIndex ==  0 && aDefineOrCheck == TEST_STATE.CHECK) //after process
        {
            FWSimVariable.setValue(new Double[] {13.624360856350041,13.399968504634286,12.599999999999845,12.2,11.4,10.6,9.799999999999999,9.0}, iFieldMap.get("STMPsimCalculator.SoilTempArray"), this);
        }
        else return null;
        return iFieldMap;
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new STMPsimCalculator(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("cSoilLayerDepth", "Depth of soil layer", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.constant,"", 0.03, 20.0, null, this));
        addVariable(FWSimVariable.createSimVariable("cFirstDayMeanTemp", "Mean temperature on first day", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", -40.0, 50.0, null, this));
        addVariable(FWSimVariable.createSimVariable("cAVT", "Constant Temperature of deepest soil layer", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", -10.0, 20.0, null, this));
        addVariable(FWSimVariable.createSimVariable("cABD", "Mean bulk density", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", 1.0, 4.0, 2.0, this));
        addVariable(FWSimVariable.createSimVariable("cDampingDepth", "Initial value for damping depth of soil", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", 1.5, 20.0, 6.0, this));
        addVariable(FWSimVariable.createSimVariable("iSoilWaterContent", "Content of water in Soil", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 1.5, 20.0, 5.0, this));
        addVariable(FWSimVariable.createSimVariable("iSoilSurfaceTemperature", "Temperature at soil surface", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", 1.5, 20.0, null, this));
        addVariable(FWSimVariable.createSimVariable("SoilTempArray", "Array of temperature ", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"", -20, 40, null, this));
        addVariable(FWSimVariable.createSimVariable("pSoilLayerDepth", "Depth of soil layer plus additional depth", DATA_TYPE.DOUBLEARRAY, CONTENT_TYPE.state,"", 0.03, 20.0, null, this));

        return iFieldMap;
    }
}