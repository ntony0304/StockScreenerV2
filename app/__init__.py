from flask import Flask
from app.config import Config
app = Flask(__name__)
app.config.from_object(Config) #read the config file and apply the setting
from app import routes
