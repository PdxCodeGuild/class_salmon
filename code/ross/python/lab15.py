import requests

def get_quote():
    response = requests.get('https://favqs.com/api/qotd', headers={'Accept': "application/json"})
    data = response.json()
    data = data['quote']
    quote = data['body']
    author = data['author']
    return print(f"\n{quote}\n\n\t- {author}\n")

def keyword_search(keyword, page):
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(f'https://favqs.com/api/quotes/?page={page}&filter={keyword}', headers=headers)
    data = response.json()
    page_num = data['page']
    # print(f"Data: {data}")
    data = data['quotes']
    # print(f"Data: {data}")
    print(f"There are {len(data)} quotes associated with the keyword {keyword} - page {page_num}")
    for i in range(len(data)):
        try: 
            print(f"""
            \n{data[i]['body']}
            \n\t- {data[i]['author']}
            """)
        except KeyError:
            print("Sorry, we could not find any more quotes with your keyword.")

def choice():
    choice = input("Would you like a random quote or to search for a quote by keyword?\n'R' for random, 'K' for keyword, or any other key to exit: ").upper()
    page = 1
    if choice == 'R':
        get_quote()
    elif choice == 'K':
        keyword = input("Type in the keyword you'd like to search by: ")
        keyword_search(keyword, page)
        while True:
            next_choice = input("Enter 'next page' for more quotes containing your keyword, 'new' for starting over, or 'done' to exit: ")
            if next_choice == 'next page':
                page += 1
            elif next_choice == 'new':
                page = 1
                keyword = input("Type in the keyword you'd like to search by: ")
            else:
                break
            keyword_search(keyword, page)
    else:
        print("Okay, have a good day!")

choice()