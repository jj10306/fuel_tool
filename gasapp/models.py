from datetime import datetime
from gasapp import db
from flask_sqlalchemy import SQLAlchemy

class Vehicle(db.Model): #ORMs (Object relation Manager) use different classes to represent tables of a database
    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30), nullable=False)#must be unique and must have a username (cant be null)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer)
    fuel_type = db.Column(db.String(30), nullable=False)
    mpg = db.Column(db.Integer)



