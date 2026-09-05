"""Central registry for source languages and platforms converted to Crop2ML."""

from dataclasses import dataclass
from importlib import import_module


@dataclass(frozen=True)
class SourceSpec:
    """Describe one source adapter that produces a Crop2ML package."""

    module: str
    runner: str


SOURCES = {
    "dssat": SourceSpec(
        "pycropml.transpiler.antlr_py.dssat.run", "run_dssat"
    ),
    "simplace": SourceSpec(
        "pycropml.transpiler.antlr_py.simplace.run", "run_simplace"
    ),
    "bioma": SourceSpec(
        "pycropml.transpiler.antlr_py.bioma.run", "run_bioma"
    ),
    "openalea": SourceSpec(
        "pycropml.transpiler.antlr_py.openalea.run", "run_openalea"
    ),
    "f90": SourceSpec(
        "pycropml.transpiler.antlr_py.fortran.run", "run_fortran"
    ),
    "stics": SourceSpec(
        "pycropml.transpiler.antlr_py.stics.run", "run_stics"
    ),
    "py": SourceSpec(
        "pycropml.transpiler.antlr_py.python.run", "run_python"
    ),
    "apsim": SourceSpec(
        "pycropml.transpiler.antlr_py.apsim.run", "run_apsim"
    ),
    "cs": SourceSpec(
        "pycropml.transpiler.antlr_py.csharp.run", "run_csharp"
    ),
}


def get_source(name):
    """Return the source specification with a helpful error message."""
    try:
        return SOURCES[name]
    except KeyError as error:
        supported = ", ".join(sorted(SOURCES))
        raise ValueError(
            f"Unknown source {name!r}. Supported sources: {supported}"
        ) from error


def load_source_adapter(name):
    """Load the conversion function registered for a source."""
    spec = get_source(name)
    return getattr(import_module(spec.module), spec.runner)
