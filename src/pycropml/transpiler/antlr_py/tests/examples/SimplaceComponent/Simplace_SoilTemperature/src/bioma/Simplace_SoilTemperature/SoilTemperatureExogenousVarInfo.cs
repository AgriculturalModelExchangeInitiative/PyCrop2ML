
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SoilTemperature.DomainClass
{
    public class SoilTemperatureExogenousVarInfo : IVarInfoClass
    {
        static VarInfo _iAirTemperatureMax = new VarInfo();
        static VarInfo _iTempMax = new VarInfo();
        static VarInfo _iAirTemperatureMin = new VarInfo();
        static VarInfo _iTempMin = new VarInfo();
        static VarInfo _iGlobalSolarRadiation = new VarInfo();
        static VarInfo _iRadiation = new VarInfo();
        static VarInfo _iRAIN = new VarInfo();
        static VarInfo _iCropResidues = new VarInfo();
        static VarInfo _iPotentialSoilEvaporation = new VarInfo();
        static VarInfo _iLeafAreaIndex = new VarInfo();
        static VarInfo _SoilTempArray = new VarInfo();
        static VarInfo _iSoilTempArray = new VarInfo();
        static VarInfo _iSoilWaterContent = new VarInfo();
        static VarInfo _iSoilSurfaceTemperature = new VarInfo();

        static SoilTemperatureExogenousVarInfo()
        {
            SoilTemperatureExogenousVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "SoilTemperatureExogenous Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "SoilTemperatureExogenous";}
        }

        public static  VarInfo iAirTemperatureMax
        {
            get { return _iAirTemperatureMax;}
        }

        public static  VarInfo iTempMax
        {
            get { return _iTempMax;}
        }

        public static  VarInfo iAirTemperatureMin
        {
            get { return _iAirTemperatureMin;}
        }

        public static  VarInfo iTempMin
        {
            get { return _iTempMin;}
        }

        public static  VarInfo iGlobalSolarRadiation
        {
            get { return _iGlobalSolarRadiation;}
        }

        public static  VarInfo iRadiation
        {
            get { return _iRadiation;}
        }

        public static  VarInfo iRAIN
        {
            get { return _iRAIN;}
        }

        public static  VarInfo iCropResidues
        {
            get { return _iCropResidues;}
        }

        public static  VarInfo iPotentialSoilEvaporation
        {
            get { return _iPotentialSoilEvaporation;}
        }

        public static  VarInfo iLeafAreaIndex
        {
            get { return _iLeafAreaIndex;}
        }

        public static  VarInfo SoilTempArray
        {
            get { return _SoilTempArray;}
        }

        public static  VarInfo iSoilTempArray
        {
            get { return _iSoilTempArray;}
        }

        public static  VarInfo iSoilWaterContent
        {
            get { return _iSoilWaterContent;}
        }

        public static  VarInfo iSoilSurfaceTemperature
        {
            get { return _iSoilSurfaceTemperature;}
        }

        static void DescribeVariables()
        {
            _iAirTemperatureMax.Name = "iAirTemperatureMax";
            _iAirTemperatureMax.Description = "Daily maximum temperature";
            _iAirTemperatureMax.MaxValue = 50.0;
            _iAirTemperatureMax.MinValue = -40.0;
            _iAirTemperatureMax.DefaultValue = -1D;
            _iAirTemperatureMax.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _iAirTemperatureMax.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iTempMax.Name = "iTempMax";
            _iTempMax.Description = "Daily maximum temperature";
            _iTempMax.MaxValue = 50.0;
            _iTempMax.MinValue = -40.0;
            _iTempMax.DefaultValue = -1D;
            _iTempMax.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _iTempMax.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iAirTemperatureMin.Name = "iAirTemperatureMin";
            _iAirTemperatureMin.Description = "Daily minimum temperature";
            _iAirTemperatureMin.MaxValue = 50.0;
            _iAirTemperatureMin.MinValue = -40.0;
            _iAirTemperatureMin.DefaultValue = -1D;
            _iAirTemperatureMin.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _iAirTemperatureMin.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iTempMin.Name = "iTempMin";
            _iTempMin.Description = "Daily minimum temperature";
            _iTempMin.MaxValue = 50.0;
            _iTempMin.MinValue = -40.0;
            _iTempMin.DefaultValue = -1D;
            _iTempMin.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _iTempMin.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iGlobalSolarRadiation.Name = "iGlobalSolarRadiation";
            _iGlobalSolarRadiation.Description = "Solar radiation";
            _iGlobalSolarRadiation.MaxValue = 2000.0;
            _iGlobalSolarRadiation.MinValue = 0.0;
            _iGlobalSolarRadiation.DefaultValue = -1D;
            _iGlobalSolarRadiation.Units = "http://www.wurvoc.org/vocabularies/om-1.8/megajoule_per_square_metre";
            _iGlobalSolarRadiation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iRadiation.Name = "iRadiation";
            _iRadiation.Description = "Solar radiation";
            _iRadiation.MaxValue = 2000.0;
            _iRadiation.MinValue = 0.0;
            _iRadiation.DefaultValue = -1D;
            _iRadiation.Units = "http://www.wurvoc.org/vocabularies/om-1.8/megajoule_per_square_metre";
            _iRadiation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iRAIN.Name = "iRAIN";
            _iRAIN.Description = "Rain amount";
            _iRAIN.MaxValue = 60.0;
            _iRAIN.MinValue = 0.0;
            _iRAIN.DefaultValue = -1D;
            _iRAIN.Units = "http://www.wurvoc.org/vocabularies/om-1.8/millimetre";
            _iRAIN.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iCropResidues.Name = "iCropResidues";
            _iCropResidues.Description = "Crop residues plus above ground biomass";
            _iCropResidues.MaxValue = 20000.0;
            _iCropResidues.MinValue = 0.0;
            _iCropResidues.DefaultValue = -1D;
            _iCropResidues.Units = "http://www.wurvoc.org/vocabularies/om-1.8/gram_per_square_metre";
            _iCropResidues.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iPotentialSoilEvaporation.Name = "iPotentialSoilEvaporation";
            _iPotentialSoilEvaporation.Description = "Potenial Evaporation";
            _iPotentialSoilEvaporation.MaxValue = 12.0;
            _iPotentialSoilEvaporation.MinValue = 0.0;
            _iPotentialSoilEvaporation.DefaultValue = -1D;
            _iPotentialSoilEvaporation.Units = "http://www.wurvoc.org/vocabularies/om-1.8/millimetre";
            _iPotentialSoilEvaporation.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iLeafAreaIndex.Name = "iLeafAreaIndex";
            _iLeafAreaIndex.Description = "Leaf area index";
            _iLeafAreaIndex.MaxValue = 10.0;
            _iLeafAreaIndex.MinValue = 0.0;
            _iLeafAreaIndex.DefaultValue = -1D;
            _iLeafAreaIndex.Units = "http://www.wurvoc.org/vocabularies/om-1.8/square_metre_per_square_metre";
            _iLeafAreaIndex.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _SoilTempArray.Name = "SoilTempArray";
            _SoilTempArray.Description = "Soil Temp array of last day";
            _SoilTempArray.MaxValue = -1D;
            _SoilTempArray.MinValue = -1D;
            _SoilTempArray.DefaultValue = -1D;
            _SoilTempArray.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _SoilTempArray.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _iSoilTempArray.Name = "iSoilTempArray";
            _iSoilTempArray.Description = "Soil Temp array of last day";
            _iSoilTempArray.MaxValue = -1D;
            _iSoilTempArray.MinValue = -1D;
            _iSoilTempArray.DefaultValue = -1D;
            _iSoilTempArray.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _iSoilTempArray.ValueType = VarInfoValueTypes.GetInstanceForName("ArrayDouble");

            _iSoilWaterContent.Name = "iSoilWaterContent";
            _iSoilWaterContent.Description = "Content of water in Soil";
            _iSoilWaterContent.MaxValue = 20.0;
            _iSoilWaterContent.MinValue = 1.5;
            _iSoilWaterContent.DefaultValue = 5.0;
            _iSoilWaterContent.Units = "http://www.wurvoc.org/vocabularies/om-1.8/millimetre";
            _iSoilWaterContent.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _iSoilSurfaceTemperature.Name = "iSoilSurfaceTemperature";
            _iSoilSurfaceTemperature.Description = "Temperature at soil surface";
            _iSoilSurfaceTemperature.MaxValue = 20.0;
            _iSoilSurfaceTemperature.MinValue = 1.5;
            _iSoilSurfaceTemperature.DefaultValue = -1D;
            _iSoilSurfaceTemperature.Units = "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius";
            _iSoilSurfaceTemperature.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}