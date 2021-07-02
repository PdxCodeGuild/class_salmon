from flask import Flask, render_template, request
app = Flask(__name__)
from unit_converter import Converter

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        converter = Converter()
        output = converter.convert(request.form['input-unit'], request.form['num_of_units'], request.form['output-unit'])
        return render_template('return.html', user_dict=request.form, output=output)

    else:
        return render_template('index.html')

app.run(debug=True)