import requests

response = requests.get('https://api.ipify.org?format=json')
response = requests.get('https://api.ipify.org', params={"format": "json"})

data = response.json()

# print(response.url)
# print(data)
# print(list(data.keys()))

print(type(response.text))
print(type(response.json()))