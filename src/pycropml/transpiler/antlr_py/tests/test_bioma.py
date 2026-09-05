from pathlib import Path

from pycropml.transpiler.antlr_py.bioma.run import run_bioma


EXAMPLES = Path(__file__).parent / "examples"


def test_run_bioma_generates_crop2ml_package(tmp_path):
    """Convert the BioMA phenology component into a temporary package."""
    component = (
        EXAMPLES
        / "SiriusComponent"
        / "phenology"
        / "original"
        / "src"
        / "sirius"
        / "original"
    )

    run_bioma(component, tmp_path)

    crop2ml_directory = tmp_path / "crop2ml"
    assert list(crop2ml_directory.glob("unit*.xml"))
    assert list(crop2ml_directory.glob("composition.*.xml"))
