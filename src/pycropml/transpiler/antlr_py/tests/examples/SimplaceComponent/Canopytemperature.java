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
import org.jdom.Element;


public class Canopytemperature extends FWSimComponent
{
    private int[] jj;
    private FWSimVariable<Double[]> SoilTempArray;
    int j;
    List<String> list;
    private FWSimVariable<FWSimVariable<GOGO>> lambdaV;
    private FWSimVariable<Double> lambdaV;
    private FWSimVariable<Double> rhoDensityAir;
    private FWSimVariable<Double> specificHeatCapacityAir;
    private FWSimVariable<Double> minTair;
    private FWSimVariable<Double> maxTair;
    private FWSimVariable<Double> conductance;
    private FWSimVariable<Double> minCanopyTemperature;
    private FWSimVariable<Double> maxCanopyTemperature;
    private FWSimVariable<Double> cropHeatFlux;

    public Canopytemperature(String aName, HashMap<String, FWSimVariable<?>> aFieldMap, HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
    {
        super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
    }

    public Canopytemperature(){
        super();
    }
    @Override
    protected void process()
    {
        double a = 5 - 3 * 3 + Math.max(15,12);
        double tminTair = minTair.getValue();
        double tmaxTair = maxTair.getValue();
        double tcropHeatFlux = cropHeatFlux.getValue();
        double tconductance = conductance.getValue();
        double tlambdaV = lambdaV.getValue();
        double trhoDensityAir = rhoDensityAir.getValue();
        double tspecificHeatCapacityAir = specificHeatCapacityAir.getValue();
        double tminCanopyTemperature;
        double tmaxCanopyTemperature;
        tminCanopyTemperature = tminTair + (tcropHeatFlux / (trhoDensityAir * tspecificHeatCapacityAir * tconductance / tlambdaV * 1000.0d));
        tmaxCanopyTemperature = tmaxTair + (tcropHeatFlux / (trhoDensityAir * tspecificHeatCapacityAir * tconductance / tlambdaV * 1000.0d));
        minCanopyTemperature.setValue(tminCanopyTemperature, this);
        maxCanopyTemperature.setValue(tmaxCanopyTemperature, this);
    }

    @Override
    protected void init()
    {
    }

    @Override
    protected FWSimComponent clone(FWSimVarMap aVarMap, int a)
    {
        return new Canopytemperature(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
    }

    @Override
    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("clambdaV", "latent heat of vaporization of water", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", 0, 10, 2.454, this));
        addVariable(FWSimVariable.createSimVariable("crhoDensityAir", "Density of air", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", null, null, 1.225, this));
        addVariable(FWSimVariable.createSimVariable("cspecificHeatCapacityAir", "Specific heat capacity of dry air", DATA_TYPE.DOUBLE, CONTENT_TYPE.constant,"", null, null, 0.00101, this));
        addVariable(FWSimVariable.createSimVariable("iminTair", "minimum air temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", -30, 45, 0.7, this));
        addVariable(FWSimVariable.createSimVariable("imaxTair", "maximum air Temperature", DATA_TYPE.DOUBLE, CONTENT_TYPE.input,"", -30, 45, 7.2, this));
        addVariable(FWSimVariable.createSimVariable("sconductance", "the boundary layer conductance", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", 0, 10000, 598.685, this));
        addVariable(FWSimVariable.createSimVariable("sminCanopyTemperature", "minimal Canopy Temperature  ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", -30, 45, null, this));
        addVariable(FWSimVariable.createSimVariable("smaxCanopyTemperature", "maximal Canopy Temperature ", DATA_TYPE.DOUBLE, CONTENT_TYPE.state,"", -30, 45, null, this));
        addVariable(FWSimVariable.createSimVariable("rcropHeatFlux", "Crop heat flux", DATA_TYPE.DOUBLE, CONTENT_TYPE.rate,"", 0, 10000, 447.912, this));
        return iFieldMap;
    }
}