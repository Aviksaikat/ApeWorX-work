#!/usr/bin/python3
from ape import project
from scripts.helper_functions import get_account


def deploy_simple_storage(unlocked_password=False) -> project.SimpleStorage:
    account = get_account(unlock_password=unlocked_password)
    simple_storage = account.deploy(project.SimpleStorage)
    
    #print(account.balance)
    return simple_storage

def main():
    deploy_simple_storage("a")