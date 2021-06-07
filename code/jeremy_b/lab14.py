"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 14
Version: 1
Date: 6/4/2021

"""

import requests


def get_dad_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json', })
    data = response.json()
    return data['joke']


def search_dad_jokes():
    term = input("Enter search term: ")
    response = requests.get('https://icanhazdadjoke.com/search?term='+term, headers={'Accept': 'application/json', })
    data = response.json()
    jokes = [data['results'][i]['joke'] for i in range(len(data['results']))]
    print(f"Search returned {len(jokes)} jokes.")
    for joke in range(len(jokes)):
        print(f"Joke #{joke + 1}: {jokes[joke]}")


while True:
    print(" Dad Joke Machine ".center(24, '='))
    print("(G)et random dad joke\n(S)earch for dad joke\nE(x)it")
    try:
        choice = input("What would you like to do? ").lower()
        if choice == 'g':
            print(get_dad_joke())
        elif choice == 's':
            search_dad_jokes()
        elif choice == 'help':
            print(" Help ".center(12, '*'))
            print("Commands:\n'g': Get random dad joke\n's': Search for dad jokes\n'x': Exit")
        elif choice == 'x':
            print("Thanks for checking out the dad jokes!")
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid selection.  Type 'help' for commands.")


