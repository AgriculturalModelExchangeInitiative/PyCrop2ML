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
# `self` is the interface of this composition. The external name may differ
# from the ModelUnit input name, and the binding precedes the model call.
NoSnowSoilSurfaceTemperature.tmin = self.minimumAirTemperature
NoSnowSoilSurfaceTemperature()

WithSnowSoilSurfaceTemperature.noSnowSoilSurfaceTemperature = \
    NoSnowSoilSurfaceTemperature.soilSurfaceTemperature
WithSnowSoilSurfaceTemperature()

SoilTemperature.soilSurfaceTemperature = \
    WithSnowSoilSurfaceTemperature.soilSurfaceTemperature
SoilTemperature()

self.soilSurfaceTemperature = WithSnowSoilSurfaceTemperature.soilSurfaceTemperature
self.soilTemperature = SoilTemperature.soilTemperature
