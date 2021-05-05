!Test generation'

PROGRAM test_test_wheat1_PhylSowingDateCorrection:
    INTEGER:: sowingDay

    REAL:: latitude

    INTEGER:: sDsa_sh

    REAL:: rp

    INTEGER:: sDws

    INTEGER:: sDsa_nh

    REAL:: p

    REAL:: fixPhyll

    sowingDay = 80

    latitude = 33.069

    sDsa_sh = 151

    rp = 0.003

    sDws = 90

    sDsa_nh = 200

    p = 120

    call phylsowingdatecorrection_(sowingDay,latitude,sDsa_sh,rp,sDws,sDsa_nh,p,fixPhyll)
    print *,fixPhyll
 END PROGRAM

