"""Bitwise operators (| & ^ << >> ~) from CyML to the targets that support them."""

import pytest

from pycropml.transpiler.errors import PseudoCythonTypeCheckError
from pycropml.transpiler.main import Main

SOURCE = '''
def bitops(int a, int b, bool p, bool q):
    cdef int x
    cdef bool w
    x = a | b
    x = (a & b) | (a ^ b)
    x = (a + b) << 2
    x = a >> (b - 1)
    x = ~a
    w = (a & b) == 0
    w = p | q
    return x
'''


def transpile(language, source=SOURCE):
    main = Main(source, language)
    main.parse()
    main.to_ast(source)
    return main.to_source()


@pytest.mark.parametrize(("language", "expected"), [
    ("odin", [
        "x = a | b",
        "x = a & b | (a ~ b)",          # & binds tighter than | in Odin; ~ is xor
        "x = (a + b) << 2",
        "x = a >> uint(b - 1)",         # Odin shifts by an unsigned count
        "x = ~a",
        "w = a & b == 0",               # & binds tighter than == in Odin
        "w = p | q",
    ]),
    ("cpp2", [
        "x = (a | b);",
        "x = ((a & b) | (a ^ b));",
        "x = ((a + b) << 2);",
        "x = (a >> (b - 1));",
        "x = ~a;",
        "w = (a & b) == 0;",            # == binds tighter than & in C++
        "w = (p | q);",
    ]),
    ("py", [
        "x = a | b",
        "x = a & b | (a ^ b)",
        "x = a + b << 2",
        "x = a >> (b - 1)",
        "x = ~a",
        "w = a & b == 0",
        "w = p | q",
    ]),
])
def test_bitwise_operators_keep_their_meaning(language, expected):
    lines = [line.strip() for line in transpile(language).splitlines()]
    for statement in expected:
        assert statement in lines, f"{statement!r} not in {language} output:\n" + "\n".join(lines)


def test_tilde_needs_an_int():
    source = '''
def f(float a):
    cdef float x
    x = ~a
    return x
'''
    with pytest.raises(PseudoCythonTypeCheckError):
        transpile("odin", source)
