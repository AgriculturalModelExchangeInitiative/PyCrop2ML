using System;
using CRA.AgroManagement;
using CRA.ModelLayer.Strategy;
namespace SoilTemperature.DomainClass
{
    public interface IStrategySoilTemperature : IStrategy
    {
        void Estimate( SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex);

        string TestPreConditions( SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex, string callID);

        string TestPostConditions( SoilTemperatureState s, SoilTemperatureState s1, SoilTemperatureRate r, SoilTemperatureAuxiliary a, SoilTemperatureExogenous ex, string callID);

        void SetParametersDefaultValue();
    }
}