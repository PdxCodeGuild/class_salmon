
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    print(request.method)

    if request.method == 'POST':
        # print(request.form)
        # form = dict(request.form)
        noun1 = request.form['noun1']
        noun2 = request.form['noun2']
        noun3 = request.form['noun3']
        noun_plural = request.form['noun_plural']
        place = request.form['place']
        adjective = request.form['adjective']


        madlib = f'''Be kind to your {noun1}-footed {noun_plural}
        For a duck may be somebody`s {noun2},
        Be kind to your {noun_plural} in {place}
        Where the weather is always {adjective}.

        You may think that this is the {noun3},
        Well it is.'''

        return render_template('index.html', madlib=madlib)
    else:
        return render_template('index.html', madlib='')

app.run(debug=True)