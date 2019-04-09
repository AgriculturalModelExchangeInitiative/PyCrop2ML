using System;
using System.Collections.Generic;
public class Conductance_
{
    public static double conductance_(double vonKarman,double heightWeatherMeasurements,double zm,double zh,double d,double plantHeight,double wind)
    {
        //- Description:
    //            - Model Name: Conductance Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: The boundary layer conductance is expressed as the wind speed profile above the
    //            canopy and the canopy structure. The approach does not take into account buoyancy
    //            effects. 
        //- inputs:
    //            - name: vonKarman
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.42
    //                          - inputtype : parameter
    //                          - unit :  
    //                          - description : von Karman constant
    //            - name: heightWeatherMeasurements
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 2
    //                          - inputtype : parameter
    //                          - unit : m
    //                          - description : reference height of wind and humidity measurements
    //            - name: zm
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.13
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : roughness length governing momentum transfer, FAO
    //            - name: zh
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.013
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : roughness length governing transfer of heat and vapour, FAO
    //            - name: d
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547rl
    //                          - default : 0.67
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : corresponding to 2/3. This is multiplied to the crop heigth for calculating the zero plane displacement height, FAO
    //            - name: plantHeight
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0
    //                          - variablecategory : state
    //                          - inputtype : variable
    //                          - unit : mm
    //                          - description : plant Height
    //            - name: wind
    //                          - min : 0
    //                          - default : 124000
    //                          - max : 1000000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : m d-1
    //                          - description : wind
        //- outputs:
    //            - name: conductance
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - unit : m d-1
    //                          - description : the boundary layer conductance
        double conductance;
        double h;
        h = Math.Max(10, plantHeight) / 100.0d;
        conductance = wind * Math.Pow(vonKarman, 2) / Math.Log((heightWeatherMeasurements - d * h) / zm * h) * Math.Log((heightWeatherMeasurements - d * h) / zh * h);
        return conductance;
    }
}