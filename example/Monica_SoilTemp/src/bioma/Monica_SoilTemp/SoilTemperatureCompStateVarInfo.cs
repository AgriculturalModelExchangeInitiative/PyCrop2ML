
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SoilTemperatureComp.DomainClass
{
    public class SoilTemperatureCompStateVarInfo : IVarInfoClass
    {
        static VarInfo _V = new VarInfo();
        static VarInfo _B = new VarInfo();
        static VarInfo _volumeMatrix = new VarInfo();
        static VarInfo _volumeMatrixOld = new VarInfo();
        static VarInfo _matrixPrimaryDiagonal = new VarInfo();
        static VarInfo _matrixSecondaryDiagonal = new VarInfo();
        static VarInfo _heatConductivity = new VarInfo();
        static VarInfo _heatConductivityMean = new VarInfo();
        static VarInfo _heatCapacity = new VarInfo();
        static VarInfo _solution = new VarInfo();
        static VarInfo _matrixDiagonal = new VarInfo();
        static VarInfo _matrixLowerTriangle = new VarInfo();
        static VarInfo _heatFlow = new VarInfo();
        static VarInfo _soilSurfaceTemperature = new VarInfo();
        static VarInfo _soilTemperature = new VarInfo();
        static VarInfo _noSnowSoilSurfaceTemperature = new VarInfo();

        static SoilTemperatureCompStateVarInfo()
        {
            SoilTemperatureCompStateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureCompState Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureCompState";}
        }

        public static  VarInfo V
        {
            get { return _V;}
        }

        public static  VarInfo B
        {
            get { return _B;}
        }

        public static  VarInfo volumeMatrix
        {
            get { return _volumeMatrix;}
        }

        public static  VarInfo volumeMatrixOld
        {
            get { return _volumeMatrixOld;}
        }

        public static  VarInfo matrixPrimaryDiagonal
        {
            get { return _matrixPrimaryDiagonal;}
        }

        public static  VarInfo matrixSecondaryDiagonal
        {
            get { return _matrixSecondaryDiagonal;}
        }

        public static  VarInfo heatConductivity
        {
            get { return _heatConductivity;}
        }

        public static  VarInfo heatConductivityMean
        {
            get { return _heatConductivityMean;}
        }

        public static  VarInfo heatCapacity
        {
            get { return _heatCapacity;}
        }

        public static  VarInfo solution
        {
            get { return _solution;}
        }

        public static  VarInfo matrixDiagonal
        {
            get { return _matrixDiagonal;}
        }

        public static  VarInfo matrixLowerTriangle
        {
            get { return _matrixLowerTriangle;}
        }

        public static  VarInfo heatFlow
        {
            get { return _heatFlow;}
        }

        public static  VarInfo soilSurfaceTemperature
        {
            get { return _soilSurfaceTemperature;}
        }

        public static  VarInfo soilTemperature
        {
            get { return _soilTemperature;}
        }

        public static  VarInfo noSnowSoilSurfaceTemperature
        {
            get { return _noSnowSoilSurfaceTemperature;}
        }

        static void DescribeVariables()
        {
            _V.Name = "V";
            _V.Description = "V";
            _V.MaxValue = -1D;
            _V.MinValue = -1D;
            _V.DefaultValue = -1D;
            _V.Units = "°C";
            _V.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _B.Name = "B";
            _B.Description = "B";
            _B.MaxValue = -1D;
            _B.MinValue = -1D;
            _B.DefaultValue = -1D;
            _B.Units = "°C";
            _B.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _volumeMatrix.Name = "volumeMatrix";
            _volumeMatrix.Description = "volumeMatrix";
            _volumeMatrix.MaxValue = -1D;
            _volumeMatrix.MinValue = -1D;
            _volumeMatrix.DefaultValue = -1D;
            _volumeMatrix.Units = "°C";
            _volumeMatrix.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _volumeMatrixOld.Name = "volumeMatrixOld";
            _volumeMatrixOld.Description = "volumeMatrixOld";
            _volumeMatrixOld.MaxValue = -1D;
            _volumeMatrixOld.MinValue = -1D;
            _volumeMatrixOld.DefaultValue = -1D;
            _volumeMatrixOld.Units = "°C";
            _volumeMatrixOld.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _matrixPrimaryDiagonal.Name = "matrixPrimaryDiagonal";
            _matrixPrimaryDiagonal.Description = "matrixPrimaryDiagonal";
            _matrixPrimaryDiagonal.MaxValue = -1D;
            _matrixPrimaryDiagonal.MinValue = -1D;
            _matrixPrimaryDiagonal.DefaultValue = -1D;
            _matrixPrimaryDiagonal.Units = "°C";
            _matrixPrimaryDiagonal.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _matrixSecondaryDiagonal.Name = "matrixSecondaryDiagonal";
            _matrixSecondaryDiagonal.Description = "matrixSecondaryDiagonal";
            _matrixSecondaryDiagonal.MaxValue = -1D;
            _matrixSecondaryDiagonal.MinValue = -1D;
            _matrixSecondaryDiagonal.DefaultValue = -1D;
            _matrixSecondaryDiagonal.Units = "°C";
            _matrixSecondaryDiagonal.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _heatConductivity.Name = "heatConductivity";
            _heatConductivity.Description = "heatConductivity";
            _heatConductivity.MaxValue = -1D;
            _heatConductivity.MinValue = -1D;
            _heatConductivity.DefaultValue = -1D;
            _heatConductivity.Units = "°C";
            _heatConductivity.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _heatConductivityMean.Name = "heatConductivityMean";
            _heatConductivityMean.Description = "heatConductivityMean";
            _heatConductivityMean.MaxValue = -1D;
            _heatConductivityMean.MinValue = -1D;
            _heatConductivityMean.DefaultValue = -1D;
            _heatConductivityMean.Units = "°C";
            _heatConductivityMean.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _heatCapacity.Name = "heatCapacity";
            _heatCapacity.Description = "heatCapacity";
            _heatCapacity.MaxValue = -1D;
            _heatCapacity.MinValue = -1D;
            _heatCapacity.DefaultValue = -1D;
            _heatCapacity.Units = "°C";
            _heatCapacity.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _solution.Name = "solution";
            _solution.Description = "solution";
            _solution.MaxValue = -1D;
            _solution.MinValue = -1D;
            _solution.DefaultValue = -1D;
            _solution.Units = "°C";
            _solution.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _matrixDiagonal.Name = "matrixDiagonal";
            _matrixDiagonal.Description = "matrixDiagonal";
            _matrixDiagonal.MaxValue = -1D;
            _matrixDiagonal.MinValue = -1D;
            _matrixDiagonal.DefaultValue = -1D;
            _matrixDiagonal.Units = "°C";
            _matrixDiagonal.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _matrixLowerTriangle.Name = "matrixLowerTriangle";
            _matrixLowerTriangle.Description = "matrixLowerTriangle";
            _matrixLowerTriangle.MaxValue = -1D;
            _matrixLowerTriangle.MinValue = -1D;
            _matrixLowerTriangle.DefaultValue = -1D;
            _matrixLowerTriangle.Units = "°C";
            _matrixLowerTriangle.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _heatFlow.Name = "heatFlow";
            _heatFlow.Description = "heatFlow";
            _heatFlow.MaxValue = -1D;
            _heatFlow.MinValue = -1D;
            _heatFlow.DefaultValue = -1D;
            _heatFlow.Units = "°C";
            _heatFlow.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _soilSurfaceTemperature.Name = "soilSurfaceTemperature";
            _soilSurfaceTemperature.Description = "soilSurfaceTemperature";
            _soilSurfaceTemperature.MaxValue = -1D;
            _soilSurfaceTemperature.MinValue = -1D;
            _soilSurfaceTemperature.DefaultValue = -1D;
            _soilSurfaceTemperature.Units = "°C";
            _soilSurfaceTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _soilTemperature.Name = "soilTemperature";
            _soilTemperature.Description = "soilTemperature next day";
            _soilTemperature.MaxValue = -1D;
            _soilTemperature.MinValue = -1D;
            _soilTemperature.DefaultValue = -1D;
            _soilTemperature.Units = "°C";
            _soilTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _noSnowSoilSurfaceTemperature.Name = "noSnowSoilSurfaceTemperature";
            _noSnowSoilSurfaceTemperature.Description = "soilSurfaceTemperature without snow";
            _noSnowSoilSurfaceTemperature.MaxValue = -1D;
            _noSnowSoilSurfaceTemperature.MinValue = -1D;
            _noSnowSoilSurfaceTemperature.DefaultValue = 0.0;
            _noSnowSoilSurfaceTemperature.Units = "°C";
            _noSnowSoilSurfaceTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}