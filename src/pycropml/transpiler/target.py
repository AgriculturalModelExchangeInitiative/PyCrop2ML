"""Public contract for Crop2ML target languages and platforms."""

from dataclasses import dataclass
from importlib import import_module
from typing import Optional


TARGET_PLATFORM_API_VERSION = "1"


@dataclass(frozen=True)
class TargetPlatform:
    """Describe and load the generators provided by a target platform.

    Built-in and external targets use the same contract. Optional capabilities
    are represented by symbol names in the target module and are loaded only
    when the conversion pipeline needs them.
    """

    name: str
    module: str
    generator: str
    composer: str
    extension: Optional[str]
    simulation_class: Optional[str] = None
    generate_notebooks: bool = False
    domain_class_factory: Optional[str] = None
    wrapper_factory: Optional[str] = None
    format_fortran: bool = False
    api_version: str = TARGET_PLATFORM_API_VERSION
    composition_extension: Optional[str] = None

    def __post_init__(self):
        for attribute in ("name", "module", "generator", "composer"):
            if not getattr(self, attribute):
                raise ValueError(f"TargetPlatform.{attribute} must not be empty")
        if self.api_version != TARGET_PLATFORM_API_VERSION:
            raise ValueError(
                f"Unsupported target platform API version {self.api_version!r}; "
                f"expected {TARGET_PLATFORM_API_VERSION!r}"
            )

    def load_symbol(self, symbol):
        """Load *symbol* from the platform module."""
        return getattr(import_module(self.module), symbol)

    def load_generator(self):
        """Load the ModelUnit generator class."""
        return self.load_symbol(self.generator)

    def load_composer(self):
        """Load the model-composition generator class."""
        return self.load_symbol(self.composer)

    @property
    def effective_composition_extension(self):
        """Return the composition extension, falling back to ModelUnits."""
        return self.composition_extension or self.extension

    def load_optional(self, attribute):
        """Load an optional capability declared by a dataclass field."""
        symbol = getattr(self, attribute)
        if symbol is None:
            return None
        return self.load_symbol(symbol)

    def generate_domain_classes(self, context):
        """Generate platform domain classes from a stable generation context."""
        factory = self.load_optional("domain_class_factory")
        if factory:
            factory(
                [context.composition],
                context.target_package,
                context.component_name,
            )

    def generate_wrapper(self, context):
        """Generate a platform wrapper from a stable generation context."""
        factory = self.load_optional("wrapper_factory")
        if factory:
            factory(
                context.composition,
                context.target_package,
                context.component_name,
            )

    def load_simulation(self):
        """Load the optional platform simulation generator class."""
        return self.load_optional("simulation_class")

    def generate_simulation(self, context):
        """Generate optional simulation and package metadata files."""
        simulation_class = self.load_simulation()
        if simulation_class is None:
            return

        simulation = simulation_class(
            context.composition,
            package_name=context.package_name,
        )
        simulation.generate()
        (context.target_package / "simulation.py").write_text(
            "".join(simulation.result),
            encoding="utf-8",
        )
        (context.target_package / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )

        package_metadata = simulation_class(
            context.composition,
            package_name=context.package_name,
        )
        package_metadata.generate_pyproject()
        (context.target_root / "pyproject.toml").write_text(
            "".join(package_metadata.result),
            encoding="utf-8",
        )
