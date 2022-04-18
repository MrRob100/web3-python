import json
from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv
import web3

load_dotenv(find_dotenv())

blockchain_url = "https://ropsten.infura.io/v3/" + os.getenv('INFURA_KEY')
web3 = Web3(Web3.HTTPProvider(blockchain_url))

contract_address = web3.toChecksumAddress(os.getenv('DEPLOYED_CONTRACT_ADDRESS'))

abi = json.loads('[{"inputs": [],"name": "Greet","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "string","name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "greet","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]')

contract = web3.eth.contract(address=contract_address, abi=abi)

print(contract.functions.greet().call())