"""Tests for the central source-language and platform registry."""

import pytest

from pycropml import cyml
from pycropml.transpiler.source_registry import (
    SOURCES,
    get_source,
    load_source_adapter,
)


def test_registered_sources_load_their_adapters():
    for name, spec in SOURCES.items():
        assert load_source_adapter(name).__name__ == spec.runner


def test_transpile_component_uses_the_registered_adapter(monkeypatch):
    calls = []

    def adapter(component, package):
        calls.append((component, package))

    monkeypatch.setattr(cyml, "load_source_adapter", lambda name: adapter)

    assert cyml.transpile_component("source", "output", "py") == 0
    assert calls == [("source", "output")]


def test_unknown_source_has_a_helpful_error():
    with pytest.raises(ValueError, match="Unknown source 'unknown'"):
        get_source("unknown")
