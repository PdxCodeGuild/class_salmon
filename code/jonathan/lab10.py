with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

# text to a list
def text_to_list(str):
    # adding commas
    lines.insert(1, ',')
    lines.insert(3, ',')
    lines.insert(5, ',')
    lines.insert(7, ',')
    lines.insert(9, ',')
    # into a string
    constring = ' '.join(lines)
    # taking out spaces
    contact_list = constring.replace(" , ", ",")
    # back into a list
    new_list = list(contact_list.split(","))
    return new_list
# list with the headers
def lists(list):
    name_list = []
    counter = 0
    while counter < 1:
            counter += 1
            koto = clean_list.pop(0)
            name_list.append(koto)
            kotoba = clean_list.pop(0)
            name_list.append(kotoba)
            hako = clean_list.pop(0)
            name_list.append(hako)    
            return name_list
# clones the list
def fukusha(list):
    clone = name1.copy()
    return clone
# get names
def get_namae(list):
    counter = 0
    while counter < 1:
        counter += 1
        me = clean_list.pop(0)
        return me
# get foods
def get_kudamono(list):
    counter = 0
    while counter < 1:
        counter += 1
        food = clean_list.pop(0)
        return food
# get colors
def get_iro(list):
    counter = 0
    while counter < 1:
        counter += 1
        shade = clean_list.pop(0)
        return shade
# list to dictionary
def henshin(list):
    i = iter(list)
    list_1 = dict(zip(i, i))
    return list_1

# get clean list
clean_list = text_to_list(lines)

# set up the five lists
name1 = lists(clean_list)
name2 = fukusha(name1)
name3 = fukusha(name1)
name4 = fukusha(name1)
name5 = fukusha(name1)

# get info for 1
me = get_namae(clean_list)
food = get_kudamono(clean_list)
shade = get_iro(clean_list)
# insert them into list
name1.insert(1, me)
name1.insert(3, food)
name1.insert(5, shade)

# get info for 2
me2 = get_namae(clean_list)
food2 = get_kudamono(clean_list)
shade2 = get_iro(clean_list)
# insert them into list
name2.insert(1, me2)
name2.insert(3, food2)
name2.insert(5, shade2)

# get info for 3
me3 = get_namae(clean_list)
food3 = get_kudamono(clean_list)
shade3 = get_iro(clean_list)
# insert them into list
name3.insert(1, me3)
name3.insert(3, food3)
name3.insert(5, shade3)

# get info for 4
me4 = get_namae(clean_list)
food4 = get_kudamono(clean_list)
shade4 = get_iro(clean_list)
# insert them into list
name4.insert(1, me4)
name4.insert(3, food4)
name4.insert(5, shade4)

# get info for 5
me5 = get_namae(clean_list)
food5 = get_kudamono(clean_list)
shade5 = get_iro(clean_list)
# insert them into list
name5.insert(1, me5)
name5.insert(3, food5)
name5.insert(5, shade5)

# convert list to dict
name_dict1 = henshin(name1)
name_dict2 = henshin(name2)
name_dict3 = henshin(name3) 
name_dict4 = henshin(name4)
name_dict5 = henshin(name5)

# add to master list
contacts = []
contacts.append(name_dict1)
contacts.append(name_dict2)
contacts.append(name_dict3)
contacts.append(name_dict4)
contacts.append(name_dict5)

# grab info for user contact
user_name = input("\nPlease enter your name: \n")
user_fruit = input("Please enter your favorite fruit: \n")
user_color = input("and your favorite color please: \n")
user_list = ["Name", "Favorite Fruit", "Favorite Color"]

# insert them into list
user_list.insert(1, user_name)
user_list.insert(3, user_fruit)
user_list.insert(5, user_color)

# convert list to dict
user_dict = henshin(user_list)
# add to master list
contacts.append(user_dict)

#print(contacts)