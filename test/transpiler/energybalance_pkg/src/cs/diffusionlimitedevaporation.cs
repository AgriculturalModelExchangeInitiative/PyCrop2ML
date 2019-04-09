using System;
using System.Collections.Generic;
public class Diffusionlimitedevaporation_
{
    public static double diffusionlimitedevaporation_(double deficitOnTopLayers,double soilDiffusionConstant)
    {
        //- Description:
    //            - Model Name: DiffusionLimitedEvaporation Model
    //            - Author: Pierre Martre
    //            - Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            - Institution: INRA Montpellier
    //            - Abstract: the evaporation from the diffusion limited soil 
        //- inputs:
    //            - name: deficitOnTopLayers
    //                          - min : 0
    //                          - default : 5341
    //                          - max : 10000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : g m-2 d-1
    //                          - description : deficit On TopLayers
    //            - name: soilDiffusionConstant
    //                          - parametercategory : soil
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 10
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - default : 4.2
    //                          - inputtype : parameter
    //                          - unit : 
    //                          - description : soil Diffusion Constant
        //- outputs:
    //            - name: diffusionLimitedEvaporation
    //                          - min : 0
    //                          - variablecategory : state
    //                          - max : 5000
    //                          - uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          - datatype : DOUBLE
    //                          - unit : g m-2 d-1
    //                          - description : the evaporation from the diffusion limited soil 
        double diffusionLimitedEvaporation;
        if (deficitOnTopLayers / 1000.0d <= 0.0d)
        {
            diffusionLimitedEvaporation = 8.3d * 1000;
        }
        else
        {
            if (deficitOnTopLayers / 1000 < 25.0d)
            {
                diffusionLimitedEvaporation = 2 * soilDiffusionConstant * soilDiffusionConstant / deficitOnTopLayers / 1000.0d * 1000.0d;
            }
            else
            {
                diffusionLimitedEvaporation = 0.0d;
            }
        }
        return diffusionLimitedEvaporation;
    }
}