"""Registry and entry-point discovery for Crop2ML target platforms."""

from importlib.metadata import entry_points

from pycropml.transpiler.target import TargetPlatform


TARGET_ENTRY_POINT_GROUP = "pycropml.targets"
_external_target_names = set()
_discovery_complete = False

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


def _target_entry_points():
    """Return target entry points on all supported Python versions."""
    discovered = entry_points()
    if hasattr(discovered, "select"):
        return discovered.select(group=TARGET_ENTRY_POINT_GROUP)
    return discovered.get(TARGET_ENTRY_POINT_GROUP, ())


def _load_external_target(entry_point):
    """Load and validate one external target contract."""
    target = entry_point.load()
    if not isinstance(target, TargetPlatform) and callable(target):
        target = target()
    if not isinstance(target, TargetPlatform):
        raise TypeError(
            f"Target entry point {entry_point.name!r} must expose a "
            "TargetPlatform instance or a factory returning one"
        )
    if target.name != entry_point.name:
        raise ValueError(
            f"Target entry point name {entry_point.name!r} does not match "
            f"TargetPlatform.name {target.name!r}"
        )
    return target


def discover_targets(force=False):
    """Discover external targets once and merge them into ``TARGETS``.

    Built-in target names are reserved. Two external distributions cannot
    register the same name.
    """
    global _discovery_complete
    if _discovery_complete and not force:
        return TARGETS

    if force:
        for name in _external_target_names:
            TARGETS.pop(name, None)
        _external_target_names.clear()

    discovered_targets = {}
    for entry_point in _target_entry_points():
        if (
            entry_point.name in TARGETS
            or entry_point.name in discovered_targets
        ):
            raise ValueError(
                f"Target name {entry_point.name!r} is already registered"
            )
        target = _load_external_target(entry_point)
        discovered_targets[target.name] = target

    TARGETS.update(discovered_targets)
    _external_target_names.update(discovered_targets)

    _discovery_complete = True
    return TARGETS


def available_targets():
    """Return built-in and discovered target specifications."""
    return discover_targets()


def get_target(name):
    """Return the specification for *name* with a helpful error message."""
    targets = available_targets()
    try:
        return targets[name]
    except KeyError as error:
        supported = ", ".join(sorted(targets))
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
