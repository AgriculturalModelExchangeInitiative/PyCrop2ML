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
    //                          - description : shoot number for the whole canopy
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 288.0
    //                          - unit : shoot m-2
    //                          - inputtype : variable
    //            - name: leafNumber
    //                          - description : Leaf number 
    //                          - variablecategory : state
    //                          - inputtype : variable
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 0
    //                          - unit : leaf
    //            - name: sowingDensity
    //                          - description : number of plant /m²
    //                          - parametercategory : constant
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 500
    //                          - default : 288
    //                          - unit : plant m-2
    //                          - inputtype : parameter
    //            - name: targetFertileShoot
    //                          - description : max value of shoot number for the canopy
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 280
    //                          - max : 1000
    //                          - default : 600
    //                          - unit : shoot
    //                          - inputtype : variable
    //            - name: tilleringProfile
    //                          - description :  store the amount of new tiller created at each time a new tiller appears
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - default : [288.0]
    //                          - unit : 
    //                          - inputtype : variable
    //            - name: leafTillerNumberArray
    //                          - description : store the number of tiller for each leaf layer
    //                          - variablecategory : auxiliary
    //                          - datatype : INTLIST
    //                          - unit : leaf
    //                          - default : [1]
    //                          - inputtype : variable
    //            - name: tillerNumber
    //                          - description :  store the amount of tiller created at each time a tiller appears
    //                          - variablecategory : auxiliary
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 10000
    //                          - default : 1
    //                          - unit : 
    //                          - inputtype : variable
        //- outputs:
    //            - name: averageShootNumberPerPlant
    //                          - description : average shoot number per plant in the canopy
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : shoot m-2
    //            - name: canopyShootNumber
    //                          - description : shoot number for the whole canopy
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLE
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : m2 m-2
    //            - name: leafTillerNumberArray
    //                          - description : store the number of tiller for each leaf layer
    //                          - variablecategory : auxiliary
    //                          - datatype : INTLIST
    //                          - unit : leaf
    //            - name: tilleringProfile
    //                          - description :  store the amount of new tiller created at each time a new tiller appears
    //                          - variablecategory : auxiliary
    //                          - datatype : DOUBLELIST
    //                          - unit : 
    //            - name: tillerNumber
    //                          - description :  store the amount of new tiller created at each time a new tiller appears
    //                          - variablecategory : auxiliary
    //                          - datatype : INT
    //                          - min : 0
    //                          - max : 10000
    //                          - unit : 
        double averageShootNumberPerPlant;
        double oldCanopyShootNumber;
        int emergedLeaves;
        int shoots;
        int i;
        oldCanopyShootNumber = canopyShootNumber;
        emergedLeaves = (int)(Math.Max(1.0d, Math.Ceiling(leafNumber - 1)));
        shoots = fibonacci_(emergedLeaves);
        canopyShootNumber = Math.Min((double)(shoots * sowingDensity), targetFertileShoot);
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
        if ((canopyShootNumber != oldCanopyShootNumber))
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