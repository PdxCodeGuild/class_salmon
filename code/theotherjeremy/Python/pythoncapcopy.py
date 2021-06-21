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
percent_off = []

### _____________After Verification___________###
token = secrets.official

headers = {'accept': 'application/json', 'Authorization': f'Bearer  {token}'}


### _______________For Location Data__________###
zipper = input('What\'s your zip code?  ')
loc_params = {'filter.zipCode.near': zipper, 'filter.radiusInMiles': 8,
              'filter.limit': 200}
loc_response = requests.get(
    'https://api-ce.kroger.com/v1/locations', headers=headers, params=loc_params).json()

location_list = []
for i in loc_response['data']:
    if i['chain'] != 'SHELL COMPANY':
        location_list.append(i['locationId'])
print('I found', len(location_list), 'stores nearby!')
top_6_locations = location_list[0:6]


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
                product_id.append(response['data'][i]['productId'])
                if response['data'][i]['items'][0]['price']['promo'] == 0.00:
                    percent_off.append(0.00)
                else:
                    percent_off.append(float('{:.2f}'.format((((response['data'][i]['items'][0]['price']['regular'])-(
                        response['data'][i]['items'][0]['price']['promo'])) / (response['data'][i]['items'][0]['price']['regular']))*100)))


def item_find(decision):
    cheap_index = int(decision)
    cheap_id = df.iloc[cheap_index, 6]
    for i in top_6_locations:
        params = {'filter.fulfillment': 'ais', 'filter.locationId': i,
                  'filter.productId': cheap_id}
        response = requests.get(
            'https://api-ce.kroger.com/v1/products?', headers=headers, params=params).json()
        if response['data'][0]['productId'] == cheap_id:
            cheap_chain.append(i)
        else:
            pass
    print(f'{len(cheap_chain)} of those stores have this product.')
    loc_response = requests.get(
        f'https://api-ce.kroger.com/v1/locations/{cheap_chain[0]}', headers=headers).json()
    print(f"Your items are at your local {loc_response['data']['chain']}")
    print(
        f"The address is:  {loc_response['data']['address']['addressLine1']}, {loc_response['data']['address']['city']}")


##____________Main Game_____________##
loopy = True
while loopy == True:
    reg_price = []
    promo_price = []
    promo_per_unit = []
    brand = []
    size = []
    description = []
    cheap_chain = []
    address = []
    product_id = []
    percent_off = []
    decision = ''
    key_search()
    main_dict = {"Promo Price": promo_price, "Regular Price": reg_price, "Percent Off": percent_off,
                 'Description': description, 'Brand': brand, 'Size': size, "Product Id": product_id}
    df = pd.DataFrame(main_dict)
    df.sort_values(by=['Percent Off'], inplace=True, ascending=False)
    printout = df.head(50)
    print('\n\n', printout, '\n\n')

    decision = input(
        "Please enter: \nA column name to sort by that column: \nAn index value to see available stores: \n'new search' to search for a different item: \n'exit' to GTFO: \n")
    if decision == 'exit':
        loopy = False
    elif decision in main_dict.keys():
        while decision in main_dict.keys():
            if decision == 'Promo Price' or decision == 'Percent Off' or decision == "Size":
                df.sort_values(by=[decision], inplace=True, ascending=False)
                print('\n\n', df.head(50), '\n\n')
                decision = input(
                    "Please enter: \nA column name to sort by that column: \nAn index value to see available stores: \n'new search' to search for a different item: \n'exit' to GTFO: \n")
                if decision == 'exit':
                    loopy = False
                else:
                    continue
            else:
                df.sort_values(by=[decision], inplace=True, ascending=True)
                print('\n\n', df.head(50), '\n\n')
                decision = input(
                    "Please enter: \nA column name to sort by that column \nAn index value to see available stores \n'new search' to search for a different item \n'exit' to GTFO \n")
                if decision == 'exit':
                    loopy = False
                else:
                    continue
    elif decision == 'new search':
        pass
    else:
        item_find(decision)


"""
"""

##################_____Added Features____#####################
# pics using pillow

# pagination

# eliminate duplicates in dataframe

# price per unit using RegEx

# whole grocery list

# add other grocery chains to see ALL local prices
