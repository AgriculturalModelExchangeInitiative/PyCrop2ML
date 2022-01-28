def init_ShootNumber(float sowingDensity,
         float targetFertileShoot):
    cdef float canopyShootNumber_t1 
    cdef float leafNumber 
    cdef floatlist tilleringProfile_t1
    cdef intlist leafTillerNumberArray_t1
    cdef int numberTillerCohort_t1 
    cdef float averageShootNumberPerPlant 
    cdef float canopyShootNumber 
    cdef intlist leafTillerNumberArray
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort 
    canopyShootNumber = sowingDensity
    averageShootNumberPerPlant = 1.0
    tilleringProfile.append(sowingDensity)
    numberTillerCohort = 1