from flask import Flask, render_template, request
from db1 import JsonDB
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        # any operations you want with request.form    
        return render_template('04_todo.html')
    else:
        db = JsonDB('db.json')
        db.load()
        list_of_dicts = db.data['todos']
        print(db.data['todos'][1])
        return render_template('04_todo.html', list_of_dicts=list_of_dicts)


app.run(debug=True)