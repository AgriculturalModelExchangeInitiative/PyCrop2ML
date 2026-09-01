"""
type: composition
name: SoilTemperatureComp
id: Monica_SoilTemp.SoilTemperatureComp
version: "1"
timestep: 1

description:
  title: SoilTemperature model
  authors: Michael Berg-Mohnicke
  institution: ZALF e.V.
  reference: ""
  extended_description: ""
  short_description: >
    Calculates the soil temperature in all layers and soil surface temperature.
"""

# ModelUnit interfaces are loaded from their Crop2ML descriptions.
NoSnowSoilSurfaceTemperature()

WithSnowSoilSurfaceTemperature.noSnowSoilSurfaceTemperature = \
    NoSnowSoilSurfaceTemperature.soilSurfaceTemperature
WithSnowSoilSurfaceTemperature()

SoilTemperature.soilSurfaceTemperature = \
    WithSnowSoilSurfaceTemperature.soilSurfaceTemperature
SoilTemperature()

soilSurfaceTemperature = WithSnowSoilSurfaceTemperature.soilSurfaceTemperature
soilTemperature = SoilTemperature.soilTemperature
