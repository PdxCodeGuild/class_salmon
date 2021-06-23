from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

def password_gen(pw_length= 10):
    password = ''
    digits = string.digits
    letters = string.ascii_letters
    punctuation = string.punctuation
    all_characters = letters + digits + punctuation
    while len(password) < pw_length:
        temp = random.choice(all_characters)
        password += temp
    return password 


@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        pw_length = int(request.form['password'])
        return render_template('lab05.html', password=password_gen(pw_length))
    return render_template('lab05.html', password=password_gen(0))
    
# @app.route('/other_route')
# def other_route():
#     return render_template('lab05.html', password='abc123!@')

app.run(debug=True)
