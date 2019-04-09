MODULE Phylsowingdatecorrection_mod
    USE list_sub
    IMPLICIT NONE
CONTAINS
    SUBROUTINE phylsowingdatecorrection_(sowingDay, &
        latitude, &
        sDsa_sh, &
        rp, &
        sDws, &
        sDsa_nh, &
        p, &
        fixPhyll)
        REAL, INTENT(OUT) :: fixPhyll
        INTEGER, INTENT(IN) :: sowingDay
        REAL, INTENT(IN) :: latitude
        INTEGER, INTENT(IN) :: sDsa_sh
        REAL, INTENT(IN) :: rp
        INTEGER, INTENT(IN) :: sDws
        INTEGER, INTENT(IN) :: sDsa_nh
        REAL, INTENT(IN) :: p
        !- Description:
    !            - Model Name: PhylSowingDateCorrection Model
    !            - Author: Loic Manceau
    !            - Reference: Modeling development phase in the 
    !                Wheat Simulation Model SiriusQuality.
    !                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    !            - Institution: INRA Montpellier
    !            - Abstract: Correction of the Phyllochron Varietal parameter according to sowing date 
        !- inputs:
    !            - name: sowingDay
    !                          - parametercategory : species
    !                          - min : 1
    !                          - datatype : INT
    !                          - max : 365
    !                          - uri : some url
    !                          - default : 1
    !                          - inputtype : parameter
    !                          - unit : d
    !                          - description : Day of Year at sowing
    !            - name: latitude
    !                          - parametercategory : soil
    !                          - min : -90
    !                          - datatype : DOUBLE
    !                          - max : 90
    !                          - uri : some url
    !                          - default : 0.0
    !                          - inputtype : parameter
    !                          - unit : °
    !                          - description : Latitude
    !            - name: sDsa_sh
    !                          - parametercategory : species
    !                          - min : 1
    !                          - datatype : INT
    !                          - max : 365
    !                          - uri : some url
    !                          - default : 1
    !                          - inputtype : parameter
    !                          - unit : d
    !                          - description : Sowing date at which Phyllochrone is maximum in southern hemispher
    !            - name: rp
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 365
    !                          - uri : some url
    !                          - default : 0
    !                          - inputtype : parameter
    !                          - unit : d-1
    !                          - description : Rate of change of Phyllochrone with sowing date
    !            - name: sDws
    !                          - parametercategory : species
    !                          - min : 1
    !                          - datatype : INT
    !                          - max : 365
    !                          - uri : some url
    !                          - default : 1
    !                          - inputtype : parameter
    !                          - unit : d
    !                          - description : Sowing date at which Phyllochrone is minimum
    !            - name: sDsa_nh
    !                          - parametercategory : species
    !                          - min : 1
    !                          - datatype : INT
    !                          - max : 365
    !                          - uri : some url
    !                          - default : 1
    !                          - inputtype : parameter
    !                          - unit : d
    !                          - description : Sowing date at which Phyllochrone is maximum in northern hemispher
    !            - name: p
    !                          - parametercategory : species
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - uri : some url
    !                          - default : 120
    !                          - inputtype : parameter
    !                          - unit : °C d leaf-1
    !                          - description : Phyllochron (Varietal parameter)
        !- outputs:
    !            - name: fixPhyll
    !                          - min : 0
    !                          - datatype : DOUBLE
    !                          - max : 1000
    !                          - unit : °C d leaf-1
    !                          - description :  Phyllochron Varietal parameter 
        IF(latitude .LT. 0.0) THEN
            IF(sowingDay .GT. sDsa_sh) THEN
                fixPhyll = p * (1 - rp * MIN((sowingDay - sDsa_sh), sDws))
            ELSE
                fixPhyll = p
            END IF
        ELSE
            IF(sowingDay .LT. sDsa_nh) THEN
                fixPhyll = p * (1 - rp * MIN(sowingDay, sDws))
            ELSE
                fixPhyll = p
            END IF
        END IF
    END SUBROUTINE phylsowingdatecorrection_
END MODULE
