import requests
import json
url = 'https://icanhazdadjoke.com/'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
 
r = requests.post(url, data=json.dumps(payload), headers=headers)

r = requests.get('https://icanhazdadjoke.com/')
print(r.status_code)
print(r.status_code == requests.codes.ok)
print(requests.codes["temporary_redirect"])
print(requests.codes.teapot)
print(requests.codes["o/"])

# HTML / CSS output
# print(r.text) 
print(r.json)

response = requests.get('https://api.ipify.org')
print(response.url)
print(response.text) # 76.105.187.182
print(response.status_code) # 200
print(response.encoding) # ISO-8859-1
print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}
