"""Public contract for Crop2ML source languages and platforms."""

from dataclasses import dataclass
from importlib import import_module


@dataclass(frozen=True)
class SourcePlatform:
    """Describe a source adapter that converts a component to Crop2ML."""

    name: str
    module: str
    runner: str

    def __post_init__(self):
        for attribute in ("name", "module", "runner"):
            if not getattr(self, attribute):
                raise ValueError(f"SourcePlatform.{attribute} must not be empty")

    def load_adapter(self):
        """Load the registered component-to-Crop2ML conversion function."""
        return getattr(import_module(self.module), self.runner)

    def convert(self, component, output):
        """Convert *component* into a Crop2ML package under *output*."""
        return self.load_adapter()(component, output)
