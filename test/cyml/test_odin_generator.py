"""Tests for the Odin target."""

import os
import shutil
import subprocess
from pathlib import Path

import pytest

from pycropml.cyml import transpile_package
from pycropml.transpiler.generators.odinGenerator import OdinGenerator, OdinNameError
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.rules.odinRules import to_ada, to_snake


EXAMPLE = Path(__file__).resolve().parents[2] / "example" / "Monica_SoilTemp"


def local(name, pseudo_type):
    return Node("local", name=name, pseudo_type=pseudo_type)


def binop(op, left, right, pseudo_type="float"):
    return Node("binary_op", op=op, left=left, right=right, pseudo_type=pseudo_type)


def expr(node):
    return OdinGenerator(None).expr(node)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("noOfTempLayersPlus1", "no_of_temp_layers_plus1"),
        ("hasSnowCover", "has_snow_cover"),
        ("LAI", "lai"),
        ("lti_1", "lti_1"),
        ("in", "in_"),
        ("len", "len_"),
    ],
)
def test_names_become_snake_case(name, expected):
    assert to_snake(name) == expected


def test_type_names_become_ada_case():
    assert to_ada("SoilTemperatureCompState") == "Soil_Temperature_Comp_State"


def test_names_that_collide_after_conversion_are_rejected():
    with pytest.raises(OdinNameError, match="'V' and 'v'"):
        OdinGenerator(None).check_names(["V", "v"], "model")


def test_int_operand_of_float_operation_is_converted():
    node = binop("/", local("x", "float"), local("n", "int"))
    assert expr(node) == "x / f64(n)"


def test_int_literal_stays_untyped():
    node = binop("*", Node("int", value="2", pseudo_type="int"), local("x", "float"))
    assert expr(node) == "2 * x"


def test_int_only_operation_is_not_converted():
    node = binop("-", local("n", "int"), Node("int", value="1", pseudo_type="int"), "int")
    assert expr(node) == "n - 1"


def test_parentheses_follow_odin_precedence():
    a, b, c = local("a", "float"), local("b", "float"), local("c", "float")
    assert expr(binop("-", a, binop("-", b, c))) == "a - (b - c)"
    assert expr(binop("-", binop("-", a, b), c)) == "a - b - c"
    assert expr(binop("*", a, binop("+", b, c))) == "a * (b + c)"


def test_not_wraps_a_comparison():
    test = binop("<", local("a", "float"), local("b", "float"), "bool")
    node = Node("unary_op", operator="not", value=test, pseudo_type="bool")
    assert expr(node) == "!(a < b)"


def test_math_call_arguments_are_typed():
    node = Node(
        "standard_call",
        namespace="math",
        function="pow",
        args=[local("n", "int"), Node("float", value="0.5", pseudo_type="float")],
        pseudo_type="float",
    )
    assert expr(node) == "math.pow(f64(n), f64(0.5))"


def test_log_with_one_argument_is_the_natural_logarithm():
    node = Node("standard_call", namespace="math", function="log",
                args=[local("x", "float")], pseudo_type="float")
    assert expr(node) == "math.ln(x)"


def test_log_with_a_base_keeps_the_base():
    node = Node("standard_call", namespace="math", function="log",
                args=[local("x", "float"), Node("int", value="10", pseudo_type="int")], pseudo_type="float")
    assert expr(node) == "math.log(x, f64(10))"


def test_cr_math_is_used_for_transcendental_functions(monkeypatch):
    monkeypatch.setenv("CYML_ODIN_MATH", "../../support/cr_math")
    generator = OdinGenerator(None)
    call = Node("standard_call", namespace="math", function="exp", args=[local("x", "float")],
                pseudo_type="float")
    assert generator.expr(call) == "cr_math.exp(x)"
    assert generator.imports == {'cr_math "../../support/cr_math"'}


def test_cr_math_log_with_a_base_divides_natural_logarithms(monkeypatch):
    monkeypatch.setenv("CYML_ODIN_MATH", "../../support/cr_math")
    node = Node("standard_call", namespace="math", function="log",
                args=[local("x", "float"), Node("int", value="10", pseudo_type="int")], pseudo_type="float")
    assert expr(node) == "(cr_math.log(x) / cr_math.log(f64(10)))"


def test_functions_cr_math_lacks_stay_core_math(monkeypatch):
    monkeypatch.setenv("CYML_ODIN_MATH", "../../support/cr_math")
    generator = OdinGenerator(None)
    call = Node("standard_call", namespace="math", function="sqrt", args=[local("x", "float")],
                pseudo_type="float")
    assert generator.expr(call) == "math.sqrt(x)"
    assert generator.imports == {'"core:math"'}


