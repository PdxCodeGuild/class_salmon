

import requests
import json

# prompt the user for how many cat facts they'd like
num_facts = input('How many cat facts would you like? ')

# send the request to the cat fact api
response = requests.get('https://catfact.ninja/facts/', params={'limit': num_facts})

# import urllib
# num_facts = urllib.urlencode(num_facts)
# requests.get('https://catfact.ninja/facts/?limit='+num_facts)

# print(response.text)

data = response.json()

# print(json.dumps(data, indent=4))
# data = json.loads(response.text)
# print(data)

# display the facts we get in response

fact_list = data['data']
# print(fact_list)
for fact in fact_list:
    print(fact['fact'])



