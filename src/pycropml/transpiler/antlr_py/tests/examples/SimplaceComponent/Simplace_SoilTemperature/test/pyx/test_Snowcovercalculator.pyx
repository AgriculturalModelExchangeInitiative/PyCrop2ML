#'Test generation'

from snowcovercalculator import *
from math import *
import numpy 



def test_test1():
    params= snowcovercalculator(
    cCarbonContent = 10.0,
    iTempMax = 3.0,
    iTempMin = -9.0,
    iRadiation = 1.4,
    iRAIN = 6.0,
    iCropResidues = 30.0,
    iPotentialSoilEvaporation = 0.6,
    iLeafAreaIndex = 0.1,
    iSoilTempArray = [2.6, 5.4, 8.6, 12.2, 11.4, 10.6, 9.8, 9.0],
    SnowWaterContent = 5.0,
    AgeOfSnow = 5,
    SoilSurfaceTemperature = 1.8397688,
     )
    SnowWaterContent_estimated = round(params[0], 5)
    SnowWaterContent_computed = 10.7
    assert (SnowWaterContent_estimated == SnowWaterContent_computed)
    SoilSurfaceTemperature_estimated = round(params[1], 5)
    SoilSurfaceTemperature_computed = 2.6
    assert (SoilSurfaceTemperature_estimated == SoilSurfaceTemperature_computed)
    AgeOfSnow_estimated = params[2]
    AgeOfSnow_computed = 6
    assert (AgeOfSnow_estimated == AgeOfSnow_computed)
    SnowIsolationIndex_estimated = round(params[3], 5)
    SnowIsolationIndex_computed = 1.0
    assert (SnowIsolationIndex_estimated == SnowIsolationIndex_computed)