from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mnmgqggkougpmr:6HJy8a3ssg3kDpwzdZZUfMKLrR@ec2-23-23-180-133.compute-1.amazonaws.com:5432/dfqcq2aq8vlaie'
app.config['SECRET_KEY'] = "itsasecret"
db = SQLAlchemy(app)

from app import views
