from jsondb import JsonDB
from flask import Flask, render_template, request
app = Flask(__name__)
db = JsonDB()
db.load()
print(db.data)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return render_template('return.html', user_dict=request.form)

    else:
        return render_template('index.html')

app.run(debug=True)



