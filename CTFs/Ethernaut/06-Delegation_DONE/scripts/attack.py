#!/usr/bin/python3
from ape import accounts, networks, project
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


# sepolia: 0xE3C8089e2FBE88995DEA29D91f983aeBE8cDF043
ADDRESS = "0xE3C8089e2FBE88995DEA29D91f983aeBE8cDF043"


def attack():
    attacker = accounts[0]
    contract = project.Delegation.at(ADDRESS)

    print(f"{green}Owner Before The Hack: {magenta}{contract.owner()}{reset}")
    print(f"{red}Attacking Now...{reset}")

    # The call context i.e. msg.sender & msg.value will of the calling contract to the delegated contract. So sharing the storage

    print(f"{green}Attacker Balance After The Hack: {magenta}{contract.owner()}{reset}")

    assert contract.owner() == attacker.address


def main():
    attack()


if __name__ == "__main__":
    main()
