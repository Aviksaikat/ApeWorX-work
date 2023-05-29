#!/usr/bin/python3
from ape import project
from scripts.helper_functions import get_account


def deploy(unlocked_password=False) -> project.CoinFlip:
    owner, _ = get_account(unlock_password=unlocked_password)
    cf = owner.deploy(project.CoinFlip)
    
    #print("Contract deployed to: ", fb.address)
    return cf

def main():
    deploy("a")