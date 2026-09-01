# corrected for very low radiation in winter
cdef float shadingCoefficient
globrad = max(8.33, globrad)
shadingCoefficient = 0.1 + ((soilCoverage * dampingFactor) + ((1 - soilCoverage) * (1 - dampingFactor)))

# Soil surface temperature calculation following Williams 1984
soilSurfaceTemperature = \
    (1.0 - shadingCoefficient) \
    * (tmin + ((tmax - tmin) * pow((0.03 * globrad), 0.5))) \
    + shadingCoefficient * soilSurfaceTemperature

# damping negative temperatures due to heat loss for freezing water
if soilSurfaceTemperature < 0.0:
    soilSurfaceTemperature = soilSurfaceTemperature * 0.5
