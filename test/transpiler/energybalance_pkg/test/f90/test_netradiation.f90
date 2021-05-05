!Test generation'

PROGRAM test_test1_NetRadiation:
    REAL:: minTair

    REAL:: maxTair

    REAL:: albedoCoefficient

    REAL:: stefanBoltzman

    REAL:: elevation

    REAL:: solarRadiation

    REAL:: vaporPressure

    REAL:: extraSolarRadiation

    REAL:: netRadiation

    REAL:: netOutGoingLongWaveRadiation

    elevation = 0

    solarRadiation = 3

    vaporPressure = 6.1

    minTair = 0.7

    maxTair = 7.2

    albedoCoefficient = 0.23

    stefanBoltzman = 4.903E-09

    extraSolarRadiation = 11.7

    call netradiation_(minTair,maxTair,albedoCoefficient,stefanBoltzman,elevation,solarRadiation,vaporPressure,extraSolarRadiation,netRadiation,netOutGoingLongWaveRadiation)
    print *,netRadiation,netOutGoingLongWaveRadiation
 END PROGRAM

