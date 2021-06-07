import requests
##########################  Version 1  #######################################
'''
response = requests.get('https://favqs.com/api/qotd', headers={
                        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

data = response.json()
# print(data)

quote = data['quote']['body']
print(quote)
author = data['quote']['author']
print('Author: ', author)
'''
##########################  Version 2  #######################################

'''
'''


def keyword_search(keyword='funny', page=1, ):
    response = requests.get(
        f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers={
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data = response.json()
    print(f'25 quotes about {keyword} - page {page}')
    num = 1
    for i in data['quotes']:
        print(f'{num}: ', i['body'])
        print(i['author'])
        num += 1


keyword = input('Enter a keyword to search for quotes:  ')
keyword_search(keyword)
page = 1
next = ''
while next != 'done':
    next = input('enter "next page", "new keyword", or "done": ')
    if next == 'next page':
        page += 1
        keyword_search(keyword, page)
    elif next == 'new keyword':
        keyword = input('Enter a keyword to search for quotes:  ')
        keyword_search(keyword)
