from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

blockchain_url = "HTTP://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(blockchain_url))

print(web3.isConnected())

balance1 = web3.eth.getBalance(os.getenv('ETH_ADDRESS_1'))
balance2 = web3.eth.getBalance(os.getenv('ETH_ADDRESS_2'))
print(web3.fromWei(balance1, "ether"))
print(web3.fromWei(balance2, "ether"))
