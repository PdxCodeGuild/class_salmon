
from flask import Flask, render_template, request
app = Flask(__name__)

import json

@app.route('/')
def index():
    print('we\'re inside the flask index view')
    return render_template('index.html')

@app.route('/create_contact/', methods=['GET', 'POST'])
def create_contact():
    
    with open('contacts.json', 'r') as file:
        text = file.read()
        data = json.loads(text)
        contacts = data['contacts']

    print(request.form)
    print(request.form['first_name'])
    print(dict(request.form))

    contacts.append(dict(request.form))
    
    with open('contacts.json', 'w') as file:
        data = {'contacts': contacts}
        text = json.dumps(data, indent=4)
        file.write(text)

    return 'received form submission'


app.run(debug=True)
