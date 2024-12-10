from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
#pip install flask-sqlalchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "arandomsetofcharacters"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from ICT import routes
