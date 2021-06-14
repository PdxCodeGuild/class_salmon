
from flask import Flask, render_template, request
app = Flask(__name__)



def make_change(amount):
    amount = int(amount * 100)
    quarters = amount // 25
    amount -= quarters*25 # amount %= 25
    dimes = amount // 10
    amount -= dimes * 10
    nickles = amount // 5
    amount -= nickles * 5
    pennies = amount

    return quarters, dimes, nickles, pennies




@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    print(request.form)
    print(dict(request.form))
    if request.method == 'POST':
        dollar_amount = request.form['dollar_amount']
        dollar_amount = float(dollar_amount)
        quarters, dimes, nickles, pennies = make_change(dollar_amount)
        return render_template('index.html', quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
    else:
        return render_template('index.html', quarters='', dimes='', nickles='', pennies='')

app.run(debug=True)