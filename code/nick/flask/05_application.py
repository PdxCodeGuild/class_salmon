from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        # any operations you want with request.form
        mass_flow = float(request.form['mass-flow'])
        c_p = float(request.form['c_p'])
        dT = float(request.form['temperature-initial'])-float(request.form['temperature-exit'])
        utilized_power = mass_flow*c_p*dT
        max_power = mass_flow*c_p*float(request.form['temperature-initial'])
        efficiency = int(utilized_power/max_power*100)
        return render_template('output.html', max_power="{:,}".format(int(max_power)), utilized_power="{:,}".format(int(utilized_power)), efficiency=efficiency)
    else:
        return render_template('power_conversion.html')

app.run(debug=True)