using System;
using System.Collections.Generic;
public class Penman_
{
    public static double penman_(double evapoTranspirationPriestlyTaylor,double hslope,double VPDair,double psychrometricConstant,double Alpha,double lambdaV,double rhoDensityAir,double specificHeatCapacityAir,double conductance)
    {
        //- Description:
    //            - Model Name: Penman Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: This method is used when wind and vapor pressure daily data are available 
    //        
        //- inputs:
    //            - name: evapoTranspirationPriestlyTaylor
    //                          - min : 0
    //                          - default : 449.367
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : rate
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : g m-2 d-1
    //                          - description : evapoTranspiration of Priestly Taylor 
    //            - name: hslope
    //                          - min : 0
    //                          - default : 0.584
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : hPa °C-1
    //                          - description : the slope of saturated vapor pressure temperature curve at a given temperature 
    //            - name: VPDair
    //                          - min : 0
    //                          - default : 2.19
    //                          - max : 1000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : hPa
    //                          - description :  vapour pressure density
    //            - name: psychrometricConstant
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.66
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : psychrometric constant
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
    //            - name: lambdaV
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 2.454
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : latent heat of vaporization of water
    //            - name: rhoDensityAir
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 1.225
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : Density of air
    //            - name: specificHeatCapacityAir
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 0.00101
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : Specific heat capacity of dry air
    //            - name: conductance
    //                          - min : 0
    //                          - default : 598.685
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : m d-1
    //                          - description : conductance
        //- outputs:
    //            - name: evapoTranspirationPenman
    //                          - min : 0
    //                          - variablecategory : rate
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description :  evapoTranspiration of Penman Monteith
        double evapoTranspirationPenman;
        evapoTranspirationPenman = evapoTranspirationPriestlyTaylor / Alpha + 1000 * rhoDensityAir * specificHeatCapacityAir * VPDair * conductance / lambdaV * (hslope + psychrometricConstant);
        return evapoTranspirationPenman;
    }
}