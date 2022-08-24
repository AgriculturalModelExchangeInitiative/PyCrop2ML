using System;
using CRA.AgroManagement;
using CRA.ModelLayer.Strategy;
namespace SiriusQualitySoilTemp.DomainClass
{
    public interface IStrategySiriusQualitySoilTemp : IStrategy
    {
        void Estimate( SoilTempState s, SoilTempState s1, SoilTempRate r, SoilTempAuxiliary a, SoilTempExogenous ex);

        string TestPreConditions( SoilTempState s, SoilTempState s1, SoilTempRate r, SoilTempAuxiliary a, SoilTempExogenous ex, string callID);

        string TestPostConditions( SoilTempState s, SoilTempState s1, SoilTempRate r, SoilTempAuxiliary a, SoilTempExogenous ex, string callID);

        void SetParametersDefaultValue();
    }
}