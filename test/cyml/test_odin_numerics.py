"""The generated Odin code computes what the generated Python code computes.

Needs an Odin compiler ($ODIN or ``odin`` on PATH) and the linker it uses
(``clang`` on Linux and macOS); skipped otherwise. Runs
``example/Monica_SoilTemp``; more packages can be added with
``CROP2ML_ODIN_PACKAGES`` (package directories separated by ``os.pathsep``).
See ``odin_reference.py`` for how inputs are built and compared.
"""
import os
import shutil
import sys
from pathlib import Path

import pytest

from pycropml.cyml import transpile_package

sys.path.insert(0, str(Path(__file__).parent))
from odin_reference import compare  # noqa: E402

EXAMPLE = Path(__file__).resolve().parents[2] / "example" / "Monica_SoilTemp"
DAYS = 30

ODIN = os.environ.get("ODIN") or shutil.which("odin")
LINKER = sys.platform == "win32" or shutil.which("clang")
PACKAGES = [EXAMPLE] + [Path(p) for p in os.environ.get("CROP2ML_ODIN_PACKAGES", "").split(os.pathsep) if p]

pytestmark = pytest.mark.skipif(
    not (ODIN and LINKER), reason="needs an Odin compiler ($ODIN or PATH) and clang to link")


@pytest.mark.parametrize("source", PACKAGES, ids=lambda p: p.name)
def test_odin_matches_python(source, tmp_path):
    package = tmp_path / source.name
    shutil.copytree(source, package, ignore=shutil.ignore_patterns("src"))
    assert transpile_package(package, "py") == 0
    assert transpile_package(package, "odin") == 0

    result = compare(package, DAYS, ODIN, tmp_path / "driver")

    assert result.python_error is None, result.summary()
    assert not result.differences, result.summary()
    assert result.identical + result.close > 0, result.summary()
