#package = "C:/Users/midingoy/Documents/dssat/SoilTemperature/EPIC_ST_standalone"
package = "C:/Users/midingoy/Documents/dssat/SoilTemperature/DSSAT_EPICST_standalone"
#package = "C:/Users/midingoy/Documents/dssat/SoilTemperature/DSSAT_ST_standalone"
from pycropml.transpiler.antlr_py.dssat.run import execute

def test_dssat():
    execute(package)

test_dssat()