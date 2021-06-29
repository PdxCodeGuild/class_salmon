import string
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("lab05.html")

@app.route("/cipher", methods=["GET", "POST"])
def cipher():
    unencrypted_message = request.form.get("message")
    encrypt_shift = int(request.form.get("rotation"))
    unencrypted_message = unencrypted_message.replace(" ", "")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for p in unencrypted_message: 
        if p in string.punctuation:
            unencrypted_message = unencrypted_message.replace(p, "") 
    encrypted_message = "".join([alphabet[(alphabet.find(c) + encrypt_shift) % 26] for c in unencrypted_message])
    return render_template("lab05_2.html", encrypted_message=encrypted_message)

if __name__ == "__main__":
    app.run(debug=True)