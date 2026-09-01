#include "SoilTemperatureCompComponent.h"
using namespace Monica_SoilTemp;
SoilTemperatureCompComponent::SoilTemperatureCompComponent()
{
       
}


double SoilTemperatureCompComponent::getdampingFactor(){ return this->dampingFactor; }
double SoilTemperatureCompComponent::gettimeStep(){ return this->timeStep; }
std::vector<double> & SoilTemperatureCompComponent::getsoilMoistureConst(){ return this->soilMoistureConst; }
double SoilTemperatureCompComponent::getbaseTemp(){ return this->baseTemp; }
double SoilTemperatureCompComponent::getinitialSurfaceTemp(){ return this->initialSurfaceTemp; }
double SoilTemperatureCompComponent::getdensityAir(){ return this->densityAir; }
double SoilTemperatureCompComponent::getspecificHeatCapacityAir(){ return this->specificHeatCapacityAir; }
double SoilTemperatureCompComponent::getdensityHumus(){ return this->densityHumus; }
double SoilTemperatureCompComponent::getspecificHeatCapacityHumus(){ return this->specificHeatCapacityHumus; }
double SoilTemperatureCompComponent::getdensityWater(){ return this->densityWater; }
double SoilTemperatureCompComponent::getspecificHeatCapacityWater(){ return this->specificHeatCapacityWater; }
double SoilTemperatureCompComponent::getquartzRawDensity(){ return this->quartzRawDensity; }
double SoilTemperatureCompComponent::getspecificHeatCapacityQuartz(){ return this->specificHeatCapacityQuartz; }
double SoilTemperatureCompComponent::getnTau(){ return this->nTau; }
int SoilTemperatureCompComponent::getnoOfTempLayers(){ return this->noOfTempLayers; }
int SoilTemperatureCompComponent::getnoOfTempLayersPlus1(){ return this->noOfTempLayersPlus1; }
int SoilTemperatureCompComponent::getnoOfSoilLayers(){ return this->noOfSoilLayers; }
std::vector<double> & SoilTemperatureCompComponent::getlayerThickness(){ return this->layerThickness; }
std::vector<double> & SoilTemperatureCompComponent::getsoilBulkDensity(){ return this->soilBulkDensity; }
std::vector<double> & SoilTemperatureCompComponent::getsaturation(){ return this->saturation; }
std::vector<double> & SoilTemperatureCompComponent::getsoilOrganicMatter(){ return this->soilOrganicMatter; }

