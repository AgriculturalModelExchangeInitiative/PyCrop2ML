import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
public class SoilTemperature
{
    public void Init(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a,  SoilTemperatureCompExogenous ex)
    {
        double soilSurfaceTemperature = 0.0;
        Double[] soilTemperature =  new Double [noOfTempLayers];
        Double[] V =  new Double [noOfTempLayers];
        Double[] B =  new Double [noOfTempLayers];
        Double[] volumeMatrix =  new Double [noOfTempLayers];
        Double[] volumeMatrixOld =  new Double [noOfTempLayers];
        Double[] matrixPrimaryDiagonal =  new Double [noOfTempLayers];
        Double[] matrixSecondaryDiagonal =  new Double [noOfTempLayersPlus1];
        Double[] heatConductivity =  new Double [noOfTempLayers];
        Double[] heatConductivityMean =  new Double [noOfTempLayers];
        Double[] heatCapacity =  new Double [noOfTempLayers];
        Double[] solution =  new Double [noOfTempLayers];
        Double[] matrixDiagonal =  new Double [noOfTempLayers];
        Double[] matrixLowerTriangle =  new Double [noOfTempLayers];
        Double[] heatFlow =  new Double [noOfTempLayers];
        soilTemperature= new Double[noOfTempLayers];
        Arrays.fill(soilTemperature, 0.0d);
        V= new Double[noOfTempLayers];
        Arrays.fill(V, 0.0d);
        B= new Double[noOfTempLayers];
        Arrays.fill(B, 0.0d);
        volumeMatrix= new Double[noOfTempLayers];
        Arrays.fill(volumeMatrix, 0.0d);
        volumeMatrixOld= new Double[noOfTempLayers];
        Arrays.fill(volumeMatrixOld, 0.0d);
        matrixPrimaryDiagonal= new Double[noOfTempLayers];
        Arrays.fill(matrixPrimaryDiagonal, 0.0d);
        matrixSecondaryDiagonal= new Double[noOfTempLayersPlus1];
        Arrays.fill(matrixSecondaryDiagonal, 0.0d);
        heatConductivity= new Double[noOfTempLayers];
        Arrays.fill(heatConductivity, 0.0d);
        heatConductivityMean= new Double[noOfTempLayers];
        Arrays.fill(heatConductivityMean, 0.0d);
        heatCapacity= new Double[noOfTempLayers];
        Arrays.fill(heatCapacity, 0.0d);
        solution= new Double[noOfTempLayers];
        Arrays.fill(solution, 0.0d);
        matrixDiagonal= new Double[noOfTempLayers];
        Arrays.fill(matrixDiagonal, 0.0d);
        matrixLowerTriangle= new Double[noOfTempLayers];
        Arrays.fill(matrixLowerTriangle, 0.0d);
        heatFlow= new Double[noOfTempLayers];
        Arrays.fill(heatFlow, 0.0d);
        Integer groundLayer;
        Integer bottomLayer;
        double lti_1;
        double lti;
        double ts;
        double dw;
        double cw;
        double dq;
        double cq;
        double da;
        double ca;
        double dh;
        double ch;
        double sbdi;
        double smi;
        double sati;
        double somi;
        double hci_1;
        double hci;
        Integer i;
        for (i=0 ; i!=noOfSoilLayers ; i+=1)
        {
            soilTemperature[i] = (1.0d - ((double)(i) / noOfSoilLayers)) * initialSurfaceTemp + ((double)(i) / noOfSoilLayers * baseTemp);
        }
        groundLayer = noOfTempLayers - 2;
        bottomLayer = noOfTempLayers - 1;
        layerThickness[groundLayer] = 2.0d * layerThickness[(groundLayer - 1)];
        layerThickness[bottomLayer] = 1.0d;
        soilTemperature[groundLayer] = (soilTemperature[groundLayer - 1] + baseTemp) * 0.5d;
        soilTemperature[bottomLayer] = baseTemp;
        V[0] = layerThickness[0];
        B[0] = 2.0d / layerThickness[0];
        for (i=1 ; i!=noOfTempLayers ; i+=1)
        {
            lti_1 = layerThickness[i - 1];
            lti = layerThickness[i];
            B[i] = 2.0d / (lti + lti_1);
            V[i] = lti * nTau;
        }
        ts = timeStep;
        dw = densityWater;
        cw = specificHeatCapacityWater;
        dq = quartzRawDensity;
        cq = specificHeatCapacityQuartz;
        da = densityAir;
        ca = specificHeatCapacityAir;
        dh = densityHumus;
        ch = specificHeatCapacityHumus;
        for (i=0 ; i!=noOfSoilLayers ; i+=1)
        {
            sbdi = soilBulkDensity[i];
            smi = soilMoistureConst[i];
            heatConductivity[i] = (3.0d * (sbdi / 1000.0d) - 1.7d) * 0.001d / (1.0d + ((11.5d - (5.0d * (sbdi / 1000.0d))) * Math.exp(-50.0d * Math.pow(smi / (sbdi / 1000.0d), 1.5d)))) * 86400.0d * ts * 100.0d * 4.184d;
            sati = saturation[i];
            somi = soilOrganicMatter[i] / da * sbdi;
            heatCapacity[i] = smi * dw * cw + ((sati - smi) * da * ca) + (somi * dh * ch) + ((1.0d - sati - somi) * dq * cq);
        }
        heatCapacity[groundLayer] = heatCapacity[groundLayer - 1];
        heatCapacity[bottomLayer] = heatCapacity[groundLayer];
        heatConductivity[groundLayer] = heatConductivity[groundLayer - 1];
        heatConductivity[bottomLayer] = heatConductivity[groundLayer];
        soilSurfaceTemperature = initialSurfaceTemp;
        heatConductivityMean[0] = heatConductivity[0];
        for (i=1 ; i!=noOfTempLayers ; i+=1)
        {
            lti_1 = layerThickness[i - 1];
            lti = layerThickness[i];
            hci_1 = heatConductivity[i - 1];
            hci = heatConductivity[i];
            heatConductivityMean[i] = (lti_1 * hci_1 + (lti * hci)) / (lti + lti_1);
        }
        for (i=0 ; i!=noOfTempLayers ; i+=1)
        {
            volumeMatrix[i] = V[i] * heatCapacity[i];
            volumeMatrixOld[i] = volumeMatrix[i];
            matrixSecondaryDiagonal[i] = -B[i] * heatConductivityMean[i];
        }
        matrixSecondaryDiagonal[bottomLayer + 1] = 0.0d;
        for (i=0 ; i!=noOfTempLayers ; i+=1)
        {
            matrixPrimaryDiagonal[i] = volumeMatrix[i] - matrixSecondaryDiagonal[i] - matrixSecondaryDiagonal[i + 1];
        }
        s.setsoilSurfaceTemperature(soilSurfaceTemperature);
        s.setsoilTemperature(soilTemperature);
        s.setV(V);
        s.setB(B);
        s.setvolumeMatrix(volumeMatrix);
        s.setvolumeMatrixOld(volumeMatrixOld);
        s.setmatrixPrimaryDiagonal(matrixPrimaryDiagonal);
        s.setmatrixSecondaryDiagonal(matrixSecondaryDiagonal);
        s.setheatConductivity(heatConductivity);
        s.setheatConductivityMean(heatConductivityMean);
        s.setheatCapacity(heatCapacity);
        s.setsolution(solution);
        s.setmatrixDiagonal(matrixDiagonal);
        s.setmatrixLowerTriangle(matrixLowerTriangle);
        s.setheatFlow(heatFlow);
    }
    private Integer noOfSoilLayers;
    public Integer getnoOfSoilLayers()
    { return noOfSoilLayers; }

