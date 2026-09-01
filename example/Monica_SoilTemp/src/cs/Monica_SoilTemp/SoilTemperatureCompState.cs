using System;
using System.Collections.Generic;
public class SoilTemperatureCompState 
{
    private double[] _V = new double[noOfTempLayers];
    private double[] _B = new double[noOfTempLayers];
    private double[] _volumeMatrix = new double[noOfTempLayers];
    private double[] _volumeMatrixOld = new double[noOfTempLayers];
    private double[] _matrixPrimaryDiagonal = new double[noOfTempLayers];
    private double[] _matrixSecondaryDiagonal = new double[noOfTempLayersPlus1];
    private double[] _heatConductivity = new double[noOfTempLayers];
    private double[] _heatConductivityMean = new double[noOfTempLayers];
    private double[] _heatCapacity = new double[noOfTempLayers];
    private double[] _solution = new double[noOfTempLayers];
    private double[] _matrixDiagonal = new double[noOfTempLayers];
    private double[] _matrixLowerTriangle = new double[noOfTempLayers];
    private double[] _heatFlow = new double[noOfTempLayers];
    private double _soilSurfaceTemperature;
    private double[] _soilTemperature = new double[22];
    private double _noSnowSoilSurfaceTemperature;
    
        public SoilTemperatureCompState() { }
    
    
    public SoilTemperatureCompState(SoilTemperatureCompState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    V = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { V[i] = toCopy.V[i]; }
    
    B = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { B[i] = toCopy.B[i]; }
    
    volumeMatrix = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { volumeMatrix[i] = toCopy.volumeMatrix[i]; }
    
    volumeMatrixOld = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { volumeMatrixOld[i] = toCopy.volumeMatrixOld[i]; }
    
    matrixPrimaryDiagonal = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { matrixPrimaryDiagonal[i] = toCopy.matrixPrimaryDiagonal[i]; }
    
    matrixSecondaryDiagonal = new double[noOfTempLayersPlus1];
            for (int i = 0; i < noOfTempLayersPlus1; i++)
            { matrixSecondaryDiagonal[i] = toCopy.matrixSecondaryDiagonal[i]; }
    
    heatConductivity = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { heatConductivity[i] = toCopy.heatConductivity[i]; }
    
    heatConductivityMean = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { heatConductivityMean[i] = toCopy.heatConductivityMean[i]; }
    
    heatCapacity = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { heatCapacity[i] = toCopy.heatCapacity[i]; }
    
    solution = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { solution[i] = toCopy.solution[i]; }
    
    matrixDiagonal = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { matrixDiagonal[i] = toCopy.matrixDiagonal[i]; }
    
    matrixLowerTriangle = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { matrixLowerTriangle[i] = toCopy.matrixLowerTriangle[i]; }
    
    heatFlow = new double[noOfTempLayers];
            for (int i = 0; i < noOfTempLayers; i++)
            { heatFlow[i] = toCopy.heatFlow[i]; }
    
    soilSurfaceTemperature = toCopy.soilSurfaceTemperature;
    soilTemperature = new double[22];
            for (int i = 0; i < 22; i++)
            { soilTemperature[i] = toCopy.soilTemperature[i]; }
    
    noSnowSoilSurfaceTemperature = toCopy.noSnowSoilSurfaceTemperature;
    }
    }
    public double[] V
        {
            get { return this._V; }
            set { this._V= value; } 
        }
    public double[] B
        {
            get { return this._B; }
            set { this._B= value; } 
        }
    public double[] volumeMatrix
        {
            get { return this._volumeMatrix; }
            set { this._volumeMatrix= value; } 
        }
    public double[] volumeMatrixOld
        {
            get { return this._volumeMatrixOld; }
            set { this._volumeMatrixOld= value; } 
        }
    public double[] matrixPrimaryDiagonal
        {
            get { return this._matrixPrimaryDiagonal; }
            set { this._matrixPrimaryDiagonal= value; } 
        }
    public double[] matrixSecondaryDiagonal
        {
            get { return this._matrixSecondaryDiagonal; }
            set { this._matrixSecondaryDiagonal= value; } 
        }
    public double[] heatConductivity
        {
            get { return this._heatConductivity; }
            set { this._heatConductivity= value; } 
        }
    public double[] heatConductivityMean
        {
            get { return this._heatConductivityMean; }
            set { this._heatConductivityMean= value; } 
        }
    public double[] heatCapacity
        {
            get { return this._heatCapacity; }
            set { this._heatCapacity= value; } 
        }
    public double[] solution
        {
            get { return this._solution; }
            set { this._solution= value; } 
        }
    public double[] matrixDiagonal
        {
            get { return this._matrixDiagonal; }
            set { this._matrixDiagonal= value; } 
        }
    public double[] matrixLowerTriangle
        {
            get { return this._matrixLowerTriangle; }
            set { this._matrixLowerTriangle= value; } 
        }
    public double[] heatFlow
        {
            get { return this._heatFlow; }
            set { this._heatFlow= value; } 
        }
    public double soilSurfaceTemperature
        {
            get { return this._soilSurfaceTemperature; }
            set { this._soilSurfaceTemperature= value; } 
        }
    public double[] soilTemperature
        {
            get { return this._soilTemperature; }
            set { this._soilTemperature= value; } 
        }
    public double noSnowSoilSurfaceTemperature
        {
            get { return this._noSnowSoilSurfaceTemperature; }
            set { this._noSnowSoilSurfaceTemperature= value; } 
        }
}