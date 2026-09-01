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


public class NoSnowSoilSurfaceTemperature extends FWSimComponent
{
    private FWSimVariable<Double> tmin;
    private FWSimVariable<Double> tmax;
    private FWSimVariable<Double> globrad;
    private FWSimVariable<Double> soilCoverage;
    private FWSimVariable<Double> dampingFactor;
    private FWSimVariable<Double> soilSurfaceTemperature;

    public NoSnowSoilSurfaceTemperature(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public NoSnowSoilSurfaceTemperature(){
        super();
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("tmin", "the days min air temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"°C", -50.0, 70.0, null, this));
        addVariable(FWSimVariable.createSimVariable("tmax", "the days max air temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"°C", -50.0, 70.0, null, this));
        addVariable(FWSimVariable.createSimVariable("globrad", "the days global radiation", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"MJ/m**2/d", 0.0, 30.0, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("soilCoverage", "soilCoverage", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"dimensionless", 0.0, null, 0.0, this));
        addVariable(FWSimVariable.createSimVariable("dampingFactor", "dampingFactor", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"dimensionless", null, null, 0.8, this));
        addVariable(FWSimVariable.createSimVariable("soilSurfaceTemperature", "soilSurfaceTemperature of previous day", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"°C", null, null, 0.0, this));

        return iFieldMap;
    }
    @Override
    protected void process()
    {
        double t_tmin = tmin.getValue();
        double t_tmax = tmax.getValue();
        double t_globrad = globrad.getValue();
        double t_soilCoverage = soilCoverage.getValue();
        double t_dampingFactor = dampingFactor.getValue();
        double t_soilSurfaceTemperature = soilSurfaceTemperature.getValue();
        double shadingCoefficient;
        t_globrad = Math.max(8.33d, t_globrad);
        shadingCoefficient = 0.1d + (t_soilCoverage * t_dampingFactor + ((1 - t_soilCoverage) * (1 - t_dampingFactor)));
        t_soilSurfaceTemperature = (1.0d - shadingCoefficient) * (t_tmin + ((t_tmax - t_tmin) * Math.pow(0.03d * t_globrad, 0.5d))) + (shadingCoefficient * t_soilSurfaceTemperature);
        if (t_soilSurfaceTemperature < 0.0d)
        {
            t_soilSurfaceTemperature = t_soilSurfaceTemperature * 0.5d;
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
        return new NoSnowSoilSurfaceTemperature(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }
}