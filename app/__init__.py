'''Initializes the app'''
from flask import Flask
import config

App = Flask(__name__)
App.config.from_object(config)