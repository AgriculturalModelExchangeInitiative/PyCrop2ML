"""Stable context passed to Crop2ML target-platform hooks."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class GenerationContext:
    """Collect models, names, paths, and extensible options for one build."""

    package: Path
    package_name: str
    target_name: str
    model_units: List[Any]
    composition: Any
    component_name: str
    crop2ml_directory: Path
    cyml_directory: Path
    target_root: Path
    target_package: Path
    test_directory: Path
    documentation_directory: Path
    image_directory: Path
    metadata: Dict[str, Any] = field(default_factory=dict)
    options: Dict[str, Any] = field(default_factory=dict)
