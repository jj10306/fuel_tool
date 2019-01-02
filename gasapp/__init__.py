print('__init__1')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
print('__init__2')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1f29df353116235147f3affcc651ded'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Jakob/Desktop/Personal/CS/gasExpenditurePy/Gas_App/vehicles.db' #creates the database /Users/Jakob/Desktop/Personal/CS/gasExpenditurePy/Gas_App/vehicles.db
db = SQLAlchemy(app)

from gasapp import routes