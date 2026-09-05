"""Registry of the source platforms built into PyCropML."""

from pycropml.transpiler.source import SourcePlatform


SOURCES = {
    "dssat": SourcePlatform(
        "dssat",
        "pycropml.transpiler.antlr_py.dssat.run", "run_dssat"
    ),
    "simplace": SourcePlatform(
        "simplace",
        "pycropml.transpiler.antlr_py.simplace.run", "run_simplace"
    ),
    "bioma": SourcePlatform(
        "bioma",
        "pycropml.transpiler.antlr_py.bioma.run", "run_bioma"
    ),
    "openalea": SourcePlatform(
        "openalea",
        "pycropml.transpiler.antlr_py.openalea.run", "run_openalea"
    ),
    "f90": SourcePlatform(
        "f90",
        "pycropml.transpiler.antlr_py.fortran.run", "run_fortran"
    ),
    "stics": SourcePlatform(
        "stics",
        "pycropml.transpiler.antlr_py.stics.run", "run_stics"
    ),
    "py": SourcePlatform(
        "py",
        "pycropml.transpiler.antlr_py.python.run", "run_python"
    ),
    "apsim": SourcePlatform(
        "apsim",
        "pycropml.transpiler.antlr_py.apsim.run", "run_apsim"
    ),
    "cs": SourcePlatform(
        "cs",
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
    return get_source(name).load_adapter()
