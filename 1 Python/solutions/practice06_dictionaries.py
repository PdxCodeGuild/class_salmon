



contact = {'name': 'Bob', 'age': 67, 'favorite color': 'blue'}

# for key in contact:
#     print(key, contact[key])
# print(type(contact.keys()))

# for key in contact.keys():
# print(list(contact.keys()))
# print(list(contact.values()))
# print(list(contact.items()))

# print(contact['name'])
# print(contact['favorite number']) # KeyError
# if 'favorite number' in contact:
# print(contact.get('favorite number')) # None
# print(contact.get('favorite number', 4)) # None

# exit()




# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

def create_contact(name, age):

    address_book = {}
    address_book['name'] = name
    address_book['age'] = age
    return address_book

    # return {'name': name, 'age': age}

# print(create_contact('Bob', 67))  # {'name': 'Bob', 'age': 67}
# print(create_contact('Linda', 34)) # {'name': 'Linda', 'age': 34}

# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

def has_key(d, key):
    if key in d:
        return True
    else:
        return False
    
    # return key in d

# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False

# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

def is_empty(d):
    if len(d) == 0:
        return True
    else:
        return False
    # return len(d) == 0
    # return d == {}
# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False

# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.

def find_key(d, value):

    # iterate over the keys of the dictionary
    for key in d:
        # if the value for the key is equal to the value we're looking for
        if value == d[key]:
            # return the key for that value
            return key
    # if we cannot find the key for the value, return None
    return None


# print(find_key({'a': 1, 'b': 2, 'c': 3}, 2)) # b
# print(find_key({'a': 1, 'b': 2}, 3)) # None

# Reverse Dict =================================================================
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

def reverse_dict(d):
    # key_list = list(d.keys())
    # value_list = list(d.values())
    # new_d = {}
    # for i in range(len(key_list)):
    #     new_d[value_list[i]] = key_list[i]
    # return new_d

    new_d = {}
    for key in d:
        new_d[d[key]] = key
    return new_d

# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}

# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

def merge(list1, list2):
    new_d = {}
    for i in range(len(list1)):
        new_d[list1[i]] = list2[i]
    return new_d
# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}


# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    new_d = d.copy()
    for key in d:
        if d[key] < 10:
            del new_d[key]
    return new_d

    # new_d = {}
    # for key in d:
    #     if d[key] >= 10:
    #         new_d[key] = d[key]
    # return new_d

# print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) # {'b': 15, 'c': 12}

# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def average_age(ld):
    total = 0
    for i in range(len(ld)):
        total += ld[i]['age']
    total /= len(ld)
    return total

contacts = [{
    'name': 'Bob',
    'age': 67
},{
    'name': 'Jane',
    'age': 45
},{
    'name': 'Joanne',
    'age': 8
}]
# print(average_age(contacts)) # 40


# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def average_lists(d):
    ...
# print(average_lists({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]})) # {'a': 4, 'b': 5, 'c': 3}

# Merge Dictionaries ===========================================================
# Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key

def merge_dictionaries(d1, d2):
    ...

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(merge_dictionaries(d1, d2)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Count Votes ==================================================================
# Write a function that takes a list of strings and counts of the number of occurances.

def count_votes(votes):
    # initialize a blank dictionary
    votes_d = {}
    # iterate over the list of votes

    # for candidate in votes:
    #     if candidate not in votes_d:
    #         votes_d[candidate] = 1
    #     else:
    #         votes_d[candidate] += 1

    for i in range(len(votes)):
        # add the name to the dictionary or update the value

        # votes_d[votes[i]] = votes_d.get(votes[i], 0) + 1

        if votes[i] not in votes_d:
            votes_d[votes[i]] = 1
        else:
            votes_d[votes[i]] += 1
    return votes_d
        

    # return the dictionary
# votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
# print(count_votes(votes)) # {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}



# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries representing a cart and a dictionary representing prices.

def cart_total(prices, cart):
    total = 0
    for item in cart:
        name = item['name']
        quantity = item['quantity']
        total += quantity*prices[name]

        # total += item['quantity']*prices[item['name']]

    return total

# prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
# cart = [{'name': 'apples', 'quantity': 3}, {'name': 'kiwis', 'quantity': 4}]
# print(cart_total(prices, cart)) # 11.0

