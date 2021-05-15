


from flask import Flask

app = Flask(__name__)

@app.route('/index/')
def index():
    return "hi!"

@app.route('/data/')
def data():
    return {'name': 'josephine', 'favorite color': 'blue'}



app.run(debug=True)

