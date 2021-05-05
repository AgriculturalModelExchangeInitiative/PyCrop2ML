!Test generation'

PROGRAM test_test1_NetRadiationEquivalentEvaporation:
    REAL:: lambdaV

    REAL:: netRadiation

    REAL:: netRadiationEquivalentEvaporation

    netRadiation = 1.566

    lambdaV = 2.454

    call netradiationequivalentevaporation_(lambdaV,netRadiation,netRadiationEquivalentEvaporation)
    print *,netRadiationEquivalentEvaporation
 END PROGRAM

