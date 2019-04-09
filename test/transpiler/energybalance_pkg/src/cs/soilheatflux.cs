using System;
using System.Collections.Generic;
public class Soilheatflux_
{
    public static double soilheatflux_(double netRadiationEquivalentEvaporation,double tau,double soilEvaporation)
    {
        //- Description:
    //            - Model Name: SoilHeatFlux Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: The available energy in the soil 
        //- inputs:
    //            - name: netRadiationEquivalentEvaporation
    //                          - min : 0
    //                          - default : 638.142
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : g m-2 d-1
    //                          - description : net Radiation Equivalent Evaporation
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
    //            - name: soilEvaporation
    //                          - min : 0
    //                          - default : 448.240
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : g m-2 d-1
    //                          - description : soil Evaporation
        //- outputs:
    //            - name: soilHeatFlux
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description : soil Heat Flux 
        double soilHeatFlux;
        soilHeatFlux = tau * netRadiationEquivalentEvaporation - soilEvaporation;
        return soilHeatFlux;
    }
}