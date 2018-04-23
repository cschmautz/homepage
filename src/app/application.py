""" app.py: sets up the application.
"""
from flask import Flask

application = Flask(__name__, instance_relative_config=True)
# application.config.from_object('app_config')
application.config.from_pyfile('config.py')

from src.app import views
