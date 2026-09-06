"""Tests for the stable context exposed to target platforms."""

from pycropml.transpiler.generation_context import GenerationContext


def make_context(tmp_path, name="package"):
    package = tmp_path / name
    return GenerationContext(
        package=package,
        package_name=name,
        target_name="py",
        model_units=["unit"],
        composition="composition",
        component_name="Component",
        crop2ml_directory=package / "crop2ml",
        cyml_directory=package / "src" / "pyx",
        target_root=package / "src" / "py",
        target_package=package / "src" / "py" / name,
        test_directory=package / "test" / "py",
        documentation_directory=package / "doc",
        image_directory=package / "doc" / "images",
    )


def test_generation_context_exposes_models_names_and_paths(tmp_path):
    context = make_context(tmp_path)

    assert context.package_name == "package"
    assert context.target_name == "py"
    assert context.model_units == ["unit"]
    assert context.composition == "composition"
    assert context.target_package == context.package / "src" / "py" / "package"
    assert context.image_directory == context.package / "doc" / "images"


def test_generation_context_extension_mappings_are_not_shared(tmp_path):
    first = make_context(tmp_path, "first")
    second = make_context(tmp_path, "second")

    first.metadata["version"] = "1.0"
    first.options["debug"] = True

    assert second.metadata == {}
    assert second.options == {}
