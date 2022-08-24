from datetime import datetime
from math import *
from sq_energybalance_generated.Netradiation import model_netradiation
from sq_energybalance_generated.Conductance import model_conductance
from sq_energybalance_generated.Diffusionlimitedevaporation import model_diffusionlimitedevaporation
from sq_energybalance_generated.Netradiationequivalentevaporation import model_netradiationequivalentevaporation
from sq_energybalance_generated.Priestlytaylor import model_priestlytaylor
from sq_energybalance_generated.Ptsoil import model_ptsoil
from sq_energybalance_generated.Penman import model_penman
from sq_energybalance_generated.Soilevaporation import model_soilevaporation
from sq_energybalance_generated.Evapotranspiration import model_evapotranspiration
from sq_energybalance_generated.Soilheatflux import model_soilheatflux
from sq_energybalance_generated.Potentialtranspiration import model_potentialtranspiration
from sq_energybalance_generated.Cropheatflux import model_cropheatflux
from sq_energybalance_generated.Canopytemperature import model_canopytemperature
def model_energybalance(float albedoCoefficient,
      float vaporPressure,
      float stefanBoltzman,
      float extraSolarRadiation,
      float solarRadiation,
      float minTair,
      float elevation,
      float maxTair,
      float plantHeight,
      float vonKarman,
      float d,
      float zm,
      float wind,
      float heightWeatherMeasurements,
      float zh,
      float deficitOnTopLayers,
      float soilDiffusionConstant,
      float lambdaV,
      float hslope,
      float psychrometricConstant,
      float Alpha,
      float tau,
      float tauAlpha,
      float VPDair,
      float rhoDensityAir,
      float specificHeatCapacityAir,
      int isWindVpDefined):
    cdef float netRadiation
    cdef float netOutGoingLongWaveRadiation
    cdef float conductance
    cdef float diffusionLimitedEvaporation
    cdef float netRadiationEquivalentEvaporation
    cdef float evapoTranspirationPriestlyTaylor
    cdef float energyLimitedEvaporation
    cdef float evapoTranspirationPenman
    cdef float soilEvaporation
    cdef float evapoTranspiration
    cdef float soilHeatFlux
    cdef float potentialTranspiration
    cdef float cropHeatFlux
    cdef float minCanopyTemperature
    cdef float maxCanopyTemperature
    netRadiation, netOutGoingLongWaveRadiation = model_netradiation( minTair,maxTair,solarRadiation,vaporPressure,extraSolarRadiation,albedoCoefficient,stefanBoltzman,elevation)
    conductance = model_conductance( plantHeight,wind,vonKarman,heightWeatherMeasurements,zm,zh,d)
    diffusionLimitedEvaporation = model_diffusionlimitedevaporation( deficitOnTopLayers,soilDiffusionConstant)
    netRadiationEquivalentEvaporation = model_netradiationequivalentevaporation( netRadiation,lambdaV)
    evapoTranspirationPriestlyTaylor = model_priestlytaylor( netRadiationEquivalentEvaporation,hslope,psychrometricConstant,Alpha)
    energyLimitedEvaporation = model_ptsoil( evapoTranspirationPriestlyTaylor,Alpha,tau,tauAlpha)
    evapoTranspirationPenman = model_penman( evapoTranspirationPriestlyTaylor,hslope,VPDair,conductance,psychrometricConstant,Alpha,lambdaV,rhoDensityAir,specificHeatCapacityAir)
    soilEvaporation = model_soilevaporation( diffusionLimitedEvaporation,energyLimitedEvaporation)
    evapoTranspiration = model_evapotranspiration( evapoTranspirationPriestlyTaylor,evapoTranspirationPenman,isWindVpDefined)
    soilHeatFlux = model_soilheatflux( netRadiationEquivalentEvaporation,soilEvaporation,tau)
    potentialTranspiration = model_potentialtranspiration( evapoTranspiration,tau)
    cropHeatFlux = model_cropheatflux( netRadiationEquivalentEvaporation,soilHeatFlux,potentialTranspiration)
    minCanopyTemperature, maxCanopyTemperature = model_canopytemperature( minTair,maxTair,cropHeatFlux,conductance,lambdaV,rhoDensityAir,specificHeatCapacityAir)
    return netRadiation, netOutGoingLongWaveRadiation, conductance, diffusionLimitedEvaporation, netRadiationEquivalentEvaporation, evapoTranspirationPriestlyTaylor, energyLimitedEvaporation, evapoTranspirationPenman, soilEvaporation, evapoTranspiration, soilHeatFlux, potentialTranspiration, cropHeatFlux, minCanopyTemperature, maxCanopyTemperature