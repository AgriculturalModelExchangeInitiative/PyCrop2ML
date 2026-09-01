from . import SoilTemperatureCompComponent
import pandas as pd
import os

def simulation(datafile, vardata, params, init):
    rep = os.path.dirname(datafile)
    out = os.path.join(rep, 'output.csv')
    df = pd.read_csv(datafile, sep = ";")

    # inputs values
    t_tmin = df[vardata.loc[vardata["Variables"]=="tmin","Data columns"].iloc[0]].to_list()
    t_tmax = df[vardata.loc[vardata["Variables"]=="tmax","Data columns"].iloc[0]].to_list()
    t_globrad = df[vardata.loc[vardata["Variables"]=="globrad","Data columns"].iloc[0]].to_list()
    t_soilCoverage = df[vardata.loc[vardata["Variables"]=="soilCoverage","Data columns"].iloc[0]].to_list()
    t_soilSurfaceTemperatureBelowSnow = df[vardata.loc[vardata["Variables"]=="soilSurfaceTemperatureBelowSnow","Data columns"].iloc[0]].to_list()
    t_hasSnowCover = df[vardata.loc[vardata["Variables"]=="hasSnowCover","Data columns"].iloc[0]].to_list()
    t_V = df[vardata.loc[vardata["Variables"]=="V","Data columns"].iloc[0]].to_list()
    t_B = df[vardata.loc[vardata["Variables"]=="B","Data columns"].iloc[0]].to_list()
    t_volumeMatrix = df[vardata.loc[vardata["Variables"]=="volumeMatrix","Data columns"].iloc[0]].to_list()
    t_volumeMatrixOld = df[vardata.loc[vardata["Variables"]=="volumeMatrixOld","Data columns"].iloc[0]].to_list()
    t_matrixPrimaryDiagonal = df[vardata.loc[vardata["Variables"]=="matrixPrimaryDiagonal","Data columns"].iloc[0]].to_list()
    t_matrixSecondaryDiagonal = df[vardata.loc[vardata["Variables"]=="matrixSecondaryDiagonal","Data columns"].iloc[0]].to_list()
    t_heatConductivity = df[vardata.loc[vardata["Variables"]=="heatConductivity","Data columns"].iloc[0]].to_list()
    t_heatConductivityMean = df[vardata.loc[vardata["Variables"]=="heatConductivityMean","Data columns"].iloc[0]].to_list()
    t_heatCapacity = df[vardata.loc[vardata["Variables"]=="heatCapacity","Data columns"].iloc[0]].to_list()
    t_solution = df[vardata.loc[vardata["Variables"]=="solution","Data columns"].iloc[0]].to_list()
    t_matrixDiagonal = df[vardata.loc[vardata["Variables"]=="matrixDiagonal","Data columns"].iloc[0]].to_list()
    t_matrixLowerTriangle = df[vardata.loc[vardata["Variables"]=="matrixLowerTriangle","Data columns"].iloc[0]].to_list()
    t_heatFlow = df[vardata.loc[vardata["Variables"]=="heatFlow","Data columns"].iloc[0]].to_list()

    #parameters
    dampingFactor = params.loc[params["name"]=="dampingFactor", "value"].iloc[0]
    timeStep = params.loc[params["name"]=="timeStep", "value"].iloc[0]
    soilMoistureConst = params.loc[params["name"]=="soilMoistureConst", "value"].iloc[0]
    baseTemp = params.loc[params["name"]=="baseTemp", "value"].iloc[0]
    initialSurfaceTemp = params.loc[params["name"]=="initialSurfaceTemp", "value"].iloc[0]
    densityAir = params.loc[params["name"]=="densityAir", "value"].iloc[0]
    specificHeatCapacityAir = params.loc[params["name"]=="specificHeatCapacityAir", "value"].iloc[0]
    densityHumus = params.loc[params["name"]=="densityHumus", "value"].iloc[0]
    specificHeatCapacityHumus = params.loc[params["name"]=="specificHeatCapacityHumus", "value"].iloc[0]
    densityWater = params.loc[params["name"]=="densityWater", "value"].iloc[0]
    specificHeatCapacityWater = params.loc[params["name"]=="specificHeatCapacityWater", "value"].iloc[0]
    quartzRawDensity = params.loc[params["name"]=="quartzRawDensity", "value"].iloc[0]
    specificHeatCapacityQuartz = params.loc[params["name"]=="specificHeatCapacityQuartz", "value"].iloc[0]
    nTau = params.loc[params["name"]=="nTau", "value"].iloc[0]
    noOfTempLayers = params.loc[params["name"]=="noOfTempLayers", "value"].iloc[0]
    noOfTempLayersPlus1 = params.loc[params["name"]=="noOfTempLayersPlus1", "value"].iloc[0]
    noOfSoilLayers = params.loc[params["name"]=="noOfSoilLayers", "value"].iloc[0]
    layerThickness = params.loc[params["name"]=="layerThickness", "value"].iloc[0]
    soilBulkDensity = params.loc[params["name"]=="soilBulkDensity", "value"].iloc[0]
    saturation = params.loc[params["name"]=="saturation", "value"].iloc[0]
    soilOrganicMatter = params.loc[params["name"]=="soilOrganicMatter", "value"].iloc[0]

    #initialization

    #outputs
    output_names = ["soilSurfaceTemperature","soilTemperature"]

    df_out = pd.DataFrame(columns = output_names)
    for i in range(0,len(df.index)-1):
        tmin = t_tmin[i]
        tmax = t_tmax[i]
        globrad = t_globrad[i]
        soilCoverage = t_soilCoverage[i]
        soilSurfaceTemperatureBelowSnow = t_soilSurfaceTemperatureBelowSnow[i]
        hasSnowCover = t_hasSnowCover[i]
        V = t_V[i]
        B = t_B[i]
        volumeMatrix = t_volumeMatrix[i]
        volumeMatrixOld = t_volumeMatrixOld[i]
        matrixPrimaryDiagonal = t_matrixPrimaryDiagonal[i]
        matrixSecondaryDiagonal = t_matrixSecondaryDiagonal[i]
        heatConductivity = t_heatConductivity[i]
        heatConductivityMean = t_heatConductivityMean[i]
        heatCapacity = t_heatCapacity[i]
        solution = t_solution[i]
        matrixDiagonal = t_matrixDiagonal[i]
        matrixLowerTriangle = t_matrixLowerTriangle[i]
        heatFlow = t_heatFlow[i]
        soilSurfaceTemperature,soilTemperature= SoilTemperatureCompComponent.model_soiltemperaturecomp(tmin,tmax,globrad,dampingFactor,soilCoverage,soilSurfaceTemperatureBelowSnow,hasSnowCover,timeStep,soilMoistureConst,baseTemp,initialSurfaceTemp,densityAir,specificHeatCapacityAir,densityHumus,specificHeatCapacityHumus,densityWater,specificHeatCapacityWater,quartzRawDensity,specificHeatCapacityQuartz,nTau,noOfTempLayers,noOfTempLayersPlus1,noOfSoilLayers,layerThickness,soilBulkDensity,saturation,soilOrganicMatter,V,B,volumeMatrix,volumeMatrixOld,matrixPrimaryDiagonal,matrixSecondaryDiagonal,heatConductivity,heatConductivityMean,heatCapacity,solution,matrixDiagonal,matrixLowerTriangle,heatFlow)

        df_out.loc[i] = [soilSurfaceTemperature,soilTemperature]
    df_out.insert(0, 'date', pd.to_datetime(df.year*10000 + df.month*100 + df.day, format='%Y%m%d'), True)
    df_out.set_index("date", inplace=True)
    df_out.to_csv(out, sep=";")
    return df_out