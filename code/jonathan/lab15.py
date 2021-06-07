import requests

def clean_quote(data):
    better_data = data['quote']
    quote = better_data['body']
    author = better_data['author']
    print(f'\n"{quote}"\n\n\t— {author}')
def quote_list(response):
    raw_data = response.json()
    level_1_data = raw_data['quotes']
    counter = 0
    for i in range(len(level_1_data)):
        counter +=1
        quote = level_1_data[i]['body']
        author = level_1_data[i]['author']
        print(f'\n{counter}."{quote}"\n\n\t— {author}\n')
# Version 1: Get a Random Quote
'''response = requests.get('https://favqs.com/api/qotd', headers={'Accept': 'application/json'})
data = response.json()

clean_quote(data)'''

# Version 2: List Quotes by Keyword

search = input("Enter a keyword to search for quotes: ")

url = f'https://favqs.com/api/quotes/?filter={search}'

header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers = header)

quote_list(response)
commands = input("Enter <next> page or <done>: ").lower()
if commands == "next":
    new_url = 'https://favqs.com/api/quotes?page=0?filter={search}'
header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(new_url, headers = header)
quote_list(response)