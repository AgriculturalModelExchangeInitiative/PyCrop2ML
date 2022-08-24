# coding: utf8
from copy import copy
from array import array
from math import *

from datetime import datetime
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

def model_energybalance(albedoCoefficient,
         vaporPressure,
         stefanBoltzman,
         extraSolarRadiation,
         solarRadiation,
         minTair,
         elevation,
         maxTair,
         plantHeight,
         vonKarman,
         d,
         zm,
         wind,
         heightWeatherMeasurements,
         zh,
         deficitOnTopLayers,
         soilDiffusionConstant,
         lambdaV,
         hslope,
         psychrometricConstant,
         Alpha,
         tau,
         tauAlpha,
         VPDair,
         rhoDensityAir,
         specificHeatCapacityAir,
         isWindVpDefined):
    """
     - Name: EnergyBalance -Version: 001, -Time step: 1
     - Description:
                 * Title: EnergyBalance model
                 * Author: Peter D. Jamieson, Glen S. Francis, Derick R. Wilson, Robert J. Martin
                 * Reference: None
                 * Institution: New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd., New Zealand Institute for Crop and Food Research Ltd. 
                 * ExtendedDescription: Modelling energy balance in the wheat crop model SiriusQuality2: Evapotranspiration and canopy and soil temperature calculations                        see documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=547    
                 * ShortDescription: None
     - inputs:
                 * name: albedoCoefficient
                               ** description : albedo Coefficient
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.23
                               ** unit : 
                 * name: vaporPressure
                               ** description : vapor Pressure
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 6.1
                               ** unit : hPa
                 * name: stefanBoltzman
                               ** description : stefan Boltzman constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 4.903E-09
                               ** unit : 
                 * name: extraSolarRadiation
                               ** description : extra Solar Radiation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 11.7
                               ** unit : MJ m2 d-1
                 * name: solarRadiation
                               ** description : solar Radiation
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 3
                               ** unit : MJ m-2 d-1
                 * name: minTair
                               ** description : minimum air temperature
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 45
                               ** min : -30
                               ** default : 0.7
                               ** unit : Â°C
                 * name: elevation
                               ** description : elevation
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : -500
                               ** default : 0
                               ** unit : m
                 * name: maxTair
                               ** description : maximum air Temperature
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 45
                               ** min : -30
                               ** default : 7.2
                               ** unit : Â°C
                 * name: plantHeight
                               ** description : plant Height
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0
                               ** unit : mm
                 * name: vonKarman
                               ** description : von Karman constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.42
                               ** unit : dimensionless
                 * name: d
                               ** description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.67
                               ** unit : dimensionless
                 * name: zm
                               ** description : roughness length governing momentum transfer, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.13
                               ** unit : m
                 * name: wind
                               ** description : wind
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000000
                               ** min : 0
                               ** default : 124000
                               ** unit : m/d
                 * name: heightWeatherMeasurements
                               ** description : reference height of wind and humidity measurements
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 2
                               ** unit : m
                 * name: zh
                               ** description : roughness length governing transfer of heat and vapour, FAO
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.013
                               ** unit : m
                 * name: deficitOnTopLayers
                               ** description : deficit On TopLayers
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** min : 0
                               ** default : 5341
                               ** unit : g m-2 d-1
                 * name: soilDiffusionConstant
                               ** description : soil Diffusion Constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 4.2
                               ** unit : 
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 10
                               ** min : 0
                               ** default : 2.454
                               ** unit : MJ kg-1
                 * name: hslope
                               ** description : the slope of saturated vapor pressure temperature curve at a given temperature 
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 0.584
                               ** unit : hPa Â°C-1
                 * name: psychrometricConstant
                               ** description : psychrometric constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.66
                               ** unit : 
                 * name: Alpha
                               ** description : Priestley-Taylor evapotranspiration proportionality constant
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 1.5
                               ** unit : 
                 * name: tau
                               ** description : plant cover factor
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 100
                               ** min : 0
                               ** default : 0.9983
                               ** unit : 
                 * name: tauAlpha
                               ** description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.3
                               ** unit : 
                 * name: VPDair
                               ** description :  vapour pressure density
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** min : 0
                               ** default : 2.19
                               ** unit : hPa
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1.225
                               ** min : 1.225
                               ** default : 1.225
                               ** unit : 
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** max : 1
                               ** min : 0
                               ** default : 0.00101
                               ** unit : 
                 * name: isWindVpDefined
                               ** description : if wind and vapour pressure are defined
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : INT
                               ** max : 1
                               ** min : 0
                               ** default : 1
                               ** unit : 
     - outputs:
                 * name: netRadiation
                               ** description :  net radiation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : MJ m-2 d-1
                 * name: netOutGoingLongWaveRadiation
                               ** description : net OutGoing Long Wave Radiation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 10000
                               ** min : 0
                               ** unit : m/d
                 * name: diffusionLimitedEvaporation
                               ** description : the evaporation from the diffusion limited soil 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: netRadiationEquivalentEvaporation
                               ** description : net Radiation in Equivalent Evaporation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: evapoTranspirationPriestlyTaylor
                               ** description : evapoTranspiration of Priestly Taylor 
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: energyLimitedEvaporation
                               ** description : energy Limited Evaporation 
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: evapoTranspirationPenman
                               ** description :  evapoTranspiration of Penman Monteith
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: soilEvaporation
                               ** description : soil Evaporation
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** max : 5000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: evapoTranspiration
                               ** description : evapoTranspiration
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : mm
                 * name: soilHeatFlux
                               ** description : soil Heat Flux 
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: potentialTranspiration
                               ** description : potential Transpiration 
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: cropHeatFlux
                               ** description :  crop Heat Flux
                               ** datatype : DOUBLE
                               ** variablecategory : rate
                               ** max : 10000
                               ** min : 0
                               ** unit : g m-2 d-1
                 * name: minCanopyTemperature
                               ** description : minimal Canopy Temperature  
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 45
                               ** min : -30
                               ** unit : degC
                 * name: maxCanopyTemperature
                               ** description : maximal Canopy Temperature 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** max : 45
                               ** min : -30
                               ** unit : degC
    """

    (netRadiation, netOutGoingLongWaveRadiation) = model_netradiation(minTair, maxTair, solarRadiation, vaporPressure, extraSolarRadiation, albedoCoefficient, stefanBoltzman, elevation)
    conductance = model_conductance(plantHeight, wind, vonKarman, heightWeatherMeasurements, zm, zh, d)
    diffusionLimitedEvaporation = model_diffusionlimitedevaporation(deficitOnTopLayers, soilDiffusionConstant)
    netRadiationEquivalentEvaporation = model_netradiationequivalentevaporation(netRadiation, lambdaV)
    evapoTranspirationPriestlyTaylor = model_priestlytaylor(netRadiationEquivalentEvaporation, hslope, psychrometricConstant, Alpha)
    energyLimitedEvaporation = model_ptsoil(evapoTranspirationPriestlyTaylor, Alpha, tau, tauAlpha)
    evapoTranspirationPenman = model_penman(evapoTranspirationPriestlyTaylor, hslope, VPDair, conductance, psychrometricConstant, Alpha, lambdaV, rhoDensityAir, specificHeatCapacityAir)
    soilEvaporation = model_soilevaporation(diffusionLimitedEvaporation, energyLimitedEvaporation)
    evapoTranspiration = model_evapotranspiration(evapoTranspirationPriestlyTaylor, evapoTranspirationPenman, isWindVpDefined)
    soilHeatFlux = model_soilheatflux(netRadiationEquivalentEvaporation, soilEvaporation, tau)
    potentialTranspiration = model_potentialtranspiration(evapoTranspiration, tau)
    cropHeatFlux = model_cropheatflux(netRadiationEquivalentEvaporation, soilHeatFlux, potentialTranspiration)
    (minCanopyTemperature, maxCanopyTemperature) = model_canopytemperature(minTair, maxTair, cropHeatFlux, conductance, lambdaV, rhoDensityAir, specificHeatCapacityAir)
    return (netRadiation, netOutGoingLongWaveRadiation, conductance, diffusionLimitedEvaporation, netRadiationEquivalentEvaporation, evapoTranspirationPriestlyTaylor, energyLimitedEvaporation, evapoTranspirationPenman, soilEvaporation, evapoTranspiration, soilHeatFlux, potentialTranspiration, cropHeatFlux, minCanopyTemperature, maxCanopyTemperature)