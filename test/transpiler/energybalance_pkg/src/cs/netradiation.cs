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
    //                          - description : minimal temperature
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -30
    //                          - max : 45
    //                          - default : 0.7
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: maxTair
    //                          - description : maximal Temperature
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -30
    //                          - max : 45
    //                          - default : 7.2
    //                          - unit : °C
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: albedoCoefficient
    //                          - description : albedoCoefficient
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0.23
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: stefanBoltzman
    //                          - description : stefanBoltzman
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 4.903E-09
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: elevation
    //                          - description : elevation
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 0
    //                          - min : -500
    //                          - max : 10000
    //                          - unit : m
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : parameter
    //            - name: solarRadiation
    //                          - description : solar Radiation
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 3
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : MJ/m²/d
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: vaporPressure
    //                          - description : vapor Pressure
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 6.1
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : hPa
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
    //            - name: extraSolarRadiation
    //                          - description : extra Solar Radiation
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - default : 11.7
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : MJ m2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - inputtype : variable
        //- outputs:
    //            - name: netRadiation
    //                          - description :  net radiation 
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            - name: netOutGoingLongWaveRadiation
    //                          - description : net OutGoing Long Wave Radiation 
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - unit : g m-2 d-1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
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