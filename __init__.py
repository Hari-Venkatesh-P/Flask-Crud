from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

#Creating flask app
app = Flask(__name__)

#Configuring Flask application with Postgresql Database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/crud_apis"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


