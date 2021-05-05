!Test generation'

PROGRAM test_test1_PotentialTranspiration:
    REAL:: evapoTranspiration

    REAL:: tau

    REAL:: potentialTranspiration

    tau = 0.9983

    evapoTranspiration = 830.958

    call potentialtranspiration_(evapoTranspiration,tau,potentialTranspiration)
    print *,potentialTranspiration
 END PROGRAM

