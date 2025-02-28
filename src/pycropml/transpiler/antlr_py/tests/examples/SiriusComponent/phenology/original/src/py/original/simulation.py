from . import PhenologyComponent
import pandas as pd
import os

def simulation(datafile, vardata, params, init):
    rep = os.path.dirname(datafile)
    out = os.path.join(rep, 'output.csv')
    df = pd.read_csv(datafile, sep = ";")

    # inputs values
    t_deltaTT = df[vardata.loc[vardata["Variables"]=="deltaTT","Data columns"].iloc[0]].to_list()
    t_gAI = df[vardata.loc[vardata["Variables"]=="gAI","Data columns"].iloc[0]].to_list()
    t_pAR = df[vardata.loc[vardata["Variables"]=="pAR","Data columns"].iloc[0]].to_list()
    t_cumulTT = df[vardata.loc[vardata["Variables"]=="cumulTT","Data columns"].iloc[0]].to_list()
    t_dayLength = df[vardata.loc[vardata["Variables"]=="dayLength","Data columns"].iloc[0]].to_list()
    t_currentdate = df[vardata.loc[vardata["Variables"]=="currentdate","Data columns"].iloc[0]].to_list()
    t_grainCumulTT = df[vardata.loc[vardata["Variables"]=="grainCumulTT","Data columns"].iloc[0]].to_list()

    #parameters
    tTWindowForPTQ = params.loc[params["name"]=="tTWindowForPTQ", "value"].iloc[0]
    kl = params.loc[params["name"]=="kl", "value"].iloc[0]
    intTvern = params.loc[params["name"]=="intTvern", "value"].iloc[0]
    minTvern = params.loc[params["name"]=="minTvern", "value"].iloc[0]
    vBEE = params.loc[params["name"]=="vBEE", "value"].iloc[0]
    maxDL = params.loc[params["name"]=="maxDL", "value"].iloc[0]
    pNini = params.loc[params["name"]=="pNini", "value"].iloc[0]
    aMXLFNO = params.loc[params["name"]=="aMXLFNO", "value"].iloc[0]
    maxTvern = params.loc[params["name"]=="maxTvern", "value"].iloc[0]
    vAI = params.loc[params["name"]=="vAI", "value"].iloc[0]
    isVernalizable = params.loc[params["name"]=="isVernalizable", "value"].iloc[0]
    minDL = params.loc[params["name"]=="minDL", "value"].iloc[0]
    p = params.loc[params["name"]=="p", "value"].iloc[0]
    sDsa_nh = params.loc[params["name"]=="sDsa_nh", "value"].iloc[0]
    sowingDay = params.loc[params["name"]=="sowingDay", "value"].iloc[0]
    sDsa_sh = params.loc[params["name"]=="sDsa_sh", "value"].iloc[0]
    latitude = params.loc[params["name"]=="latitude", "value"].iloc[0]
    rp = params.loc[params["name"]=="rp", "value"].iloc[0]
    sDws = params.loc[params["name"]=="sDws", "value"].iloc[0]
    ignoreGrainMaturation = params.loc[params["name"]=="ignoreGrainMaturation", "value"].iloc[0]
    sLDL = params.loc[params["name"]=="sLDL", "value"].iloc[0]
    pFLLAnth = params.loc[params["name"]=="pFLLAnth", "value"].iloc[0]
    degfm = params.loc[params["name"]=="degfm", "value"].iloc[0]
    dgf = params.loc[params["name"]=="dgf", "value"].iloc[0]
    choosePhyllUse = params.loc[params["name"]=="choosePhyllUse", "value"].iloc[0]
    dse = params.loc[params["name"]=="dse", "value"].iloc[0]
    pHEADANTH = params.loc[params["name"]=="pHEADANTH", "value"].iloc[0]
    dcd = params.loc[params["name"]=="dcd", "value"].iloc[0]
    sowingDensity = params.loc[params["name"]=="sowingDensity", "value"].iloc[0]
    targetFertileShoot = params.loc[params["name"]=="targetFertileShoot", "value"].iloc[0]
    intTSFLN = params.loc[params["name"]=="intTSFLN", "value"].iloc[0]
    der = params.loc[params["name"]=="der", "value"].iloc[0]
    slopeTSFLN = params.loc[params["name"]=="slopeTSFLN", "value"].iloc[0]
    lNeff = params.loc[params["name"]=="lNeff", "value"].iloc[0]
    B = params.loc[params["name"]=="B", "value"].iloc[0]
    lARmin = params.loc[params["name"]=="lARmin", "value"].iloc[0]
    lincr = params.loc[params["name"]=="lincr", "value"].iloc[0]
    lARmax = params.loc[params["name"]=="lARmax", "value"].iloc[0]
    areaSL = params.loc[params["name"]=="areaSL", "value"].iloc[0]
    pdecr = params.loc[params["name"]=="pdecr", "value"].iloc[0]
    ldecr = params.loc[params["name"]=="ldecr", "value"].iloc[0]
    pTQhf = params.loc[params["name"]=="pTQhf", "value"].iloc[0]
    pincr = params.loc[params["name"]=="pincr", "value"].iloc[0]
    areaSS = params.loc[params["name"]=="areaSS", "value"].iloc[0]

    #initialization
    listTTShootWindowForPTQ1_t1 = init.loc[init["name"]=="listTTShootWindowForPTQ1_t1", "value"].iloc[0]
    pastMaxAI_t1 = init.loc[init["name"]=="pastMaxAI_t1", "value"].iloc[0]
    listGAITTWindowForPTQ_t1 = init.loc[init["name"]=="listGAITTWindowForPTQ_t1", "value"].iloc[0]
    listPARTTWindowForPTQ_t1 = init.loc[init["name"]=="listPARTTWindowForPTQ_t1", "value"].iloc[0]
    listTTShootWindowForPTQ_t1 = init.loc[init["name"]=="listTTShootWindowForPTQ_t1", "value"].iloc[0]
    calendarCumuls_t1 = init.loc[init["name"]=="calendarCumuls_t1", "value"].iloc[0]
    calendarMoments_t1 = init.loc[init["name"]=="calendarMoments_t1", "value"].iloc[0]
    calendarDates_t1 = init.loc[init["name"]=="calendarDates_t1", "value"].iloc[0]
    vernaprog_t1 = init.loc[init["name"]=="vernaprog_t1", "value"].iloc[0]
    leafNumber_t1 = init.loc[init["name"]=="leafNumber_t1", "value"].iloc[0]
    minFinalNumber_t1 = init.loc[init["name"]=="minFinalNumber_t1", "value"].iloc[0]
    hasLastPrimordiumAppeared_t1 = init.loc[init["name"]=="hasLastPrimordiumAppeared_t1", "value"].iloc[0]
    finalLeafNumber_t1 = init.loc[init["name"]=="finalLeafNumber_t1", "value"].iloc[0]
    phase_t1 = init.loc[init["name"]=="phase_t1", "value"].iloc[0]
    phyllochron_t1 = init.loc[init["name"]=="phyllochron_t1", "value"].iloc[0]
    tilleringProfile_t1 = init.loc[init["name"]=="tilleringProfile_t1", "value"].iloc[0]
    leafTillerNumberArray_t1 = init.loc[init["name"]=="leafTillerNumberArray_t1", "value"].iloc[0]
    canopyShootNumber_t1 = init.loc[init["name"]=="canopyShootNumber_t1", "value"].iloc[0]
    hasFlagLeafLiguleAppeared_t1 = init.loc[init["name"]=="hasFlagLeafLiguleAppeared_t1", "value"].iloc[0]
    currentZadokStage_t1 = init.loc[init["name"]=="currentZadokStage_t1", "value"].iloc[0]

    #outputs
    output_names = ["listGAITTWindowForPTQ","pastMaxAI","listTTShootWindowForPTQ1","gAImean","listTTShootWindowForPTQ","listPARTTWindowForPTQ","ptq","cumulTTFromZC_65","cumulTTFromZC_91","cumulTTFromZC_39","isMomentRegistredZC_39","minFinalNumber","calendarCumuls","vernaprog","calendarMoments","calendarDates","fixPhyll","phase","hasLastPrimordiumAppeared","finalLeafNumber","leafNumber","averageShootNumberPerPlant","leafTillerNumberArray","canopyShootNumber","numberTillerCohort","tilleringProfile","hasFlagLeafLiguleAppeared","currentZadokStage","hasZadokStageChanged","phyllochron"]

    df_out = pd.DataFrame(columns = output_names)
    for i in range(0,len(df.index)-1):
        deltaTT = t_deltaTT[i]
        gAI = t_gAI[i]
        pAR = t_pAR[i]
        cumulTT = t_cumulTT[i]
        dayLength = t_dayLength[i]
        currentdate = t_currentdate[i]
        grainCumulTT = t_grainCumulTT[i]
        listGAITTWindowForPTQ,pastMaxAI,listTTShootWindowForPTQ1,gAImean,listTTShootWindowForPTQ,listPARTTWindowForPTQ,ptq,cumulTTFromZC_65,cumulTTFromZC_91,cumulTTFromZC_39,isMomentRegistredZC_39,minFinalNumber,calendarCumuls,vernaprog,calendarMoments,calendarDates,fixPhyll,phase,hasLastPrimordiumAppeared,finalLeafNumber,leafNumber,averageShootNumberPerPlant,leafTillerNumberArray,canopyShootNumber,numberTillerCohort,tilleringProfile,hasFlagLeafLiguleAppeared,currentZadokStage,hasZadokStageChanged,phyllochron= PhenologyComponent.model_phenology(deltaTT,gAI,tTWindowForPTQ,listTTShootWindowForPTQ1_t1,pastMaxAI_t1,listGAITTWindowForPTQ_t1,listPARTTWindowForPTQ_t1,pAR,listTTShootWindowForPTQ_t1,kl,cumulTT,calendarCumuls_t1,calendarMoments_t1,intTvern,minTvern,vBEE,calendarDates_t1,maxDL,pNini,dayLength,vernaprog_t1,aMXLFNO,maxTvern,vAI,leafNumber_t1,isVernalizable,minDL,minFinalNumber_t1,currentdate,p,sDsa_nh,sowingDay,sDsa_sh,latitude,rp,sDws,hasLastPrimordiumAppeared_t1,ignoreGrainMaturation,grainCumulTT,sLDL,pFLLAnth,finalLeafNumber_t1,degfm,phase_t1,dgf,choosePhyllUse,dse,pHEADANTH,dcd,phyllochron_t1,tilleringProfile_t1,sowingDensity,leafTillerNumberArray_t1,targetFertileShoot,canopyShootNumber_t1,hasFlagLeafLiguleAppeared_t1,intTSFLN,der,slopeTSFLN,currentZadokStage_t1,lNeff,B,lARmin,lincr,lARmax,areaSL,pdecr,ldecr,pTQhf,pincr,areaSS)

        listTTShootWindowForPTQ1_t1 = listTTShootWindowForPTQ1
        pastMaxAI_t1 = pastMaxAI
        listGAITTWindowForPTQ_t1 = listGAITTWindowForPTQ
        listPARTTWindowForPTQ_t1 = listPARTTWindowForPTQ
        listTTShootWindowForPTQ_t1 = listTTShootWindowForPTQ
        calendarCumuls_t1 = calendarCumuls
        calendarMoments_t1 = calendarMoments
        calendarDates_t1 = calendarDates
        vernaprog_t1 = vernaprog
        leafNumber_t1 = leafNumber
        minFinalNumber_t1 = minFinalNumber
        hasLastPrimordiumAppeared_t1 = hasLastPrimordiumAppeared
        finalLeafNumber_t1 = finalLeafNumber
        phase_t1 = phase
        phyllochron_t1 = phyllochron
        tilleringProfile_t1 = tilleringProfile
        leafTillerNumberArray_t1 = leafTillerNumberArray
        canopyShootNumber_t1 = canopyShootNumber
        hasFlagLeafLiguleAppeared_t1 = hasFlagLeafLiguleAppeared
        currentZadokStage_t1 = currentZadokStage
        df_out.loc[i] = [listGAITTWindowForPTQ,pastMaxAI,listTTShootWindowForPTQ1,gAImean,listTTShootWindowForPTQ,listPARTTWindowForPTQ,ptq,cumulTTFromZC_65,cumulTTFromZC_91,cumulTTFromZC_39,isMomentRegistredZC_39,minFinalNumber,calendarCumuls,vernaprog,calendarMoments,calendarDates,fixPhyll,phase,hasLastPrimordiumAppeared,finalLeafNumber,leafNumber,averageShootNumberPerPlant,leafTillerNumberArray,canopyShootNumber,numberTillerCohort,tilleringProfile,hasFlagLeafLiguleAppeared,currentZadokStage,hasZadokStageChanged,phyllochron]
    df_out.insert(0, 'date', pd.to_datetime(df.year*10000 + df.month*100 + df.day, format='%Y%m%d'), True)
    df_out.set_index("date", inplace=True)
    df_out.to_csv(out, sep=";")
    return df_out