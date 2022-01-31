import config
from app import app
from web3 import Web3
import logging
import json
import os
from dotenv import load_dotenv


class Web3client:
    def __init__(self, web3_node):
        load_dotenv()
        self.web3_node = web3_node
        self.web3 = Web3(Web3.HTTPProvider(self.web3_node))
        self.wallet = self.web3.eth.account.privateKeyToAccount(os.getenv('PK'))

        with open('./app/static/abis/info_facade.json') as f:
            self.info_facade_abi = json.loads(f.read())
        with open('./app/static/abis/vault_saver.json') as f:
            self.vault_saver_abi = json.loads(f.read())

        self.info_facade_addr = app.config['INFO_FACADE']
        self.vault_saver_addr = app.config['VAULT_SAVER']
        self.info_facade = self.web3.eth.contract(address=self.web3.toChecksumAddress(self.info_facade_addr),
                                                  abi=self.info_facade_abi)
        self.vault_saver = self.web3.eth.contract(address=self.web3.toChecksumAddress(self.vault_saver_addr),
                                                  abi=self.vault_saver_abi)

        while not self.is_connected():
            self.reconnect(self.web3_node)
            logging.log(logging.CRITICAL, "Reconnecting to node...")
        logging.log(logging.CRITICAL, "Bot is ready!")

    def is_connected(self):
        return self.web3.isConnected()

    def reconnect(self, web3_node):
        self.web3_node = web3_node
        self.web3 = Web3(Web3.HTTPProvider(self.web3_node))

    def save_vaults(self):
        res = self.info_facade.functions.getSavableVaults().call()
        addresses = res[0]
        # any one needs help?
        if len(addresses) > 0:
            for address in addresses:
                logging.log(logging.CRITICAL, "Saving Vault {0}".format(address))
                nonce = self.web3.eth.getTransactionCount(self.wallet.address)
                tx = self.vault_saver.functions.saveVault(self.web3.toChecksumAddress(address)).buildTransaction({
                    'from': self.wallet.address,
                    'nonce': nonce
                })
                signed_tx = self.web3.eth.account.signTransaction(tx, config.Config.PK)
                try:
                    tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                    hex_hash = self.web3.toHex(tx_hash)
                    logging.critical("sent tx for saving " + str(hex_hash))
                except ValueError as e:
                    logging.critical("could not send transaction, error:" + str(e))
        else:
            logging.log(logging.CRITICAL, "No Vault needs to be saved.")
