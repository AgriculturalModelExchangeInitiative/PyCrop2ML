"""Tests for context-sensitive source and target selection in the CLI."""

import sys

import pytest

import pycropml.main as cli


def test_package_mode_dispatches_a_target(monkeypatch, tmp_path):
    calls = []
    package = tmp_path / "package"
    package.mkdir()
    monkeypatch.setattr(
        cli, "transpile_package",
        lambda source, target: calls.append((source, target)),
    )
    monkeypatch.setattr(sys, "argv", ["cyml", "-p", str(package), "r"])

    cli.main()

    assert calls == [(package, "r")]


def test_positional_package_dispatches_a_target(monkeypatch, tmp_path):
    calls = []
    package = tmp_path / "package"
    package.mkdir()
    monkeypatch.setattr(
        cli, "transpile_package",
        lambda source, target: calls.append((source, target)),
    )
    monkeypatch.setattr(sys, "argv", ["cyml", str(package), "py"])

    cli.main()

    assert calls == [(package, "py")]


def test_component_mode_dispatches_a_source(monkeypatch, tmp_path):
    calls = []
    component = tmp_path / "component"
    component.mkdir()
    output = tmp_path / "output"
    monkeypatch.setattr(
        cli, "transpile_component",
        lambda source, package, language: calls.append(
            (source, package, language)
        ),
    )
    monkeypatch.setattr(
        sys, "argv",
        ["cyml", "-c", str(component), str(output), "apsim"],
    )

    cli.main()

    assert calls == [(component, str(output), "apsim")]


def test_component_mode_rejects_a_target_only_name(
    monkeypatch, tmp_path, capsys
):
    component = tmp_path / "component"
    component.mkdir()
    monkeypatch.setattr(
        sys, "argv",
        ["cyml", "-c", str(component), "output", "r"],
    )

    with pytest.raises(SystemExit):
        cli.main()

    assert "r is not a supported source" in capsys.readouterr().err


def test_component_mode_reports_the_missing_path(monkeypatch, capsys):
    missing = "BiomaSurfacePartonSoilSWAT"
    monkeypatch.setattr(
        sys, "argv", ["cyml", "-c", missing, missing, "bioma"]
    )

    with pytest.raises(SystemExit) as error:
        cli.main()

    assert error.value.code == 2
    assert (
        f"Component directory does not exist: {missing}"
        in capsys.readouterr().err
    )


def test_help_lists_sources_and_targets(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["cyml", "--help"])

    with pytest.raises(SystemExit) as error:
        cli.main()

    assert error.value.code == 0
    output = capsys.readouterr().out
    assert "Available targets:" in output
    assert "Available sources:" in output


def test_help_lists_discovered_external_targets(monkeypatch, capsys):
    monkeypatch.setattr(
        cli,
        "available_targets",
        lambda: {"py": object(), "external": object()},
    )
    monkeypatch.setattr(sys, "argv", ["cyml", "--help"])

    with pytest.raises(SystemExit) as error:
        cli.main()

    assert error.value.code == 0
    assert "Available targets: py, external" in capsys.readouterr().out
