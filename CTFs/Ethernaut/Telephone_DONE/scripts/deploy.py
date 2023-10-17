#!/usr/bin/python3
from ape import project
from scripts.helper_functions import get_account


def deploy() -> project.Telephone:
    owner, _ = get_account()
    cf = owner.deploy(project.Telephone)

    # print("Contract deployed to: ", fb.address)
    return cf


def main():
    deploy("a")
