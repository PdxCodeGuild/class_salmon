import requests
import json
# from kroger import official
# print(official)
query = json.load(open('response_json.json', 'r'))
'''
# import urllib.request
# from PIL import Image
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
# token = official #'eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLWNlLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoidnl6bG52Y3dSUUZyRzZkWDBzU1pEQT09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJjaGVja2VyLTliY2YwZWRjNzU5NDRiMjYwZGU4Mjc5ZDdhNmQ4MTc0NjA2NzE3MDEzMTk1NDM0MjIxNiIsImV4cCI6MTYyMzI3OTIzNCwiaWF0IjoxNjIzMjc3NDI5LCJpc3MiOiJhcGktY2Uua3JvZ2VyLmNvbSIsInN1YiI6IjU0MmVkNDhkLWQwMjctNWMyZS1iYzU5LTY1NDk0NGU1NGYzZiIsInNjb3BlIjoicHJvZHVjdC5jb21wYWN0IiwiYXV0aEF0IjoxNjIzMjc3NDM0ODc4NDg4MTA5LCJhenAiOiJjaGVja2VyLTliY2YwZWRjNzU5NDRiMjYwZGU4Mjc5ZDdhNmQ4MTc0NjA2NzE3MDEzMTk1NDM0MjIxNiJ9.QS_rATVyBVKLr_9DkyF9HyLEih3FKKHkDwFvl1ekBr94u9jPUZvhbRvP2gmwQcqAaZbOuZgm-bjJmAcNZ8Fjb8Ag-5lcl3j_QrF0jcKL1kXS3HBqq4u5TSp42PaX1gPGbyWGHczezAO2dKmANH7AXPdzAOc8seAVX6zL5MPSX_IoEwp4mSrPTFsvx9bSWxYnSx5GKOr5taq1CqkdWtMM-1fgAeVU7MDYjdIJ5DHGcoHqQTSsK2whO9O2QJsbwC9NHBS-eRp47wX7EsStIXj4Od-lS5NMM4lUKNTSLEuelcPAQoWdcbxawyGf3dxb17CqYFdrT4Q1rUAYMYD3JCZJcQ'
# headers = {'accept': 'application/json', 'Authorization': f'Bearer  {token}'}
# params = {'filter.zipCode.near': 91321, 'filter.radiusInMiles': 15
#           'filter.term': 'hummus', 'filter.fulfillment': 'ais', 'filter.limit': 200}
# response = requests.get(
#     'https://api-ce.kroger.com/v1/products?', headers=headers, params=params)
# print(response)
# # response2 = response.text
# with open('response_json.json', 'w') as file:
#     file.write(response.text)
# response = response.json()


#________Playground_________________________________#


# ---------------print this to see if price was given in request
reg_price = []
for i in range(len(query['data'])):
    reg_price.append(query['data']
                     [i]['items'][0])
print(reg_price)

# ------------------if price is given, delete one above, then below will give regular price list


def reg_price_search():
    reg_price = []
    for i in range(len(query['data'])):
        reg_price.append(query['data']
                         [i]['items'][0]['price']['regular'])
    return reg_price


def promo_price_search():
    promo_price = []
    for i in range(len(query['data'])):
        promo_price.append(query['data']
                           [i]['items'][0]['price']['promo'])
    return promo_price


def promo_per_unit_search():
    promo_per_unit = []
    for i in range(len(query['data'])):
        promo_per_unit.append(query['data']
                              [i]['items'][0]['price']['promoPerUnitEstimate'])
    return promo_per_unit


def brand_search():
    brand = []
    for i in range(len(query['data'])):
        brand.append(query['data'][i]['brand'])
    return brand


def size_search():
    size = []
    for i in range(len(query['data'])):
        size.append(query['data'][i]['items'][0]['size'])
    return size


def description_search():
    description = []
    for i in range(len(query['data'])):
        description.append(query['data'][i]['description'])
    return description


def sold_by_search():
    sold_by = []
    for i in range(len(query['data'])):
        sold_by.append(query['data'][i]['items'][0]['soldBy'])
    return sold_by


def ppu(keyword, zipper):

    ### _________________MAIN GAME_______________##
zipper = input('What\'s your zip code?  ')
keyword = input('What item would you like to search for?  ')
params = {'filter.zipCode.near': 91321, 'filter.radiusInMiles': 15,
          'filter.term': 'hummus', 'filter.fulfillment': 'ais', 'filter.limit': 200}
# response = requests.get('https://api-ce.kroger.com/v1/products?', headers=headers, params=params)
# Then run my functions to get lists of data


'''

##################_____Added Features____#####################
pics = input('Do you want pictures of the items? "y" or "n":  ')
if pics = 'y':
    pictures =

'''
