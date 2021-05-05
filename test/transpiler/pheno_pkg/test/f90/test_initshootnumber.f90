!Test generation'

PROGRAM test_test_wheat1_initShootNumber:
    REAL:: sowingDensity

    REAL:: averageShootNumberPerPlant

    REAL:: canopyShootNumber

    REAL, ALLOCATABLE, DIMENSION(:):: tilleringProfile

    INTEGER:: tillerNumber

    sowingDensity = 288

    call initshootnumber_(sowingDensity,averageShootNumberPerPlant,canopyShootNumber,tilleringProfile,tillerNumber)
    print *,averageShootNumberPerPlant,canopyShootNumber,tilleringProfile,tillerNumber
 END PROGRAM

