import json
from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv
from web3.middleware import construct_sign_and_send_raw_middleware

load_dotenv(find_dotenv())

blockchain_url = "https://ropsten.infura.io/v3/" + os.getenv('INFURA_KEY')
web3 = Web3(Web3.HTTPProvider(blockchain_url))

web3.middleware_onion.add(construct_sign_and_send_raw_middleware(os.getenv('METAMASK_PRIVATE_KEY')))

web3.eth.defaultAccount = os.getenv('METAMASK_ETH_ADDRESS')

abi = json.loads('[{"inputs": [],"name": "Greet","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "string","name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "greet","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]')

# bytecode = {
# 	"functionDebugData": {},
# 	"generatedSources": [],
# 	"linkReferences": {},
# 	"object": "608060405234801561001057600080fd5b506105c2806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c80635ae5d4aa14610051578063a41368621461005b578063cfae321714610077578063ef690cc014610095575b600080fd5b6100596100b3565b005b6100756004803603810190610070919061034e565b610101565b005b61007f61011b565b60405161008c91906103d0565b60405180910390f35b61009d6101ad565b6040516100aa91906103d0565b60405180910390f35b6040518060400160405280600581526020017f48656c6c6f000000000000000000000000000000000000000000000000000000815250600090805190602001906100fe92919061023b565b50565b806000908051906020019061011792919061023b565b5050565b60606000805461012a906104a6565b80601f0160208091040260200160405190810160405280929190818152602001828054610156906104a6565b80156101a35780601f10610178576101008083540402835291602001916101a3565b820191906000526020600020905b81548152906001019060200180831161018657829003601f168201915b5050505050905090565b600080546101ba906104a6565b80601f01602080910402602001604051908101604052809291908181526020018280546101e6906104a6565b80156102335780601f1061020857610100808354040283529160200191610233565b820191906000526020600020905b81548152906001019060200180831161021657829003601f168201915b505050505081565b828054610247906104a6565b90600052602060002090601f01602090048101928261026957600085556102b0565b82601f1061028257805160ff19168380011785556102b0565b828001600101855582156102b0579182015b828111156102af578251825591602001919060010190610294565b5b5090506102bd91906102c1565b5090565b5b808211156102da5760008160009055506001016102c2565b5090565b60006102f16102ec84610417565b6103f2565b90508281526020810184848401111561030d5761030c61056c565b5b610318848285610464565b509392505050565b600082601f83011261033557610334610567565b5b81356103458482602086016102de565b91505092915050565b60006020828403121561036457610363610576565b5b600082013567ffffffffffffffff81111561038257610381610571565b5b61038e84828501610320565b91505092915050565b60006103a282610448565b6103ac8185610453565b93506103bc818560208601610473565b6103c58161057b565b840191505092915050565b600060208201905081810360008301526103ea8184610397565b905092915050565b60006103fc61040d565b905061040882826104d8565b919050565b6000604051905090565b600067ffffffffffffffff82111561043257610431610538565b5b61043b8261057b565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b83811015610491578082015181840152602081019050610476565b838111156104a0576000848401525b50505050565b600060028204905060018216806104be57607f821691505b602082108114156104d2576104d1610509565b5b50919050565b6104e18261057b565b810181811067ffffffffffffffff82111715610500576104ff610538565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea26469706673582212206a63a20dec8282c1b9e9d6f5a68e26b55bce178e28e3888d2bb9daa995cc0cd564736f6c63430008070033",
# 	"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x5C2 DUP1 PUSH2 0x20 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x4 CALLDATASIZE LT PUSH2 0x4C JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x5AE5D4AA EQ PUSH2 0x51 JUMPI DUP1 PUSH4 0xA4136862 EQ PUSH2 0x5B JUMPI DUP1 PUSH4 0xCFAE3217 EQ PUSH2 0x77 JUMPI DUP1 PUSH4 0xEF690CC0 EQ PUSH2 0x95 JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x59 PUSH2 0xB3 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x75 PUSH1 0x4 DUP1 CALLDATASIZE SUB DUP2 ADD SWAP1 PUSH2 0x70 SWAP2 SWAP1 PUSH2 0x34E JUMP JUMPDEST PUSH2 0x101 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x7F PUSH2 0x11B JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x8C SWAP2 SWAP1 PUSH2 0x3D0 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x9D PUSH2 0x1AD JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0xAA SWAP2 SWAP1 PUSH2 0x3D0 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH1 0x40 MLOAD DUP1 PUSH1 0x40 ADD PUSH1 0x40 MSTORE DUP1 PUSH1 0x5 DUP2 MSTORE PUSH1 0x20 ADD PUSH32 0x48656C6C6F000000000000000000000000000000000000000000000000000000 DUP2 MSTORE POP PUSH1 0x0 SWAP1 DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH2 0xFE SWAP3 SWAP2 SWAP1 PUSH2 0x23B JUMP JUMPDEST POP JUMP JUMPDEST DUP1 PUSH1 0x0 SWAP1 DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH2 0x117 SWAP3 SWAP2 SWAP1 PUSH2 0x23B JUMP JUMPDEST POP POP JUMP JUMPDEST PUSH1 0x60 PUSH1 0x0 DUP1 SLOAD PUSH2 0x12A SWAP1 PUSH2 0x4A6 JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x156 SWAP1 PUSH2 0x4A6 JUMP JUMPDEST DUP1 ISZERO PUSH2 0x1A3 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x178 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x1A3 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x186 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD PUSH2 0x1BA SWAP1 PUSH2 0x4A6 JUMP JUMPDEST DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH2 0x1E6 SWAP1 PUSH2 0x4A6 JUMP JUMPDEST DUP1 ISZERO PUSH2 0x233 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x208 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x233 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x216 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST DUP3 DUP1 SLOAD PUSH2 0x247 SWAP1 PUSH2 0x4A6 JUMP JUMPDEST SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV DUP2 ADD SWAP3 DUP3 PUSH2 0x269 JUMPI PUSH1 0x0 DUP6 SSTORE PUSH2 0x2B0 JUMP JUMPDEST DUP3 PUSH1 0x1F LT PUSH2 0x282 JUMPI DUP1 MLOAD PUSH1 0xFF NOT AND DUP4 DUP1 ADD OR DUP6 SSTORE PUSH2 0x2B0 JUMP JUMPDEST DUP3 DUP1 ADD PUSH1 0x1 ADD DUP6 SSTORE DUP3 ISZERO PUSH2 0x2B0 JUMPI SWAP2 DUP3 ADD JUMPDEST DUP3 DUP2 GT ISZERO PUSH2 0x2AF JUMPI DUP3 MLOAD DUP3 SSTORE SWAP2 PUSH1 0x20 ADD SWAP2 SWAP1 PUSH1 0x1 ADD SWAP1 PUSH2 0x294 JUMP JUMPDEST JUMPDEST POP SWAP1 POP PUSH2 0x2BD SWAP2 SWAP1 PUSH2 0x2C1 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x2DA JUMPI PUSH1 0x0 DUP2 PUSH1 0x0 SWAP1 SSTORE POP PUSH1 0x1 ADD PUSH2 0x2C2 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST PUSH1 0x0 PUSH2 0x2F1 PUSH2 0x2EC DUP5 PUSH2 0x417 JUMP JUMPDEST PUSH2 0x3F2 JUMP JUMPDEST SWAP1 POP DUP3 DUP2 MSTORE PUSH1 0x20 DUP2 ADD DUP5 DUP5 DUP5 ADD GT ISZERO PUSH2 0x30D JUMPI PUSH2 0x30C PUSH2 0x56C JUMP JUMPDEST JUMPDEST PUSH2 0x318 DUP5 DUP3 DUP6 PUSH2 0x464 JUMP JUMPDEST POP SWAP4 SWAP3 POP POP POP JUMP JUMPDEST PUSH1 0x0 DUP3 PUSH1 0x1F DUP4 ADD SLT PUSH2 0x335 JUMPI PUSH2 0x334 PUSH2 0x567 JUMP JUMPDEST JUMPDEST DUP2 CALLDATALOAD PUSH2 0x345 DUP5 DUP3 PUSH1 0x20 DUP7 ADD PUSH2 0x2DE JUMP JUMPDEST SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 DUP5 SUB SLT ISZERO PUSH2 0x364 JUMPI PUSH2 0x363 PUSH2 0x576 JUMP JUMPDEST JUMPDEST PUSH1 0x0 DUP3 ADD CALLDATALOAD PUSH8 0xFFFFFFFFFFFFFFFF DUP2 GT ISZERO PUSH2 0x382 JUMPI PUSH2 0x381 PUSH2 0x571 JUMP JUMPDEST JUMPDEST PUSH2 0x38E DUP5 DUP3 DUP6 ADD PUSH2 0x320 JUMP JUMPDEST SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0x3A2 DUP3 PUSH2 0x448 JUMP JUMPDEST PUSH2 0x3AC DUP2 DUP6 PUSH2 0x453 JUMP JUMPDEST SWAP4 POP PUSH2 0x3BC DUP2 DUP6 PUSH1 0x20 DUP7 ADD PUSH2 0x473 JUMP JUMPDEST PUSH2 0x3C5 DUP2 PUSH2 0x57B JUMP JUMPDEST DUP5 ADD SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 ADD SWAP1 POP DUP2 DUP2 SUB PUSH1 0x0 DUP4 ADD MSTORE PUSH2 0x3EA DUP2 DUP5 PUSH2 0x397 JUMP JUMPDEST SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH2 0x3FC PUSH2 0x40D JUMP JUMPDEST SWAP1 POP PUSH2 0x408 DUP3 DUP3 PUSH2 0x4D8 JUMP JUMPDEST SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x40 MLOAD SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x0 PUSH8 0xFFFFFFFFFFFFFFFF DUP3 GT ISZERO PUSH2 0x432 JUMPI PUSH2 0x431 PUSH2 0x538 JUMP JUMPDEST JUMPDEST PUSH2 0x43B DUP3 PUSH2 0x57B JUMP JUMPDEST SWAP1 POP PUSH1 0x20 DUP2 ADD SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP2 MLOAD SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP3 DUP3 MSTORE PUSH1 0x20 DUP3 ADD SWAP1 POP SWAP3 SWAP2 POP POP JUMP JUMPDEST DUP3 DUP2 DUP4 CALLDATACOPY PUSH1 0x0 DUP4 DUP4 ADD MSTORE POP POP POP JUMP JUMPDEST PUSH1 0x0 JUMPDEST DUP4 DUP2 LT ISZERO PUSH2 0x491 JUMPI DUP1 DUP3 ADD MLOAD DUP2 DUP5 ADD MSTORE PUSH1 0x20 DUP2 ADD SWAP1 POP PUSH2 0x476 JUMP JUMPDEST DUP4 DUP2 GT ISZERO PUSH2 0x4A0 JUMPI PUSH1 0x0 DUP5 DUP5 ADD MSTORE JUMPDEST POP POP POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x2 DUP3 DIV SWAP1 POP PUSH1 0x1 DUP3 AND DUP1 PUSH2 0x4BE JUMPI PUSH1 0x7F DUP3 AND SWAP2 POP JUMPDEST PUSH1 0x20 DUP3 LT DUP2 EQ ISZERO PUSH2 0x4D2 JUMPI PUSH2 0x4D1 PUSH2 0x509 JUMP JUMPDEST JUMPDEST POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH2 0x4E1 DUP3 PUSH2 0x57B JUMP JUMPDEST DUP2 ADD DUP2 DUP2 LT PUSH8 0xFFFFFFFFFFFFFFFF DUP3 GT OR ISZERO PUSH2 0x500 JUMPI PUSH2 0x4FF PUSH2 0x538 JUMP JUMPDEST JUMPDEST DUP1 PUSH1 0x40 MSTORE POP POP POP JUMP JUMPDEST PUSH32 0x4E487B7100000000000000000000000000000000000000000000000000000000 PUSH1 0x0 MSTORE PUSH1 0x22 PUSH1 0x4 MSTORE PUSH1 0x24 PUSH1 0x0 REVERT JUMPDEST PUSH32 0x4E487B7100000000000000000000000000000000000000000000000000000000 PUSH1 0x0 MSTORE PUSH1 0x41 PUSH1 0x4 MSTORE PUSH1 0x24 PUSH1 0x0 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x0 PUSH1 0x1F NOT PUSH1 0x1F DUP4 ADD AND SWAP1 POP SWAP2 SWAP1 POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 PUSH11 0x63A20DEC8282C1B9E9D6F5 0xA6 DUP15 0x26 0xB5 JUMPDEST 0xCE OR DUP15 0x28 0xE3 DUP9 DUP14 0x2B 0xB9 0xDA 0xA9 SWAP6 0xCC 0xC 0xD5 PUSH5 0x736F6C6343 STOP ADDMOD SMOD STOP CALLER ",
# 	"sourceMap": "66:262:0:-:0;;;;;;;;;;;;;;;;;;;"
# }

