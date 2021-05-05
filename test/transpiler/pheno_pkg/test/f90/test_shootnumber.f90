!Test generation'

PROGRAM test_test_wheat1_ShootNumber:
    REAL:: canopyShootNumber

    REAL:: leafNumber

    REAL:: sowingDensity

    REAL:: targetFertileShoot

    REAL, ALLOCATABLE, DIMENSION(:):: tilleringProfile

    INTEGER, ALLOCATABLE, DIMENSION(:):: leafTillerNumberArray

    INTEGER:: tillerNumber

    REAL:: averageShootNumberPerPlant

    targetFertileShoot = 600.0

    sowingDensity = 288

    canopyShootNumber = 288.0

    leafNumber = 3.34348137255

    leafTillerNumberArray = [1, 1, 1]

    tilleringProfile = [288.0]

    tillerNumber = 1

    call shootnumber_(canopyShootNumber,leafNumber,sowingDensity,targetFertileShoot,tilleringProfile,leafTillerNumberArray,tillerNumber,averageShootNumberPerPlant)
    print *,averageShootNumberPerPlant,canopyShootNumber,leafTillerNumberArray,tilleringProfile,tillerNumber
 END PROGRAM

