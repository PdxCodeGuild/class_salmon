import requests
import os
def number_of_pages(search_term):
    #response1 = requests.get('https://icanhazdadjoke.com/search', headers={'accept':'application/json'})
    response = requests.get('https://icanhazdadjoke.com/search', params = {'term': search_term}, headers={'accept':'application/json'})
    pages = (response.json()['total_pages'])
    #print(pages)
    return pages
def number_of_jokes(search_term):
    #response1 = requests.get('https://icanhazdadjoke.com/search', headers={'accept':'application/json'})
    response = requests.get('https://icanhazdadjoke.com/search', params = {'term': search_term}, headers={'accept':'application/json'})
    jokes = (response.json()['total_jokes'])
    #print(pages)
    return jokes
def matching_jokes(search_term):
    pages = (number_of_pages(search_term))
    jokes =[]
    for i in range(1,pages + 1):
        response = requests.get('https://icanhazdadjoke.com/search', params = {'term': search_term, 'pages': i}, headers={'accept':'application/json'})
        data = (response.json())['results']
        for j in data:
            jokes.append(j['joke'])
    return jokes
def search_jokes():
    found = 0
    while found == 0:
        search_term= input('Enter a word to search for dad jokes containing that word \n(or just hit enter to see all jokes):')
        found = number_of_jokes(search_term)
        if found == 0:
            print('No matches for that search found!! Try another search')
    return look_at_results(search_term, found)
def look_at_results(search_term, found):
    i = 0
    matches = matching_jokes(search_term)
    print(matches[0])
    while i < found:
        if found == 1:
            print('This is the only joke that matched you search')
        print('\n')
        choice = input('Would you like to see the next joke?\n1:"previous joke", 2:"next joke", 3: "exit"\n' ).lower()
        if choice == '1':
            if i == 0:
                i = found - 1
            else:
                i -= 1
            os.system('cls')
            print(matches[i])
        elif choice == '2':
            if i == found - 1:
                i = 0
            else:
                i += 1
            os.system('cls')
            print(matches[i])
        elif choice == '3':
            os.system('cls')
            return ('See you later alligator!')
        else:
            os.system('cls')
            print( 'Error: must choose 1,2 or 3' )
print(search_jokes())