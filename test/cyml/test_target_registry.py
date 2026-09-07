"""Tests for the central Crop2ML target registry."""

import sys
from types import ModuleType, SimpleNamespace

import pytest

from pycropml.transpiler.target import (
    TARGET_PLATFORM_API_VERSION,
    TargetPlatform,
)
import pycropml.transpiler.target_registry as target_registry
from pycropml.transpiler.target_registry import (
    TARGETS,
    TARGET_ENTRY_POINT_GROUP,
    available_targets,
    discover_targets,
    get_target,
    load_composer,
    load_generator,
    load_target_callable,
)


class FakeEntryPoint:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def load(self):
        return self.value


class FakeEntryPoints(list):
    def select(self, *, group):
        assert group == TARGET_ENTRY_POINT_GROUP
        return self


def make_external_target(name="external"):
    return TargetPlatform(
        name=name,
        module="external_platform",
        generator="Generator",
        composer="Composer",
        extension="py",
    )


@pytest.fixture
def external_targets(monkeypatch):
    def discover(*entry_point_values):
        entry_point_objects = FakeEntryPoints(entry_point_values)
        monkeypatch.setattr(
            target_registry,
            "entry_points",
            lambda: entry_point_objects,
        )
        monkeypatch.setattr(
            target_registry,
            "_discovery_complete",
            False,
        )
        return discover_targets(force=True)

    yield discover
    monkeypatch.setattr(target_registry, "entry_points", lambda: FakeEntryPoints())
    discover_targets(force=True)


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


def test_composition_extension_defaults_to_modelunit_extension():
    assert get_target("py").effective_composition_extension == "py"


def test_target_may_declare_a_distinct_composition_extension():
    target = TargetPlatform(
        name="xml_composite",
        module="example.platform",
        generator="Generator",
        composer="Composer",
        extension="py",
        composition_extension="xml",
    )

    assert target.extension == "py"
    assert target.effective_composition_extension == "xml"


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


def test_target_contract_has_a_supported_api_version():
    assert make_external_target().api_version == TARGET_PLATFORM_API_VERSION
    with pytest.raises(ValueError, match="Unsupported target platform API"):
        TargetPlatform(
            name="future",
            module="future_platform",
            generator="Generator",
            composer="Composer",
            extension="py",
            api_version="2",
        )


def test_discovers_an_external_target(external_targets):
    target = make_external_target()

    targets = external_targets(FakeEntryPoint("external", target))

    assert targets["external"] is target
    assert available_targets()["external"] is target
    assert get_target("external") is target


def test_external_entry_point_may_expose_a_factory(external_targets):
    target = make_external_target("factory_target")

    targets = external_targets(
        FakeEntryPoint("factory_target", lambda: target)
    )

    assert targets["factory_target"] is target


def test_external_target_name_must_match_its_entry_point(external_targets):
    with pytest.raises(ValueError, match="does not match"):
        external_targets(
            FakeEntryPoint("entry_point_name", make_external_target("other"))
        )


def test_external_target_cannot_replace_a_builtin(external_targets):
    with pytest.raises(ValueError, match="already registered"):
        external_targets(FakeEntryPoint("py", make_external_target("py")))


def test_failed_discovery_does_not_partially_register_plugins(
    external_targets,
):
    with pytest.raises(ValueError, match="already registered"):
        external_targets(
            FakeEntryPoint(
                "first_external",
                make_external_target("first_external"),
            ),
            FakeEntryPoint("py", make_external_target("py")),
        )

    assert "first_external" not in TARGETS


def test_external_entry_point_must_expose_the_contract(external_targets):
    with pytest.raises(TypeError, match="must expose a TargetPlatform"):
        external_targets(FakeEntryPoint("invalid", object()))


def test_target_platform_adapts_context_to_legacy_hooks(monkeypatch):
    calls = []
    module = ModuleType("test_platform_hooks")
    module.Generator = object
    module.Composer = object
    module.generate_domain = lambda *args: calls.append(("domain", args))
    module.generate_wrapper = lambda *args: calls.append(("wrapper", args))
    monkeypatch.setitem(sys.modules, module.__name__, module)
    target = TargetPlatform(
        name="test",
        module=module.__name__,
        generator="Generator",
        composer="Composer",
        extension="py",
        domain_class_factory="generate_domain",
        wrapper_factory="generate_wrapper",
    )
    context = SimpleNamespace(
        composition="composition",
        target_package="output",
        component_name="Component",
    )

    target.generate_domain_classes(context)
    target.generate_wrapper(context)

    assert calls == [
        ("domain", (["composition"], "output", "Component")),
        ("wrapper", ("composition", "output", "Component")),
    ]
