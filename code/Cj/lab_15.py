import requests

response = requests.get('https://favqs.com/api/qotd', headers={'accept' : 'application/json'}).json()

print(f"Author: {response['quote']['author']} \nQuote: {response['quote']['body']} ")