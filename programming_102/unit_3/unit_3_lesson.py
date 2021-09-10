'''
Programming 102
Unit 3
'''

'''
Dictionaries ('dict')

- are one of the most powerful datatypes in Python
- can be used to store large amounts of data and make accessing that data quick and easy
- are collections of key:value pairs
- keys are used to access the values

- are defined using curly brackets {}
- keys and values are separated with colons
- key:value pairs are called 'items'
- items are separated with commas
'''

# blank dictionary
blank_dictionary = {}
# print(blank_dictionary, type(blank_dictionary)) # {} <class 'dict'>

# ----------------------------------------------------------------------------------------------- #

# keys are generally strings
# values can be ANY datatype, including other dictionaries

example_dict = {'a': 11, 'b': 22, 'c': 33}

# dictionaries can be organized vertically
example_dict = {
    # key: value,
    'a': 11,
    'b': 22,
    'c': 33,
}

# -------------------------------------------------------------------------------------- #

# dictionary values are retrieved by placing their
# keys in SQUARE brackets after the dictionary name
# print(example_dict['a']) # 11
# print(example_dict['b']) # 22
# print(example_dict['c']) # 33

# -------------------------------------------------------------------------------------- #


# dictionaries are usually used to group related data

address = {
    'street': '123 Faux St.',
    'city': 'Portland',
    'state': 'Oregon',
    'zipcode': 123456
}

# print(address['street'])
# print(address['city'], address['state'])
# print(address['zipcode'])

# ------------------------------------------------------------------------------------------- #

book = {
    'title': 'The Hobbit',
    'author': 'J.R.R Tolkien',
    'pages': 200
}

# print(f"The book {book['title']} has {book['pages']} pages and was written by {book['author']}")

# -------------------------------------------------------------------------------------------- #

# cannot retrieve values at non-existent keys
# book['characters'] # KeyError: 'characters'

# -------------------------------------------------------------------------------------------- #

# add a key:value pair to the dictionary
book['characters'] = ['Bilbo', 'Gandalf', 'Smaug']
# print(book)

# add an item to the list at the key of 'characters'

# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug']
book['characters'].append('Balin')
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug', 'Balin']

# -------------------------------------------------------------------------------------------- #

# change the value at a key
book['pages'] = 1000
# print(book)

# ----------------------------------------------------------------------------------------------- #

# delete a key:value pair
# keyword 'del'
# del book['pages']
# print(book)

# ------------------------------------------------------------------------------------------------ #

# dictionary methods

# .pop(key) - remove the key:value pair at the key and return the value
pages = book.pop('pages')
# print(pages, book)

# ------------------------------------------------------------------------------------------------- #

# .update(new_dict) - add the items from the new_dict to the original

new_items = {
    'pages': 200,
    'isbn_number': 98765432345678
}

# book.update(new_items)
# print(book)

# -------------------------------------------------------------------------------------------------- #

# as of Python 3.9, we can use the 'merge' operator |

book = book | new_items # merge the two dictionaries
# print(book)

# ------------------------------------------------------------------------------------------------ #


# Fruit Stand

fruit_prices = {
    'apple': 2.33,
    'banana': 1.76,
    'mango': 3.99,
}

# could use a dictionary to manage inventory as well
inventory = {
    'apple': 10,
    'banana': 20,
    'mango': 30
}

while True:
    # ask the user which fruit they want to buy
    fruit_name = input("\nEnter the name of the fruit you want to buy or 'done' to quit: ")

    # exit if 'done'
    if fruit_name == 'done':
        print("\nThanks for shopping!")
        break  # end the loop

    # use the user's fruit_name as the key in the dictionary to get its price
    price_per = fruit_prices[fruit_name]

    # ask the user how many they want
    quantity = input("Enter the quantity: ")

    # convert the quantity to integer
    quantity = int(quantity)

    # calculate the total
    total = quantity * price_per

    print(f"{quantity} {fruit_name} @ ${price_per} each - ${total}")

