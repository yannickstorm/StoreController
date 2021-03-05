from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from DummyController import DummyController

dummyMode = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

if dummyMode == True:
    storeController = DummyController()
else:
    from StoreController import StoreController
    storeController = StoreController()


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
