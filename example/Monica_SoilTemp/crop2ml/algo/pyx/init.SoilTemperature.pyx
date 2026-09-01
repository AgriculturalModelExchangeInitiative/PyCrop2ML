# initialize the two additional layers to the same values 
# as the bottom most standard soil layer
# even though this hadn't been done before it was ok, 
# as these two layers seam to be used only for 
# calculating heat capacity and conductivity, the layer sizes are set
# manually below, nevertheless initializing them to some sensible values
# shouldn't hurt
#if(!_soilColumn.empty()) _soilColumnGroundLayer = _soilColumnBottomLayer = _soilColumn.back();

#double baseTemp = _params.pt_BaseTemperature;  // temperature for lowest layer (avg yearly air temp)
#double initialSurfaceTemp = _params.pt_InitialSurfaceTemperature; // Replace by Mean air temperature

cdef int groundLayer 
cdef int bottomLayer 
cdef float lti_1, lti
cdef float ts, dw, cw, dq, cq, da, ca, dh, ch,sbdi, smi, sati, somi
cdef float hci_1, hci

# Initialising the soil properties
cdef int i
for i in range(noOfSoilLayers):
    # Initialising the soil temperature
    soilTemperature[i] = ((1.0 - (float(i) / noOfSoilLayers)) * initialSurfaceTemp) \
        + ((float(i) / noOfSoilLayers) * baseTemp)


# Determination of the geometry parameters for soil temperature calculation
# with Cholesky-Method

groundLayer = noOfTempLayers - 2
bottomLayer = noOfTempLayers - 1
layerThickness[groundLayer] = 2.0 * layerThickness[groundLayer - 1]
layerThickness[bottomLayer] = 1.0
soilTemperature[groundLayer] = (soilTemperature[groundLayer - 1] + baseTemp) * 0.5
soilTemperature[bottomLayer] = baseTemp

V[0] = layerThickness[0]
B[0] = 2.0 / layerThickness[0]
for i in range(1, noOfTempLayers):
    lti_1 = layerThickness[i-1] # [m]
    lti = layerThickness[i] # [m]
    B[i] = 2.0 / (lti + lti_1) # [m]
    V[i] = lti * nTau # [m3]
# End determination of the geometry parameters for soil temperature calculation


ts = timeStep  
dw = densityWater # [kg m-3]
cw = specificHeatCapacityWater # [J kg-1 K-1]
dq = quartzRawDensity
cq = specificHeatCapacityQuartz # [J kg-1 K-1]

da = densityAir # [kg m-3]
ca = specificHeatCapacityAir # [J kg-1 K-1]
dh = densityHumus # [kg m-3]
ch = specificHeatCapacityHumus # [J kg-1 K-1]

# initializing heat state variables
# iterates only over the standard soil number of layers, the other two layers
# will be assigned below that loop

for i in range(noOfSoilLayers):
    #######################################################################################
    # Calculate heat conductivity following Neusypina 1979
    # Neusypina, T.A. (1979): Rascet teplovo rezima pocvi v modeli formirovanija urozaja.
    # Teoreticeskij osnovy i kolicestvennye metody programmirovanija urozaev. Leningrad,
    # 53 -62.
    # Note: in this original publication lambda is calculated in cal cm-1 s-1 K-1!
    #######################################################################################
    sbdi = soilBulkDensity[i]
    smi = soilMoistureConst[i]
    heatConductivity[i] = \
        ((3.0 * (sbdi / 1000.0) - 1.7) * 0.001) \
        / (1.0 + (11.5 - 5.0 * (sbdi / 1000.0)) \
                * exp((-50.0) * pow((smi / (sbdi / 1000.0)), 1.5))) \
        * 86400.0 \
        * ts * 100.0 * 4.184 # gives result in [days] -> [m] -> [J] -> [J m-1 d-1 K-1]

    ####################################################################################
    # Calculate specific heat capacity following DAISY
    # Abrahamsen, P, and S. Hansen (2000): DAISY - An open soil-crop-atmosphere model
    # system. Environmental Modelling and Software 15, 313-330
    ####################################################################################
    sati = saturation[i]
    somi = soilOrganicMatter[i] / da * sbdi #  Converting [kg kg-1] to [m3 m-3]
    heatCapacity[i] = \
        (smi * dw * cw) \
        + ((sati - smi) * da * ca) \
        + (somi * dh * ch) \
        + ((1.0 - sati - somi) * dq * cq)
        # --> [J m-3 K-1]

heatCapacity[groundLayer] = heatCapacity[groundLayer - 1]
heatCapacity[bottomLayer] = heatCapacity[groundLayer]
heatConductivity[groundLayer] = heatConductivity[groundLayer - 1]
heatConductivity[bottomLayer] = heatConductivity[groundLayer]

# Initialisation soil surface temperature
soilSurfaceTemperature = initialSurfaceTemp

##################################################################
# Initialising Numerical Solution
# Suckow,F. (1985): A model serving the calculation of soil
# temperatures. Zeitschrift für Meteorologie 35 (1), 66 -70.
##################################################################

# Calculation of the mean heat conductivity per layer
heatConductivityMean[0] = heatConductivity[0]
 
for i in range(1, noOfTempLayers):
    lti_1 = layerThickness[i - 1]
    lti = layerThickness[i]
    hci_1 = heatConductivity[i - 1]
    hci = heatConductivity[i]

    # @todo Claas: check formula
    heatConductivityMean[i] = ((lti_1 * hci_1) + (lti * hci)) / (lti + lti_1)

# Determination of the volume matrix
for i in range(noOfTempLayers):
    volumeMatrix[i] = V[i] * heatCapacity[i] # [J K-1]

    # If initial entry, rearrengement of volume matrix
    volumeMatrixOld[i] = volumeMatrix[i]

    # Determination of the matrix secondary diagonal
    matrixSecondaryDiagonal[i] = -B[i] * heatConductivityMean[i] # [J K-1]

matrixSecondaryDiagonal[bottomLayer + 1] = 0.0

# Determination of the matrix primary diagonal
for i in range(noOfTempLayers):
    matrixPrimaryDiagonal[i] = volumeMatrix[i] \
        - matrixSecondaryDiagonal[i] - matrixSecondaryDiagonal[i + 1] # [J K-1]


