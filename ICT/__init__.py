#Handles imports, creates app, creates database, don't forget import routes at the end

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
#pip install flask-sqlalchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "arandomsetofcharacters"
#create the database, import db anywhere you need to access your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from ICT import routes
