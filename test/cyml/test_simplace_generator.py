"""Regression tests for Simplace path handling."""

from pathlib import Path
from types import SimpleNamespace

from pycropml.transpiler.generators.simplaceGenerator import Pl2Crop2ml


def test_simplace_composition_accepts_pathlib_model_path():
    composition = SimpleNamespace(
        path=Path("/models/Example-Model"),
        name="ExampleComposition",
        ord=[],
        inputlink=[],
        outputlink=[],
        internallink=[],
        model=[],
    )

    xml = Pl2Crop2ml(composition, "Simplace.SoilTemp").run_simplace()

    assert (
        'Class="net.simplace.sim.components.Example-Model.ExampleComposition"'
        in xml.unicode()
    )
