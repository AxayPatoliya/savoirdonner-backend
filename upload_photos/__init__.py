from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins="*")

app.config['APP_SECRET_KEY'] = 'super-super-secret-key'
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#modules import
import upload_photos.modules.upload_photos


# Set up logging
import logging
from logging.handlers import SysLogHandler

# Set up logging for Flask
syslog_handler = SysLogHandler(address='/dev/log')
syslog_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
syslog_handler.setFormatter(formatter)

# Add the handler to your Flask app logger
app.logger.addHandler(syslog_handler)
app.logger.setLevel(logging.INFO)
