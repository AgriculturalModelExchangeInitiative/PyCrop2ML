
#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include "SoilTemperatureCompState.h"
#include "SoilTemperatureCompRate.h"
#include "SoilTemperatureCompAuxiliary.h"
#include "SoilTemperatureCompExogenous.h"
namespace Monica_SoilTemp {
class WithSnowSoilSurfaceTemperature
{
private:
public:
    WithSnowSoilSurfaceTemperature();

    void Calculate_Model(SoilTemperatureCompState &s, SoilTemperatureCompState &s1, SoilTemperatureCompRate &r, SoilTemperatureCompAuxiliary &a, SoilTemperatureCompExogenous &ex);

};
}