"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 15
Version: 1
Date: 6/7/2021

"""

import requests


def get_random_quote():
    response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json',
                                                                   'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', })
    data = response.json()
    return data['quote']['body'], data['quote']['author']


def quote_keyword_search(keyword):
    last_page = False
    result = []
    current_page = 1
    print("Searching...")
    while not last_page:
        response = requests.get('https://favqs.com/api/quotes/?filter=' + keyword + '&page=' + str(current_page),
                                headers={'Content-Type': 'application/json',
                                'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', })
        data = response.json()
        result.append([{'quote': data["quotes"][quote]["body"], 'author': data["quotes"][quote]["author"]} for quote in
                       range(len(data['quotes']))])
        last_page = data['last_page']
        current_page += 1
    print("Search complete!")
    return result


def print_keyword_search_results(results):
    page_number = 0
    nav_choice = ''
    while True:
        print(f"Page {page_number + 1} of {len(results)}")
        for quote in results[page_number]:
            print(f"{quote['quote']}\n   -{quote['author']}")
        if page_number == 0:
            print(" > >>\n n l")
        elif page_number == len(results) - 1:
            print("<< <\n f p")
        else:
            print("<< < > >>\n f p n l ")
        nav_choice = input("Action: ").lower()
        if nav_choice == 'f':
            page_number = 0
        elif nav_choice == 'p':
            page_number -= 1
        elif nav_choice == 'n':
            print(page_number)
            page_number += 1
            print(page_number)
        elif nav_choice == 'l':
            page_number = len(results) - 1
        elif nav_choice == 'h':
            get_help()
        elif nav_choice == 'b':
            break


def get_help():
    print("Available Commands:\n'g': Get random quote.\n'h': get help\n'x': Exit")
    print("Navigating search results:\n'f': Goto first page\n'p': Goto previous page\n'n': Goto next page\n"
          "'l': Goto last page\n'b': Return to main menu")


# Implement functions here
print(" Quote Machine ".center(25, '*'))
while True:
    choice = ''
    print("Menu\n====\n(R)andom Quote\n(K)eyword Search\n(H)elp\nE(x)it")
    choice = input(">> ").lower()
    try:
        if choice == 'r':
            quote, author = get_random_quote()
            print(f"Random Quote:\n{quote}\n  -{author}")
        elif choice == 'k':
            keyword = input("Enter keyword to search: ")
            search_results = quote_keyword_search(keyword)
            print_keyword_search_results(search_results)

        elif choice == 'h':
            get_help()
        elif choice == 'x':
            break
        else:
            raise ValueError
    except ValueError:
        print("invalid choice!  Please try again or type 'h' for help.")
