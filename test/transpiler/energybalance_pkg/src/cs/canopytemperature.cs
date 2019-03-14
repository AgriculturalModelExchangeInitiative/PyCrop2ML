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
    //                          - description : minimal temperature
    //                          - datatype : DOUBLE
    //                          - variablecategory : auxiliary
    //                          - min : -30
    //                          - max : 45
    //                          - default : 0.7
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: maxTair
    //                          - description : max Temperature
    //                          - datatype : DOUBLE
    //                          - variablecategory : auxiliary
    //                          - min : -30
    //                          - max : 45
    //                          - default : 7.2
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: cropHeatFlux
    //                          - description : Crop heat flux
    //                          - variablecategory : rate
    //                          - inputtype : variable
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 447.912
    //                          - unit : g m² d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: conductance
    //                          - description : the boundary layer conductance
    //                          - variablecategory : state
    //                          - inputtype : variable
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 598.685
    //                          - unit : m d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: lambdaV
    //                          - description : latent heat of vaporization of water
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 2.454
    //                          - min : 0
    //                          - max : 10
    //                          - unit : MJ kg-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: rhoDensityAir
    //                          - description : Density of air
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 1.225
    //                          - unit : kg m3
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: specificHeatCapacityAir
    //                          - description : Specific heat capacity of dry air
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0.00101
    //                          - unit : MJ kg-1 °C-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
        //- outputs:
    //            - name: minCanopyTemperature
    //                          - description : minimal Canopy Temperature  
    //                          - datatype : DOUBLE
    //                          - min : -30
    //                          - max : 45
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: maxCanopyTemperature
    //                          - description : maximal Canopy Temperature 
    //                          - datatype : DOUBLE
    //                          - min : -30
    //                          - max : 45
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
        double minCanopyTemperature;
        double maxCanopyTemperature;
        minCanopyTemperature = minTair + cropHeatFlux / rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000;
        maxCanopyTemperature = maxTair + cropHeatFlux / rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000;
        return Tuple.Create(minCanopyTemperature, maxCanopyTemperature);
    }
}