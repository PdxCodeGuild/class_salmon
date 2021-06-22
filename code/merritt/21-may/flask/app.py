from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # any operations you want with request.form
        return render_template('results.html', user_dict=request.form)
    else:
        name = 'merritt'
        temperature = 67
        nums = [1, 2, 3]  
        return render_template('index.html', name=name, temperature=temperature, nums=nums)

@app.route('/add/', methods=['POST'])
def add():
    num1 = int(request.form['add1'])
    num2 = int(request.form['add2'])
    total = num1 + num2
    return render_template('add_results.html', total=total)

app.run(debug=True)