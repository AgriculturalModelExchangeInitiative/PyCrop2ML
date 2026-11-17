"""Odin specific rules: types, operators, built-in functions and naming."""
import re

from pycropml.transpiler.rules.generalRule import GeneralRule


# Odin keywords, and builtins/packages a generated variable must not shadow
# (shadowing `len` or `math` would break later calls in the same scope).
RESERVED = {
    "asm", "auto_cast", "bit_field", "bit_set", "break", "case", "cast",
    "context", "continue", "defer", "distinct", "do", "dynamic", "else",
    "enum", "fallthrough", "for", "foreign", "if", "import", "in", "map",
    "matrix", "not_in", "or_break", "or_continue", "or_else", "or_return",
    "package", "proc", "return", "struct", "switch", "transmute", "typeid",
    "union", "using", "when", "where", "nil", "true", "false",
    "len", "cap", "min", "max", "abs", "clamp", "size_of", "align_of",
    "offset_of", "type_of", "append", "delete", "make", "new", "free",
    "resize", "reserve", "clear", "copy", "inject_at", "ordered_remove",
    "unordered_remove", "pop", "assert", "panic", "string", "int", "bool",
    "f32", "f64", "rune", "byte", "any", "rawptr", "uint",
    "math", "slice", "strings", "strconv", "fmt", "cr_math", "allocator",
}


def to_snake(name):
    """``noOfTempLayersPlus1`` -> ``no_of_temp_layers_plus1``, ``LAI`` -> ``lai``."""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", str(name))
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"_+", "_", s.lower())
    return s + "_" if s in RESERVED else s


def to_ada(name):
    """``SoilTemperatureCompState`` -> ``Soil_Temperature_Comp_State``."""
    return "_".join(part[:1].upper() + part[1:] for part in to_snake(name).rstrip("_").split("_") if part)


def package_name(path_name):
    """Odin package identifier for a Crop2ML package directory name."""
    return re.sub(r"\W", "_", str(path_name)).lower()


def string_literal(value):
    value = value.decode() if isinstance(value, bytes) else str(value)
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t")
    return f'"{escaped}"'


def float_literal(value):
    value = str(value)
    if value.endswith("."):
        value += "0"
    if value.startswith("."):
        value = "0" + value
    return value


class OdinRules(GeneralRule):
    def __init__(self):
        GeneralRule.__init__(self)

    types = {
        "int": "int",
        "float": "f64",
        "double": "f64",
        "bool": "bool",
        "str": "string",
        "datetime": "string",
        "DateTime": "string",
    }

    # Odin precedence (higher binds tighter); unary operators are above all of these.
    odin_binop_precedence = {
        "or": 1,
        "and": 2,
        "==": 3, "!=": 3, "<": 3, ">": 3, "<=": 3, ">=": 3,
        "+": 4, "-": 4, "|": 4, "^": 4,
        "*": 5, "/": 5, "%": 5, "&": 5, "<<": 5, ">>": 5,
    }
    odin_unary_precedence = 6
    odin_atom_precedence = 10

    binary_op = {
        "and": "&&",
        "or": "||",
        "==": "==",
        "!=": "!=",
        "<": "<",
        ">": ">",
        "<=": "<=",
        ">=": ">=",
        "+": "+",
        "-": "-",
        "*": "*",
        "/": "/",
        "%": "%",
        "|": "|",
        "&": "&",
        "^": "~",  # Odin's binary xor
        "<<": "<<",
        ">>": ">>",
    }

    unary_op = {
        "not": "!",
        "+": "+",
        "-": "-",
        "~": "~",
    }

    # core:math procs taking and returning f64; int arguments get an f64() cast.
    math_functions = {
        "ln": "math.ln",
        "tan": "math.tan",
        "sin": "math.sin",
        "cos": "math.cos",
        "asin": "math.asin",
        "acos": "math.acos",
        "atan": "math.atan",
        "sqrt": "math.sqrt",
        "exp": "math.exp",
        "pow": "math.pow",
        "floor": "math.floor",
        "ceil": "math.ceil",
        "round": "math.round",
        "isnan": "math.is_nan",
    }

    # core:math name -> cr_math name (CORE-MATH, correctly rounded; MONICA's CONVENTIONS.md
    # requires it for transcendental functions). log is the two-argument form.
    cr_math_functions = {
        "exp": "exp",
        "ln": "log",
        "log": "log",
        "pow": "pow",
        "sin": "sin",
        "cos": "cos",
        "tan": "tan",
        "asin": "asin",
        "acos": "acos",
        "atan": "atan",
    }

    constants = {
        "math": {
            "pi": "math.PI",
        }
    }
