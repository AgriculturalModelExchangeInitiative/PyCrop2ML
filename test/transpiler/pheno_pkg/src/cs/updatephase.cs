using System;
using System.Collections.Generic;
public class Updatephase_
{
    public static Tuple<double,double,int>  updatephase_(double cumulTT,double leafNumber,double cumulTTFromZC_39,int isMomentRegistredZC_39,double gai,double grainCumulTT,double dayLength,double vernaprog,double minFinalNumber,double fixPhyll,int isVernalizable,double dse,double pFLLAnth,double dcd,double dgf,double degfm,double maxDL,double sLDL,bool ignoreGrainMaturation,double pHEADANTH,int switchMaize,string choosePhyllUse,double p,double phase,double cumulTTFromZC_91,double phyllochron,int hasLastPrimordiumAppeared)
    {
        //- Description:
    //            - Model Name: UpdatePhase Model
    //            - Author: Pierre MARTRE
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA Montpellier
    //            - Abstract: This strategy advances the phase and calculate the final leaf number
    //    	
        //- inputs:
    //            - name: cumulTT
    //                          - description : cumul thermal times at current date
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : -200
    //                          - max : 10000
    //                          - default : 354.582294511779
    //                          - unit : °C d
    //                          - inputtype : variable
    //            - name: leafNumber
    //                          - description : Actual number of phytomers
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 25
    //                          - default :  4.620511621863958
    //                          - unit : leaf
    //                          - inputtype : variable
    //            - name: cumulTTFromZC_39
    //                          - description : cumul of the thermal time ( DeltaTT) since the moment ZC_39
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : °C d-1
    //                          - inputtype : variable
    //            - name: isMomentRegistredZC_39
    //                          - description : true if ZC_39 is registered in the calendar
    //                          - variablecategory : auxiliary
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: gai
    //                          - description : used to calculate Terminal spikelet
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0.3255196285135
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: grainCumulTT
    //                          - description : cumulTT used for the grain developpment
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : °C d
    //                          - inputtype : variable
    //            - name: dayLength
    //                          - description : length of the day
    //                          - datatype : DOUBLE
    //                          - variablecategory : auxiliary
    //                          - min : 0
    //                          - max : 24
    //                          - unit : h
    //                          - default : 12.7433275303389
    //                          - inputtype : variable
    //            - name: vernaprog
    //                          - description : progression on a 0  to 1 scale of the vernalization
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10
    //                          - default :  1.0532526829571554
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: minFinalNumber
    //                          - description : minimum final leaf number
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 25
    //                          - default : 6.879410413987549
    //                          - unit : leaf
    //                          - inputtype : variable
    //            - name: fixPhyll
    //                          - description : Phyllochron with sowing date fix
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 91.2
    //                          - unit : °C d
    //                          - inputtype : variable
    //            - name: isVernalizable
    //                          - description : true if the plant is vernalizable
    //                          - parametercategory : constant
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
    //                          - default : 1
    //                          - inputtype : parameter
    //            - name: dse
    //                          - description : Thermal time from sowing to emergence
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - default : 105
    //                          - unit : °C d
    //                          - inputtype : parameter
    //            - name: pFLLAnth
    //                          - description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
    //                          - parametercategory : constant
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - unit : 
    //                          - default : 2.22
    //                          - inputtype : parameter
    //            - name: dcd
    //                          - description : Duration of the endosperm cell division phase
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 100
    //                          - unit : °C d
    //                          - inputtype : parameter
    //            - name: dgf
    //                          - description : Grain filling duration (from anthesis to physiological maturity)
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 450
    //                          - unit : °C d
    //                          - inputtype : parameter
    //            - name: degfm
    //                          - description : Grain maturation duration (from physiological maturity to harvest ripeness)
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 50
    //                          - default : 0
    //                          - unit : °C d
    //                          - inputtype : parameter
    //            - name: maxDL
    //                          - description : Saturating photoperiod above which final leaf number is not influenced by daylength
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 24
    //                          - default : 15
    //                          - unit : h
    //                          - inputtype : parameter
    //            - name: sLDL
    //                          - description : Daylength response of leaf production
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0.85
    //                          - unit : leaf h-1
    //                          - inputtype : parameter
    //            - name: ignoreGrainMaturation
    //                          - description : true to ignore grain maturation
    //                          - datatype : BOOLEAN
    //                          - default : FALSE
    //                          - unit : 
    //                          - inputtype : parameter
    //            - name: pHEADANTH
    //                          - description : Number of phyllochron between heading and anthesiss
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - default : 1
    //                          - unit : 
    //                          - inputtype : parameter
    //            - name: switchMaize
    //                          - description : true if maize
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0
    //                          - unit : 
    //                          - inputtype : parameter
    //            - name: choosePhyllUse
    //                          - description : Switch to choose the type of phyllochron calculation to be used
    //                          - datatype : STRING
    //                          - unit : 
    //                          - default : Default
    //                          - inputtype : parameter
    //            - name: p
    //                          - description : Phyllochron (Varietal parameter)
    //                          - parametercategory : species
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - default : 120
    //                          - unit : °C d leaf-1
    //                          - inputtype : parameter
    //            - name: phase
    //                          - description :  the name of the phase
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 7
    //                          - default : 1
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: cumulTTFromZC_91
    //                          - description : cumul of the thermal time (DeltaTT) since the moment ZC_91
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 5000
    //                          - default : 0
    //                          - unit : °C d-1
    //                          - inputtype : variable
    //            - name: phyllochron
    //                          - description : Phyllochron
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 1000
    //                          - default : 91.2
    //                          - unit : °C d leaf-1
    //                          - inputtype : variable
    //            - name: hasLastPrimordiumAppeared
    //                          - description : if Last Primordium has Appeared
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - default : 0
    //                          - unit : 
    //                          - inputtype : variable
        //- outputs:
    //            - name: finalLeafNumber
    //                          - description : final leaf number
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 25
    //                          - unit : leaf
    //            - name: phase
    //                          - description : the name of the phase
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 7
    //                          - unit : 
    //            - name: hasLastPrimordiumAppeared
    //                          - description : if Last Primordium has Appeared
    //                          - variablecategory : state
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 1
    //                          - unit : 
        double finalLeafNumber;
        double phase1;
        double ttFromLastLeafToHeading;
        double appFLN;
        double localDegfm;
        double ttFromLastLeafToAnthesis;
        phase1 = phase;
        if (phase1 >= 0.0d && phase1 < 1.0d)
        {
            if (switchMaize == 0)
            {
                if (cumulTT >= dse)
                {
                    phase = 1.0d;
                }
                else
                {
                    phase = phase1;
                }
            }
            else
            {
                if (cumulTT >= dse)
                {
                    phase = 1.0d;
                }
                else
                {
                    phase = phase1;
                }
            }
        }
        else if ( phase1 >= 1.0d && phase1 < 2.0d)
        {
            if (isVernalizable == 1 && vernaprog >= 1.0d || isVernalizable == 0)
            {
                if (switchMaize == 0)
                {
                    if (dayLength > maxDL)
                    {
                        finalLeafNumber = minFinalNumber;
                        hasLastPrimordiumAppeared = 1;
                    }
                    else
                    {
                        appFLN = minFinalNumber + sLDL * (maxDL - dayLength);
                        if (appFLN / 2.0d <= leafNumber)
                        {
                            finalLeafNumber = appFLN;
                            hasLastPrimordiumAppeared = 1;
                        }
                        else
                        {
                            phase = phase1;
                        }
                    }
                }
                else
                {
                    hasLastPrimordiumAppeared = 1;
                }
                if (hasLastPrimordiumAppeared == 1)
                {
                    phase = 2.0d;
                }
            }
            else
            {
                phase = phase1;
            }
        }
        else if ( phase1 >= 2.0d && phase1 < 4.0d)
        {
            if (isMomentRegistredZC_39 == 1)
            {
                if (phase1 < 3.0d)
                {
                    ttFromLastLeafToHeading = 0.0d;
                    if (choosePhyllUse == "Default")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll;
                    }
                    else if ( choosePhyllUse == "PTQ")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
                    }
                    else if ( choosePhyllUse == "Test")
                    {
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p;
                    }
                    if (cumulTTFromZC_39 >= ttFromLastLeafToHeading)
                    {
                        phase = 3.0d;
                    }
                    else
                    {
                        phase = phase1;
                    }
                }
                else
                {
                    phase = phase1;
                }
                ttFromLastLeafToAnthesis = 0.0d;
                if (choosePhyllUse == "Default")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll;
                }
                else if ( choosePhyllUse == "PTQ")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron;
                }
                else if ( choosePhyllUse == "Test")
                {
                    ttFromLastLeafToAnthesis = pFLLAnth * p;
                }
                if (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis)
                {
                    phase = 4.0d;
                }
            }
            else
            {
                phase = phase1;
            }
        }
        else if ( phase1 == 4.0d)
        {
            if (grainCumulTT >= dcd)
            {
                phase = 4.5d;
            }
            else
            {
                phase = phase1;
            }
        }
        else if ( phase1 == 4.5d)
        {
            if (grainCumulTT >= dgf || gai <= 0.0d)
            {
                phase = 5.0d;
            }
            else
            {
                phase = phase1;
            }
        }
        else if ( phase1 >= 5.0d && phase1 < 6.0d)
        {
            localDegfm = degfm;
            if (ignoreGrainMaturation)
            {
                localDegfm = -1.0d;
            }
            if (cumulTTFromZC_91 >= localDegfm)
            {
                phase = 6.0d;
            }
            else
            {
                phase = phase1;
            }
        }
        else if ( phase1 >= 6.0d && phase1 < 7.0d)
        {
            phase = phase1;
        }
        return Tuple.Create(finalLeafNumber, phase, hasLastPrimordiumAppeared);
    }
}