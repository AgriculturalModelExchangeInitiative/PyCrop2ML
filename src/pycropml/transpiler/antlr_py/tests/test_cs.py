from pathlib import Path
from pycropml.transpiler.antlr_py.to_CASG import to_CASG, to_dictASG
from pprint import pprint



EXAMPLES = Path(__file__).parent / "examples"


def test_csharp_source_can_be_converted_to_casg():
    """Parse a deterministic C# strategy and build its common ASG."""
    source = (
        EXAMPLES
        / "SiriusComponent"
        / "phenology"
        / "original"
        / "src"
        / "sirius"
        / "original"
        / "CumulTTFrom.cs"
    )
    code = source.read_text(encoding="utf-8-sig")

    tree = to_dictASG(code, "cs")
    casg = to_CASG(tree)
    for node in casg:
        pprint(node.y, width=120)
    pprint(tree, width=120)

    assert tree["body"]
    assert len(casg) == 1

    module = casg[0]
    assert module.type == "module"
    assert module.pseudo_type == "Void"
    assert "System" in module.using
    assert "SiriusQualityPhenology.DomainClass" in module.using

    namespace = module.body[0]
    assert namespace.type == "namespace"
    assert namespace.name == "SiriusQualityPhenology.Strategies"

    class_node = namespace.body[0][0]
    assert class_node.type == "classDef"
    assert class_node.name == "CumulTTFrom"

    method_names = {
        node.name
        for node in class_node.block
        if node.type == "methodDef"
    }
    assert {"Estimate", "CalculateModel"} <= method_names
