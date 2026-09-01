#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>

namespace Monica_SoilTemp {
struct SoilTemperatureCompExogenous
{
    double tmin{0.0};
    double tmax{0.0};
    double globrad{0.0};
    double soilCoverage{0.0};
    double soilSurfaceTemperatureBelowSnow{0.0};
    bool hasSnowCover{false};
};
}