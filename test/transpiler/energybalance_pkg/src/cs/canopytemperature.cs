using System;
using System.Collections.Generic;
public class Canopytemperature_
{
    public static Tuple<double,double>  canopytemperature_(double minTair,double maxTair,double cropHeatFlux,double conductance,double lambdaV,double rhoDensityAir,double specificHeatCapacityAir)
    {
        //- Description:
    //            - Model Name: CanopyTemperature Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: It is calculated from the crop heat flux and the boundary layer conductance 
        //- inputs:
    //            - name: minTair
    //                          - min : -30
    //                          - default : 0.7
    //                          - max : 45
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - variablecategory : auxiliary
    //                          - inputtype : variable
    //                          - unit : °C
    //                          - description : minimum air temperature
    //            - name: maxTair
    //                          - min : -30
    //                          - default : 7.2
    //                          - max : 45
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - variablecategory : auxiliary
    //                          - inputtype : variable
    //                          - unit : °C
    //                          - description : maximum air Temperature
    //            - name: cropHeatFlux
    //                          - min : 0
    //                          - default : 447.912
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : rate
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : g m² d-1
    //                          - description : Crop heat flux
    //            - name: conductance
    //                          - min : 0
    //                          - default : 598.685
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : m d-1
    //                          - description : the boundary layer conductance
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
    //            - name: rhoDensityAir
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 1.225
    //                          - inputtype : parameter
    //                          - unit : kg m3
    //                          - description : Density of air
    //            - name: specificHeatCapacityAir
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.00101
    //                          - inputtype : parameter
    //                          - unit : MJ kg-1 °C-1
    //                          - description : Specific heat capacity of dry air
        //- outputs:
    //            - name: minCanopyTemperature
    //                          - min : -30
    //                          - datatype : DOUBLE
    //                          - max : 45
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - unit : °C
    //                          - description : minimal Canopy Temperature  
    //            - name: maxCanopyTemperature
    //                          - min : -30
    //                          - datatype : DOUBLE
    //                          - max : 45
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - unit : °C
    //                          - description : maximal Canopy Temperature 
        double minCanopyTemperature;
        double maxCanopyTemperature;
        minCanopyTemperature = minTair + cropHeatFlux / rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000;
        maxCanopyTemperature = maxTair + cropHeatFlux / rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000;
        return Tuple.Create(minCanopyTemperature, maxCanopyTemperature);
    }
}