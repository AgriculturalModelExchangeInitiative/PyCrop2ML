!Test generation'

PROGRAM test_test1_PriestlyTaylor:
    REAL:: netRadiationEquivalentEvaporation

    REAL:: hslope

    REAL:: psychrometricConstant

    REAL:: Alpha

    REAL:: evapoTranspirationPriestlyTaylor

    Alpha = 1.5

    netRadiationEquivalentEvaporation = 638.142

    hslope = 0.584

    psychrometricConstant = 0.66

    call priestlytaylor_(netRadiationEquivalentEvaporation,hslope,psychrometricConstant,Alpha,evapoTranspirationPriestlyTaylor)
    print *,evapoTranspirationPriestlyTaylor
 END PROGRAM

