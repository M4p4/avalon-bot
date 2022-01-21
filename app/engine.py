from app import app
from app import scheduler
from app import web3client
import logging
import time

@scheduler.task('cron', id='background_checker', second='*')
def background_checker():
    client = web3client.Web3client(app.config['CHECKER_NODE'])
    while (True):
        try:
            client.save_vaults()
        except:
            client.reconnect(app.config['CHECKER_NODE'])
            logging.log(logging.CRITICAL, "[Error] parsing contracts")
        time.sleep(app.config['CHECKER_DELAY'])
