"""Central registry for Crop2ML target languages and platforms."""

from dataclasses import dataclass
from importlib import import_module
from typing import Optional


@dataclass(frozen=True)
class TargetSpec:
    """Describe the code generators and capabilities of one target."""

    module: str
    generator: str
    composer: str
    extension: Optional[str]
    generate_notebooks: bool = False
    domain_class_factory: Optional[str] = None
    wrapper_factory: Optional[str] = None
    format_fortran: bool = False


TARGETS = {
    "r": TargetSpec(
        "pycropml.transpiler.generators.rGenerator",
        "RGenerator", "RCompo", "r", generate_notebooks=True,
    ),
    "cs": TargetSpec(
        "pycropml.transpiler.generators.csharpGenerator",
        "CsharpGenerator", "CsharpCompo", "cs", generate_notebooks=True,
        domain_class_factory="to_struct_cs", wrapper_factory="to_wrapper_cs",
    ),
    "cpp": TargetSpec(
        "pycropml.transpiler.generators.cppGenerator",
        "CppGenerator", "CppCompo", "cpp", generate_notebooks=True,
        domain_class_factory="to_struct_cpp",
    ),
    "cpp2": TargetSpec(
        "pycropml.transpiler.generators.cpp2Generator",
        "Cpp2Generator", "Cpp2Compo", "cpp",
        domain_class_factory="to_struct_cpp2",
    ),
    "py": TargetSpec(
        "pycropml.transpiler.generators.pythonGenerator",
        "PythonGenerator", "PythonCompo", "py", generate_notebooks=True,
    ),
    "f90": TargetSpec(
        "pycropml.transpiler.generators.fortranGenerator",
        "FortranGenerator", "FortranCompo", "f90", generate_notebooks=True,
        format_fortran=True,
    ),
    "java": TargetSpec(
        "pycropml.transpiler.generators.javaGenerator",
        "JavaGenerator", "JavaCompo", "java", generate_notebooks=True,
        domain_class_factory="to_struct_java",
    ),
    "simplace": TargetSpec(
        "pycropml.transpiler.generators.simplaceGenerator",
        "SimplaceGenerator", "SimplaceCompo", "java",
    ),
    "sirius": TargetSpec(
        "pycropml.transpiler.generators.siriusGenerator",
        "SiriusGenerator", "SiriusCompo", "cs",
        domain_class_factory="to_struct_sirius",
        wrapper_factory="to_wrapper_sirius",
    ),
    "openalea": TargetSpec(
        "pycropml.transpiler.generators.openaleaGenerator",
        "OpenaleaGenerator", "OpenaleaCompo", "py",
    ),
    "check": TargetSpec(
        "pycropml.transpiler.generators.checkGenerator",
        "CheckGenerator", "CheckCompo", None,
    ),
    "apsim": TargetSpec(
        "pycropml.transpiler.generators.apsimGenerator",
        "ApsimGenerator", "ApsimCompo", "cs",
        domain_class_factory="to_struct_apsim",
        wrapper_factory="to_wrapper_apsim",
    ),
    "record": TargetSpec(
        "pycropml.transpiler.generators.recordGenerator",
        "RecordGenerator", "RecordCompo", "cpp",
    ),
    "dssat": TargetSpec(
        "pycropml.transpiler.generators.dssatGenerator",
        "DssatGenerator", "DssatCompo", "f90", format_fortran=True,
    ),
    "stics": TargetSpec(
        "pycropml.transpiler.generators.sticsGenerator",
        "SticsGenerator", "SticsCompo", "f90", format_fortran=True,
    ),
    "bioma": TargetSpec(
        "pycropml.transpiler.generators.biomaGenerator",
        "BiomaGenerator", "BiomaCompo", "cs",
        domain_class_factory="to_struct_bioma",
        wrapper_factory="to_wrapper_bioma",
    ),
}


def get_target(name):
    """Return the specification for *name* with a helpful error message."""
    try:
        return TARGETS[name]
    except KeyError as error:
        supported = ", ".join(sorted(TARGETS))
        raise ValueError(
            f"Unknown target {name!r}. Supported targets: {supported}"
        ) from error


def load_generator(name):
    """Load the ModelUnit generator class for a target."""
    spec = get_target(name)
    return getattr(import_module(spec.module), spec.generator)


def load_composer(name):
    """Load the model-composition generator class for a target."""
    spec = get_target(name)
    return getattr(import_module(spec.module), spec.composer)


def load_target_callable(name, attribute):
    """Load an optional target-specific helper declared by its specification."""
    spec = get_target(name)
    callable_name = getattr(spec, attribute)
    if callable_name is None:
        return None
    return getattr(import_module(spec.module), callable_name)
