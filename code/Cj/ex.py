import requests
def search(keyword, page=1):
        response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}).json()
        # results = []
        print(response)
        # counter = 1
        # line = f'Results for quotes with keyword {keyword}'
        # for i in response['quotes']:
        #     print(f'{counter}. {i["body"]} \n- {i["author"]}')
        #     # print(f'{counter}. {i}')
        #     counter += 1
        

search('dog')