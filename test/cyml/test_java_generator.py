"""Regression tests for Java domain-class generation."""

import pytest

from pycropml.transpiler.codeGenerator import CodeGenerator
from pycropml.transpiler.generators import javaGenerator
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.rules.javaRules import JavaRules


def make_generator():
    generator = object.__new__(javaGenerator.JavaGenerator)
    CodeGenerator.__init__(generator)
    JavaRules.__init__(generator)
    return generator


@pytest.mark.parametrize(
    ("operator", "expected"),
    [
        ("==", 'Objects.equals(ISWWAT, "Y")'),
        ("!=", '!Objects.equals(ISWWAT, "Y")'),
    ],
)
def test_string_comparison_uses_value_equality(operator, expected):
    generator = make_generator()
    comparison = Node(
        "comparison",
        op=operator,
        left=Node("local", name="ISWWAT", pseudo_type="str"),
        right=Node("str", value="Y"),
    )

    generator.visit_comparison(comparison)

    assert "".join(generator.result) == expected


def test_numeric_comparison_keeps_java_operator():
    generator = make_generator()
    comparison = Node(
        "comparison",
        op="==",
        left=Node("local", name="day", pseudo_type="int"),
        right=Node("int", value="30"),
    )

    generator.visit_comparison(comparison)

    assert "".join(generator.result) == "day == 30"


def test_repeated_array_value_uses_java_arrays_fill():
    generator = make_generator()
    assignment = Node(
        "assignment",
        target=Node("local", name="WetDay"),
        value=Node(
            "binary_op",
            op="*",
            left=Node("list", elements=[Node("int", value="0")]),
            right=Node("int", value="30"),
        ),
    )

    generator.visit_assignment(assignment)

    assert "".join(generator.result) == "Arrays.fill(WetDay, 0);"


def test_java_domain_class_paths_are_formatted_before_joining(
    monkeypatch, tmp_path
):
    class StubJavaTrans:
        def __init__(self, models):
            self.result = []
            self.node_states = []
            self.node_rates = []
            self.node_auxiliary = []
            self.node_exogenous = []

        def model2Node(self):
            pass

        def generate(self, nodes, name):
            self.result.append(name)

    monkeypatch.setattr(javaGenerator, "JavaTrans", StubJavaTrans)

    javaGenerator.to_struct_java([], tmp_path, "Example")

    assert {path.name for path in tmp_path.iterdir()} == {
        "ExampleState.java",
        "ExampleRate.java",
        "ExampleAuxiliary.java",
        "ExampleExogenous.java",
    }
