MODULE Ptsoil_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE ptsoil_(evapoTranspirationPriestlyTaylor, &
        tau, &
        tauAlpha, &
        energyLimitedEvaporation)
        REAL, INTENT(OUT) :: energyLimitedEvaporation
        REAL:: AlphaE
        REAL, INTENT(IN) :: evapoTranspirationPriestlyTaylor
        REAL, PARAMETER :: Alpha = 1.5
        REAL, INTENT(IN) :: tau
        REAL, INTENT(IN) :: tauAlpha
        !- Description:
    !            - Model Name: PtSoil EnergyLimitedEvaporation Model
    !            - Author: Pierre Martre
    !            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    !            Evapotranspiration and canopy and soil temperature calculations
    !            - Institution: INRA Montpellier
    !            - Abstract: Evaporation from the soil in the energy-limited stage 
        !- inputs:
    !            - name: evapoTranspirationPriestlyTaylor
    !                          - description : evapoTranspiration Priestly Taylor
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - default : 120
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : °g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : variable
    !            - name: Alpha
    !                          - description : Priestley-Taylor evapotranspiration proportionality constant
    !                          - parametercategory : constant
    !                          - datatype : DOUBLE
    !                          - default : 1.5
    !                          - min : 0
    !                          - max : 100
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: tau
    !                          - description : plant cover factor
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - default : 0.9983
    !                          - min : 0
    !                          - max : 100
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
    !            - name: tauAlpha
    !                          - description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
    !                          - parametercategory : soil
    !                          - datatype : DOUBLE
    !                          - default : 0.3
    !                          - min : 0
    !                          - max : 1
    !                          - unit : 
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    !                          - inputtype : parameter
        !- outputs:
    !            - name: energyLimitedEvaporation
    !                          - description : energy Limited Evaporation 
    !                          - variablecategory : state
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 5000
    !                          - unit : g m-2 d-1
    !                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        IF(tau .LT. tauAlpha) THEN
            AlphaE = 1.0
        ELSE
            AlphaE = Alpha - (Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha)
        END IF
        energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha *  &
                AlphaE * tau
    END SUBROUTINE ptsoil_
END MODULE
