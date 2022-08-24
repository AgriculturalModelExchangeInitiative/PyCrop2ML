using System;
using CRA.AgroManagement;
using CRA.ModelLayer.Strategy;
namespace SiriusQualityEnergyBalance.DomainClass
{
    public interface IStrategySiriusQualityEnergyBalance : IStrategy
    {
        void Estimate( EnergyBalanceState s, EnergyBalanceState s1, EnergyBalanceRate r, EnergyBalanceAuxiliary a, EnergyBalanceExogenous ex);

        string TestPreConditions( EnergyBalanceState s, EnergyBalanceState s1, EnergyBalanceRate r, EnergyBalanceAuxiliary a, EnergyBalanceExogenous ex, string callID);

        string TestPostConditions( EnergyBalanceState s, EnergyBalanceState s1, EnergyBalanceRate r, EnergyBalanceAuxiliary a, EnergyBalanceExogenous ex, string callID);

        void SetParametersDefaultValue();
    }
}