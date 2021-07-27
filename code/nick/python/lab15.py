import requests
#Version 1 Get a random quote

# while True:
#     command = input('Want to see a random quote? Type yes or exit ')
#     if command == 'exit':
#         break
#     else:
#         response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json'})
#         # print(response.text) #JSON format
#         quote_dict1 = response.json()#this is a dictionary with another dictionary as a value
#         quote_dict2 = quote_dict1['quote']
#         random_quote = quote_dict2['body']
#         random_author = quote_dict2['author']
#         print(f'The once admired or distained {random_author} once said: \n "{random_quote}"')
#Version 2
#get a list of quotes associated with a give kw
while True:
    command = input('Search for a quote by keyword. Type your keyword or exit ')
    if command == 'exit':
        break
    else:
        counter = 1
        response = requests.get(f'https://favqs.com/api/quotes?page={counter}&filter={command}', headers={'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        # print(response.text) #JSON format
        quote_dict1 = response.json()#this is a dictionary with another dictionary as a value
        quote_dict2 = quote_dict1['quotes']
        for i in quote_dict2:
            body = i['body']
            author = i['author']
            print(f'"{body}" -{author}')
        nextpage = input('Want to see another page of quotes with the same keyword? yes, no, or any to restart ')
        if nextpage == 'yes':
            counter += 1
            response = requests.get(f'https://favqs.com/api/quotes?page={counter}&filter={command}', headers={'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            quote_dict1 = response.json()#this is a dictionary with another dictionary as a value
            quote_dict2 = quote_dict1['quotes']
            for i in quote_dict2:
                body = i['body']
                author = i['author']
                print(f'"{body}" -{author}')
        elif nextpage == 'no':
            break
        else:
            print('Restarting your search. ')