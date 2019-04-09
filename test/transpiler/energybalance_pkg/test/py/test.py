from math import *

from CanopyTemperature import *

def test_test1():
    params= canopytemperature(
    rhoDensityAir = 1.225,
    minTair = 0.7,
    maxTair = 7.2,
     )
    minCanopyTemperature_estimated = round(params[0], 3)
    minCanopyTemperature_computed = 2.184
    assert (minCanopyTemperature_estimated == minCanopyTemperature_computed)
    maxCanopyTemperature_estimated = round(params[1], 3)
    maxCanopyTemperature_computed = 8.684
    assert (maxCanopyTemperature_estimated == maxCanopyTemperature_computed)

from Conductance import *

def test_test1():
    params= conductance(
    d = 0.67,
    zh = 0.013,
    zm = 0.13,
    wind = 124000,
    plantHeight = 0,
     )
    conductance_estimated = round(params, 3)
    conductance_computed = 598.685
    assert (conductance_estimated == conductance_computed)

from CropHeatFlux import *

def test_test1():
    params= cropheatflux(
    netRadiationEquivalentEvaporation = 638.142,
    soilHeatFlux = 188.817,
    potentialTranspiration =  1.413,
     )
    cropHeatFlux_estimated = round(params, 3)
    cropHeatFlux_computed =  447.912
    assert (cropHeatFlux_estimated == cropHeatFlux_computed)

from DiffusionLimitedEvaporation import *

def test_test1():
    params= diffusionlimitedevaporation(
    soilDiffusionConstant = 4.2,
    deficitOnTopLayers = 5341,
     )
    diffusionLimitedEvaporation_estimated = round(params, 3)
    diffusionLimitedEvaporation_computed =  6605.505
    assert (diffusionLimitedEvaporation_estimated == diffusionLimitedEvaporation_computed)

from EvapoTranspiration import *

def test_test1():
    params= evapotranspiration(
    isWindVpDefined = 1,
    evapoTranspirationPriestlyTaylor = 449.367,
    evapoTranspirationPenman = 830.957,
     )
    evapoTranspiration_estimated = round(params, 3)
    evapoTranspiration_computed = 830.957
    assert (evapoTranspiration_estimated == evapoTranspiration_computed)

from NetRadiation import *

def test_test1():
    params= netradiation(
    elevation = 0,
    solarRadiation = 3,
    vaporPressure = 6.1,
     )
    netRadiation_estimated = round(params[0], 3)
    netRadiation_computed = 1.566
    assert (netRadiation_estimated == netRadiation_computed)
    netOutGoingLongWaveRadiation_estimated = round(params[1], 3)
    netOutGoingLongWaveRadiation_computed = 0.744
    assert (netOutGoingLongWaveRadiation_estimated == netOutGoingLongWaveRadiation_computed)

from NetRadiationEquivalentEvaporation import *

def test_test1():
    params= netradiationequivalentevaporation(
    netRadiation = 1.566,
     )
    netRadiationEquivalentEvaporation_estimated = round(params, 3)
    netRadiationEquivalentEvaporation_computed = 638.142
    assert (netRadiationEquivalentEvaporation_estimated == netRadiationEquivalentEvaporation_computed)

from Penman import *

def test_test1():
    params= penman(
    Alpha = 1.5,
    lambdaV = 2.454,
    evapoTranspirationPriestlyTaylor = 449.367,
    hslope = 0.584,
    VPDair = 2.19,
     )
    evapoTranspirationPenman_estimated = round(params, 3)
    evapoTranspirationPenman_computed = 830.958
    assert (evapoTranspirationPenman_estimated == evapoTranspirationPenman_computed)

from PotentialTranspiration import *

def test_test1():
    params= potentialtranspiration(
    tau = 0.9983,
    evapoTranspiration = 830.958,
     )
    potentialTranspiration_estimated = round(params, 3)
    potentialTranspiration_computed = 1.413
    assert (potentialTranspiration_estimated == potentialTranspiration_computed)

from PriestlyTaylor import *

def test_test1():
    params= priestlytaylor(
    Alpha = 1.5,
    netRadiationEquivalentEvaporation = 638.142,
     )
    evapoTranspirationPriestlyTaylor_estimated = round(params, 3)
    evapoTranspirationPriestlyTaylor_computed = 449.367
    assert (evapoTranspirationPriestlyTaylor_estimated == evapoTranspirationPriestlyTaylor_computed)

from PtSoil import *

def test_test1():
    params= ptsoil(
    tau = 0.9983,
    evapoTranspirationPriestlyTaylor = 449.367,
     )
    energyLimitedEvaporation_estimated = round(params, 3)
    energyLimitedEvaporation_computed = 448.240
    assert (energyLimitedEvaporation_estimated == energyLimitedEvaporation_computed)

from SoilEvaporation import *

def test_test1():
    params= soilevaporation(
    diffusionLimitedEvaporation = 6605.505,
    energyLimitedEvaporation = 448.240,
     )
    soilEvaporation_estimated = round(params, 3)
    soilEvaporation_computed = 448.240
    assert (soilEvaporation_estimated == soilEvaporation_computed)

from SoilHeatFlux import *

def test_test1():
    params= soilheatflux(
    tau = 0.9983,
    netRadiationEquivalentEvaporation = 638.142,
    soilEvaporation = 448.240,
     )
    soilHeatFlux_estimated = round(params, 3)
    soilHeatFlux_computed = 188.817
    assert (soilHeatFlux_estimated == soilHeatFlux_computed)
