!Test generation'

PROGRAM test_test1_SoilEvaporation:
    REAL:: diffusionLimitedEvaporation

    REAL:: energyLimitedEvaporation

    REAL:: soilEvaporation

    diffusionLimitedEvaporation = 6605.505

    energyLimitedEvaporation = 448.240

    call soilevaporation_(diffusionLimitedEvaporation,energyLimitedEvaporation,soilEvaporation)
    print *,soilEvaporation
 END PROGRAM

