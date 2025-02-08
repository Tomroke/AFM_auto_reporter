from src.tools.positions_searched import positions_searched
import pytest

# Handle command line arguments for the user selecting a month
@pytest.fixture(scope="session")
def month_fixture(pytestconfig):
    return pytestconfig.getoption("month")

# Handle command line arguments for if the user wants, work, interviews or both
@pytest.fixture(scope="session")
def options_fixture(pytestconfig):
    return pytestconfig.getoption("options")

def test_check(month_fixture, options_fixture):
    positions_searched(month_fixture, options_fixture)
