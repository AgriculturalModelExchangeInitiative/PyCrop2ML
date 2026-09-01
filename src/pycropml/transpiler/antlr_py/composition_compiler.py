"""Parse and compile composition algorithms to Crop2ML composition XML."""

from pathlib import Path
import os
import re
import xml.etree.ElementTree as ET

from antlr4 import CommonTokenStream, FileStream
import yaml

from .composition_visitor import (
    CompositionSemanticError,
    SemanticCompositionVisitor,
    load_model_interfaces,
)
from .grammars.Crop2MLCompositionLexer import Crop2MLCompositionLexer
from .grammars.Crop2MLCompositionParser import Crop2MLCompositionParser


DOCSTRING_PATTERN = re.compile(
    r'''^\s*(?P<quote>"""|\'\'\')(?P<content>.*?)(?P=quote)''',
    re.DOTALL,
)
COMPOSITION_MARKER = re.compile(
    r"(?m)^\s*type\s*:\s*composition\s*(?:#.*)?$"
)


def read_algorithm_metadata(filename):
    """Read YAML metadata when a source starts with a composition docstring."""
    filename = Path(filename)
    match = DOCSTRING_PATTERN.match(filename.read_text(encoding="utf-8"))
    if match is None or COMPOSITION_MARKER.search(match.group("content")) is None:
        return None
    try:
        metadata = yaml.safe_load(match.group("content"))
    except yaml.YAMLError as error:
        raise CompositionSemanticError(
            f"Invalid YAML metadata in {filename}: {error}"
        ) from error
    if not isinstance(metadata, dict):
        raise CompositionSemanticError(
            f"Composition metadata in {filename} must be a YAML mapping"
        )
    return metadata


def find_composition_algorithms(crop2ml_directory):
    """Find every marked composition algorithm below crop2ml/algo."""
    algorithm_directory = Path(crop2ml_directory) / "algo"
    return [
        filename
        for filename in sorted(algorithm_directory.glob("**/*.pyx"))
        if read_algorithm_metadata(filename) is not None
    ]


def find_composition_algorithm(crop2ml_directory, name=None):
    """Find one composition algorithm, optionally selected by metadata name."""
    candidates = find_composition_algorithms(crop2ml_directory)
    if name is not None:
        candidates = [
            filename
            for filename in candidates
            if read_algorithm_metadata(filename).get("name") == name
        ]
    if not candidates:
        requested = f" named {name!r}" if name is not None else ""
        raise FileNotFoundError(
            f"No composition algorithm{requested} found in {crop2ml_directory}"
        )
    if len(candidates) > 1:
        raise CompositionSemanticError(
            "Several composition algorithms were found: "
            + ", ".join(str(filename) for filename in candidates)
        )
    return candidates[0]


def find_crop2ml_directory(algorithm_file):
    """Find the nearest ancestor containing ModelUnit XML descriptions."""
    path = Path(algorithm_file).resolve().parent
    for directory in (path, *path.parents):
        if any(directory.glob("unit.*.xml")):
            return directory
    raise FileNotFoundError(f"No unit.*.xml files found above {algorithm_file}")


def parse_composition(algorithm_file, error_listener=None):
    lexer = Crop2MLCompositionLexer(FileStream(str(algorithm_file), encoding="utf-8"))
    parser = Crop2MLCompositionParser(CommonTokenStream(lexer))
    if error_listener is not None:
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
    return parser, parser.composition()


def compile_composition(algorithm_file, crop2ml_directory=None, error_listener=None):
    algorithm_file = Path(algorithm_file)
    directory = (
        Path(crop2ml_directory)
        if crop2ml_directory is not None
        else find_crop2ml_directory(algorithm_file)
    )
    parser, tree = parse_composition(algorithm_file, error_listener)
    if parser.getNumberOfSyntaxErrors() or (error_listener and error_listener.errors):
        return None, directory
    interfaces = load_model_interfaces(directory)
    result = SemanticCompositionVisitor(interfaces).visit(tree)
    return result, directory


def composition_xml(algorithm, interfaces, algorithm_file, crop2ml_directory):
    metadata = algorithm.metadata
    description = metadata["description"]
    attributes = {"name": str(metadata["name"]), "id": str(metadata["id"])}
    for name in ("version", "timestep"):
        if name in metadata:
            attributes[name] = str(metadata[name])

    root = ET.Element("ModelComposition", attributes)
    description_element = ET.SubElement(root, "Description")
    fields = (
        ("Title", "title"),
        ("Authors", "authors"),
        ("Institution", "institution"),
        ("Reference", "reference"),
        ("ExtendedDescription", "extended_description"),
        ("ShortDescription", "short_description"),
    )
    for xml_name, yaml_name in fields:
        node = ET.SubElement(description_element, xml_name)
        node.text = str(description.get(yaml_name, ""))

    algorithm_path = os.path.relpath(Path(algorithm_file).resolve(), Path(crop2ml_directory).resolve())
    ET.SubElement(
        root,
        "Algorithm",
        {"language": "cyml-composition", "filename": algorithm_path},
    )
    composition = ET.SubElement(root, "Composition")
    for model in algorithm.models:
        interface = interfaces[model]
        ET.SubElement(
            composition,
            "Model",
            {
                "name": model,
                "id": interface.identifier,
                "filename": os.path.relpath(interface.filename, crop2ml_directory),
            },
        )

    links = ET.SubElement(composition, "Links")
    for tag, values in (
        ("InputLink", algorithm.input_links),
        ("InternalLink", algorithm.internal_links),
        ("OutputLink", algorithm.output_links),
    ):
        for link in values:
            ET.SubElement(links, tag, link)
    ET.indent(root, space="    ")
    return root


def write_composition_xml(algorithm_file, output_file=None, crop2ml_directory=None):
    result, directory = compile_composition(algorithm_file, crop2ml_directory)
    interfaces = load_model_interfaces(directory)
    root = composition_xml(result, interfaces, algorithm_file, directory)
    if output_file is None:
        output_file = directory / f"composition.{result.metadata['name']}.xml"
    output_file = Path(output_file)
    body = ET.tostring(root, encoding="unicode")
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE ModelComposition PUBLIC " " '
        '"https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">\n'
        f"{body}\n"
    )
    output_file.write_text(content, encoding="utf-8")
    return output_file