bytecode = "608060405234801561001057600080fd5b506105c2806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c80635ae5d4aa14610051578063a41368621461005b578063cfae321714610077578063ef690cc014610095575b600080fd5b6100596100b3565b005b6100756004803603810190610070919061034e565b610101565b005b61007f61011b565b60405161008c91906103d0565b60405180910390f35b61009d6101ad565b6040516100aa91906103d0565b60405180910390f35b6040518060400160405280600581526020017f48656c6c6f000000000000000000000000000000000000000000000000000000815250600090805190602001906100fe92919061023b565b50565b806000908051906020019061011792919061023b565b5050565b60606000805461012a906104a6565b80601f0160208091040260200160405190810160405280929190818152602001828054610156906104a6565b80156101a35780601f10610178576101008083540402835291602001916101a3565b820191906000526020600020905b81548152906001019060200180831161018657829003601f168201915b5050505050905090565b600080546101ba906104a6565b80601f01602080910402602001604051908101604052809291908181526020018280546101e6906104a6565b80156102335780601f1061020857610100808354040283529160200191610233565b820191906000526020600020905b81548152906001019060200180831161021657829003601f168201915b505050505081565b828054610247906104a6565b90600052602060002090601f01602090048101928261026957600085556102b0565b82601f1061028257805160ff19168380011785556102b0565b828001600101855582156102b0579182015b828111156102af578251825591602001919060010190610294565b5b5090506102bd91906102c1565b5090565b5b808211156102da5760008160009055506001016102c2565b5090565b60006102f16102ec84610417565b6103f2565b90508281526020810184848401111561030d5761030c61056c565b5b610318848285610464565b509392505050565b600082601f83011261033557610334610567565b5b81356103458482602086016102de565b91505092915050565b60006020828403121561036457610363610576565b5b600082013567ffffffffffffffff81111561038257610381610571565b5b61038e84828501610320565b91505092915050565b60006103a282610448565b6103ac8185610453565b93506103bc818560208601610473565b6103c58161057b565b840191505092915050565b600060208201905081810360008301526103ea8184610397565b905092915050565b60006103fc61040d565b905061040882826104d8565b919050565b6000604051905090565b600067ffffffffffffffff82111561043257610431610538565b5b61043b8261057b565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b83811015610491578082015181840152602081019050610476565b838111156104a0576000848401525b50505050565b600060028204905060018216806104be57607f821691505b602082108114156104d2576104d1610509565b5b50919050565b6104e18261057b565b810181811067ffffffffffffffff82111715610500576104ff610538565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea26469706673582212206a63a20dec8282c1b9e9d6f5a68e26b55bce178e28e3888d2bb9daa995cc0cd564736f6c63430008070033"

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('POTATO').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))
