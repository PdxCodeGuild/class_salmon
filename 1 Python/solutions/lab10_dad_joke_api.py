


import requests
import json

# url = 'https://icanhazdadjoke.com/'
# response = requests.get(url, headers={'Accept': 'application/json'})
# print(response.text)
# data = response.json()
# joke = data['joke']
# print(joke)


term = input('Enter search term: ')
# response = requests.get('https://icanhazdadjoke.com/search?term=' + term)
response = requests.get('https://icanhazdadjoke.com/search', params={'term': 'hipster'}, headers={'Accept': 'application/json'})
print(response.text)


# data = response.json()
data = json.loads(response.text)
# print(json.dumps(data, indent=4))

# print(data)


for result in data['results']:
    print(result['joke'])


