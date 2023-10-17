#!/usr/bin/python3
from ape import accounts, project
from ape.cli import account_option
from scripts.helper_functions import get_account


def deploy_simple_storage(account, unlocked_password=False) -> project.SimpleStorage:
    if unlocked_password:
        account = get_account(unlock_password=unlocked_password)
    else:
        account = accounts.load(account.alias)
        account.set_autosign(True)
    simple_storage = account.deploy(project.SimpleStorage)
    print(account)

    # print(account.balance)
    return simple_storage


@click.command()
@account_option()
def main(account):
    deploy_simple_storage(account)
