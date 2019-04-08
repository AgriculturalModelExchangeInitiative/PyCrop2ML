using System;
using System.Collections.Generic;
public class Shootnumber_
{
    public static Tuple<double,double,List<int>,List<double>,int>  shootnumber_(double canopyShootNumber,double leafNumber,int sowingDensity,double targetFertileShoot,List<double> tilleringProfile,List<int> leafTillerNumberArray,int tillerNumber)
    {
        //- Description:
    //            - Model Name: CalculateShootNumber Model
    //            - Author: Pierre MARTRE
    //            - Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            - Institution: INRA/LEPSE Montpellier
    //            - Abstract: calculate the shoot number and update the related variables if needed
        //- inputs:
    //            - name: canopyShootNumber
    //                          - min : 0
    //                          - default : 288.0
    //                          - max : 10000
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : shoot m-2
    //                          - description : shoot number for the whole canopy
    //            - name: leafNumber
    //                          - min : 0
    //                          - default : 0
    //                          - max : 10000
    //                          - variablecategory : state
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : leaf
    //                          - description : Leaf number 
    //            - name: sowingDensity
    //                          - parametercategory : constant
    //                          - min : 0
    //                          - datatype : INT
    //                          - max : 500
    //                          - default : 288
    //                          - inputtype : parameter
    //                          - unit : plant m-2
    //                          - description : number of plant /m²
    //            - name: targetFertileShoot
    //                          - min : 280
    //                          - default : 600
    //                          - max : 1000
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - inputtype : variable
    //                          - unit : shoot
    //                          - description : max value of shoot number for the canopy
    //            - name: tilleringProfile
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - default : [288.0]
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description :  store the amount of new tiller created at each time a new tiller appears
    //            - name: leafTillerNumberArray
    //                          - variablecategory : auxiliary
    //                          - datatype : INTLIST
    //                          - default : [1]
    //                          - inputtype : variable
    //                          - unit : leaf
    //                          - description : store the number of tiller for each leaf layer
    //            - name: tillerNumber
    //                          - min : 0
    //                          - default : 1
    //                          - max : 10000
    //                          - variablecategory : auxiliary
    //                          - datatype : INT
    //                          - inputtype : variable
    //                          - unit : 
    //                          - description :  Number of tiller which appears
        //- outputs:
    //            - name: averageShootNumberPerPlant
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - variablecategory : auxiliary
    //                          - max : 10000
    //                          - unit : shoot m-2
    //                          - description : average shoot number per plant in the canopy
    //            - name: canopyShootNumber
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - variablecategory : auxiliary
    //                          - max : 10000
    //                          - unit : shoot m-2
    //                          - description : shoot number for the whole canopy
    //            - name: leafTillerNumberArray
    //                          - variablecategory : auxiliary
    //                          - datatype : INTLIST
    //                          - unit : leaf
    //                          - description : store the number of tiller for each leaf layer
    //            - name: tilleringProfile
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - unit : 
    //                          - description :  store the amount of new tiller created at each time a new tiller appears
    //            - name: tillerNumber
    //                          - datatype : INT
    //                          - min : 0
    //                          - variablecategory : auxiliary
    //                          - max : 10000
    //                          - unit : 
    //                          - description :  store the amount of new tiller created at each time a new tiller appears
        double averageShootNumberPerPlant;
        double oldCanopyShootNumber;
        int emergedLeaves;
        int shoots;
        int i;
        oldCanopyShootNumber = canopyShootNumber;
        emergedLeaves = (int)(Math.Max(1.0d, Math.Ceiling(leafNumber - 1)));
        shoots = fibonacci_(emergedLeaves).result;
        canopyShootNumber = Math.Min((double)(shoots * sowingDensity), targetFertileShoot);
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
        if (canopyShootNumber != oldCanopyShootNumber)
        {
            tilleringProfile.Add(canopyShootNumber - oldCanopyShootNumber);
        }
        tillerNumber = tilleringProfile.Count();
        for (i=leafTillerNumberArray.Count() ; i<(int)(Math.Ceiling(leafNumber)) ; i+=1)
        {
            leafTillerNumberArray.Add(tillerNumber);
        }
        return Tuple.Create(averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, tillerNumber);
    }
}