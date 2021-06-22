from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form['input_text']
        print(user_text)
        ciph = user_text
        return render_template('ciphered.html', ciph=ciph)
        # return render_template('index.html')
    else: 
        ciph = user_text
        return render_template('ciphered.html', ciph=ciph)

# @app.route('/', methods=["GET"])
def ciphered(text):
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



app.run(debug=True)