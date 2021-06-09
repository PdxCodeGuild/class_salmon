import requests
import json
query = json.load(open('response_json.json', 'r'))

# import urllib.request
# from PIL import Image
'''
# ______________________- to veryify
data = {'grant_type': 'client_credentials', 'scope': 'product.compact'}
headers = {'accept': 'application/json', 'Authorization': 'Basic Y2hlY2tlci05YmNmMGVkYzc1OTQ0YjI2MGRlODI3OWQ3YTZkODE3NDYwNjcxNzAxMzE5NTQzNDIyMTY6Qm9zTWRlWXVHS2NRSm95T0Y1SnladVJlbG9pY2g2MGtldHZ3Q3Z0Ug==',
           'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(
    'https://api-ce.kroger.com/v1/connect/oauth2/token', headers=headers, data=data)
response2 = response.text
print(response2)

'''

# ____________________________ after verification
# token = 'eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLWNlLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoidnl6bG52Y3dSUUZyRzZkWDBzU1pEQT09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJjaGVja2VyLTliY2YwZWRjNzU5NDRiMjYwZGU4Mjc5ZDdhNmQ4MTc0NjA2NzE3MDEzMTk1NDM0MjIxNiIsImV4cCI6MTYyMzI3OTIzNCwiaWF0IjoxNjIzMjc3NDI5LCJpc3MiOiJhcGktY2Uua3JvZ2VyLmNvbSIsInN1YiI6IjU0MmVkNDhkLWQwMjctNWMyZS1iYzU5LTY1NDk0NGU1NGYzZiIsInNjb3BlIjoicHJvZHVjdC5jb21wYWN0IiwiYXV0aEF0IjoxNjIzMjc3NDM0ODc4NDg4MTA5LCJhenAiOiJjaGVja2VyLTliY2YwZWRjNzU5NDRiMjYwZGU4Mjc5ZDdhNmQ4MTc0NjA2NzE3MDEzMTk1NDM0MjIxNiJ9.QS_rATVyBVKLr_9DkyF9HyLEih3FKKHkDwFvl1ekBr94u9jPUZvhbRvP2gmwQcqAaZbOuZgm-bjJmAcNZ8Fjb8Ag-5lcl3j_QrF0jcKL1kXS3HBqq4u5TSp42PaX1gPGbyWGHczezAO2dKmANH7AXPdzAOc8seAVX6zL5MPSX_IoEwp4mSrPTFsvx9bSWxYnSx5GKOr5taq1CqkdWtMM-1fgAeVU7MDYjdIJ5DHGcoHqQTSsK2whO9O2QJsbwC9NHBS-eRp47wX7EsStIXj4Od-lS5NMM4lUKNTSLEuelcPAQoWdcbxawyGf3dxb17CqYFdrT4Q1rUAYMYD3JCZJcQ'
# headers = {'accept': 'application/json', 'Authorization': f'Bearer  {token}'}
# params = {'filter.zipCode.near': 91321,
#           'filter.term': 'beer', 'filter.fulfillment': 'ais', 'filter.limit': 50}
# response = requests.get(
#     'https://api-ce.kroger.com/v1/products?', headers=headers, params=params)
# print(response)
# # response2 = response.text
# with open('response_json.json', 'w') as file:
#     file.write(response.text)
# response = response.json()


#________Playground_________________________________#
print(query['data'][0]['brand'])

'''
for i in range(len(query['data'])):
    print(query['data'][i]['brand'])


def keyword_search(keyword,):
    response = requests.get(
    'https://api-ce.kroger.com/v1/products?', headers=headers, params=params)
    params = {'filter.zipCode.near': 91321,
          'filter.term': f'{keyword}', 'filter.fulfillment': 'ais'}
    print(data[0]['brand'])


keyword = input('What would you like to search for?  ')
keyword_search(keyword, )


##################_____Added Features____#####################
pics = input('Do you want pictures of the items? "y" or "n":  ')
if pics = 'y':
    pictures =

'''