    public void setnoOfSoilLayers(Integer _noOfSoilLayers)
    { this.noOfSoilLayers= _noOfSoilLayers; } 
    
    private Integer noOfTempLayers;
    public Integer getnoOfTempLayers()
    { return noOfTempLayers; }

    public void setnoOfTempLayers(Integer _noOfTempLayers)
    { this.noOfTempLayers= _noOfTempLayers; } 
    
    private Integer noOfTempLayersPlus1;
    public Integer getnoOfTempLayersPlus1()
    { return noOfTempLayersPlus1; }

    public void setnoOfTempLayersPlus1(Integer _noOfTempLayersPlus1)
    { this.noOfTempLayersPlus1= _noOfTempLayersPlus1; } 
    
    private double timeStep;
    public double gettimeStep()
    { return timeStep; }

    public void settimeStep(double _timeStep)
    { this.timeStep= _timeStep; } 
    
    private Double [] soilMoistureConst;
    public Double [] getsoilMoistureConst()
    { return soilMoistureConst; }

    public void setsoilMoistureConst(Double [] _soilMoistureConst)
    { this.soilMoistureConst= _soilMoistureConst; } 
    
    private double baseTemp;
    public double getbaseTemp()
    { return baseTemp; }

    public void setbaseTemp(double _baseTemp)
    { this.baseTemp= _baseTemp; } 
    
