#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <array>
#include <map>
#include <tuple>
#include "SoilTemperature.h"
using namespace Monica_SoilTemp;
void SoilTemperature::Init(SoilTemperatureCompState &s, SoilTemperatureCompState &s1, SoilTemperatureCompRate &r, SoilTemperatureCompAuxiliary &a, SoilTemperatureCompExogenous &ex)
{
    s.soilSurfaceTemperature = 0.0;
    s.soilTemperature = std::vector<double>(noOfTempLayers);
    s.V = std::vector<double>(noOfTempLayers);
    s.B = std::vector<double>(noOfTempLayers);
    s.volumeMatrix = std::vector<double>(noOfTempLayers);
    s.volumeMatrixOld = std::vector<double>(noOfTempLayers);
    s.matrixPrimaryDiagonal = std::vector<double>(noOfTempLayers);
    s.matrixSecondaryDiagonal = std::vector<double>(noOfTempLayersPlus1);
    s.heatConductivity = std::vector<double>(noOfTempLayers);
    s.heatConductivityMean = std::vector<double>(noOfTempLayers);
    s.heatCapacity = std::vector<double>(noOfTempLayers);
    s.solution = std::vector<double>(noOfTempLayers);
    s.matrixDiagonal = std::vector<double>(noOfTempLayers);
    s.matrixLowerTriangle = std::vector<double>(noOfTempLayers);
    s.heatFlow = std::vector<double>(noOfTempLayers);
    s.soilTemperature = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.V = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.B = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.volumeMatrix = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.volumeMatrixOld = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.matrixPrimaryDiagonal = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.matrixSecondaryDiagonal = std::move(std::vector<double>(noOfTempLayersPlus1, 0.0));
    s.heatConductivity = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.heatConductivityMean = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.heatCapacity = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.solution = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.matrixDiagonal = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.matrixLowerTriangle = std::move(std::vector<double>(noOfTempLayers, 0.0));
    s.heatFlow = std::move(std::vector<double>(noOfTempLayers, 0.0));
    int groundLayer;
    int bottomLayer;
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
    int i;
    for (i=0 ; i!=noOfSoilLayers ; i+=1)
    {
        s.soilTemperature[i] = (1.0 - (float(i) / noOfSoilLayers)) * initialSurfaceTemp + (float(i) / noOfSoilLayers * baseTemp);
    }
    groundLayer = noOfTempLayers - 2;
    bottomLayer = noOfTempLayers - 1;
    layerThickness[groundLayer] = 2.0 * layerThickness[(groundLayer - 1)];
    layerThickness[bottomLayer] = 1.0;
    s.soilTemperature[groundLayer] = (s.soilTemperature[groundLayer - 1] + baseTemp) * 0.5;
    s.soilTemperature[bottomLayer] = baseTemp;
    s.V[0] = layerThickness[0];
    s.B[0] = 2.0 / layerThickness[0];
    for (i=1 ; i!=noOfTempLayers ; i+=1)
    {
        lti_1 = layerThickness[i - 1];
        lti = layerThickness[i];
        s.B[i] = 2.0 / (lti + lti_1);
        s.V[i] = lti * nTau;
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
        s.heatConductivity[i] = (3.0 * (sbdi / 1000.0) - 1.7) * 0.001 / (1.0 + ((11.5 - (5.0 * (sbdi / 1000.0))) * std::exp(-50.0 * std::pow(smi / (sbdi / 1000.0), 1.5)))) * 86400.0 * ts * 100.0 * 4.184;
        sati = saturation[i];
        somi = soilOrganicMatter[i] / da * sbdi;
        s.heatCapacity[i] = smi * dw * cw + ((sati - smi) * da * ca) + (somi * dh * ch) + ((1.0 - sati - somi) * dq * cq);
    }
    s.heatCapacity[groundLayer] = s.heatCapacity[groundLayer - 1];
    s.heatCapacity[bottomLayer] = s.heatCapacity[groundLayer];
    s.heatConductivity[groundLayer] = s.heatConductivity[groundLayer - 1];
    s.heatConductivity[bottomLayer] = s.heatConductivity[groundLayer];
    s.soilSurfaceTemperature = initialSurfaceTemp;
    s.heatConductivityMean[0] = s.heatConductivity[0];
    for (i=1 ; i!=noOfTempLayers ; i+=1)
    {
        lti_1 = layerThickness[i - 1];
        lti = layerThickness[i];
        hci_1 = s.heatConductivity[i - 1];
        hci = s.heatConductivity[i];
        s.heatConductivityMean[i] = (lti_1 * hci_1 + (lti * hci)) / (lti + lti_1);
    }
    for (i=0 ; i!=noOfTempLayers ; i+=1)
    {
        s.volumeMatrix[i] = s.V[i] * s.heatCapacity[i];
        s.volumeMatrixOld[i] = s.volumeMatrix[i];
        s.matrixSecondaryDiagonal[i] = -s.B[i] * s.heatConductivityMean[i];
    }
    s.matrixSecondaryDiagonal[bottomLayer + 1] = 0.0;
    for (i=0 ; i!=noOfTempLayers ; i+=1)
    {
        s.matrixPrimaryDiagonal[i] = s.volumeMatrix[i] - s.matrixSecondaryDiagonal[i] - s.matrixSecondaryDiagonal[i + 1];
    }
}
SoilTemperature::SoilTemperature() {}
int SoilTemperature::getnoOfSoilLayers() { return this->noOfSoilLayers; }
int SoilTemperature::getnoOfTempLayers() { return this->noOfTempLayers; }
int SoilTemperature::getnoOfTempLayersPlus1() { return this->noOfTempLayersPlus1; }
double SoilTemperature::gettimeStep() { return this->timeStep; }
std::vector<double> & SoilTemperature::getsoilMoistureConst() { return this->soilMoistureConst; }
double SoilTemperature::getbaseTemp() { return this->baseTemp; }
double SoilTemperature::getinitialSurfaceTemp() { return this->initialSurfaceTemp; }
double SoilTemperature::getdensityAir() { return this->densityAir; }
double SoilTemperature::getspecificHeatCapacityAir() { return this->specificHeatCapacityAir; }
double SoilTemperature::getdensityHumus() { return this->densityHumus; }
double SoilTemperature::getspecificHeatCapacityHumus() { return this->specificHeatCapacityHumus; }
double SoilTemperature::getdensityWater() { return this->densityWater; }
double SoilTemperature::getspecificHeatCapacityWater() { return this->specificHeatCapacityWater; }
double SoilTemperature::getquartzRawDensity() { return this->quartzRawDensity; }
double SoilTemperature::getspecificHeatCapacityQuartz() { return this->specificHeatCapacityQuartz; }
double SoilTemperature::getnTau() { return this->nTau; }
std::vector<double> & SoilTemperature::getlayerThickness() { return this->layerThickness; }
std::vector<double> & SoilTemperature::getsoilBulkDensity() { return this->soilBulkDensity; }
std::vector<double> & SoilTemperature::getsaturation() { return this->saturation; }
std::vector<double> & SoilTemperature::getsoilOrganicMatter() { return this->soilOrganicMatter; }
void SoilTemperature::setnoOfSoilLayers(int _noOfSoilLayers) { this->noOfSoilLayers = _noOfSoilLayers; }
void SoilTemperature::setnoOfTempLayers(int _noOfTempLayers) { this->noOfTempLayers = _noOfTempLayers; }
void SoilTemperature::setnoOfTempLayersPlus1(int _noOfTempLayersPlus1) { this->noOfTempLayersPlus1 = _noOfTempLayersPlus1; }
void SoilTemperature::settimeStep(double _timeStep) { this->timeStep = _timeStep; }
void SoilTemperature::setsoilMoistureConst(std::vector<double> const &_soilMoistureConst){
    this->soilMoistureConst = _soilMoistureConst;
}
void SoilTemperature::setbaseTemp(double _baseTemp) { this->baseTemp = _baseTemp; }
void SoilTemperature::setinitialSurfaceTemp(double _initialSurfaceTemp) { this->initialSurfaceTemp = _initialSurfaceTemp; }
void SoilTemperature::setdensityAir(double _densityAir) { this->densityAir = _densityAir; }
void SoilTemperature::setspecificHeatCapacityAir(double _specificHeatCapacityAir) { this->specificHeatCapacityAir = _specificHeatCapacityAir; }
void SoilTemperature::setdensityHumus(double _densityHumus) { this->densityHumus = _densityHumus; }
void SoilTemperature::setspecificHeatCapacityHumus(double _specificHeatCapacityHumus) { this->specificHeatCapacityHumus = _specificHeatCapacityHumus; }
void SoilTemperature::setdensityWater(double _densityWater) { this->densityWater = _densityWater; }
void SoilTemperature::setspecificHeatCapacityWater(double _specificHeatCapacityWater) { this->specificHeatCapacityWater = _specificHeatCapacityWater; }
void SoilTemperature::setquartzRawDensity(double _quartzRawDensity) { this->quartzRawDensity = _quartzRawDensity; }
void SoilTemperature::setspecificHeatCapacityQuartz(double _specificHeatCapacityQuartz) { this->specificHeatCapacityQuartz = _specificHeatCapacityQuartz; }
void SoilTemperature::setnTau(double _nTau) { this->nTau = _nTau; }
void SoilTemperature::setlayerThickness(std::vector<double> const &_layerThickness){
    this->layerThickness = _layerThickness;
}
void SoilTemperature::setsoilBulkDensity(std::vector<double> const &_soilBulkDensity){
    this->soilBulkDensity = _soilBulkDensity;
}
void SoilTemperature::setsaturation(std::vector<double> const &_saturation){
    this->saturation = _saturation;
}
void SoilTemperature::setsoilOrganicMatter(std::vector<double> const &_soilOrganicMatter){
    this->soilOrganicMatter = _soilOrganicMatter;
}
void SoilTemperature::Calculate_Model(SoilTemperatureCompState &s, SoilTemperatureCompState &s1, SoilTemperatureCompRate &r, SoilTemperatureCompAuxiliary &a, SoilTemperatureCompExogenous &ex)
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
    int groundLayer;
    int bottomLayer;
    int i;
    int j;
    int j_1;
    groundLayer = noOfTempLayers - 2;
    bottomLayer = noOfTempLayers - 1;
    s.heatFlow[0] = s.soilSurfaceTemperature * s.B[0] * s.heatConductivityMean[0];
    for (i=0 ; i!=noOfTempLayers ; i+=1)
    {
        s.solution[i] = (s.volumeMatrixOld[i] + ((s.volumeMatrix[i] - s.volumeMatrixOld[i]) / layerThickness[i])) * s.soilTemperature[i] + s.heatFlow[i];
    }
    s.matrixDiagonal[0] = s.matrixPrimaryDiagonal[0];
    for (i=1 ; i!=noOfTempLayers ; i+=1)
    {
        s.matrixLowerTriangle[i] = s.matrixSecondaryDiagonal[i] / s.matrixDiagonal[(i - 1)];
        s.matrixDiagonal[i] = s.matrixPrimaryDiagonal[i] - (s.matrixLowerTriangle[i] * s.matrixSecondaryDiagonal[i]);
    }
    for (i=1 ; i!=noOfTempLayers ; i+=1)
    {
        s.solution[i] = s.solution[i] - (s.matrixLowerTriangle[i] * s.solution[(i - 1)]);
    }
    s.solution[bottomLayer] = s.solution[bottomLayer] / s.matrixDiagonal[bottomLayer];
    for (i=0 ; i!=bottomLayer ; i+=1)
    {
        j = bottomLayer - 1 - i;
        j_1 = j + 1;
        s.solution[j] = s.solution[j] / s.matrixDiagonal[j] - (s.matrixLowerTriangle[j_1] * s.solution[j_1]);
    }
    for (i=0 ; i!=noOfTempLayers ; i+=1)
    {
        s.soilTemperature[i] = s.solution[i];
    }
    for (i=0 ; i!=noOfSoilLayers ; i+=1)
    {
        s.volumeMatrixOld[i] = s.volumeMatrix[i];
    }
    s.volumeMatrixOld[groundLayer] = s.volumeMatrix[groundLayer];
    s.volumeMatrixOld[bottomLayer] = s.volumeMatrix[bottomLayer];
}