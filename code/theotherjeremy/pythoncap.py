import requests
import pandas as pd
import secrets
reg_price = []
promo_price = []
promo_per_unit = []
brand = []
size = []
description = []
cheap_chain = []
address = []
product_id = []


# ____________________________ after verification
token = secrets.official

headers = {'accept': 'application/json', 'Authorization': f'Bearer  {token}'}


### _________________MAIN GAME_______________##
zipper = input('What\'s your zip code?  ')
# ___________________For location data------------------
loc_params = {'filter.zipCode.near': zipper, 'filter.radiusInMiles': 20,
              'filter.limit': 200}
loc_response = requests.get(
    'https://api-ce.kroger.com/v1/locations', headers=headers, params=loc_params).json()

location_list = []
for i in loc_response['data']:
    if i['chain'] != 'SHELL COMPANY':
        location_list.append(i['locationId'])
print(len(location_list), 'stores nearby')
top_6_locations = location_list[0:6]
'''


def key_search(sorta='Promo Price'):
    keyword = input('What item would you like to search for?  ')
    for i in top_6_locations:
        params = {'filter.term': keyword, 'filter.fulfillment': 'ais',
                  'filter.limit': 50, 'filter.locationId': i}
        response = requests.get(
            'https://api-ce.kroger.com/v1/products?', headers=headers, params=params).json()
        for i in range(len(response['data'])):
            if 'price' in response['data'][i]['items'][0].keys():
                reg_price.append(response['data']
                                 [i]['items'][0]['price']['regular'])
                promo_price.append(response['data']
                                   [i]['items'][0]['price']['promo'])
                brand.append(response['data'][i]['brand'])
                size.append(response['data'][i]['items'][0]['size'])
                description.append(response['data'][i]['description'])
                product_id.append(response['data'][0]['productId'])


while True:
    key_search()
    main_dict = {"Promo Price": promo_price, "Regular Price": reg_price,
                 'Description': description, 'Brand': brand, 'Size': size, "Product Id": product_id}
    df = pd.DataFrame(main_dict)
    df.sort_values(by=['Promo Price'], inplace=True, ascending=False)
    printout = df.head(50)
    print('\n\n', printout)

    decision = input(
        "Enter a column name to sort by that column, 'new search' to search for a different item, or 'exit' to GTFO:  ")
    if decision == 'exit':
        break
    elif decision in main_dict.keys():
        while decision in main_dict.keys():
            if decision == 'Promo Price':
                df.sort_values(by=[decision], inplace=True, ascending=False)
                print('\n\n', df.head(50))
                decision = input(
                    "Enter a column name to sort by that column, 'new search' to search for a different item, or 'exit' to GTFO:  ")
            else:
                df.sort_values(by=[decision], inplace=True, ascending=True)
                print('\n\n', df.head(50))
                decision = input(
                    "Enter a column name to sort by that column, 'new search' to search for a different item, or 'exit' to GTFO:  ")
    elif decision == 'new search':
        pass


# Enter the index to see what store this is at near you:
'''
for i in top_6_locations:
    params = {'filter.fulfillment': 'ais', 'filter.productId': ['0008700070060'],
              'filter.locationId': i}
    response = requests.get(
        'https://api-ce.kroger.com/v1/products?', headers=headers, params=params).json()
    if response['data'][0]['items'][0]['fulfillment']['instore'] == True:
        cheap_chain.append(i)
        print(cheap_chain)

loc_response = requests.get(
    f'https://api-ce.kroger.com/v1/locations/{cheap_chain[0]}', headers=headers).json()
print(f"Your items are at:  {loc_response['data']['chain']}")
print(f"The address is:  {loc_response['data']['address']}")


"""
##################_____Added Features____#####################
pics = input('Do you want pictures of the items? "y" or "n":  ')
if pics == 'y':
    pictures = ''

"""
