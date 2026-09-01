cdef int groundLayer
cdef int bottomLayer
cdef int i
cdef int j, j_1

groundLayer = noOfTempLayers - 2
bottomLayer = noOfTempLayers - 1

##############################################################
# Internal Subroutine Numerical Solution - Suckow,F. (1986)
##############################################################
#soilSurfaceTemperature = calcSoilSurfaceTemperature(prevDaySoilSurfaceTemperature, tmin, tmax, globrad)
heatFlow[0] = soilSurfaceTemperature * B[0] * heatConductivityMean[0] # [J]
#assert _heatFlow[i>0] == 0.0;


for i in range(noOfTempLayers):
    solution[i] = (volumeMatrixOld[i] + (volumeMatrix[i] - volumeMatrixOld[i]) / layerThickness[i]) \
                  * soilTemperature[i] + heatFlow[i]
# end subroutine NumericalSolution

########################################################
# Internal Subroutine Cholesky Solution Method
#
# Solution of EX=Z with E tridiagonal and symmetric
# according to CHOLESKY (E=LDL')
########################################################

# Determination of the lower matrix triangle L and the diagonal matrix D
matrixDiagonal[0] = matrixPrimaryDiagonal[0]
for i in range(1, noOfTempLayers):
    matrixLowerTriangle[i] = matrixSecondaryDiagonal[i] / matrixDiagonal[i - 1]
    matrixDiagonal[i] = matrixPrimaryDiagonal[i] - (matrixLowerTriangle[i] * matrixSecondaryDiagonal[i])

# Solution of LY=Z
for i in range(1, noOfTempLayers):
    solution[i] = solution[i] - (matrixLowerTriangle[i] * solution[i - 1])

# Solution of L'X=D(-1)Y
solution[bottomLayer] = solution[bottomLayer] / matrixDiagonal[bottomLayer]

for i in range(bottomLayer):
    j = (bottomLayer - 1) - i
    j_1 = j + 1
    solution[j] = (solution[j] / matrixDiagonal[j]) - (matrixLowerTriangle[j_1] * solution[j_1])
# end subroutine CholeskyMethod

# Internal Subroutine Rearrangement
for i in range(noOfTempLayers):
    soilTemperature[i] = solution[i]

for i in range(noOfSoilLayers):
    volumeMatrixOld[i] = volumeMatrix[i]
    #newSoilTemperature[i] = soilTemperature[i]

volumeMatrixOld[groundLayer] = volumeMatrix[groundLayer]
volumeMatrixOld[bottomLayer] = volumeMatrix[bottomLayer]