def test_assignment_converts_int_to_float_target():
    generator = OdinGenerator(None)
    generator.visit_assignment(Node("assignment", target=local("x", "float"), value=local("i", "int")))
    assert "".join(generator.result).strip() == "x = f64(i)"


def test_assigning_none_to_a_list_clears_it():
    generator = OdinGenerator(None)
    generator.visit_assignment(
        Node("assignment", target=local("xs", ["list", "float"]), value=Node("none"))
    )
    assert "".join(generator.result).strip() == "clear(&xs)"


def test_list_index_is_a_linear_search():
    generator = OdinGenerator(None)
    call = Node("standard_method_call", receiver=local("calendarMoments_t1", ["list", "str"]),
                message="index", args=[Node("str", value="Anthesis", pseudo_type="str")], pseudo_type="int")
    assert generator.expr(call) == '(slice.linear_search(calendar_moments_t1[:], "Anthesis") or_else -1)'
    assert generator.imports == {'"core:slice"'}


def test_numbers_as_conditions_compare_with_zero():
    generator = OdinGenerator(None)
    generator.visit_if_statement(Node("if_statement", test=local("ignoreGrainMaturation", "int"),
                                      block=[], otherwise=[]))
    assert "".join(generator.result).strip().startswith("if ignore_grain_maturation != 0 {")
    not_ = Node("unary_op", operator="not", value=local("n", "int"), pseudo_type="bool")
    assert expr(not_) == "!(n != 0)"
    and_ = binop("and", local("flag", "bool"), local("x", "float"), "bool")
    assert expr(and_) == "flag && x != 0"
    assert expr(Node("unary_op", operator="not", value=local("flag", "bool"), pseudo_type="bool")) == "!flag"


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    package = tmp_path_factory.mktemp("odin") / EXAMPLE.name
    shutil.copytree(EXAMPLE, package, ignore=shutil.ignore_patterns("src"))
    assert transpile_package(package, "odin") == 0
    return package / "src" / "odin" / EXAMPLE.name


def test_package_generates_one_file_per_struct_and_model_unit(generated):
    assert sorted(p.name for p in generated.glob("*.odin")) == [
        "NoSnowSoilSurfaceTemperature.odin",
        "SoilTemperature.odin",
        "SoilTemperatureCompAuxiliary.odin",
        "SoilTemperatureCompComponent.odin",
        "SoilTemperatureCompExogenous.odin",
        "SoilTemperatureCompRate.odin",
        "SoilTemperatureCompState.odin",
        "WithSnowSoilSurfaceTemperature.odin",
    ]


def test_component_drives_the_model_units(generated):
    code = (generated / "SoilTemperatureCompComponent.odin").read_text(encoding="utf-8")
    assert code.startswith("package monica_soiltemp\n")
    assert "soil_temperature_comp_component_calculate_model :: proc(c: ^Soil_Temperature_Comp_Component" in code
    assert "\tsoil_temperature_calculate_model(&c.soil_temperature, s, s1, r, a, ex)\n" in code
    assert "\ts.no_snow_soil_surface_temperature = s.soil_surface_temperature\n" in code


def test_model_unit_has_constructor_with_defaults(generated):
    code = (generated / "NoSnowSoilSurfaceTemperature.odin").read_text(encoding="utf-8")
    assert ("make_no_snow_soil_surface_temperature :: proc(allocator := context.allocator) "
            "-> (m: No_Snow_Soil_Surface_Temperature) {") in code
    assert "\tm.damping_factor = 0.8\n" in code


def test_allocating_procs_take_an_allocator(generated):
    code = (generated / "SoilTemperature.odin").read_text(encoding="utf-8")
    for proc in ("soil_temperature_init", "soil_temperature_calculate_model"):
        header = next(line for line in code.splitlines() if line.startswith(f"{proc} :: proc("))
        assert header.endswith(", allocator := context.allocator) {"), header
    assert code.count("\tcontext.allocator = allocator\n") == 3  # make_, init, calculate_model


def odin_compiler():
    return os.environ.get("ODIN") or shutil.which("odin")


@pytest.mark.skipif(odin_compiler() is None, reason="no Odin compiler (set $ODIN or put odin on PATH)")
def test_generated_package_compiles(generated):
    result = subprocess.run(
        [odin_compiler(), "check", str(generated), "-no-entry-point", "-vet"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
