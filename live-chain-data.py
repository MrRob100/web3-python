from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

blockchain_url = "https://mainnet.infura.io/v3/" + os.getenv('INFURA_KEY')
rl = "HTTP://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(blockchain_url))

print(web3.isConnected())
print(web3.eth.blockNumber)
