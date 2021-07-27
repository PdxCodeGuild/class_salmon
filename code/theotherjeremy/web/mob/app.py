from database import JsonDB
from flask import Flask, render_template, request

app = Flask(__name__)
db = JsonDB('db.json')
db.load()
print(db)

x = db.get('todos', 0)
x += 1
db.set('x', x)
db.save()


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return


# app.run(debug=True)
