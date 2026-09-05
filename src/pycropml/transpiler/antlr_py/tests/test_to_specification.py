from pycropml.transpiler.antlr_py.to_specification import extractMetaInfo


FORTRAN_SPECIFICATION = """
!%%CyML Description Begin%%
! ABD      Average bulk density for soil profile (g [soil] / cm3 [soil])
!            (10.5, [0.5 - 100.0])  state variable
! TLL      Total soil water in the profile at the lower limit of
!            plant-extractable water (cm) (, [0.0 - 10000]) exogenous variable
!%%CyML Description End%%
"""

PYTHON_ARRAY_SPECIFICATION = """
#%%CyML Description Begin%%
# ABD(L)      Average bulk density for soil profile (g [soil] / cm3 [soil])
#            (10.5, [0.5 - 100.0])  state variable
#%%CyML Description End%%
"""


def test_extract_meta_info_from_fortran_comments():
    assert extractMetaInfo(FORTRAN_SPECIFICATION, "!") == {
        "ABD": {
            "description": "Average bulk density for soil profile",
            "unit": "g [soil] / cm3 [soil]",
            "default": "10.5",
            "max": "100.0",
            "min": "0.5",
            "len": "",
            "category": "state",
            "type": "variable",
        },
        "TLL": {
            "description": (
                "Total soil water in the profile at the lower limit of "
                "plant-extractable water"
            ),
            "unit": "cm",
            "default": "",
            "min": "0.0",
            "max": "10000",
            "len": "",
            "category": "exogenous",
            "type": "variable",
        },
    }


def test_extract_meta_info_preserves_array_length():
    assert extractMetaInfo(PYTHON_ARRAY_SPECIFICATION, "#") == {
        "ABD": {
            "description": "Average bulk density for soil profile",
            "unit": "g [soil] / cm3 [soil]",
            "default": "10.5",
            "max": "100.0",
            "min": "0.5",
            "len": "L",
            "category": "state",
            "type": "variable",
        }
    }
