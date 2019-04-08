using System;
using System.Collections.Generic;
public class Netradiationequivalentevaporation_
{
    public static double netradiationequivalentevaporation_(double lambdaV,double netRadiation)
    {
        //- Description:
    //            - Model Name: NetRadiationEquivalentEvaporation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract:  It is given by dividing net radiation by latent heat of vaporization of water 
        //- inputs:
    //            - name: lambdaV
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 2.454
    //                          - inputtype : parameter
    //                          - unit : MJ kg-1
    //                          - description : latent heat of vaporization of water
    //            - name: netRadiation
    //                          - min : 0
    //                          - default : 1.566
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : MJ m-2 d-1
    //                          - description : net radiation
        //- outputs:
    //            - name: netRadiationEquivalentEvaporation
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - unit : g m-2 d-1
    //                          - description : net Radiation in Equivalent Evaporation 
        double netRadiationEquivalentEvaporation;
        netRadiationEquivalentEvaporation = netRadiation / lambdaV * 1000.0d;
        return netRadiationEquivalentEvaporation;
    }
}