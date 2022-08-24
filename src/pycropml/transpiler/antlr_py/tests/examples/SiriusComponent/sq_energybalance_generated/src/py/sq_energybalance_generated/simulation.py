from . import EnergyBalanceComponent
import pandas as pd
import os

def simulation(datafile, vardata, params, init):
    rep = os.path.dirname(datafile)
    out = os.path.join(rep, 'output.csv')
    df = pd.read_csv(datafile, sep = ";")

    # inputs values
    t_vaporPressure = df[vardata.loc[vardata["Variables"]=="vaporPressure","Data columns"].iloc[0]].to_list()
    t_extraSolarRadiation = df[vardata.loc[vardata["Variables"]=="extraSolarRadiation","Data columns"].iloc[0]].to_list()
    t_solarRadiation = df[vardata.loc[vardata["Variables"]=="solarRadiation","Data columns"].iloc[0]].to_list()
    t_minTair = df[vardata.loc[vardata["Variables"]=="minTair","Data columns"].iloc[0]].to_list()
    t_maxTair = df[vardata.loc[vardata["Variables"]=="maxTair","Data columns"].iloc[0]].to_list()
    t_plantHeight = df[vardata.loc[vardata["Variables"]=="plantHeight","Data columns"].iloc[0]].to_list()
    t_wind = df[vardata.loc[vardata["Variables"]=="wind","Data columns"].iloc[0]].to_list()
    t_deficitOnTopLayers = df[vardata.loc[vardata["Variables"]=="deficitOnTopLayers","Data columns"].iloc[0]].to_list()
    t_hslope = df[vardata.loc[vardata["Variables"]=="hslope","Data columns"].iloc[0]].to_list()
    t_VPDair = df[vardata.loc[vardata["Variables"]=="VPDair","Data columns"].iloc[0]].to_list()

    #parameters
    albedoCoefficient = params.loc[params["name"]=="albedoCoefficient", "value"].iloc[0]
    stefanBoltzman = params.loc[params["name"]=="stefanBoltzman", "value"].iloc[0]
    elevation = params.loc[params["name"]=="elevation", "value"].iloc[0]
    vonKarman = params.loc[params["name"]=="vonKarman", "value"].iloc[0]
    d = params.loc[params["name"]=="d", "value"].iloc[0]
    zm = params.loc[params["name"]=="zm", "value"].iloc[0]
    heightWeatherMeasurements = params.loc[params["name"]=="heightWeatherMeasurements", "value"].iloc[0]
    zh = params.loc[params["name"]=="zh", "value"].iloc[0]
    soilDiffusionConstant = params.loc[params["name"]=="soilDiffusionConstant", "value"].iloc[0]
    lambdaV = params.loc[params["name"]=="lambdaV", "value"].iloc[0]
    psychrometricConstant = params.loc[params["name"]=="psychrometricConstant", "value"].iloc[0]
    Alpha = params.loc[params["name"]=="Alpha", "value"].iloc[0]
    tau = params.loc[params["name"]=="tau", "value"].iloc[0]
    tauAlpha = params.loc[params["name"]=="tauAlpha", "value"].iloc[0]
    rhoDensityAir = params.loc[params["name"]=="rhoDensityAir", "value"].iloc[0]
    specificHeatCapacityAir = params.loc[params["name"]=="specificHeatCapacityAir", "value"].iloc[0]
    isWindVpDefined = params.loc[params["name"]=="isWindVpDefined", "value"].iloc[0]

    #initialization

    #outputs
    output_names = ["netRadiation","netOutGoingLongWaveRadiation","conductance","diffusionLimitedEvaporation","netRadiationEquivalentEvaporation","evapoTranspirationPriestlyTaylor","energyLimitedEvaporation","evapoTranspirationPenman","soilEvaporation","evapoTranspiration","soilHeatFlux","potentialTranspiration","cropHeatFlux","minCanopyTemperature","maxCanopyTemperature"]

    df_out = pd.DataFrame(columns = output_names)
    for i in range(0,len(df.index)-1):
        vaporPressure = t_vaporPressure[i]
        extraSolarRadiation = t_extraSolarRadiation[i]
        solarRadiation = t_solarRadiation[i]
        minTair = t_minTair[i]
        maxTair = t_maxTair[i]
        plantHeight = t_plantHeight[i]
        wind = t_wind[i]
        deficitOnTopLayers = t_deficitOnTopLayers[i]
        hslope = t_hslope[i]
        VPDair = t_VPDair[i]
        netRadiation,netOutGoingLongWaveRadiation,conductance,diffusionLimitedEvaporation,netRadiationEquivalentEvaporation,evapoTranspirationPriestlyTaylor,energyLimitedEvaporation,evapoTranspirationPenman,soilEvaporation,evapoTranspiration,soilHeatFlux,potentialTranspiration,cropHeatFlux,minCanopyTemperature,maxCanopyTemperature= EnergyBalanceComponent.model_energybalance(albedoCoefficient,vaporPressure,stefanBoltzman,extraSolarRadiation,solarRadiation,minTair,elevation,maxTair,plantHeight,vonKarman,d,zm,wind,heightWeatherMeasurements,zh,deficitOnTopLayers,soilDiffusionConstant,lambdaV,hslope,psychrometricConstant,Alpha,tau,tauAlpha,VPDair,rhoDensityAir,specificHeatCapacityAir,isWindVpDefined)

        df_out.loc[i] = [netRadiation,netOutGoingLongWaveRadiation,conductance,diffusionLimitedEvaporation,netRadiationEquivalentEvaporation,evapoTranspirationPriestlyTaylor,energyLimitedEvaporation,evapoTranspirationPenman,soilEvaporation,evapoTranspiration,soilHeatFlux,potentialTranspiration,cropHeatFlux,minCanopyTemperature,maxCanopyTemperature]
    df_out.insert(0, 'date', pd.to_datetime(df.year*10000 + df.month*100 + df.day, format='%Y%m%d'), True)
    df_out.set_index("date", inplace=True)
    df_out.to_csv(out, sep=";")
    return df_out