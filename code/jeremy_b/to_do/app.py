from database import JsonDB
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
db = JsonDB('db.json')
db.load()

data = db.get('todos')
# x += 1
#db.set('x', data)
#db.save()


@app.route('/', methods=['GET'])
def index():
    data = db.get('todos')
    return render_template('index.html', todos=data)

@app.route('/add', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      db.data["todos"].append(result)
      db.save()
      return redirect("/")




app.run(debug=True)
