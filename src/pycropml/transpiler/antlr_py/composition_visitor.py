"""Semantic visitor for the Crop2ML composition language."""

from dataclasses import dataclass, field
from pathlib import Path
import xml.etree.ElementTree as ET

import yaml

from .grammars.Crop2MLCompositionVisitor import Crop2MLCompositionVisitor


REQUIRED_METADATA = {"type", "name", "id", "description"}
ALLOWED_METADATA = {"type", "name", "id", "version", "timestep", "description"}
REQUIRED_DESCRIPTION = {"title", "authors", "institution", "extended_description"}
ALLOWED_DESCRIPTION = REQUIRED_DESCRIPTION | {"reference", "short_description"}


class CompositionSemanticError(ValueError):
    """An invalid reference or declaration in a composition algorithm."""

    def __init__(self, message, line=None, column=None):
        if line is not None:
            message = f"{line}:{column}: {message}"
        super().__init__(message)


@dataclass(frozen=True)
class PortDefinition:
    name: str
    datatype: str
    unit: str | None = None
    category: str | None = None


@dataclass(frozen=True)
class ModelInterface:
    name: str
    identifier: str
    filename: Path
    inputs: dict[str, PortDefinition]
    outputs: dict[str, PortDefinition]


@dataclass(frozen=True)
class ModelPort:
    model: str
    port: str

    def __str__(self):
        return f"{self.model}.{self.port}"


@dataclass
class CompositionAlgorithm:
    metadata: dict = field(default_factory=dict)
    models: list[str] = field(default_factory=list)
    input_links: list[dict[str, str]] = field(default_factory=list)
    internal_links: list[dict[str, str]] = field(default_factory=list)
    output_links: list[dict[str, str]] = field(default_factory=list)


def _ports(root, section, element):
    result = {}
    for node in root.findall(f"./{section}/{element}"):
        name = node.attrib["name"]
        result[name] = PortDefinition(
            name=name,
            datatype=node.attrib.get("datatype", ""),
            unit=node.attrib.get("unit"),
            category=(
                node.attrib.get("variablecategory")
                or node.attrib.get("parametercategory")
            ),
        )
    return result


def load_model_interfaces(crop2ml_directory):
    """Load all unit.*.xml interfaces indexed by their ModelUnit name."""
    directory = Path(crop2ml_directory)
    interfaces = {}
    for filename in sorted(directory.glob("unit.*.xml")):
        root = ET.parse(filename).getroot()
        if root.tag != "ModelUnit":
            continue
        name = root.attrib["name"]
        if name in interfaces:
            raise CompositionSemanticError(f"Duplicate ModelUnit name: {name}")
        interfaces[name] = ModelInterface(
            name=name,
            identifier=root.attrib.get("modelid", root.attrib.get("id", name)),
            filename=filename,
            inputs=_ports(root, "Inputs", "Input"),
            outputs=_ports(root, "Outputs", "Output"),
        )
    return interfaces


