from pycropml.transpiler.antlr_py.parse import *
from pycropml.transpiler.helpers import *
import pycropml.transpiler.antlr_py


def process_tree( antlr_tree: ParseTree,
    base_visitor_cls: Type["BaseAstVisitor"] = None,
    transformer_cls = None,
    simplify=True,
) -> "BaseNode":
    cls_registry = BaseNodeRegistry()

    if not base_visitor_cls:
        base_visitor_cls = BaseAstVisitor
    elif not issubclass(base_visitor_cls, BaseAstVisitor):
        raise ValueError("base_visitor_cls must be a BaseAstVisitor subclass")
    tree = base_visitor_cls(cls_registry).visit(antlr_tree)

    if transformer_cls is not None:
        if not issubclass(transformer_cls, BaseNodeTransformer):
            raise ValueError("transformer_cls must be a BaseNodeTransformer subclass")
        tree = transformer_cls(cls_registry).visit(tree)

    if simplify:
        tree = simplify_tree(tree, unpack_lists=False)

    return tree