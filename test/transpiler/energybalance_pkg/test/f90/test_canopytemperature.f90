!Test generation'

PROGRAM test_test1_CanopyTemperature:
    REAL:: minTair

    REAL:: maxTair

    REAL:: cropHeatFlux

    REAL:: conductance

    REAL:: lambdaV

    REAL:: rhoDensityAir

    REAL:: specificHeatCapacityAir

    REAL:: minCanopyTemperature

    REAL:: maxCanopyTemperature

    rhoDensityAir = 1.225

    minTair = 0.7

    maxTair = 7.2

    cropHeatFlux = 447.912

    conductance = 598.685

    lambdaV = 2.454

    specificHeatCapacityAir = 0.00101

    call canopytemperature_(minTair,maxTair,cropHeatFlux,conductance,lambdaV,rhoDensityAir,specificHeatCapacityAir,minCanopyTemperature,maxCanopyTemperature)
    print *,minCanopyTemperature,maxCanopyTemperature
 END PROGRAM

