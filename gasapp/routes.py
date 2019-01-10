from flask import render_template, url_for, flash, redirect, request, jsonify
from gasapp import app, db
from gasapp.forms import Form
from gasapp.models import Vehicle
import sqlite3
from gasapp.logic import Driver
from gasapp.webscrape import WebScraper




app.secret_key = "very secret"

nissan_list = db.session.query(Vehicle).distinct().filter_by(make = "AM General").all() #how can I do all of the mess below with a query
unique_list = [nissan_list[0]]

@app.route('/', methods=['GET', 'POST'])
def dropdown():
    model_list = list()
    form = Form()
    for vehicle in nissan_list:
        aBool = True
        for vehicle1 in unique_list:
            if vehicle.model == vehicle1.model:
                aBool = False
                break
        if aBool:
            unique_list.append(vehicle)
    form.model.choices = [(vehicle.id, vehicle.model) for vehicle in unique_list]
    form.model.choices.sort(key=lambda x: x[1], reverse = True)


    if request.method == 'POST':
        return submit()

    return render_template('test.html', form=form)


def submit():
    id = request.form['year'] ###look at HTML to see that year dropdown return vehicle's ID
    start = request.form['start_address']
    start_state = get_state(start)
    end = request.form['end_address']
    end_state = get_state(end)
    driver = Driver(id, start, end)
    buffer_obj = WebScraper("","")
    gas_dict = buffer_obj.get_HTML(False, start_state)
    data = driver.drive()

    data['prices'] = gas_dict
    total = data['distance'] / data['mpg'] * data['prices'][data['fuel_type']]
    total = round(total, 2)


    return render_template('display.html', result = total)

def get_state(address): #passed address as entered in form's text field
    split_list = address.split(",")
    state = split_list[2].strip()
    url_state = state
    return state



@app.route('/model/<make>') #query to get unique and order
def model(make):
    models = db.session.query(Vehicle).filter_by(make=make).all()

    modelArray = []

    for model in models:
        modelObj = {}
        modelObj['id'] = model.id
        modelObj['model'] = model.model
        modelArray.append(modelObj)

    return jsonify({'models': modelArray})

@app.route('/year/<model>') #query to get unique and order
def year(model):
    print(model)
    years = db.session.query(Vehicle).filter_by(model=model).all()

    yearArray = []

    for year in years:
        yearObj = {}
        yearObj['id'] = year.id
        yearObj['year'] = year.year
        yearArray.append(yearObj)

    return jsonify({'years': yearArray})












