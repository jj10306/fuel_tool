#set environment variables frist
#export FLASK_APP=main.py
#export FLASK_DEBUG=1

# from flask import Flask, render_template, request
# app = Flask(__name__)
# app.debug = True


# @app.route('/', methods=['GET'])
# def dropdown():
#     colours = ['Red', 'Blue', 'Black', 'Orange']
#     return render_template('test.html', colours=colours)

# if __name__ == "__main__": #allows to call directly with python3 main.py and will be in debug mode
#     app.run()
print('main1')
from gasapp import app
print('main2')

if __name__ == '__main__':
    app.run(debug=True)