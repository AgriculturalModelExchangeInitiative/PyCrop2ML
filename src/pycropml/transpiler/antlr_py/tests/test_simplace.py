from pathlib import Path

from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
from pycropml.transpiler.pseudo_tree import Node


EXAMPLES = Path(__file__).parent / "examples"


def walk_nodes(value):
    """Yield every Node contained in a CASG value."""
    if isinstance(value, Node):
        yield value
        for child in vars(value).values():
            yield from walk_nodes(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            yield from walk_nodes(child)
    elif isinstance(value, dict):
        for child in value.values():
            yield from walk_nodes(child)


def test_simplace_java_source_can_be_converted_to_casg():
    """Parse a deterministic Simplace Java component and build its CASG."""
    source = (
        EXAMPLES
        / "SimplaceComponent"
        / "Simplace_SoilTemperature"
        / "original"
        / "STMPsimCalculator.java"
    )
    code = source.read_text(encoding="utf-8-sig")

    tree = to_dictASG(code, "java")
    casg = to_CASG(tree)
    nodes = list(walk_nodes(casg))

    assert tree["body"]
    assert casg
    assert any(
        node.type == "classDef" and node.name == "STMPsimCalculator"
        for node in nodes
    )
    method_names = {
        node.name
        for node in nodes
        if node.type == "methodDef"
    }
    assert {"createVariables", "init", "process"} <= method_names
