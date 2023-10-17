#!/usr/bin/python3
from ape import project
from scripts.helper_functions import get_account


def deploy_fallback(unlocked_password=False) -> project.Fallback:
    owner, _ = get_account(unlock_password=unlocked_password)
    fb = owner.deploy(project.Fallback)

    # print("Contract deployed to: ", fb.address)
    return fb


def main():
    deploy_fallback("a")
