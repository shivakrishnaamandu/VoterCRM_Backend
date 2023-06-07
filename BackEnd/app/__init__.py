from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os


application = Flask(__name__)
application.secret_key = "flask-VoterCRM-Backend-1234"
api = Api(application)  # Flask restful wraps Flask app around it.

# api.register_blueprint(Admin_Auth_API_blueprint)

application.config["SQLALCHEMY_DATABASE_URI"] ='mysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'root'),
    os.getenv('DB_PASSWORD', 'admin'),
    os.getenv('DB_HOST', 'localhost'),
    os.getenv('DB_NAME', 'voter_crm')
)
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
application.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(application)
print(type(db))
print(db)
