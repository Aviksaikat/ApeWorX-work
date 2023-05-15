import pytest
from scripts.helper_functions import get_account
from ape import accounts

@pytest.mark.staging
def test_store(simple_storage_contract_ape, wallet_password):
    account = get_account(unlock_password=wallet_password)
    with accounts.use_sender(account):
        simple_storage_contract_ape.store(15)
    assert simple_storage_contract_ape.retrieve() == 15