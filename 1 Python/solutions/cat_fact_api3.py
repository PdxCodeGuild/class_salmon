
import requests

page = 1
last_page = 1000

# send the request

while page <= last_page:

    response = requests.get('https://catfact.ninja/breeds/', params={'page': page})
    # print(response.text)
    data = response.json()

    last_page = data['last_page']

    breed_list = data['data']
    print(breed_list)

    # print out the breed info

    for breed in breed_list:
        print(breed['breed'])
        print('\tCountry:' + breed['country'])
        print('\tOrigin: ' + breed['origin'])
        print('\tCoat: ' + breed['coat'])
        print('\tPattern: ' + breed['pattern'])
    
    input('Hit enter to see the next page...')
    page += 1

print('Done!')




