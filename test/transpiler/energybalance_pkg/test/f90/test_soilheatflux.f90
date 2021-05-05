!Test generation'

PROGRAM test_test1_SoilHeatFlux:
    REAL:: netRadiationEquivalentEvaporation

    REAL:: tau

    REAL:: soilEvaporation

    REAL:: soilHeatFlux

    tau = 0.9983

    netRadiationEquivalentEvaporation = 638.142

    soilEvaporation = 448.240

    call soilheatflux_(netRadiationEquivalentEvaporation,tau,soilEvaporation,soilHeatFlux)
    print *,soilHeatFlux
 END PROGRAM

