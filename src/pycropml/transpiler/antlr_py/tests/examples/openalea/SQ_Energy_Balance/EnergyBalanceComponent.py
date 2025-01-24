# coding: utf8
from copy import copy
from array import array
from math import *
from typing import *
from datetime import datetime

from SQ_Energy_Balance.Netradiation import model_netradiation
from SQ_Energy_Balance.Netradiationequivalentevaporation import model_netradiationequivalentevaporation
from SQ_Energy_Balance.Priestlytaylor import model_priestlytaylor
from SQ_Energy_Balance.Conductance import model_conductance
from SQ_Energy_Balance.Diffusionlimitedevaporation import model_diffusionlimitedevaporation
from SQ_Energy_Balance.Penman import model_penman
from SQ_Energy_Balance.Ptsoil import model_ptsoil
from SQ_Energy_Balance.Soilevaporation import model_soilevaporation
from SQ_Energy_Balance.Evapotranspiration import model_evapotranspiration
from SQ_Energy_Balance.Soilheatflux import model_soilheatflux
from SQ_Energy_Balance.Potentialtranspiration import model_potentialtranspiration
from SQ_Energy_Balance.Cropheatflux import model_cropheatflux
from SQ_Energy_Balance.Canopytemperature import model_canopytemperature

#%%CyML Model Begin%%
def model_energybalance(minTair:float,
         maxTair:float,
         albedoCoefficient:float,
         stefanBoltzman:float,
         elevation:float,
         solarRadiation:float,
         vaporPressure:float,
         extraSolarRadiation:float,
         lambdaV:float,
         hslope:float,
         psychrometricConstant:float,
         Alpha:float,
         vonKarman:float,
         heightWeatherMeasurements:float,
         zm:float,
         d:float,
         zh:float,
         plantHeight:float,
         wind:float,
         deficitOnTopLayers:float,
         soilDiffusionConstant:float,
         VPDair:float,
         rhoDensityAir:float,
         specificHeatCapacityAir:float,
         tau:float,
         tauAlpha:float,
         isWindVpDefined:int):
    """
     - Name: EnergyBalance -Version: 001, -Time step: 1
     - Description:
                 * Title: EnergyBalance
                 * Authors: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: https://doi.org/10.1016/0168-1923(94)02214-5
                 * Institution: New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.,
                 New Zealand Institute for Crop and Food Research Ltd.
         
                 * ExtendedDescription: Modelling energy balance in the wheat crop model SiriusQuality2: Evapotranspiration and canopy and soil temperature calculations
                             see documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=547
         
                 * ShortDescription: This component calculates the canopy temperature and energy balance
     - inputs:
                 * name: minTair
                               ** description : minimum air temperature
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : -30
                               ** max : 45
                               ** default : 0.7
                               ** unit : °C
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: maxTair
                               ** description : maximum air Temperature
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : -30
                               ** max : 45
                               ** default : 7.2
                               ** unit : °C
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: albedoCoefficient
                               ** description : albedo Coefficient
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.23
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: stefanBoltzman
                               ** description : stefan Boltzman constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 4.903E-09
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: elevation
                               ** description : elevation
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0
                               ** min : -500
                               ** max : 10000
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: solarRadiation
                               ** description : solar Radiation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 3
                               ** min : 0
                               ** max : 1000
                               ** unit : MJ m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: vaporPressure
                               ** description : vapor Pressure
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 6.1
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: extraSolarRadiation
                               ** description : extra Solar Radiation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 11.7
                               ** min : 0
                               ** max : 1000
                               ** unit : MJ m2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ kg-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.584
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa °C-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.66
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.5
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: vonKarman
                               ** description : von Karman constant
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 1
                               ** default : 0.42
                               ** unit : dimensionless
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                               ** parametercategory : constant
                 * name: heightWeatherMeasurements
                               ** description : reference height of wind and humidity measurements
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10
                               ** default : 2
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: zm
                               ** description : roughness length governing momentum transfer, FAO
                               ** parametercategory : constant
                               ** inputtype : parameter
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 1
                               ** default : 0.13
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: d
                               ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.67
                               ** min : 0
                               ** max : 1
                               ** unit : dimensionless
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
                 * name: zh
                               ** description : roughness length governing transfer of heat and vapour, FAO
                               ** parametercategory : constant
                               ** inputtype : parameter
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 1
                               ** default : 0.013
                               ** unit : m
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: plantHeight
                               ** description : plant Height
                               ** datatype : DOUBLE
                               ** default : 0
                               ** min : 0
                               ** max : 1000
                               ** unit : mm
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                 * name: wind
                               ** description : wind
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 124000
                               ** min : 0
                               ** max : 1000000
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: deficitOnTopLayers
                               ** description : deficit On TopLayers
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 5341
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: soilDiffusionConstant
                               ** description : soil Diffusion Constant
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** default : 4.2
                               ** min : 0
                               ** max : 10
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: VPDair
                               ** description :  vapour pressure density
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 2.19
                               ** min : 0
                               ** max : 1000
                               ** unit : hPa
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.225
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.00101
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: tau
                               ** description : plant cover factor
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** default : 0.9983
                               ** min : 0
                               ** max : 100
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: tauAlpha
                               ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
                               ** parametercategory : soil
                               ** datatype : DOUBLE
                               ** default : 0.3
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: isWindVpDefined
                               ** description : if wind and vapour pressure are defined
                               ** parametercategory : constant
                               ** datatype : INT
                               ** default : 1
                               ** min : 0
                               ** max : 1
                               ** unit : 
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: netRadiation
                               ** description :  net radiation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : MJ m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: netOutGoingLongWaveRadiation
                               ** description : net OutGoing Long Wave Radiation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: netRadiationEquivalentEvaporation
                               ** variablecategory : auxiliary
                               ** description : net Radiation in Equivalent Evaporation 
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: diffusionLimitedEvaporation
                               ** description : the evaporation from the diffusion limited soil 
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 5000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: evapoTranspiration
                               ** description : evapoTranspiration
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : mm
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: potentialTranspiration
                               ** description : potential Transpiration 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: soilHeatFlux
                               ** description : soil Heat Flux 
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: cropHeatFlux
                               ** description :  crop Heat Flux
                               ** variablecategory : rate
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : g m-2 d-1
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: minCanopyTemperature
                               ** description : minimal Canopy Temperature  
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: maxCanopyTemperature
                               ** description : maximal Canopy Temperature 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    netRadiation:float
    netOutGoingLongWaveRadiation:float
    netRadiationEquivalentEvaporation:float
    evapoTranspirationPriestlyTaylor:float
    conductance:float
    diffusionLimitedEvaporation:float
    evapoTranspirationPenman:float
    energyLimitedEvaporation:float
    soilEvaporation:float
    evapoTranspiration:float
    soilHeatFlux:float
    potentialTranspiration:float
    cropHeatFlux:float
    minCanopyTemperature:float
    maxCanopyTemperature:float
    (netRadiation, netOutGoingLongWaveRadiation) = model_netradiation(minTair, maxTair, albedoCoefficient, stefanBoltzman, elevation, solarRadiation, vaporPressure, extraSolarRadiation)
    conductance = model_conductance(vonKarman, heightWeatherMeasurements, zm, zh, d, plantHeight, wind)
    diffusionLimitedEvaporation = model_diffusionlimitedevaporation(deficitOnTopLayers, soilDiffusionConstant)
    netRadiationEquivalentEvaporation = model_netradiationequivalentevaporation(lambdaV, netRadiation)
    evapoTranspirationPriestlyTaylor = model_priestlytaylor(netRadiationEquivalentEvaporation, hslope, psychrometricConstant, Alpha)
    energyLimitedEvaporation = model_ptsoil(evapoTranspirationPriestlyTaylor, Alpha, tau, tauAlpha)
    evapoTranspirationPenman = model_penman(evapoTranspirationPriestlyTaylor, hslope, VPDair, psychrometricConstant, Alpha, lambdaV, rhoDensityAir, specificHeatCapacityAir, conductance)
    soilEvaporation = model_soilevaporation(diffusionLimitedEvaporation, energyLimitedEvaporation)
    evapoTranspiration = model_evapotranspiration(isWindVpDefined, evapoTranspirationPriestlyTaylor, evapoTranspirationPenman)
    soilHeatFlux = model_soilheatflux(netRadiationEquivalentEvaporation, tau, soilEvaporation)
    potentialTranspiration = model_potentialtranspiration(evapoTranspiration, tau)
    cropHeatFlux = model_cropheatflux(netRadiationEquivalentEvaporation, soilHeatFlux, potentialTranspiration)
    (minCanopyTemperature, maxCanopyTemperature) = model_canopytemperature(minTair, maxTair, cropHeatFlux, conductance, lambdaV, rhoDensityAir, specificHeatCapacityAir)
    return (netRadiation, netOutGoingLongWaveRadiation, netRadiationEquivalentEvaporation, evapoTranspirationPriestlyTaylor, diffusionLimitedEvaporation, energyLimitedEvaporation, conductance, evapoTranspirationPenman, soilEvaporation, evapoTranspiration, potentialTranspiration, soilHeatFlux, cropHeatFlux, minCanopyTemperature, maxCanopyTemperature)
#%%CyML Model End%%