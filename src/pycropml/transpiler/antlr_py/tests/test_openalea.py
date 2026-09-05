from pathlib import Path

from openalea.core.pkgmanager import PackageManager


EXAMPLES = Path(__file__).parent / "examples"


def test_openalea_package_exposes_energy_balance_composite():
    """Load the local OpenAlea fixture and inspect its composite node."""
    package_directory = EXAMPLES / "openalea" / "SQ_Energy_Balance"
    package_manager = PackageManager()

    package_manager.init(str(package_directory), True)
    composites = package_manager.get_composite_nodes()

    assert len(composites) == 1
    composite = composites[0]
    assert composite.name == "EnergyBalance_wf"
    assert "EnergyBalance" in composite.description
    assert "Authors:" in composite.description
    assert "Institution:" in composite.description
