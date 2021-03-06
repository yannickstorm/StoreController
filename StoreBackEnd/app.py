from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

try:
    from StoreController import StoreController
    storeController = StoreController()
except ImportError:
    print("WARNING: importing CC1101 module. Continue in dummy mode.")
    from DummyController import DummyController
    storeController = DummyController()

@app.route('/json_post', methods = ['POST'])
def jsonReceive():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'


@app.route('/store/<int:id>/<int:dir>')
def moveStore(id, dir):

    print("Store nbr: " + str(id) + " ,  direction: " + str(dir))
    storeController.transmitCommand(id, dir)
    return redirect('/store/')


@app.route('/store/')
def storeDisplay():

    storeList = storeController.clusterOfStores.listOfStores
    return render_template('index.html', tasks=storeList)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
