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
    !                          - description : Day of Year at sowing
    !                          - parametercategory : species
    !                          - datatype : INT
    !                          - min : 1
    !                          - max : 365
    !                          - default : 1
    !                          - unit : d
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: latitude
    !                          - description : Latitude
    !                          - parametercategory : soil
    !                          - datatype : DOUBLE
    !                          - min : -90
    !                          - max : 90
    !                          - default : 0.0
    !                          - unit : °
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: sDsa_sh
    !                          - description : Sowing date at which Phyllochrone is maximum in southern hemispher
    !                          - parametercategory : species
    !                          - inputtype : parameter
    !                          - datatype : INT
    !                          - min : 1
    !                          - max : 365
    !                          - default : 1
    !                          - unit : d
    !                          - uri : some url
    !            - name: rp
    !                          - description : Rate of change of Phyllochrone with sowing date
    !                          - parametercategory : species
    !                          - inputtype : parameter
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 365
    !                          - default : 0
    !                          - unit : d-1
    !                          - uri : some url
    !            - name: sDws
    !                          - description : Sowing date at which Phyllochrone is minimum
    !                          - parametercategory : species
    !                          - datatype : INT
    !                          - default : 1
    !                          - min : 1
    !                          - max : 365
    !                          - unit : d
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: sDsa_nh
    !                          - description : Sowing date at which Phyllochrone is maximum in northern hemispher
    !                          - parametercategory : species
    !                          - datatype : INT
    !                          - default : 1
    !                          - min : 1
    !                          - max : 365
    !                          - unit : d
    !                          - uri : some url
    !                          - inputtype : parameter
    !            - name: p
    !                          - description : Phyllochron (Varietal parameter)
    !                          - parametercategory : species
    !                          - datatype : DOUBLE
    !                          - default : 120
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : °C d leaf-1
    !                          - uri : some url
    !                          - inputtype : parameter
        !- outputs:
    !            - name: fixPhyll
    !                          - description :  Phyllochron Varietal parameter 
    !                          - datatype : DOUBLE
    !                          - min : 0
    !                          - max : 1000
    !                          - unit : °C d leaf-1
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
