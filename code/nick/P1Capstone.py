import requests
while True:
    api_key = input('What is your API key? or type exit')
    response = requests.get(f'https://api.openei.org/utility_rates?version=3&format=json&api_key={api_key}')
    print(response.text) #JSON format
    openenergyinformation_dict = response.json()#this is the joke dictionary, key is 'joke'
    elif api_key == 'exit':
        break
    else:
        print('Command not recognized')

# while True:
#     command = input('What is your API key?')
#     if command == 'yes':
#         print(joke_dict['joke'])
#     elif command == 'no':
#         break
#     else:
#         print('Command not recognized')