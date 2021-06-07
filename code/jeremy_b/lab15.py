"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 15
Version: 1
Date: 6/7/2021

"""


import requests


def get_random_quote():
    response = requests.get('https://favqs.com/api/qotd', headers ={'Content-Type':'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', })
    data = response.json()
    quote = data['quote']['body']
    author = data['quote']['author']
    return {quote, author}


def get_help():
    print("Available COmmands:\n 'g': Get random quote.\n'h': get help\n'x': Exit")


# Implement functions here
print(" Quote Machine ".center(25, '*'))
while True:
    choice = ''
    print("Menu\n====\n(R)andom Quote\n(H)elp\nE(x)it")
    choice = input(">> ").lower()
    try:
        if choice == "r":
            quote, author = get_random_quote()
            print(f"Random Quote:\n{quote}\n  -{author}")
        elif choice == 'h':
            get_help()
        elif choice == 'x':
            break
        else:
            raise ValueError
    except ValueError:
        print("invalid choice!  Please try again or type 'h' for help.")
