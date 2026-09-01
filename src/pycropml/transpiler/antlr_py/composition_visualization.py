"""Visualize a CyML composition algorithm as a directed graph."""

from pathlib import Path
import shutil

import networkx as nx
from networkx.drawing.nx_pydot import to_pydot

from .composition_compiler import compile_composition


INPUT_NODE = "__composition_inputs__"
OUTPUT_NODE = "__composition_outputs__"


def create_composition_graph(composition, include_interfaces=False):
    """Create a directed composition graph from a compiled algorithm.

    ModelUnits are always represented. When ``include_interfaces`` is true,
    composition inputs and outputs are represented by two additional nodes.
    Multiple links between the same pair of nodes are retained and labelled.
    """
    name = str(composition.metadata.get("name", "ModelComposition"))
    graph = nx.MultiDiGraph(name=name)
    graph.graph.update(rankdir="LR", label=name, labelloc="t")

    for order, model in enumerate(composition.models, start=1):
        graph.add_node(
            model,
            label=f"{order}. {model}",
            kind="model",
            shape="box",
            style="rounded,filled",
            fillcolor="#dcefd8",
        )

    for link in composition.internal_links:
        source_model, source_port = link["source"].split(".", 1)
        target_model, target_port = link["target"].split(".", 1)
        graph.add_edge(
            source_model,
            target_model,
            kind="internal",
            source_port=source_port,
            target_port=target_port,
            label=f"{source_port} → {target_port}",
            color="#356b35",
        )

    if include_interfaces:
        graph.add_node(
            INPUT_NODE,
            label="Composition inputs",
            kind="inputs",
            shape="oval",
            style="filled",
            fillcolor="#d9eaf7",
        )
        graph.add_node(
            OUTPUT_NODE,
            label="Composition outputs",
            kind="outputs",
            shape="oval",
            style="filled",
            fillcolor="#f8e3c5",
        )
        for link in composition.input_links:
            target_model, target_port = link["target"].split(".", 1)
            graph.add_edge(
                INPUT_NODE,
                target_model,
                kind="input",
                source_port=link["source"],
                target_port=target_port,
                label=f"{link['source']} → {target_port}",
                color="#3979a8",
            )
        for link in composition.output_links:
            source_model, source_port = link["source"].split(".", 1)
            graph.add_edge(
                source_model,
                OUTPUT_NODE,
                kind="output",
                source_port=source_port,
                target_port=link["target"],
                label=f"{source_port} → {link['target']}",
                color="#c47a19",
            )
    return graph


def composition_graph_from_file(
    algorithm_file,
    crop2ml_directory=None,
    include_interfaces=False,
):
    """Compile an algorithm file and return its NetworkX graph."""
    composition, _ = compile_composition(algorithm_file, crop2ml_directory)
    return create_composition_graph(composition, include_interfaces)


def write_composition_graph(
    algorithm_file,
    output_file,
    crop2ml_directory=None,
    include_interfaces=False,
):
    """Write a composition graph as DOT, SVG, PNG, or PDF."""
    output_file = Path(output_file)
    graph = composition_graph_from_file(
        algorithm_file,
        crop2ml_directory,
        include_interfaces,
    )
    dot_graph = to_pydot(graph)
    output_format = output_file.suffix.lower().lstrip(".") or "dot"
    if output_format in {"dot", "gv"}:
        output_file.write_text(dot_graph.to_string(), encoding="utf-8")
    elif output_format in {"svg", "png", "pdf"}:
        if shutil.which("dot") is None:
            raise RuntimeError(
                "Graphviz executable 'dot' is required to render "
                f"{output_format.upper()}; write a .dot file instead or install Graphviz"
            )
        dot_graph.write(str(output_file), format=output_format, prog="dot")
    else:
        raise ValueError("Graph format must be .dot, .gv, .svg, .png, or .pdf")
    return output_file


def display_composition_graph(
    algorithm_file,
    crop2ml_directory=None,
    include_interfaces=False,
):
    """Render and display the graph as SVG in a Jupyter notebook."""
    if shutil.which("dot") is None:
        raise RuntimeError("Graphviz executable 'dot' is required for notebook display")
    from IPython.display import SVG, display

    graph = composition_graph_from_file(
        algorithm_file,
        crop2ml_directory,
        include_interfaces,
    )
    svg = to_pydot(graph).create_svg(prog="dot")
    rendered = SVG(svg)
    display(rendered)
    return rendered
