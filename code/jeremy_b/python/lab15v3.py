"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 15
Version: 3
Date: 6/7/2021

"""

import requests


def get_random_quote():
    response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json',
                                                                   'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', })
    data = response.json()
    return data['quote']['body'], data['quote']['author']


def quote_keyword_search(keyword, page=1):
    result = []
    print("Searching...")
    response = requests.get('https://favqs.com/api/quotes/?filter=' + keyword + '&page=' + str(page),
                            headers={'Content-Type': 'application/json',
                            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', })
    data = response.json()
    result.append([{'quote': data["quotes"][quote]["body"], 'author': data["quotes"][quote]["author"]} for quote in
                   range(len(data['quotes']))])
    is_last_page = data['last_page']
    current_page = data['page']
    print("Search complete!")
    print_keyword_search_results(result, is_last_page, keyword, current_page)


def print_keyword_search_results(results, last_page, keyword, page):
    nav_choice = ''
    while True:
        print(f"Page {page}")
        for quote in range(len(results[0])):
            print(f"{results[0][quote]['quote']}\n   -{results[0][quote]['author']}")
        print(f"Page {page}")
        if page == 1 and last_page is False:
            print(" > \n n ")
        elif last_page is True:
            print("<< <\n f p")
        else:
            print("<< < > \n f p n ")
        nav_choice = input("Action: ").lower()
        if nav_choice == 'b':
            return
        elif nav_choice == 'f':
            page = 1
            quote_keyword_search(keyword)
        elif nav_choice == 'p':
            page -= 1
            quote_keyword_search(keyword, page)
        elif nav_choice == 'n':
            page += 1
            quote_keyword_search(keyword, page)
        elif nav_choice == 'h':
            get_help()


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
            quote_keyword_search(input("Enter keyword to search: "))
        elif choice == 'h':
            get_help()
        elif choice == 'x':
            break
        else:
            raise ValueError
    except ValueError:
        print("invalid choice!  Please try again or type 'h' for help.")
