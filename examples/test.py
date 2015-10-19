import pymongo

from bottle import route, run, template
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.test
item = db.things.find_one()

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}} - {{test}}</b>!', name=name, test=item['a'])

run(host='localhost', port=8080)
