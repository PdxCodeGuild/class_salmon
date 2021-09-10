todo = {
    "title": "Go grocery shopping",
    "completed": False
}

title = todo['title']
completed = todo['completed']

# print(title, completed) # Go grocery shopping False

# -------------------------------------------------------------------------------- # 

# change the value at a key
todo['completed'] = True # yay!
# print(todo) # {'title': 'Go grocery shopping', 'completed': True}

# cannot access keys that don't exist
# todo['id'] # KeyError: 'id'

# add a value at the key of 'id'
todo['id'] = 1
# print(todo) # {'title': 'Go grocery shopping', 'completed': True, 'id': 1}

# --------------------------------------------------------------------------------- #

# keyword 'del' to delete items
# del todo['id']
# print(todo) # {'title': 'Go grocery shopping', 'completed': True}

# --------------------------------------------------------------------------------- #

# delete just the value of an item
# todo['id'] = None
# print(todo) # {'title': 'Go grocery shopping', 'completed': True, 'id': None}

# .pop(key) - remove the item at the key and return its value
todo_id = todo.pop('id')
# print(todo_id, todo) # 1 {'title': 'Go grocery shopping', 'completed': True}

# ---------------------------------------------------------------------------------- #

#
# todo['id'] # KeyError: 'id'

# to avoid the KeyError on line 43, 
# we can check if the key is in the dictionary before getting its value

key = 'title'
default = f'That is not a valid key in the dictionary: "{key}"'

# check if the key is in the dictionary's keys
if key in todo.keys():
    value = todo[key]
else:
    value = default

# print(value)

# .get(key, default) - return the value at the key if it exists,
#                      otherwise, return the default value
#                      default value is None if not provided

key = 'id'
default = f'That is not a valid key in the dictionary: "{key}"'

todo_id = todo.get(key)
# print(todo_id) # None

todo_id = todo.get(key, default)
# print(todo_id) # That is not a valid key in the dictionary: "id"

key = 'title'
title = todo.get(key, default)
# print(title) # Go grocery shopping

# ----------------------------------------------------------------------------------- #

# .update(dict) - add the items from the dict to the original

todo.update({
    'id': 1,
    'user': 'KG'
})

# print(todo) # {'title': 'Go grocery shopping', 'completed': True, 'id': 1, 'user': 'KG'}

# -------------------------------------------------------------------------------- #

# .keys(), .values(), .items() - access different parts of the dictionary

# print(todo.keys()) # dict_keys(['title', 'completed', 'id', 'user'])

for key in todo.keys():
    # get the value at the current key
    value = todo[key]

    # print(f'{key}: {value}')

# -------------------------------------------------------------------------------- #

# print(todo.values()) # dict_values(['Go grocery shopping', True, 1, 'KG'])
'''
for value in todo.values():
    print(value)
    
'''

# -------------------------------------------------------------------------------- #

# print(todo.items()) # dict_items([('title', 'Go grocery shopping'), ('completed', True), ('id', 1), ('user', 'KG')]) 

for item in todo.items():
    # use indices to get the key and value from each tuple item
    key = item[0]
    value = item[1]

    # print(f'{key}: {value}')

# ------------------------------------------------------------------------------ #

# instead of creating 3+ individual todo item dictionaries, create a list instead
# todo_1 = {'title': 'Go grocery shopping', 'completed': False, 'id':1}
# todo_2 = {'title': 'Walk the dog', 'completed': True, 'id':2}
# todo_3 = {'title': 'Master Python dictionaries', 'completed': False, 'id':3}

todo_list = [
    {'title': 'Go grocery shopping', 'completed': False, 'id':1},
    {'title': 'Walk the dog', 'completed': True, 'id':2},
    {'title': 'Master Python dictionaries', 'completed': False, 'id':3}
]

# access the value at the key of 'title' for the item at index 1
# print(todo_list[1]['title']) # Walk the dog

for todo in todo_list:
    output = f"{todo['id']}. {todo['title']}\n   Completed: {todo['completed']}\n"
    # print(output)

# ----------------------------------------------------------------------------------- #

# 'nested' dictionaries

fruit_prices = {
    'apple': {
        'green': {
            'inventory': 65, # how many green apples
            'price': 1.33 # price of green apples
        },
        'yellow': 3.33,
        'red': 4.33
    },
    'citrus': {
        'lemon': 2.33,
        'lime': 3.42,
        'grapefruit': 1.23
    }
}

# print(fruit_prices['apple']) # {'green': 2.33, 'yellow': 3.33, 'red': 4.33}

apple_prices = fruit_prices['apple']
# print(apple_prices) # {'green': 2.33, 'yellow': 3.33, 'red': 4.33}
# print(apple_prices['yellow']) 3.33

# print(fruit_prices['apple']['yellow']) # 3.33

# print(fruit_prices['apple']['green']['inventory'])

