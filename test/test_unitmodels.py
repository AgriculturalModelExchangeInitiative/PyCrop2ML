"""Tests for parsing and transpiling the Tutorial Crop2ML packages."""

from pathlib import Path
from shutil import copytree

from pycropml import pparse, render_cyml
from pycropml.cyml import transpile_package


TUTORIAL = Path(__file__).parent / "Tutorial"
ENERGY_BALANCE = TUTORIAL / "energybalance_pkg"
PHENOLOGY = TUTORIAL / "pheno_pkg"


def copy_crop2ml_package(source, tmp_path):
    """Copy only the source Crop2ML description into a fresh package."""
    package = tmp_path / source.name
    copytree(source / "crop2ml", package / "crop2ml")
    return package


def assert_generated_component(package, language):
    output = package / "src" / language / package.name
    assert output.is_dir()
    assert list(output.glob("*Component.py"))
    return output


def test_energy_balance_model_parser():
    models = pparse.model_parser(ENERGY_BALANCE)
    assert len(models) == 13


def test_phenology_model_parser():
    models = pparse.model_parser(PHENOLOGY)
    assert len(models) == 13


def test_energy_balance_package_generation(tmp_path):
    package = copy_crop2ml_package(ENERGY_BALANCE, tmp_path)
    models = pparse.model_parser(package)

    cyml_output = tmp_path / "generated-cyml"
    render_cyml.Model2Package(
        models, dir=cyml_output, pkg_name="EnergyBalance"
    ).run()
    assert len(list((cyml_output / "pyx").glob("*.pyx"))) == len(models)

    transpile_package(package, "py")
    assert_generated_component(package, "py")

    transpile_package(package, "openalea")
    openalea_output = assert_generated_component(package, "openalea")
    assert (openalea_output / "__wralea__.py").is_file()


def test_phenology_package_generation(tmp_path):
    package = copy_crop2ml_package(PHENOLOGY, tmp_path)

    transpile_package(package, "py")

    assert_generated_component(package, "py")