void SoilTemperatureCompComponent::setdampingFactor(double _dampingFactor)
{
    _NoSnowSoilSurfaceTemperature.setdampingFactor(_dampingFactor);
}
void SoilTemperatureCompComponent::settimeStep(double _timeStep)
{
    _SoilTemperature.settimeStep(_timeStep);
}
void SoilTemperatureCompComponent::setsoilMoistureConst(const std::vector<double> & _soilMoistureConst)
{
    _SoilTemperature.setsoilMoistureConst(_soilMoistureConst);
}
void SoilTemperatureCompComponent::setbaseTemp(double _baseTemp)
{
    _SoilTemperature.setbaseTemp(_baseTemp);
}
void SoilTemperatureCompComponent::setinitialSurfaceTemp(double _initialSurfaceTemp)
{
    _SoilTemperature.setinitialSurfaceTemp(_initialSurfaceTemp);
}
void SoilTemperatureCompComponent::setdensityAir(double _densityAir)
{
    _SoilTemperature.setdensityAir(_densityAir);
}
void SoilTemperatureCompComponent::setspecificHeatCapacityAir(double _specificHeatCapacityAir)
{
    _SoilTemperature.setspecificHeatCapacityAir(_specificHeatCapacityAir);
}
void SoilTemperatureCompComponent::setdensityHumus(double _densityHumus)
{
    _SoilTemperature.setdensityHumus(_densityHumus);
}
void SoilTemperatureCompComponent::setspecificHeatCapacityHumus(double _specificHeatCapacityHumus)
{
    _SoilTemperature.setspecificHeatCapacityHumus(_specificHeatCapacityHumus);
}
void SoilTemperatureCompComponent::setdensityWater(double _densityWater)
{
    _SoilTemperature.setdensityWater(_densityWater);
}
void SoilTemperatureCompComponent::setspecificHeatCapacityWater(double _specificHeatCapacityWater)
{
    _SoilTemperature.setspecificHeatCapacityWater(_specificHeatCapacityWater);
}
void SoilTemperatureCompComponent::setquartzRawDensity(double _quartzRawDensity)
{
    _SoilTemperature.setquartzRawDensity(_quartzRawDensity);
}
void SoilTemperatureCompComponent::setspecificHeatCapacityQuartz(double _specificHeatCapacityQuartz)
{
    _SoilTemperature.setspecificHeatCapacityQuartz(_specificHeatCapacityQuartz);
}
void SoilTemperatureCompComponent::setnTau(double _nTau)
{
    _SoilTemperature.setnTau(_nTau);
}
void SoilTemperatureCompComponent::setnoOfTempLayers(int _noOfTempLayers)
{
    _SoilTemperature.setnoOfTempLayers(_noOfTempLayers);
}
void SoilTemperatureCompComponent::setnoOfTempLayersPlus1(int _noOfTempLayersPlus1)
{
    _SoilTemperature.setnoOfTempLayersPlus1(_noOfTempLayersPlus1);
}
void SoilTemperatureCompComponent::setnoOfSoilLayers(int _noOfSoilLayers)
{
    _SoilTemperature.setnoOfSoilLayers(_noOfSoilLayers);
}
void SoilTemperatureCompComponent::setlayerThickness(const std::vector<double> & _layerThickness)
{
    _SoilTemperature.setlayerThickness(_layerThickness);
}
void SoilTemperatureCompComponent::setsoilBulkDensity(const std::vector<double> & _soilBulkDensity)
{
    _SoilTemperature.setsoilBulkDensity(_soilBulkDensity);
}
void SoilTemperatureCompComponent::setsaturation(const std::vector<double> & _saturation)
{
    _SoilTemperature.setsaturation(_saturation);
}
void SoilTemperatureCompComponent::setsoilOrganicMatter(const std::vector<double> & _soilOrganicMatter)
{
    _SoilTemperature.setsoilOrganicMatter(_soilOrganicMatter);
}
void SoilTemperatureCompComponent::Calculate_Model(SoilTemperatureCompState &s, SoilTemperatureCompState &s1, SoilTemperatureCompRate &r, SoilTemperatureCompAuxiliary &a, SoilTemperatureCompExogenous &ex)
{
    _NoSnowSoilSurfaceTemperature.Calculate_Model(s, s1, r, a, ex);
    s.noSnowSoilSurfaceTemperature = s.soilSurfaceTemperature;
    _WithSnowSoilSurfaceTemperature.Calculate_Model(s, s1, r, a, ex);
    _SoilTemperature.Calculate_Model(s, s1, r, a, ex);
}
SoilTemperatureCompComponent::SoilTemperatureCompComponent(SoilTemperatureCompComponent& toCopy)
{
    dampingFactor = toCopy.getdampingFactor();
    timeStep = toCopy.gettimeStep();
    for (int i = 0; i < noOfSoilLayers; i++)
{
    soilMoistureConst[i] = toCopy.getsoilMoistureConst()[i];
}

    baseTemp = toCopy.getbaseTemp();
    initialSurfaceTemp = toCopy.getinitialSurfaceTemp();
    densityAir = toCopy.getdensityAir();
    specificHeatCapacityAir = toCopy.getspecificHeatCapacityAir();
    densityHumus = toCopy.getdensityHumus();
    specificHeatCapacityHumus = toCopy.getspecificHeatCapacityHumus();
    densityWater = toCopy.getdensityWater();
    specificHeatCapacityWater = toCopy.getspecificHeatCapacityWater();
    quartzRawDensity = toCopy.getquartzRawDensity();
    specificHeatCapacityQuartz = toCopy.getspecificHeatCapacityQuartz();
    nTau = toCopy.getnTau();
    noOfTempLayers = toCopy.getnoOfTempLayers();
    noOfTempLayersPlus1 = toCopy.getnoOfTempLayersPlus1();
    noOfSoilLayers = toCopy.getnoOfSoilLayers();
    for (int i = 0; i < noOfTempLayers; i++)
{
    layerThickness[i] = toCopy.getlayerThickness()[i];
}

    for (int i = 0; i < noOfSoilLayers; i++)
{
    soilBulkDensity[i] = toCopy.getsoilBulkDensity()[i];
}

    for (int i = 0; i < noOfSoilLayers; i++)
{
    saturation[i] = toCopy.getsaturation()[i];
}

    for (int i = 0; i < noOfSoilLayers; i++)
{
    soilOrganicMatter[i] = toCopy.getsoilOrganicMatter()[i];
}

}