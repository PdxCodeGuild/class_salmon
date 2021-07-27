from flask import Flask, redirect, url_for, render_template, request
from rot_13 import rot13

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        phrase = request.form["input_text"]
        print(phrase)

        rotation = int(request.form["rotate"])
        print(rotation)
        
        output_text = rot13(phrase,rotation)

        return render_template("index.html", output_text=output_text)
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)