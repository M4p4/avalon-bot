from flask import Flask
from config import Config
from flask_apscheduler import APScheduler
import logging

app = Flask(__name__,static_folder='static')
app.config.from_object(Config)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
logging.getLogger('apscheduler.scheduler').setLevel(logging.ERROR)

from app import routes
from app import engine