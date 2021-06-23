from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phrase = request.form["input_text"]
        print(phrase)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)