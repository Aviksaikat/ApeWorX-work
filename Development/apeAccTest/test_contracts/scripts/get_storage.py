from scripts.deploy_simple_storage import deploy_simple_storage
from scripts.helper_functions import get_account


def test_simple_storage():
    simple_storage = deploy_simple_storage()

    assert simple_storage.retrieve() == 0


def test_retrieve_data():
    simple_storage = deploy_simple_storage()
    account = get_account()

    expected = 15
    # * we can send a tx both ways
    txn = simple_storage.store(expected, sender=account)
    print(simple_storage.retrieve())

    # txn = simple_storage.store.as_transaction(expected, sender=account)
    # account.call(txn)

    # Assert
    assert expected == simple_storage.retrieve()


def main():
    test_simple_storage()
    test_retrieve_data()
