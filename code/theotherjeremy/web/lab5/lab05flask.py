from flask import Flask, render_template, request


app = Flask(__name__)


def secret_maker(secret):

    secret = secret.lower()
    english = 'abcdefghijklmnopqrstuvwxyz .'
    rot = 'nopqrstuvwxyz .abcdefghijklm'
    rot2 = []
    for i in rot:
        rot2.append(i)
    rot_idx = []
    for let in secret:
        if let in english:
            rot_idx.append(english.index(let))
    code = []
    for indx in rot_idx:
        code.append(rot[indx])
    code = ''.join(code)

    return code


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        secret = request.form['secret']
        code = secret_maker(secret)
        return render_template('lab05results.html', encoded_message=code)
    return render_template('lab05results.html', encoded_message='')


app.run(debug=True)
