#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include<vector>
#include<string>
namespace Monica_SoilTemp {
struct SoilTemperatureCompState
{
    std::vector<double> V;
    std::vector<double> B;
    std::vector<double> volumeMatrix;
    std::vector<double> volumeMatrixOld;
    std::vector<double> matrixPrimaryDiagonal;
    std::vector<double> matrixSecondaryDiagonal;
    std::vector<double> heatConductivity;
    std::vector<double> heatConductivityMean;
    std::vector<double> heatCapacity;
    std::vector<double> solution;
    std::vector<double> matrixDiagonal;
    std::vector<double> matrixLowerTriangle;
    std::vector<double> heatFlow;
    double soilSurfaceTemperature{0.0};
    std::vector<double> soilTemperature;
    double noSnowSoilSurfaceTemperature{0.0};
};
}