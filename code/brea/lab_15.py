import requests

def search_keyword(keyword, page=1):
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data = response.json()
    num = 1
    for x in data['quotes']:
       print(f'{num}. {x["body"]}')
       print(x['author'])
       num += 1
new_search = True
page = 1
while True:
    if new_search:
        user_input = input('Enter what you\'d like to search for here: ')
    new_search = False
    print(f'Page - {page}')
    search_keyword(user_input, page)
    nav = input('Enter "next" and "previous" to use page navigation, enter "quit" or "new" to exit or search for a new keyword: ').lower()
    if nav == 'next':
        page += 1
    elif nav == 'previous':
        if page == 1:
            print('User Error! Page does not exist!')
            continue
        page -= 1    
    elif nav == "quit":
        exit()
    elif nav == 'new':
        new_search = True

    else:
        print('Invalid Entry!')