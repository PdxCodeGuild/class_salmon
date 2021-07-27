from flask import Flask, request, render_template, redirect
app = Flask(__name__)

user_text =""

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form['input_text']
        # print(request.form['input_text'])
        # print(user_text)
        # ciph = user_text
        # return render_template('ciphered.html', ciph=ciph)
        return render_template('index.html')
    else: 
        return render_template('index.html')

def cipher(text):
    user_input = text
    user_input = list(user_input)

    cipher_input = []
    cipher_dict = {' ':' ', 'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f':'s', 'g': 't', 'h': 'u', "i": 'v', "j": 'w', "k": "x", 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', "z":'m'}

    for i in range(len(user_input)):
        cipher_input.append(user_input[i])

    output_string = []

    for i in range(len(cipher_input)):
        output_string.append(cipher_dict[cipher_input[i]])

    # output ciphered list
    output = ''.join(output_string)

    return output

@app.route('/ciphered/', methods=["POST"])
def ciphered():
    ciph = cipher(request.form['input_text'])
    return render_template('ciphered.html', ciph=ciph)


app.run(debug=True)