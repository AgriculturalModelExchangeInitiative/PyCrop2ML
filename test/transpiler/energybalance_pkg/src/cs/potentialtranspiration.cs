using System;
using System.Collections.Generic;
public class Potentialtranspiration_
{
    public static double potentialtranspiration_(double evapoTranspiration,double tau)
    {
        //- Description:
    //            - Model Name: PotentialTranspiration Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: SiriusQuality2 uses availability of water from the soil reservoir as a method to restrict
    //                    transpiration as soil moisture is depleted 
        //- inputs:
    //            - name: evapoTranspiration
    //                          - min : 0
    //                          - default : 830.958
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : rate
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : mm
    //                          - description : evapoTranspiration
    //            - name: tau
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.9983
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : plant cover factor
        //- outputs:
    //            - name: potentialTranspiration
    //                          - min : 0
    //                          - variablecategory : rate
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description : potential Transpiration 
        double potentialTranspiration;
        potentialTranspiration = evapoTranspiration * (1 - tau);
        return potentialTranspiration;
    }
}