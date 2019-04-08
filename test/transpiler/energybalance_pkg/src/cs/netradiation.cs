using System;
using System.Collections.Generic;
public class Netradiation_
{
    public static Tuple<double,double>  netradiation_(double minTair,double maxTair,double albedoCoefficient,double stefanBoltzman,double elevation,double solarRadiation,double vaporPressure,double extraSolarRadiation)
    {
        //- Description:
    //            - Model Name: NetRadiation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA Montpellier
    //            - Abstract: It is calculated at the surface of the canopy and is givenby the difference between incoming and outgoing radiation of both short 
    //                     and long wavelength radiation 
        //- inputs:
    //            - name: minTair
    //                          - min : -30
    //                          - default : 0.7
    //                          - max : 45
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C
    //                          - description : minimum air temperature
    //            - name: maxTair
    //                          - min : -30
    //                          - default : 7.2
    //                          - max : 45
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : °C
    //                          - description : maximum air Temperature
    //            - name: albedoCoefficient
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.23
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : albedo Coefficient
    //            - name: stefanBoltzman
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 4.903E-09
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : stefan Boltzman constant
    //            - name: elevation
    //                          - parametercategory : constant
    //                          - min : -500
    //                          - datatype : DOUBLE
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0
    //                          - inputtype : parameter
    //                          - unit : m
    //                          - description : elevation
    //            - name: solarRadiation
    //                          - min : 0
    //                          - default : 3
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : MJ m-2 d-1
    //                          - description : solar Radiation
    //            - name: vaporPressure
    //                          - min : 0
    //                          - default : 6.1
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : hPa
    //                          - description : vapor Pressure
    //            - name: extraSolarRadiation
    //                          - min : 0
    //                          - default : 11.7
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : MJ m2 d-1
    //                          - description : extra Solar Radiation
        //- outputs:
    //            - name: netRadiation
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description :  net radiation 
    //            - name: netOutGoingLongWaveRadiation
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description : net OutGoing Long Wave Radiation 
        double netRadiation;
        double netOutGoingLongWaveRadiation;
        double Nsr;
        double clearSkySolarRadiation;
        double averageT;
        double surfaceEmissivity;
        double cloudCoverFactor;
        double Nolr;
        Nsr = (1 - albedoCoefficient) * solarRadiation;
        clearSkySolarRadiation = (0.75d + 2 * Math.Pow(10, -5) * elevation) * extraSolarRadiation;
        averageT = (Math.Pow(maxTair + 273.16d, 4) + Math.Pow(minTair + 273.16d, 4)) / 2;
        surfaceEmissivity = 0.34d - 0.14d * Math.Sqrt(vaporPressure / 10);
        cloudCoverFactor = 1.35d * solarRadiation / clearSkySolarRadiation - 0.35d;
        Nolr = stefanBoltzman * averageT * surfaceEmissivity * cloudCoverFactor;
        netRadiation = Nsr - Nolr;
        netOutGoingLongWaveRadiation = Nolr;
        return Tuple.Create(netRadiation, netOutGoingLongWaveRadiation);
    }
}