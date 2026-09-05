"""Tests for the central Crop2ML target registry."""

import pytest

from pycropml.transpiler.target import TargetPlatform
from pycropml.transpiler.target_registry import (
    TARGETS,
    get_target,
    load_composer,
    load_generator,
    load_target_callable,
)


def test_builtin_targets_use_the_public_platform_contract():
    for name, target in TARGETS.items():
        assert isinstance(target, TargetPlatform)
        assert target.name == name


def test_registered_targets_load_their_generators():
    for name, spec in TARGETS.items():
        assert load_generator(name).__name__ == spec.generator
        assert load_composer(name).__name__ == spec.composer


def test_registered_target_helpers_are_loadable():
    for name, spec in TARGETS.items():
        for attribute in (
            "domain_class_factory",
            "wrapper_factory",
            "simulation_class",
        ):
            helper = load_target_callable(name, attribute)
            if getattr(spec, attribute) is None:
                assert helper is None
            else:
                assert callable(helper)


def test_python_platforms_share_the_python_extension():
    assert get_target("py").extension == "py"
    assert get_target("openalea").extension == "py"


def test_only_python_registers_a_simulation_generator():
    assert load_target_callable("py", "simulation_class").__name__ == (
        "PythonSimulation"
    )
    assert get_target("openalea").simulation_class is None


def test_unknown_target_has_a_helpful_error():
    with pytest.raises(ValueError, match="Unknown target 'unknown'"):
        get_target("unknown")


def test_target_platform_rejects_empty_required_fields():
    with pytest.raises(ValueError, match="TargetPlatform.name must not be empty"):
        TargetPlatform(
            name="",
            module="example.platform",
            generator="Generator",
            composer="Composer",
            extension="py",
        )
