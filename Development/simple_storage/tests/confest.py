import ape
import pytest
from scripts.deploy_simple_storage import deploy_simple_storage
from scripts.helper_functions import get_account


def pytest_addoption(parser):
    parser.addoption(
        "--wallet-password",
        action="store",
        default=None,
        help="Wallet password for tests.",
    )


@pytest.fixture
def wallet_password(request):
    return request.config.getoption("--wallet-password")


@pytest.fixture
def simple_storage_contract_ape(wallet_password) -> ape.contracts.base.ContractInstance:
    return deploy_simple_storage(unlock_password=wallet_password)
