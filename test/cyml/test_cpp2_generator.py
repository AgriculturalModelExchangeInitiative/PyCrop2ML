"""Tests for the cpp2 target."""

import shutil
import subprocess

import pytest

from pycropml.transpiler.main import Main

HELPER = '''
def add(int a, int b):
    cdef int x
    cdef float y
    x = a + b
    y = 2.0 * x
    if y > 10.0:
        x = 10
    return x
'''


def transpile(source):
    main = Main(source, "cpp2")
    main.parse()
    main.to_ast(source)
    return main.to_source()


def test_returned_local_of_a_helper_function_is_declared():
    lines = [line.strip() for line in transpile(HELPER).splitlines()]
    assert "int x;" in lines
    assert "double y;" in lines


@pytest.mark.skipif(shutil.which("clang++") is None, reason="no clang++ on PATH")
def test_helper_function_compiles(tmp_path):
    source = tmp_path / "helper.cpp"
    source.write_text(transpile(HELPER), encoding="utf-8")
    result = subprocess.run(["clang++", "-fsyntax-only", "-Wall", "-Werror",
                             "-Wno-unused-command-line-argument", str(source)],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
