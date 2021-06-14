
import requests
import json

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/qotd/')
def qotd():
    response = requests.get('https://favqs.com/api/qotd')
    data = response.json()
    print(data)
    author = data['quote']['author']
    quote = data['quote']['body']
    return render_template('index.html', author=author, quote=quote)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html', search_term='', search_page=1)
    else:
        search_term = request.form['search_term']
        search_page = request.form['search_page']
        search_page = int(search_page)
        # print(request.method)
        # print(request.form)
        params = {
            'filter': search_term,
            'page': search_page
        }
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get('https://favqs.com/api/quotes', params=params, headers=headers)
        data = response.json()
        # print(json.dumps(data, indent=4))

        quotes = []
        for quote_data in data['quotes']:
            quotes.append({
                'author': quote_data['author'],
                'body': quote_data['body']
            })

        return render_template('search.html', search_term=search_term, search_page=search_page, quotes=quotes)


app.run(debug=True)

