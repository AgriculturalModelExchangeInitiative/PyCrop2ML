!Test generation'

PROGRAM test_test1_DiffusionLimitedEvaporation:
    REAL:: deficitOnTopLayers

    REAL:: soilDiffusionConstant

    REAL:: diffusionLimitedEvaporation

    soilDiffusionConstant = 4.2

    deficitOnTopLayers = 5341

    call diffusionlimitedevaporation_(deficitOnTopLayers,soilDiffusionConstant,diffusionLimitedEvaporation)
    print *,diffusionLimitedEvaporation
 END PROGRAM