class SemanticCompositionVisitor(Crop2MLCompositionVisitor):
    """Validate a parse tree and lower it to models and Crop2ML links."""

    def __init__(self, interfaces):
        self.interfaces = interfaces
        self.algorithm = CompositionAlgorithm()
        self.pending_bindings = {}
        self.called_models = set()
        self.output_names = set()

    def visitComposition(self, ctx):
        self.visitChildren(ctx)
        self._validate_metadata(ctx)
        if not self.algorithm.models:
            self._error(ctx, "A composition must call at least one ModelUnit")
        unconsumed = [
            f"{model}.{port}"
            for model, bindings in self.pending_bindings.items()
            for port in bindings
        ]
        if unconsumed:
            self._error(ctx, "Inputs assigned to a ModelUnit that is never called: " + ", ".join(unconsumed))
        return self.algorithm

    def visitDocumentation(self, ctx):
        token = ctx.DOCSTRING().getText()
        try:
            metadata = yaml.safe_load(token[3:-3])
        except yaml.YAMLError as error:
            self._error(ctx, f"Invalid YAML metadata: {error}")
        if not isinstance(metadata, dict):
            self._error(ctx, "The YAML docstring must contain a mapping")
        self.algorithm.metadata = metadata

    def visitModelInputAssignment(self, ctx):
        target = self._model_port(ctx.modelPort())
        interface = self._require_model(target.model, ctx)
        self._require_port(interface.inputs, target, "input", ctx)
        if target.model in self.called_models:
            self._error(ctx, f"Input assignment for {target} must appear before its model call")

        bindings = self.pending_bindings.setdefault(target.model, {})
        if target.port in bindings:
            self._error(ctx, f"Duplicate assignment for input {target}")

        source_ctx = ctx.source()
        if source_ctx.modelPort() is None:
            source = source_ctx.identifier().getText()
        else:
            source = self._model_port(source_ctx.modelPort())
            source_interface = self._require_model(source.model, ctx)
            source_definition = self._require_port(
                source_interface.outputs, source, "output", ctx
            )
            if source.model not in self.called_models:
                self._error(ctx, f"Output {source} is used before {source.model} is called")
            target_definition = interface.inputs[target.port]
            self._validate_compatibility(source_definition, target_definition, source, target, ctx)
        bindings[target.port] = source

    def visitModelCall(self, ctx):
        model = ctx.modelName().getText()
        interface = self._require_model(model, ctx)
        if model in self.called_models:
            self._error(ctx, f"ModelUnit {model} is called more than once")

        bindings = self.pending_bindings.pop(model, {})
        for port in interface.inputs:
            target = f"{model}.{port}"
            source = bindings.get(port, port)
            link = {"source": str(source), "target": target}
            if isinstance(source, ModelPort):
                self.algorithm.internal_links.append(link)
            else:
                self.algorithm.input_links.append(link)

        self.algorithm.models.append(model)
        self.called_models.add(model)

    def visitCompositionOutputAssignment(self, ctx):
        target = ctx.identifier().getText()
        source = self._model_port(ctx.modelPort())
        interface = self._require_model(source.model, ctx)
        self._require_port(interface.outputs, source, "output", ctx)
        if source.model not in self.called_models:
            self._error(ctx, f"Output {source} is published before {source.model} is called")
        if target in self.output_names:
            self._error(ctx, f"Duplicate composition output: {target}")
        self.output_names.add(target)
        self.algorithm.output_links.append({"source": str(source), "target": target})

    def _validate_metadata(self, ctx):
        metadata = self.algorithm.metadata
        unknown = set(metadata) - ALLOWED_METADATA
        missing = REQUIRED_METADATA - set(metadata)
        if unknown:
            self._error(ctx, "Unknown metadata fields: " + ", ".join(sorted(unknown)))
        if missing:
            self._error(ctx, "Missing metadata fields: " + ", ".join(sorted(missing)))
        if metadata.get("type") != "composition":
            self._error(ctx, "Metadata type must be 'composition'")
        description = metadata.get("description")
        if not isinstance(description, dict):
            self._error(ctx, "description must be a YAML mapping")
        unknown = set(description) - ALLOWED_DESCRIPTION
        missing = REQUIRED_DESCRIPTION - set(description)
        if unknown:
            self._error(ctx, "Unknown description fields: " + ", ".join(sorted(unknown)))
        if missing:
            self._error(ctx, "Missing description fields: " + ", ".join(sorted(missing)))
        if not str(metadata.get("name", "")).strip() or not str(metadata.get("id", "")).strip():
            self._error(ctx, "name and id must not be empty")
        if "timestep" in metadata and float(metadata["timestep"]) <= 0:
            self._error(ctx, "timestep must be positive")

    def _require_model(self, name, ctx):
        try:
            return self.interfaces[name]
        except KeyError:
            self._error(ctx, f"Unknown ModelUnit: {name}")

    def _require_port(self, ports, port, kind, ctx):
        try:
            return ports[port.port]
        except KeyError:
            self._error(ctx, f"Unknown {kind} port: {port}")

    def _validate_compatibility(self, source_definition, target_definition, source, target, ctx):
        if source_definition.datatype != target_definition.datatype:
            self._error(
                ctx,
                f"Datatype mismatch: {source} ({source_definition.datatype}) -> "
                f"{target} ({target_definition.datatype})",
            )
        source_unit = (source_definition.unit or "").strip()
        target_unit = (target_definition.unit or "").strip()
        if source_unit and target_unit and source_unit != target_unit:
            self._error(ctx, f"Unit mismatch: {source} ({source_unit}) -> {target} ({target_unit})")

    @staticmethod
    def _model_port(ctx):
        return ModelPort(
            model=ctx.modelName().getText(),
            port=ctx.portName().getText(),
        )

    @staticmethod
    def _error(ctx, message):
        raise CompositionSemanticError(message, ctx.start.line, ctx.start.column)
