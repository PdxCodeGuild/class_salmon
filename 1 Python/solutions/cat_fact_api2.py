
import requests

# what page of breeds would you like to see?

page = input('what page of breeds would you like to see?')


# send the request

response = requests.get('https://catfact.ninja/breeds/', params={'page': page})
# print(response.text)
data = response.json()

breed_list = data['data']
print(breed_list)

# print out the breed info

for breed in breed_list:
    print(breed['breed'])
    print('\tCountry:' + breed['country'])
    print('\tOrigin: ' + breed['origin'])
    print('\tCoat: ' + breed['coat'])
    print('\tPattern: ' + breed['pattern'])






