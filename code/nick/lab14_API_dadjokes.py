import requests
response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
print(response.text) #JSON format
joke_dict = response.json()#this is the joke dictionary, key is 'joke'
while True:
    command = input('Want to hear a joke? yes or no ')
    if command == 'yes':
        print(joke_dict['joke'])
    elif command == 'no':
        break
    else:
        print('Command not recognized')