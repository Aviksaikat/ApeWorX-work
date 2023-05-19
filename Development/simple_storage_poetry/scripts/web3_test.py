from ape import networks
web3 = networks.provider._web3
from eth_abi import encode

encoded_data = encode(
    ["uint", "string", "address"],
    [1, "test1", "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"],
)

def main():
	print(web3.solidity_keccak(["uint8"], [0]).hex())
	print(web3.keccak(0).hex())

	print(web3.keccak(encoded_data).hex())

if __name__ == "__main__":
	main()