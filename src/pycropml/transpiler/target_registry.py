"""Registry of the target platforms built into PyCropML."""

from pycropml.transpiler.target import TargetPlatform


TARGETS = {
    "r": TargetPlatform(
        "r",
        "pycropml.transpiler.generators.rGenerator",
        "RGenerator", "RCompo", "r", generate_notebooks=True,
    ),
    "cs": TargetPlatform(
        "cs",
        "pycropml.transpiler.generators.csharpGenerator",
        "CsharpGenerator", "CsharpCompo", "cs", generate_notebooks=True,
        domain_class_factory="to_struct_cs", wrapper_factory="to_wrapper_cs",
    ),
    "cpp": TargetPlatform(
        "cpp",
        "pycropml.transpiler.generators.cppGenerator",
        "CppGenerator", "CppCompo", "cpp", generate_notebooks=True,
        domain_class_factory="to_struct_cpp",
    ),
    "cpp2": TargetPlatform(
        "cpp2",
        "pycropml.transpiler.generators.cpp2Generator",
        "Cpp2Generator", "Cpp2Compo", "cpp",
        domain_class_factory="to_struct_cpp2",
    ),
    "py": TargetPlatform(
        "py",
        "pycropml.transpiler.generators.pythonGenerator",
        "PythonGenerator", "PythonCompo", "py",
        simulation_class="PythonSimulation", generate_notebooks=True,
    ),
    "f90": TargetPlatform(
        "f90",
        "pycropml.transpiler.generators.fortranGenerator",
        "FortranGenerator", "FortranCompo", "f90", generate_notebooks=True,
        format_fortran=True,
    ),
    "java": TargetPlatform(
        "java",
        "pycropml.transpiler.generators.javaGenerator",
        "JavaGenerator", "JavaCompo", "java", generate_notebooks=True,
        domain_class_factory="to_struct_java",
    ),
    "simplace": TargetPlatform(
        "simplace",
        "pycropml.transpiler.generators.simplaceGenerator",
        "SimplaceGenerator", "SimplaceCompo", "java",
    ),
    "sirius": TargetPlatform(
        "sirius",
        "pycropml.transpiler.generators.siriusGenerator",
        "SiriusGenerator", "SiriusCompo", "cs",
        domain_class_factory="to_struct_sirius",
        wrapper_factory="to_wrapper_sirius",
    ),
    "openalea": TargetPlatform(
        "openalea",
        "pycropml.transpiler.generators.openaleaGenerator",
        "OpenaleaGenerator", "OpenaleaCompo", "py",
    ),
    "check": TargetPlatform(
        "check",
        "pycropml.transpiler.generators.checkGenerator",
        "CheckGenerator", "CheckCompo", None,
    ),
    "apsim": TargetPlatform(
        "apsim",
        "pycropml.transpiler.generators.apsimGenerator",
        "ApsimGenerator", "ApsimCompo", "cs",
        domain_class_factory="to_struct_apsim",
        wrapper_factory="to_wrapper_apsim",
    ),
    "record": TargetPlatform(
        "record",
        "pycropml.transpiler.generators.recordGenerator",
        "RecordGenerator", "RecordCompo", "cpp",
    ),
    "dssat": TargetPlatform(
        "dssat",
        "pycropml.transpiler.generators.dssatGenerator",
        "DssatGenerator", "DssatCompo", "f90", format_fortran=True,
    ),
    "stics": TargetPlatform(
        "stics",
        "pycropml.transpiler.generators.sticsGenerator",
        "SticsGenerator", "SticsCompo", "f90", format_fortran=True,
    ),
    "bioma": TargetPlatform(
        "bioma",
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
    return get_target(name).load_generator()


def load_composer(name):
    """Load the model-composition generator class for a target."""
    return get_target(name).load_composer()


def load_target_callable(name, attribute):
    """Load an optional target-specific helper declared by its specification."""
    return get_target(name).load_optional(attribute)
