from database import JsonDB
from flask import Flask, render_template, request

app = Flask(__name__)
db = JsonDB('db.json')
db.load()

data = db.get('todos')
# x += 1
db.set('x', data)
db.save()


@app.route('/', methods=['GET', 'POST'])
def index():
    return


app.run(debug=True)
