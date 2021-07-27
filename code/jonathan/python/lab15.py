import requests

def clean_quote(data):
    better_data = data['quote']
    quote = better_data['body']
    author = better_data['author']
    print(f'\n"{quote}"\n\n\t— {author}')
def quote_list(response):
    raw_data = response.json()
    level_1_data = raw_data['quotes']
    quote_counter = 0
    for i in range(len(level_1_data)):
        quote_counter +=1
        quote = level_1_data[i]['body']
        author = level_1_data[i]['author']
        print(f'\n{quote_counter}."{quote}"\n\n\t— {author}\n')

# Version 1: Get a Random Quote

'''response = requests.get('https://favqs.com/api/qotd', headers={'Accept': 'application/json'})
data = response.json()
clean_quote(data)'''

# Version 2: List Quotes by Keyword

search = input("Enter a keyword to search for quotes: ")

url = 'https://favqs.com/api/quotes'
add = f'/?filter={search}'
header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url+add, headers = header)

while True:
    quote_list(response)
    page_counter = -1
    commands = input("Enter <next> for next page, <search> for a new keyword or <done> to exit: ").lower()
    if commands == "next":
        try:
            page_counter +=1
            user = f'?page={page_counter}?filter={search}'
            header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
            response = requests.get(url+user, headers = header)
            quote_list(response)
        except KeyError:
            print("\nEnd of line.\n")
            commands = input("Enter <search> for a new keyword or <done> to exit: ").lower()
            if commands == "search":
                user_key = input("Please enter the new keyword to search for: ")
                user = f'/?filter={user_key}'
                header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
                response = requests.get(url+user, headers = header)
                quote_list(response)
            else:
                print("Goodbye.")
    elif commands == "search":
        user_key = input("Please enter the new keyword to search for: ")
        user = f'/?filter={user_key}'
    else:
        print("Goodbye.")
        break
    