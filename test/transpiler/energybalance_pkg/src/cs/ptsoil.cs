using System;
using System.Collections.Generic;
public class Ptsoil_
{
    public static double ptsoil_(double evapoTranspirationPriestlyTaylor,double Alpha,double tau,double tauAlpha)
    {
        //- Description:
    //            - Model Name: PtSoil EnergyLimitedEvaporation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA Montpellier
    //            - Abstract: Evaporation from the soil in the energy-limited stage 
        //- inputs:
    //            - name: evapoTranspirationPriestlyTaylor
    //                          - min : 0
    //                          - default : 120
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °g m-2 d-1
    //                          - description : evapoTranspiration Priestly Taylor
    //            - name: Alpha
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 100
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 1.5
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : Priestley-Taylor evapotranspiration proportionality constant
    //            - name: tau
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 100
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.9983
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : plant cover factor
    //            - name: tauAlpha
    //                          - parametercategory : soil
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.3
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : Fraction of the total net radiation exchanged at the soil surface when AlpaE = 1
        //- outputs:
    //            - name: energyLimitedEvaporation
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description : energy Limited Evaporation 
        double energyLimitedEvaporation;
        double AlphaE;
        if (tau < tauAlpha)
        {
            AlphaE = 1.0d;
        }
        else
        {
            AlphaE = Alpha - (Alpha - 1.0d) * (1.0d - tau) / (1.0d - tauAlpha);
        }
        energyLimitedEvaporation = evapoTranspirationPriestlyTaylor / Alpha * AlphaE * tau;
        return energyLimitedEvaporation;
    }
}