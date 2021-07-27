from jsondb import JsonDB
from flask import Flask, render_template, request
app = Flask(__name__)
db = JsonDB()


@app.route('/', methods=['GET', 'POST'])
def index():
    db.load()
    x=db.get('todos')
    if request.method == "POST":
        print(dict(request.form))
        db.data["todos"].append(request.form)
        db.save()
        return render_template('return.html', user_dict=request.form, todo=x)
    
    else:
        return render_template('index.html')

app.run(debug=True)