    private double initialSurfaceTemp;
    public double getinitialSurfaceTemp()
    { return initialSurfaceTemp; }

    public void setinitialSurfaceTemp(double _initialSurfaceTemp)
    { this.initialSurfaceTemp= _initialSurfaceTemp; } 
    
    private double densityAir;
    public double getdensityAir()
    { return densityAir; }

    public void setdensityAir(double _densityAir)
    { this.densityAir= _densityAir; } 
    
    private double specificHeatCapacityAir;
    public double getspecificHeatCapacityAir()
    { return specificHeatCapacityAir; }

    public void setspecificHeatCapacityAir(double _specificHeatCapacityAir)
    { this.specificHeatCapacityAir= _specificHeatCapacityAir; } 
    
    private double densityHumus;
    public double getdensityHumus()
    { return densityHumus; }

    public void setdensityHumus(double _densityHumus)
    { this.densityHumus= _densityHumus; } 
    
    private double specificHeatCapacityHumus;
    public double getspecificHeatCapacityHumus()
    { return specificHeatCapacityHumus; }

    public void setspecificHeatCapacityHumus(double _specificHeatCapacityHumus)
    { this.specificHeatCapacityHumus= _specificHeatCapacityHumus; } 
    
    private double densityWater;
    public double getdensityWater()
    { return densityWater; }

    public void setdensityWater(double _densityWater)
    { this.densityWater= _densityWater; } 
    
    private double specificHeatCapacityWater;
    public double getspecificHeatCapacityWater()
    { return specificHeatCapacityWater; }

    public void setspecificHeatCapacityWater(double _specificHeatCapacityWater)
    { this.specificHeatCapacityWater= _specificHeatCapacityWater; } 
    
    private double quartzRawDensity;
    public double getquartzRawDensity()
    { return quartzRawDensity; }

    public void setquartzRawDensity(double _quartzRawDensity)
    { this.quartzRawDensity= _quartzRawDensity; } 
    
    private double specificHeatCapacityQuartz;
    public double getspecificHeatCapacityQuartz()
    { return specificHeatCapacityQuartz; }

    public void setspecificHeatCapacityQuartz(double _specificHeatCapacityQuartz)
    { this.specificHeatCapacityQuartz= _specificHeatCapacityQuartz; } 
    
    private double nTau;
    public double getnTau()
    { return nTau; }

    public void setnTau(double _nTau)
    { this.nTau= _nTau; } 
    
    private Double [] layerThickness;
    public Double [] getlayerThickness()
    { return layerThickness; }

    public void setlayerThickness(Double [] _layerThickness)
    { this.layerThickness= _layerThickness; } 
    
    private Double [] soilBulkDensity;
    public Double [] getsoilBulkDensity()
    { return soilBulkDensity; }

    public void setsoilBulkDensity(Double [] _soilBulkDensity)
    { this.soilBulkDensity= _soilBulkDensity; } 
    
    private Double [] saturation;
    public Double [] getsaturation()
    { return saturation; }

    public void setsaturation(Double [] _saturation)
    { this.saturation= _saturation; } 
    
