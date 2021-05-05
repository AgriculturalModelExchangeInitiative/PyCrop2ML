!Test generation'

PROGRAM test_test1_CropHeatFlux:
    REAL:: netRadiationEquivalentEvaporation

    REAL:: soilHeatFlux

    REAL:: potentialTranspiration

    REAL:: cropHeatFlux

    netRadiationEquivalentEvaporation = 638.142

    soilHeatFlux = 188.817

    potentialTranspiration =  1.413

    call cropheatflux_(netRadiationEquivalentEvaporation,soilHeatFlux,potentialTranspiration,cropHeatFlux)
    print *,cropHeatFlux
 END PROGRAM

