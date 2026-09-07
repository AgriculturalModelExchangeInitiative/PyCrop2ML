"""Tests for target-package pipeline orchestration."""

from pathlib import Path
from types import SimpleNamespace

from pycropml import cyml
from pycropml.transpiler.target import TargetPlatform
from pycropml.transpiler.target_pipeline import TargetPipeline


def test_transpile_package_is_a_stable_pipeline_facade(monkeypatch):
    calls = []

    class Pipeline:
        def __init__(self, package, target_name):
            calls.append((package, target_name))

        def run(self):
            return 17

    monkeypatch.setattr(cyml, "TargetPipeline", Pipeline)

    assert cyml.transpile_package("crop2ml-package", "py") == 17
    assert calls == [("crop2ml-package", "py")]


def test_pipeline_prepares_the_generation_context(tmp_path):
    pipeline = TargetPipeline(tmp_path / "my-package", "py")
    pipeline.package.mkdir()

    context = pipeline._prepare_context(["model"])

    assert context.package == Path(tmp_path / "my-package")
    assert context.package_name == "my-package"
    assert context.target_name == "py"
    assert context.model_units == ["model"]
    assert context.target_package == tmp_path / "my-package/src/py/my_package"
    assert context.cyml_directory == tmp_path / "my-package/src/pyx"
    assert context.test_directory == tmp_path / "my-package/test/py"
    assert context.image_directory == tmp_path / "my-package/doc/images"
    assert context.target_package.is_dir()
    assert context.test_directory.is_dir()
    assert context.image_directory.is_dir()


def test_pipeline_uses_the_composition_specific_extension(tmp_path):
    pipeline = TargetPipeline(tmp_path, "py")
    pipeline.target = TargetPlatform(
        name="mixed",
        module="example.platform",
        generator="Generator",
        composer="Composer",
        extension="py",
        composition_extension="xml",
    )
    context = SimpleNamespace(
        component_name="Composite",
        cyml_directory=tmp_path / "pyx",
        image_directory=tmp_path / "images",
        target_package=tmp_path / "target",
    )
    context.cyml_directory.mkdir()
    context.image_directory.mkdir()
    context.target_package.mkdir()

    class Topology:
        def algo2cyml(self, image_directory):
            assert image_directory == context.image_directory
            return "composition algorithm"

        def compotranslate(self, target_name):
            assert target_name == "py"
            return "<Workflow />"

    pipeline._generate_composition(context, Topology())

    assert (context.cyml_directory / "CompositeComponent.pyx").read_text() == (
        "composition algorithm"
    )
    assert (context.target_package / "CompositeComponent.xml").read_text() == (
        "<Workflow />"
    )
    assert not (context.target_package / "CompositeComponent.py").exists()
