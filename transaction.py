from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

blockchain_url = 'HTTP://127.0.0.1:8545'

web3 = Web3(Web3.HTTPProvider(blockchain_url))

account_1 = os.getenv('ETH_ADDRESS_1')
account_2 = os.getenv('ETH_ADDRESS_2')

account_1_private_key = os.getenv('PRIVATE_KEY_1')

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, account_1_private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))