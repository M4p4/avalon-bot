from app import app
from web3 import Web3
import logging
import json

class Web3client():
    def __init__(self, web3_node):
        self.web3_node = web3_node
        self.web3 = Web3(Web3.HTTPProvider(self.web3_node))

        with open('./app/static/abis/info_facade.json') as f:
            self.info_facade_abi = json.loads(f.read())
        with open('./app/static/abis/vault_saver.json') as f:
            self.vault_saver_abi = json.loads(f.read())

        self.info_facade_addr = app.config['INFO_FACADE']
        self.vault_saver_addr = app.config['VAULT_SAVER']

        while (self.is_connected() == False):
            self.reconnect(self.web3_node)
            logging.log(logging.CRITICAL, "Reconnecting to node...")
        logging.log(logging.CRITICAL, "Bot is ready!")

    def is_connected(self):
        return self.web3.isConnected()

    def reconnect(self, web3_node):
        self.web3_node = web3_node
        self.web3 = Web3(Web3.HTTPProvider(self.web3_node))

    def save_vaults(self):
