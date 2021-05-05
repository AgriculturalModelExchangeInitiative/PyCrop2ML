!Test generation'

PROGRAM test_test1_PtSoil:
    REAL:: evapoTranspirationPriestlyTaylor

    REAL:: Alpha

    REAL:: tau

    REAL:: tauAlpha

    REAL:: energyLimitedEvaporation

    tau = 0.9983

    evapoTranspirationPriestlyTaylor = 449.367

    Alpha = 1.5

    tauAlpha = 0.3

    call ptsoil_(evapoTranspirationPriestlyTaylor,Alpha,tau,tauAlpha,energyLimitedEvaporation)
    print *,energyLimitedEvaporation
 END PROGRAM

