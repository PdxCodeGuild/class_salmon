

from jsondb import JsonDB


# db = JsonDB()
# db.load()
# print(db)
# print(db['contacts'][0])
# print(db['contacts'][0]['first_name'])
# db['contacts'][0]['blood_type'] = 'A-'
# db['contacts'].append({
#     'first_name': 'Eleanor',
#     'last_name': 'Johnston',
#     'phone': '814-398-4326',
#     'email': 'EleanorSJohnston@rhyta.com',
#     'favorite_color': 'orange',
#     'blood_type': 'AB+'
# })
# db.save()


from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    db = JsonDB()
    db.load()
    # print(db['contacts'])
    return render_template('index.html', contacts=db['contacts'])

@app.route('/create/', methods=['GET', 'POST'])
def create():
    # print(request.method)
    # print(request.form)
    db = JsonDB()
    db.load()
    if request.method == 'POST':
        db['contacts'].append({
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'blood_type': request.form['blood_type'],
            'favorite_color': request.form['favorite_color']
        })
        db.save()
        return redirect('/')
    return render_template('create.html', blood_types=db['blood_types'])

@app.route('/delete/<int:index>/')
def delete(index):
    db = JsonDB()
    db.load()
    db['contacts'].pop(index)
    db.save()
    return redirect('/')

app.run(debug=True)


