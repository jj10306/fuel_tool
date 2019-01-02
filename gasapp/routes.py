print('routes1')
from flask import render_template, url_for, flash, redirect, request, jsonify
from gasapp import app, db
from gasapp.forms import Form
from gasapp.models import Vehicle
import sqlite3
from gasapp.logic import Driver
print('routes2')

# con = sqlite3.connect('vehicles.db')
# cursor = con.cursor()


# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
nissan_list = db.session.query(Vehicle).distinct().filter_by(make = "Nissan").all() #how can I do all of the mess below with a query
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
        # model = db.session.query(Vehicle).filter_by(id=form.model.data).first()
        # return '<h1>Make: {}, Model: {}'.format(form.make.data, model.model)

    return render_template('test.html', form=form)

# @app.route("/somewhere_else", methods=['GET', 'POST'] )
# def submit():
#     id = request.form['year'] ###look at HTML to see that year dropdown return vehicle's ID
#     start = request.form['start_address']
#     end = request.form['end_address']
#     driver = Driver(id, start, end)
#     print(driver.drive())
#     return redirect('http://localhost:5000/')

def submit():
    id = request.form['year'] ###look at HTML to see that year dropdown return vehicle's ID
    start = request.form['start_address']
    end = request.form['end_address']
    driver = Driver(id, start, end)

    data = driver.drive()
    result = data['price']
    return render_template('display.html', result=result)

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












