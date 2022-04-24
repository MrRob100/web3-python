import json
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

blockchain_url = "https://ropsten.infura.io/v3/" + os.getenv('INFURA_KEY')
web3 = Web3(Web3.HTTPProvider(blockchain_url))

web3.middleware_onion.add(construct_sign_and_send_raw_middleware(os.getenv('METAMASK_PRIVATE_KEY')))

web3.eth.defaultAccount = os.getenv('METAMASK_ETH_ADDRESS')

contract_address = web3.toChecksumAddress(os.getenv('DEPLOYED_CONTRACT_ADDRESS'))

abi = json.loads('[{"inputs": [],"name": "Greet","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "string","name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "greet","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]')

contract = web3.eth.contract(address=contract_address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('POTATO').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))
