

import requests
import json



# Chuck Norris Joke API ==============================

response = requests.get('https://api.chucknorris.io/jokes/random')
# # print(response)
# # print(type(response))

# # read the raw response
# # print(response.text)

data = response.json() # take the JSON in the response and turn it into a python dictionary
# print(data)
joke = data['value']
print(joke)



# IP API ================================


# response = requests.get('https://api.ipify.org/?format=json')
response = requests.get('https://api.ipify.org/', params={'format': 'json'})
# print(response.text) # string containing JSON
data = response.json()
# print(data)
print('Your IP address is ' + data['ip'])



# Studio Ghibli API ===============================

response = requests.get('https://ghibliapi.herokuapp.com/films')
# data = response.json()
# print(data)
# print(json.dumps(data, indent=4))

for film in data:
    print('title: ' + film['title'])
    print('director: ' + film['director'])
    if len(film['people']) > 1:
        print('characters:')
        character_urls = film['people']
        for character_url in character_urls:
            response = requests.get(character_url)
            character_data = response.json()
            print('\t' + character_data['name'])
    print()



