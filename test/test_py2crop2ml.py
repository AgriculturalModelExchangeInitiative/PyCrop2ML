import shutil
from pathlib import Path

from pycropml.cyml import transpile_component


MODELS = Path(__file__).parent / "Models"


def test_python_component_can_be_transpiled_to_crop2ml(tmp_path):
    """Transpile a copied Python component without modifying its fixture."""
    source = MODELS / "SQ_Energy_Balance_py"
    package = tmp_path / source.name
    shutil.copytree(source, package, ignore=shutil.ignore_patterns("crop2ml"))

    transpile_component(package, package, "py")

    crop2ml_directory = package / "crop2ml"
    assert list(crop2ml_directory.glob("unit*.xml"))
    assert list(crop2ml_directory.glob("composition.*.xml"))
