# Lab 14: Dad Joke API
# Use the Dad Joke API to get a dad joke and display it to the user. 
import requests

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.
response = requests.get('https://icanhazdadjoke.com/', headers= {'Accept': 'application/json'})
data = dict(response.json())
random_joke = data['joke']

print(f'\nEnjoy this dad joke from icanhazdadjoke.com!\n\n"{random_joke}"\n\nYou got it ;)\n')

# Part 2 (optional)
# Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.
# search_response = requests.get('https://icanhazdadjoke.com/search', params= {'page': 1, 'limit': 20, 'term': 'list all jokes'})
# search_data = search_response.json()
# print(search_data) # many errors