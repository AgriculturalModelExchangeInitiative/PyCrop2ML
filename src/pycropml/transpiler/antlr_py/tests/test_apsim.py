from pathlib import Path

from pycropml.transpiler.antlr_py.apsim.run import run_apsim


EXAMPLES = Path(__file__).parent / "examples"

def test_run_apsim_generates_crop2ml_package(tmp_path):
    """Convert the Toy1 APSIM component without modifying the fixture."""
    component = EXAMPLES / "apsimComponent" / "Toy1"

    run_apsim(component, tmp_path)

    crop2ml_directory = tmp_path / "crop2ml"
    assert list(crop2ml_directory.glob("unit*.xml"))
    assert list(crop2ml_directory.glob("composition.*.xml"))
