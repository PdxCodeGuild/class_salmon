
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


@app.route('/search/')
def search():
    if 'term' not in request.args:
        return render_template('search.html', term='', page=1)
    else:
        term = request.args['term']
        page = request.args['page']
        page = int(page)
        # print(request.method)
        # print(request.form)
        params = {
            'filter': term,
            'page': page
        }
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get('https://favqs.com/api/quotes', params=params, headers=headers)
        data = response.json()
        # print(json.dumps(data, indent=4))

        last_page = data['last_page']
        print(last_page)
        quotes = []
        for quote_data in data['quotes']:
            quotes.append({
                'author': quote_data['author'],
                'body': quote_data['body']
            })

        return render_template('search.html', term=term, page=page, last_page=last_page, quotes=quotes)


app.run(debug=True)

