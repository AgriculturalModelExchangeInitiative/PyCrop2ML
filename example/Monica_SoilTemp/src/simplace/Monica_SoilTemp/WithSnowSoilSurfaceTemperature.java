package net.simplace.sim.components.Monica_SoilTemp;
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


public class WithSnowSoilSurfaceTemperature extends FWSimComponent
{
    private FWSimVariable<Double> noSnowSoilSurfaceTemperature;
    private FWSimVariable<Double> soilSurfaceTemperatureBelowSnow;
    private FWSimVariable<Boolean> hasSnowCover;
    private FWSimVariable<Double> soilSurfaceTemperature;

    public WithSnowSoilSurfaceTemperature(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public WithSnowSoilSurfaceTemperature(){
        super();
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("noSnowSoilSurfaceTemperature", "soilSurfaceTemperature without snow", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"°C", null, null, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("soilSurfaceTemperatureBelowSnow", "soilSurfaceTemperature below snow cover", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"°C", null, null, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("hasSnowCover", "is soil covered by snow", DATA_TYPE.BOOLEAN, CONTENT_TYPE.input,"dimensionless", null, null, false, this));
        addVariable(FWSimVariable.createSimVariable("soilSurfaceTemperature", "soilSurfaceTemperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"°C", null, null, null, this));

        return iFieldMap;
    }
    @Override
    protected void process()
    {
        double t_noSnowSoilSurfaceTemperature = noSnowSoilSurfaceTemperature.getValue();
        double t_soilSurfaceTemperatureBelowSnow = soilSurfaceTemperatureBelowSnow.getValue();
        Boolean t_hasSnowCover = hasSnowCover.getValue();
        double t_soilSurfaceTemperature;
        if (t_hasSnowCover)
        {
            t_soilSurfaceTemperature = t_soilSurfaceTemperatureBelowSnow;
        }
        else
        {
            t_soilSurfaceTemperature = t_noSnowSoilSurfaceTemperature;
        }
        soilSurfaceTemperature.setValue(t_soilSurfaceTemperature, this);
    }

    @Override
    protected void init()
    {
    }
    public HashMap<String, FWSimVariable<?>> fillTestVariables(int aParamIndex, TEST_STATE aDefineOrCheck)
    {
        return iFieldMap;
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap)
    {
        return new WithSnowSoilSurfaceTemperature(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }
}