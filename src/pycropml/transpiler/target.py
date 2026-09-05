"""Public contract for Crop2ML target languages and platforms."""

from dataclasses import dataclass
from importlib import import_module
from typing import Optional


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

    def __post_init__(self):
        for attribute in ("name", "module", "generator", "composer"):
            if not getattr(self, attribute):
                raise ValueError(f"TargetPlatform.{attribute} must not be empty")

    def load_symbol(self, symbol):
        """Load *symbol* from the platform module."""
        return getattr(import_module(self.module), symbol)

    def load_generator(self):
        """Load the ModelUnit generator class."""
        return self.load_symbol(self.generator)

    def load_composer(self):
        """Load the model-composition generator class."""
        return self.load_symbol(self.composer)

    def load_optional(self, attribute):
        """Load an optional capability declared by a dataclass field."""
        symbol = getattr(self, attribute)
        if symbol is None:
            return None
        return self.load_symbol(symbol)

    def generate_domain_classes(self, models, output, component_name):
        """Generate platform domain classes when the capability is present."""
        factory = self.load_optional("domain_class_factory")
        if factory:
            factory(models, output, component_name)

    def generate_wrapper(self, model, output, component_name):
        """Generate a platform wrapper when the capability is present."""
        factory = self.load_optional("wrapper_factory")
        if factory:
            factory(model, output, component_name)

    def load_simulation(self):
        """Load the optional platform simulation generator class."""
        return self.load_optional("simulation_class")
