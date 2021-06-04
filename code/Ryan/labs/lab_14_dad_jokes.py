import requests
import json

url = 'https://icanhazdadjoke.com/j/R7UfaahVfFd'
response = requests.get(url)
print(response.status_code)
print(response.text)