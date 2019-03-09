using System;
using System.Collections.Generic;
public class Phyllochron_
{
    public static Tuple<double,double,double>  phyllochron_(double fixPhyll,double leafNumber,double lincr,double ldecr,double pdecr,double pincr,double ptq,double gai,double pastMaxAI,double kl,double aPTQ,double phylPTQ1,double p,string choosePhyllUse)
    {
        //- Description:
    //            - Model Name: Phyllochron Model
    //            - Author: Pierre Martre
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: Calculate different types of phyllochron 
        //- inputs:
    //            - name: fixPhyll
    //                          - description : Sowing date corrected Phyllochron
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 5
    //                          - unit : °C d leaf-1
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: leafNumber
    //                          - description : Actual number of phytomers
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 25
    //                          - default : 0
    //                          - unit : leaf
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: lincr
    //                          - description : Leaf number above which the phyllochron is increased by Pincr
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 30
    //                          - default : 8
    //                          - unit : leaf
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: ldecr
    //                          - description : Leaf number up to which the phyllochron is decreased by Pdecr
    //                          - parametercategory : species
    //                          - inputtype : parameter
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 30
    //                          - default : 10
    //                          - unit : leaf
    //                          - uri : some url
    //            - name: pdecr
    //                          - description : Factor decreasing the phyllochron for leaf number less than Ldecr
    //                          - parametercategory : constant
    //                          - inputtype : parameter
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10
    //                          - default : 0.4
    //                          - unit : 
    //                          - uri : some url
    //            - name: pincr
    //                          - description : Factor increasing the phyllochron for leaf number higher than Lincr
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 1.5
    //                          - min : 0
    //                          - max : 10
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: ptq
    //                          - description : Photothermal quotient 
    //                          - parametercategory : species
    //                          - inputtype : variable
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : MJ °C-1 d-1 m-2)
    //                          - uri : some url
    //            - name: gai
    //                          - description : Green Area Index
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : m2 m-2
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: pastMaxAI
    //                          - description : PhotoThermal Quotien
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : m2 m-2
    //                          - uri : some url
    //                          - inputtype : variable
    //            - name: kl
    //                          - description : Exctinction Coefficient
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 50
    //                          - default : 0.45
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: aPTQ
    //                          - description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
    //                          - parametercategory : constant
    //                          - inputtype : variable
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - default : 0.842934
    //                          - unit : 
    //                          - uri : some url
    //            - name: phylPTQ1
    //                          - description : Phyllochron at PTQ equal 1
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - default : 20
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : °C d leaf-1
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: p
    //                          - description : Phyllochron (Varietal parameter)
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - default : 120
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : °C d leaf-1
    //                          - uri : some url
    //                          - inputtype : parameter
    //            - name: choosePhyllUse
    //                          - description : Switch to choose the type of phyllochron calculation to be used
    //                          - datatype : STRING
    //                          - default : Default
    //                          - unit : 
    //                          - uri : some url
    //                          - inputtype : parameter
        //- outputs:
    //            - name: phyllochron
    //                          - description :  the rate of leaf appearance 
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - unit :  °C d leaf-1
    //            - name: pastMaxAI
    //                          - description : Past maximum GAI
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : m2 m-2
    //            - name: gai
    //                          - description : Green Area Index
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : m2 m-2
    //                          - uri : some url
        double phyllochron;
        double pastMaxAI1;
        phyllochron = 0.0d;
        if ((choosePhyllUse == "Default"))
        {
            if ((leafNumber < ldecr))
            {
                phyllochron = fixPhyll * pdecr;
            }
            else if ( (leafNumber >= ldecr) && (leafNumber < lincr))
            {
                phyllochron = fixPhyll;
            }
            else
            {
                phyllochron = fixPhyll * pincr;
            }
        }
        if ((choosePhyllUse == "PTQ"))
        {
            pastMaxAI1 = pastMaxAI;
            gai = Math.Max(pastMaxAI1, gai);
            pastMaxAI = gai;
            if ((gai > 0.0d))
            {
                phyllochron = phylPTQ1 * gai * kl / (1 - Math.Exp(-kl * gai)) / (ptq + aPTQ);
            }
            else
            {
                phyllochron = phylPTQ1;
            }
        }
        if ((choosePhyllUse == "Test"))
        {
            if ((leafNumber < ldecr))
            {
                phyllochron = p * pdecr;
            }
            else if ( (leafNumber >= ldecr) && (leafNumber < lincr))
            {
                phyllochron = p;
            }
            else
            {
                phyllochron = p * pincr;
            }
        }
        return Tuple.Create(phyllochron, pastMaxAI, gai);
    }
}