    private Double [] soilOrganicMatter;
    public Double [] getsoilOrganicMatter()
    { return soilOrganicMatter; }

    public void setsoilOrganicMatter(Double [] _soilOrganicMatter)
    { this.soilOrganicMatter= _soilOrganicMatter; } 
    
    public SoilTemperature() { }
    public void  Calculate_Model(SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a,  SoilTemperatureCompExogenous ex)
    {
        //- Name: SoilTemperature -Version: 1, -Time step: 1
        //- Description:
    //            * Title: Model of soil temperature
    //            * Authors: Michael Berg-Mohnicke
    //            * Reference: None
    //            * Institution: ZALF e.V.
    //            * ExtendedDescription: None
    //            * ShortDescription: Calculates the soil temperature at all soil layers
        //- inputs:
    //            * name: noOfSoilLayers
    //                          ** description : noOfSoilLayers
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : INT
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 20
    //                          ** unit : dimensionless
    //            * name: noOfTempLayers
    //                          ** description : noOfTempLayers=noOfSoilLayers+2
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : INT
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 22
    //                          ** unit : dimensionless
    //            * name: noOfTempLayersPlus1
    //                          ** description : for matrixSecondaryDiagonal
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : INT
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 23
    //                          ** unit : dimensionless
    //            * name: soilSurfaceTemperature
    //                          ** description : current soilSurfaceTemperature
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** max : 80.0
    //                          ** min : -50.0
    //                          ** default : 0.0
    //                          ** unit : °C
    //            * name: timeStep
    //                          ** description : timeStep
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 1.0
    //                          ** unit : dimensionless
    //            * name: soilMoistureConst
    //                          ** description : constant soilmoisture during the model run
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfSoilLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : m**3/m**3
    //            * name: baseTemp
    //                          ** description : baseTemperature
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 9.5
    //                          ** unit : °C
    //            * name: initialSurfaceTemp
    //                          ** description : initialSurfaceTemperature
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 10.0
    //                          ** unit : °C
    //            * name: densityAir
    //                          ** description : DensityAir
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 1.25
    //                          ** unit : kg/m**3
    //            * name: specificHeatCapacityAir
    //                          ** description : SpecificHeatCapacityAir
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 1005.0
    //                          ** unit : J/kg/K
    //            * name: densityHumus
    //                          ** description : DensityHumus
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 1300.0
    //                          ** unit : kg/m**3
    //            * name: specificHeatCapacityHumus
    //                          ** description : SpecificHeatCapacityHumus
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 1920.0
    //                          ** unit : J/kg/K
    //            * name: densityWater
    //                          ** description : DensityWater
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 1000.0
    //                          ** unit : kg/m**3
    //            * name: specificHeatCapacityWater
    //                          ** description : SpecificHeatCapacityWater
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 4192.0
    //                          ** unit : J/kg/K
    //            * name: quartzRawDensity
    //                          ** description : QuartzRawDensity
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 2650.0
    //                          ** unit : kg/m**3
    //            * name: specificHeatCapacityQuartz
    //                          ** description : SpecificHeatCapacityQuartz
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 750.0
    //                          ** unit : J/kg/K
    //            * name: nTau
    //                          ** description : NTau
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 0.65
    //                          ** unit : ?
    //            * name: layerThickness
    //                          ** description : layerThickness
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : m
    //            * name: soilBulkDensity
    //                          ** description : bulkDensity
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfSoilLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : kg/m**3
    //            * name: saturation
    //                          ** description : saturation
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfSoilLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : m**3/m**3
    //            * name: soilOrganicMatter
    //                          ** description : soilOrganicMatter
    //                          ** inputtype : parameter
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfSoilLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : m**3/m**3
    //            * name: soilTemperature
    //                          ** description : soilTemperature
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: V
    //                          ** description : V
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: B
    //                          ** description : B
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: volumeMatrix
    //                          ** description : volumeMatrix
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: volumeMatrixOld
    //                          ** description : volumeMatrixOld
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: matrixPrimaryDiagonal
    //                          ** description : matrixPrimaryDiagonal
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: matrixSecondaryDiagonal
    //                          ** description : matrixSecondaryDiagonal
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayersPlus1
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: heatConductivity
    //                          ** description : heatConductivity
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: heatConductivityMean
    //                          ** description : heatConductivityMean
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: heatCapacity
    //                          ** description : heatCapacity
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: solution
    //                          ** description : solution
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: matrixDiagonal
    //                          ** description : matrixDiagonal
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: matrixLowerTriangle
    //                          ** description : matrixLowerTriangle
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
    //            * name: heatFlow
    //                          ** description : heatFlow
    //                          ** inputtype : variable
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : noOfTempLayers
    //                          ** max : 
    //                          ** min : 
    //                          ** default : 
    //                          ** unit : °C
        //- outputs:
    //            * name: soilTemperature
    //                          ** description : soilTemperature next day
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLEARRAY
    //                          ** len : 22
    //                          ** max : 
    //                          ** min : 
    //                          ** unit : °C
        double soilSurfaceTemperature = s.getsoilSurfaceTemperature();
        Double [] soilTemperature = s.getsoilTemperature();
        Double [] V = s.getV();
        Double [] B = s.getB();
        Double [] volumeMatrix = s.getvolumeMatrix();
        Double [] volumeMatrixOld = s.getvolumeMatrixOld();
        Double [] matrixPrimaryDiagonal = s.getmatrixPrimaryDiagonal();
        Double [] matrixSecondaryDiagonal = s.getmatrixSecondaryDiagonal();
        Double [] heatConductivity = s.getheatConductivity();
        Double [] heatConductivityMean = s.getheatConductivityMean();
        Double [] heatCapacity = s.getheatCapacity();
        Double [] solution = s.getsolution();
        Double [] matrixDiagonal = s.getmatrixDiagonal();
        Double [] matrixLowerTriangle = s.getmatrixLowerTriangle();
        Double [] heatFlow = s.getheatFlow();
        Integer groundLayer;
        Integer bottomLayer;
        Integer i;
        Integer j;
        Integer j_1;
        groundLayer = noOfTempLayers - 2;
        bottomLayer = noOfTempLayers - 1;
        heatFlow[0] = soilSurfaceTemperature * B[0] * heatConductivityMean[0];
        for (i=0 ; i!=noOfTempLayers ; i+=1)
        {
            solution[i] = (volumeMatrixOld[i] + ((volumeMatrix[i] - volumeMatrixOld[i]) / layerThickness[i])) * soilTemperature[i] + heatFlow[i];
        }
        matrixDiagonal[0] = matrixPrimaryDiagonal[0];
        for (i=1 ; i!=noOfTempLayers ; i+=1)
        {
            matrixLowerTriangle[i] = matrixSecondaryDiagonal[i] / matrixDiagonal[(i - 1)];
            matrixDiagonal[i] = matrixPrimaryDiagonal[i] - (matrixLowerTriangle[i] * matrixSecondaryDiagonal[i]);
        }
        for (i=1 ; i!=noOfTempLayers ; i+=1)
        {
            solution[i] = solution[i] - (matrixLowerTriangle[i] * solution[(i - 1)]);
        }
        solution[bottomLayer] = solution[bottomLayer] / matrixDiagonal[bottomLayer];
        for (i=0 ; i!=bottomLayer ; i+=1)
        {
            j = bottomLayer - 1 - i;
            j_1 = j + 1;
            solution[j] = solution[j] / matrixDiagonal[j] - (matrixLowerTriangle[j_1] * solution[j_1]);
        }
        for (i=0 ; i!=noOfTempLayers ; i+=1)
        {
            soilTemperature[i] = solution[i];
        }
        for (i=0 ; i!=noOfSoilLayers ; i+=1)
        {
            volumeMatrixOld[i] = volumeMatrix[i];
        }
        volumeMatrixOld[groundLayer] = volumeMatrix[groundLayer];
        volumeMatrixOld[bottomLayer] = volumeMatrix[bottomLayer];
        s.setsoilTemperature(soilTemperature);
    }
}