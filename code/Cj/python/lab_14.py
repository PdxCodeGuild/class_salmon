import requests
response = requests.get('https://icanhazdadjoke.com/', headers={'accept' : 'application/json'}).json()
data = response['joke']
print(data)
# print(response)
# print(response.json())