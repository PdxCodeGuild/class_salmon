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
def clones(list):
    clone = name1.copy()
    return clone
# get names
def get_name(list):
    counter = 0
    while counter < 1:
        counter += 1
        me = clean_list.pop(0)
        return me
# get foods
def get_food(list):
    counter = 0
    while counter < 1:
        counter += 1
        food = clean_list.pop(0)
        return food
# get colors
def get_color(list):
    counter = 0
    while counter < 1:
        counter += 1
        shade = clean_list.pop(0)
        return shade
# list to tuple
def tuplation(list):
    return tuple(list)

# get clean list
clean_list = text_to_list(lines)

# set up the five lists
name1 = lists(clean_list)
name2 = clones(name1)
name3 = clones(name1)
name4 = clones(name1)
name5 = clones(name1)

# get info for 1
me = get_name(clean_list)
food = get_food(clean_list)
shade = get_color(clean_list)
# insert them into list
name1.insert(1, me)
name1.insert(3, food)
name1.insert(5, shade)

# get info for 2
me2 = get_name(clean_list)
food2 = get_food(clean_list)
shade2 = get_color(clean_list)
# insert them into list
name2.insert(1, me2)
name2.insert(3, food2)
name2.insert(5, shade2)

# get info for 3
me3 = get_name(clean_list)
food3 = get_food(clean_list)
shade3 = get_color(clean_list)
# insert them into list
name3.insert(1, me3)
name3.insert(3, food3)
name3.insert(5, shade3)

# get info for 4
me4 = get_name(clean_list)
food4 = get_food(clean_list)
shade4 = get_color(clean_list)
# insert them into list
name4.insert(1, me4)
name4.insert(3, food4)
name4.insert(5, shade4)

# get info for 5
me5 = get_name(clean_list)
food5 = get_food(clean_list)
shade5 = get_color(clean_list)
# insert them into list
name5.insert(1, me5)
name5.insert(3, food5)
name5.insert(5, shade5)

tuple_name1 = (tuplation(name1))
print(tuple_name1)

#print(name1) # ['Name', 'Jonathan', 'Favorite Fruit', 'Apple', 'Favorite Color', 'Off-White']
#print(name2) # ['Name', 'Jon', 'Favorite Fruit', 'Orange', 'Favorite Color', 'Yellow']
#print(name3) # ['Name', 'Nathan', 'Favorite Fruit', 'Papaya', 'Favorite Color', 'Chartreuse']
#print(name4) # ['Name', 'Nate', 'Favorite Fruit', 'Star Fruit', 'Favorite Color', 'Cyan'] 
#print(name5) # ['Name', 'Han', 'Favorite Fruit', 'Banana', 'Favorite Color', 'Blue']

