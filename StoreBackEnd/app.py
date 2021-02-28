from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from StoreController import StoreController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
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
    return 'There was a problem deleting that task'


@app.route('/store/')
def storeDisplay():

    storeList = storeController.clusterOfStores.listOfStores
    print(storeList)
    return render_template('index.html', tasks=storeList)


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
