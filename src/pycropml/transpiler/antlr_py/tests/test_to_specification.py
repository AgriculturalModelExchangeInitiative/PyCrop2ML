
from pycropml.transpiler.antlr_py.to_specification import *


specification ="""

!%%CyML Description Begin%%
! ABD      Average bulk density for soil profile (g [soil] / cm3 [soil])
!            (10.5, [0.5 - 100.0])  state variable
! TLL      Total soil water in the profile at the lower limit of
!            plant-extractable water (cm) (, [0.0 - 10000]) exogenous variable
!%%CyML Description End%%
"""
specification2 = """
#%%CyML Description Begin%%
# ABD(L)      Average bulk density for soil profile (g [soil] / cm3 [soil])
#            (10.5, [0.5 - 100.0])  state variable   
#%%CyML Description End%%

"""


def test_extractMetaInfo():
    
    res1 = extractMetaInfo(specification, "!")
    print(res1)
    assert res1 == {"ABD":{"description":"Average bulk density for soil profile","unit":"g [soil] / cm3 [soil]", "default":"10.5",  "max":"100.0", "min":"0.5","len":"", "category":"state", "type":"variable"},\
                    "TLL" :{"description":"Total soil water in the profile at the lower limit of plant-extractable water", "unit":"cm", "default":"", "min":"0.0", "max": "10000","len":"", "category":"exogenous", "type":"variable"} }
    res1 = extractMetaInfo(specification2, "#")
    assert res1 == {"ABD":{"description":"Average bulk density for soil profile","unit":"g [soil] / cm3 [soil]", "default":"10.5",  "max":"100.0", "min":"0.5","len":"L", "category":"state", "type":"variable"}}


test_extractMetaInfo()

