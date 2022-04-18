from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

blockchain_url = "https://ropsten.infura.io/v3/" + os.getenv('INFURA_KEY')

web3 = Web3(Web3.HTTPProvider(blockchain_url))

print(web3.isConnected())

balance1 = web3.eth.getBalance(os.getenv('METAMASK_ETH_ADDRESS'))

print(web3.fromWei(balance1, "ether"))

