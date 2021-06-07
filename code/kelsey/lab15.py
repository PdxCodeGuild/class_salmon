# Lab 15: Quotes API
# For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.
import requests

# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.
random_response = requests.get('https://favqs.com/api/qotd/', headers= {'Accept': 'application/json'})
data = random_response.json()['quote']
qotd = data['body']
author = data['author']
print(f'\n"{qotd}"\n-{author}\n')

# Version 2: List Quotes by Keyword
# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.
keyword = input('Enter a keyword to search quotes: ')
page = 1

while True:
    search_response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers= {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    response_dict = search_response.json()
    quotes = response_dict['quotes']
    last_pg = response_dict['last_page']
    for quote in quotes:
        author = quote['author']
        body = quote['body']
        print(f'\n"{body}" Author: {author}')
    num_of_results = len(quotes)
    page_number = response_dict['page']
    print(f'\n{num_of_results} quotes associated with {keyword} on page {page_number}')
    next_pg = input("\nEnter 'next' for next page, 'new' for new search, or 'done' to quit: ")
    if next_pg == 'done':
        print("\nSee you later!\n")
        break
    elif next_pg == 'next':
        if last_pg == True:
            print('\nSorry, no more pages to search.')
            break
        page += 1
    elif next_pg == 'new':
        keyword = input('Enter a keyword to search quotes: ')
        page = 1



# print(f'{num_of_results} quotes associated with {keyword} - page {pg}')
# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes:
# This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
