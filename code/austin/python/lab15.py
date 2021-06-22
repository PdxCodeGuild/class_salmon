import requests
def random_quote():  
    response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json'})
    quote = (response.json())['quote']
    return (quote['body'] + '\n-\t' + quote['author'])
def keyword_search(keyword,page):
    response = requests.get('https://favqs.com/api/quotes', headers={'Content-Type': 'application/json','Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'filter': keyword, 'page': page})
    quotes = (response.json()['quotes'])
    #print (response.json())
    quotes_lst = [quote['body'] + '\n\t-' + quote['author'] for quote in quotes]
    return '\n\n'.join(quotes_lst)
def last_page(keyword,page):
    response = requests.get('https://favqs.com/api/quotes', headers={'Content-Type': 'application/json','Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'filter': keyword, 'page': page})
    return response.json()['last_page']
def interface():
    while True:
        choice = input('enter a keyword to search for quotes:\nor enter "*" to exit\n')
        if choice == '*':
            return("Come back soon")
        print(next_page(choice))
def next_page(choice):
    page = 1
    print(keyword_search(choice,page),'\n\n' + 'Page ' + str(page) )
    while True:
        next_or_done =  input('Enter "next page" or "done":  ').lower()
        if next_or_done in ['next page','next']:
            if last_page(choice,page) == False:
                page +=1
                print(keyword_search(choice,page),'\n\n' + 'Page ' + str(page) )
            else:
                print("This is the last page!" )
        elif next_or_done == 'done':
            return ''
        else:
            print('follow directions!!!')
#print(keyword_search('doctor',1),'\n\n ^^^^^^^^^^^^^^Page 1^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')
#print(keyword_search('doctor',2))
print(interface())
#print(last_page('apple'))