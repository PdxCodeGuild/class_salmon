from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/convert_units', methods=["GET", "POST"])
def convert_units():

    units = {
        'ft': .3048,
        'm': 1,
        'mi': 1609.34,
        'km': 1000,
        'yd': .9144,
        'in': .0254
    }

    original_length = int(request.form.get("input-length"))
    original_unit = request.form.get("input-units")
    conversion_unit = request.form.get("output-units")

    length_in_meters = original_length * (units[original_unit])
    final_converted_length = length_in_meters * (1 / units[conversion_unit])

    return render_template("conversion.html", converted_length=final_converted_length, converted_unit=conversion_unit, original_length=original_length, original_unit=original_unit)

if __name__ == '__main__':
    app.run(debug=True)
