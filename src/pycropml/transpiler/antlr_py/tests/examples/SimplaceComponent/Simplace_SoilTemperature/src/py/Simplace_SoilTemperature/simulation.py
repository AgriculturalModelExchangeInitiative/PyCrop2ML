from . import SoilTemperatureComponent
import pandas as pd
import os

def simulation(datafile, vardata, params, init):
    rep = os.path.dirname(datafile)
    out = os.path.join(rep, 'output.csv')
    df = pd.read_csv(datafile, sep = ";")

    # inputs values
    t_iAirTemperatureMax = df[vardata.loc[vardata["Variables"]=="iAirTemperatureMax","Data columns"].iloc[0]].to_list()
    t_iAirTemperatureMin = df[vardata.loc[vardata["Variables"]=="iAirTemperatureMin","Data columns"].iloc[0]].to_list()
    t_iGlobalSolarRadiation = df[vardata.loc[vardata["Variables"]=="iGlobalSolarRadiation","Data columns"].iloc[0]].to_list()
    t_iRAIN = df[vardata.loc[vardata["Variables"]=="iRAIN","Data columns"].iloc[0]].to_list()
    t_iCropResidues = df[vardata.loc[vardata["Variables"]=="iCropResidues","Data columns"].iloc[0]].to_list()
    t_iPotentialSoilEvaporation = df[vardata.loc[vardata["Variables"]=="iPotentialSoilEvaporation","Data columns"].iloc[0]].to_list()
    t_iLeafAreaIndex = df[vardata.loc[vardata["Variables"]=="iLeafAreaIndex","Data columns"].iloc[0]].to_list()
    t_SoilTempArray = df[vardata.loc[vardata["Variables"]=="SoilTempArray","Data columns"].iloc[0]].to_list()
    t_iSoilWaterContent = df[vardata.loc[vardata["Variables"]=="iSoilWaterContent","Data columns"].iloc[0]].to_list()
    t_Albedo = df[vardata.loc[vardata["Variables"]=="Albedo","Data columns"].iloc[0]].to_list()
    t_SnowWaterContent = df[vardata.loc[vardata["Variables"]=="SnowWaterContent","Data columns"].iloc[0]].to_list()
    t_SoilSurfaceTemperature = df[vardata.loc[vardata["Variables"]=="SoilSurfaceTemperature","Data columns"].iloc[0]].to_list()
    t_AgeOfSnow = df[vardata.loc[vardata["Variables"]=="AgeOfSnow","Data columns"].iloc[0]].to_list()
    t_pSoilLayerDepth = df[vardata.loc[vardata["Variables"]=="pSoilLayerDepth","Data columns"].iloc[0]].to_list()

    #parameters
    cCarbonContent = params.loc[params["name"]=="cCarbonContent", "value"].iloc[0]
    cSoilLayerDepth = params.loc[params["name"]=="cSoilLayerDepth", "value"].iloc[0]
    cFirstDayMeanTemp = params.loc[params["name"]=="cFirstDayMeanTemp", "value"].iloc[0]
    cAverageGroundTemperature = params.loc[params["name"]=="cAverageGroundTemperature", "value"].iloc[0]
    cAverageBulkDensity = params.loc[params["name"]=="cAverageBulkDensity", "value"].iloc[0]
    cDampingDepth = params.loc[params["name"]=="cDampingDepth", "value"].iloc[0]

    #initialization

    #outputs
    output_names = ["SoilSurfaceTemperature","SnowIsolationIndex","SnowWaterContent","SoilTempArray","AgeOfSnow"]

    df_out = pd.DataFrame(columns = output_names)
    for i in range(0,len(df.index)-1):
        iAirTemperatureMax = t_iAirTemperatureMax[i]
        iAirTemperatureMin = t_iAirTemperatureMin[i]
        iGlobalSolarRadiation = t_iGlobalSolarRadiation[i]
        iRAIN = t_iRAIN[i]
        iCropResidues = t_iCropResidues[i]
        iPotentialSoilEvaporation = t_iPotentialSoilEvaporation[i]
        iLeafAreaIndex = t_iLeafAreaIndex[i]
        SoilTempArray = t_SoilTempArray[i]
        iSoilWaterContent = t_iSoilWaterContent[i]
        Albedo = t_Albedo[i]
        SnowWaterContent = t_SnowWaterContent[i]
        SoilSurfaceTemperature = t_SoilSurfaceTemperature[i]
        AgeOfSnow = t_AgeOfSnow[i]
        pSoilLayerDepth = t_pSoilLayerDepth[i]
        SoilSurfaceTemperature,SnowIsolationIndex,SnowWaterContent,SoilTempArray,AgeOfSnow= SoilTemperatureComponent.model_soiltemperature(cCarbonContent,iAirTemperatureMax,iAirTemperatureMin,iGlobalSolarRadiation,iRAIN,iCropResidues,iPotentialSoilEvaporation,iLeafAreaIndex,SoilTempArray,cSoilLayerDepth,cFirstDayMeanTemp,cAverageGroundTemperature,cAverageBulkDensity,cDampingDepth,iSoilWaterContent,Albedo,SnowWaterContent,SoilSurfaceTemperature,AgeOfSnow,pSoilLayerDepth)

        df_out.loc[i] = [SoilSurfaceTemperature,SnowIsolationIndex,SnowWaterContent,SoilTempArray,AgeOfSnow]
    df_out.insert(0, 'date', pd.to_datetime(df.year*10000 + df.month*100 + df.day, format='%Y%m%d'), True)
    df_out.set_index("date", inplace=True)
    df_out.to_csv(out, sep=";")
    return df_out