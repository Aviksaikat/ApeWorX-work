#!/usr/bin/python3
from ape import project
from scripts.helper_functions import get_account


def deploy_Fallout(unlocked_password=False) -> project.Fallout:
    owner, _ = get_account(unlock_password=unlocked_password)
    fo = owner.deploy(project.Fallout)

    # print("Contract deployed to: ", fo.address)
    return fo


def main():
    deploy_Fallout("a")
