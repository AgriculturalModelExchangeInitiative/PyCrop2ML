!Test generation'

PROGRAM test_test1_EvapoTranspiration:
    INTEGER:: isWindVpDefined

    REAL:: evapoTranspirationPriestlyTaylor

    REAL:: evapoTranspirationPenman

    REAL:: evapoTranspiration

    isWindVpDefined = 1

    evapoTranspirationPriestlyTaylor = 449.367

    evapoTranspirationPenman = 830.957

    call evapotranspiration_(isWindVpDefined,evapoTranspirationPriestlyTaylor,evapoTranspirationPenman,evapoTranspiration)
    print *,evapoTranspiration
 END PROGRAM

