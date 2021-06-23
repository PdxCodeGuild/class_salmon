from flask import Flask, render_template, request 
app = Flask(__name__)
from rot import encrypt_rotn
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # any operations you want with request.
        user_input = request.form
        encrypted = encrypt_rotn(user_input['input_text'],int(user_input['rot']))
        rot = user_input['rot']
        return render_template('results.html', encrypted=encrypted, rot=rot,user_input=user_input)
    else:
        return render_template('index.html')

app.run(debug=True)