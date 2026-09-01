using System;
using CRA.AgroManagement;
using CRA.ModelLayer.Strategy;
namespace SiriusQualitySoilTemperatureComp.DomainClass
{
    public interface IStrategySiriusQualitySoilTemperatureComp : IStrategy
    {
        void Estimate( SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a, SoilTemperatureCompExogenous ex);

        string TestPreConditions( SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a, SoilTemperatureCompExogenous ex, string callID);

        string TestPostConditions( SoilTemperatureCompState s, SoilTemperatureCompState s1, SoilTemperatureCompRate r, SoilTemperatureCompAuxiliary a, SoilTemperatureCompExogenous ex, string callID);

        void SetParametersDefaultValue();
    }
}