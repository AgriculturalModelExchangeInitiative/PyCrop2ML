from pathlib import Path
import xml.etree.ElementTree as ET

from pycropml.transpiler.antlr_py.composition_compiler import (
    compile_composition,
    composition_xml,
    find_composition_algorithm,
    find_composition_algorithms,
)
from pycropml.transpiler.antlr_py.composition_visitor import load_model_interfaces
from pycropml.transpiler.antlr_py.validate_composition import validate


ROOT = Path(__file__).resolve().parents[2]
CROP2ML = ROOT / "example" / "Monica_SoilTemp" / "crop2ml"
ALGORITHM = CROP2ML / "algo" / "pyx" / "SoilTemperatureComp.pyx"


def test_composition_algorithm_discovery():
    assert find_composition_algorithms(CROP2ML) == [ALGORITHM]
    assert find_composition_algorithm(CROP2ML) == ALGORITHM
    assert (
        find_composition_algorithm(CROP2ML, name="SoilTemperatureComp")
        == ALGORITHM
    )


def test_composition_metadata_marker():
    result, _ = compile_composition(find_composition_algorithm(CROP2ML), CROP2ML)
    assert result.metadata["type"] == "composition"


def test_monica_composition_is_valid():
    assert validate(ALGORITHM, CROP2ML)


def test_monica_composition_metadata_and_links():
    result, _ = compile_composition(ALGORITHM, CROP2ML)

    assert result.metadata["name"] == "SoilTemperatureComp"
    assert result.models == [
        "NoSnowSoilSurfaceTemperature",
        "WithSnowSoilSurfaceTemperature",
        "SoilTemperature",
    ]
    assert {
        "source": "NoSnowSoilSurfaceTemperature.soilSurfaceTemperature",
        "target": "WithSnowSoilSurfaceTemperature.noSnowSoilSurfaceTemperature",
    } in result.internal_links
    assert {
        "source": "WithSnowSoilSurfaceTemperature.soilSurfaceTemperature",
        "target": "SoilTemperature.soilSurfaceTemperature",
    } in result.internal_links
    assert {
        "source": "WithSnowSoilSurfaceTemperature.soilSurfaceTemperature",
        "target": "soilSurfaceTemperature",
    } in result.output_links
    assert {
        "source": "soilTemperature",
        "target": "SoilTemperature.soilTemperature",
    } in result.input_links


def test_generated_composition_xml():
    result, directory = compile_composition(ALGORITHM, CROP2ML)
    interfaces = load_model_interfaces(directory)
    root = composition_xml(result, interfaces, ALGORITHM, directory)

    assert root.tag == "ModelComposition"
    assert root.attrib["id"] == "Monica_SoilTemp.SoilTemperatureComp"
    assert root.findtext("./Description/Title") == "SoilTemperature model"
    assert root.find("./Algorithm").attrib == {
        "language": "cyml-composition",
        "filename": "algo/pyx/SoilTemperatureComp.pyx",
    }
    assert len(root.findall("./Composition/Model")) == 3
    assert len(root.findall("./Composition/Links/InternalLink")) == 2
    assert len(root.findall("./Composition/Links/OutputLink")) == 2

    # Ensure the generated element tree can be serialized and parsed again.
    assert ET.fromstring(ET.tostring(root)).tag == "ModelComposition"
