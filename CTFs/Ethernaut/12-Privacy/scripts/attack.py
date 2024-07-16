#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console

# sepolia: 0x35eA0009d677FB59FE7b17957470Ec8356dA5a4a
ADDRESS = "0x35eA0009d677FB59FE7b17957470Ec8356dA5a4a"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.Privacy.at(ADDRESS)

    console.print(f"[green]Balance Before The Hack: [magenta]{target_contract.balance}")


    console.print(f"[green]Balance After The Hack: [magenta]{target_contract.balance}")

    assert target_contract.balance == 0



def main():
    attack()


if __name__ == "__main__":
    main()
