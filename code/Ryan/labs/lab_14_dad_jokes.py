# import requests
# import json
"""
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. 
This will return a dad joke in JSON format. 
You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user
"""
#url = 'https://icanhazdadjoke.com/j/R7UfaahVfFd'
#response = requests.get(url)
#print(response.status_code)
#print(response.text)
#print(type(response.text))
#page = response.json()
#find = page.find('<p class="subtitle">')
#r = response.json()
#print(r)
#print(find)
#print("Dad Joke:", page[5627:5714])
#print(page)

import requests
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'})
data = response.json()
joke = data["joke"]
print("Dad joke:", joke)
