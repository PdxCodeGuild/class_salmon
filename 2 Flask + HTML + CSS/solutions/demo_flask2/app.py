import random
from flask import Flask, render_template
app = Flask('demo app')

@app.route('/')
def index():
    temperature = random.randint(50, 100)
    fruits = ['apples', 'bananas', 'pears']
    return render_template('index.html', name='bill', temperature=temperature, fruits=fruits)

@app.route('/about/')
def about():
    # html = '<html><head></head><body><h1>About</h1>'
    # html += '<ul>'
    # for i in range(10):
    #     html += '<li>' + str(i) + '</li>'
    # html += '</ul>'
    # html += '</body></html>'
    # return html
    return 'About View'



# app.run(debug=True, port=8000)
app.run(debug=True)




# kwargs
# def myfunc(**data):
#     print(data) # {'a': 1, 'b': 2, 'c': 3}
# myfunc(a=1, b=2, c=3)

