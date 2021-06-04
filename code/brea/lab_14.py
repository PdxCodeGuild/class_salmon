import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
data = response.json()

print(data['joke'])