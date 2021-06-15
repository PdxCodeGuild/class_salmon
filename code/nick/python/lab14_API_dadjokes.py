import requests
# response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
# print(response.text) #JSON format
# joke_dict = response.json()#this is the joke dictionary, key is 'joke'
# while True:
#     command = input('Want to hear a joke? yes or no ')
#     if command == 'yes':
#         print(joke_dict['joke'])
#     elif command == 'no':
#         break
#     else:
#         print('Command not recognized')

#Version 2
#search for dad jokes

while True:
    command = input('Enter your dad joke search term or exit: ')
    if command == 'exit':
        break
    else:
        response2 = requests.get(f'https://icanhazdadjoke.com/search?term={command}', headers={'Accept': 'application/json'})
        #print(response2.text) #JSON format
        joke_dict2 = response2.json()
        # print(joke_dict2)
        jokes_refined = joke_dict2['results']
        # print(jokes_refined)
        for i in jokes_refined:
            print(i['joke'])
