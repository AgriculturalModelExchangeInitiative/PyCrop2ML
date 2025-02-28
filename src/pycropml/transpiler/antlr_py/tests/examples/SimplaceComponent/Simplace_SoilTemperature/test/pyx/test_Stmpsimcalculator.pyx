#'Test generation'

from stmpsimcalculator import *
from math import *
import numpy 



def test_test1():
    params= stmpsimcalculator(
    cSoilLayerDepth = [0.1, 0.5, 1.5],
    cFirstDayMeanTemp = 15.0,
    cAVT = 9.0,
    cABD = 1.4,
    cDampingDepth = 6.0,
    iSoilWaterContent = 0.3,
    iSoilSurfaceTemperature = 6.0,
     )
    SoilTempArray_estimated = np.around(params, 5)
    SoilTempArray_computed = [13.624360856350041, 13.399968504634286, 12.599999999999845, 12.2, 11.4, 10.6, 9.799999999999999, 9.0]
    assert np.all(SoilTempArray_estimated == SoilTempArray_computed)