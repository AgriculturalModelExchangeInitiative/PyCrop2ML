using System;
using System.Collections.Generic;
public class Phylsowingdatecorrection_
{
    public static double phylsowingdatecorrection_(int sowingDay,double latitude,int sDsa_sh,double rp,int sDws,int sDsa_nh,double p)
    {
        //- Description:
    //            - Model Name: PhylSowingDateCorrection Model
    //            - Author: Loic Manceau
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
        //- inputs:
    //            - name: sowingDay
    //                          - parametercategory : constant
    //                          - min : 1
    //                          - datatype : INT
    //                          - max : 365
    //                          - uri : some url
    //                          - default : 1
    //                          - inputtype : parameter
    //                          - unit : d
    //                          - description : Day of Year at sowing
    //            - name: latitude
    //                          - parametercategory : constant
    //                          - min : -90
    //                          - datatype : DOUBLE
    //                          - max : 90
    //                          - uri : some url
    //                          - default : 0.0
    //                          - inputtype : parameter
    //                          - unit : °
    //                          - description : Latitude
    //            - name: sDsa_sh
    //                          - parametercategory : constant
    //                          - min : 1
    //                          - datatype : INT
    //                          - max : 365
    //                          - uri : some url
    //                          - default : 1
    //                          - inputtype : parameter
    //                          - unit : d
    //                          - description : Sowing date at which Phyllochrone is maximum in southern hemispher
    //            - name: rp
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 365
    //                          - uri : some url
    //                          - default : 0
    //                          - inputtype : parameter
    //                          - unit : d-1
    //                          - description : Rate of change of Phyllochrone with sowing date
    //            - name: sDws
    //                          - parametercategory : constant
    //                          - min : 1
    //                          - datatype : INT
    //                          - max : 365
    //                          - uri : some url
    //                          - default : 1
    //                          - inputtype : parameter
    //                          - unit : d
    //                          - description : Sowing date at which Phyllochrone is minimum
    //            - name: sDsa_nh
    //                          - parametercategory : constant
    //                          - min : 1
    //                          - datatype : INT
    //                          - max : 365
    //                          - uri : some url
    //                          - default : 1
    //                          - inputtype : parameter
    //                          - unit : d
    //                          - description : Sowing date at which Phyllochrone is maximum in northern hemispher
    //            - name: p
    //                          - parametercategory : species
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1000
    //                          - uri : some url
    //                          - default : 120
    //                          - inputtype : parameter
    //                          - unit : °C d leaf-1
    //                          - description : Phyllochron (Varietal parameter)
        //- outputs:
    //            - name: fixPhyll
    //                          - min : 0
    //                          - datatype : DOUBLE
    //                          - max : 1000
    //                          - unit : °C d leaf-1
    //                          - description :  Phyllochron Varietal parameter 
        double fixPhyll;
        if (latitude < 0.0d)
        {
            if (sowingDay > sDsa_sh)
            {
                fixPhyll = p * (1 - rp * Math.Min((sowingDay - sDsa_sh), sDws));
            }
            else
            {
                fixPhyll = p;
            }
        }
        else
        {
            if (sowingDay < sDsa_nh)
            {
                fixPhyll = p * (1 - rp * Math.Min(sowingDay, sDws));
            }
            else
            {
                fixPhyll = p;
            }
        }
        return fixPhyll;
    }
}