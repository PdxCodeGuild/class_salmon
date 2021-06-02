filename = "contacts_list_working.csv"
open_file = open(filename)

contacts_list = []

with open(filename) as file_obj:
    lines = file_obj.read().strip().split("\n")
    #print(type(lines))
    headers = lines.pop(0)
    #print(f"Headers: {headers}")
    header_items = headers.split(",")
    headers_list = [h for h in headers.split(",")]

#print(headers_list)

#print(lines)

for l in lines:
    #print(l.split(","), "line 19")
    #print(l)
    line_list = l.split(",")
    contacts = dict(zip(header_items,line_list)) 
    contacts_list.append(contacts)

#print(contacts_list)
#print(type(contacts_list))
#print(contacts_list)

# vvv Works somewhat
#from collections import ChainMap
#res = ChainMap(*contacts_list)
#print(res)

# ChainMap({'name': 'adam', 'favorite food': 'apple', 'favorite color': 'aqua'},
#  {'name': 'brandy', 'favorite food': 'banana', 'favorite color': 'blue'},
#  {'name': 'charlie', 'favorite food': 'cherry', 'favorite color': 'cyan'})
# ^^^ Works somewhat

# vvv Works somewhat
# from functools import reduce
# res = reduce(lambda d, src:d.update(src) or d, contacts_list, {})
# print(res)

# {'name': 'charlie', 'favorite food': 'cherry', 'favorite color': 'cyan'}
# ^^^ Works somewhat

# flat_list = []

# for element in contacts_list:
#     if type(element) is dict:
#         for item in element:
#             flat_list.append(item)
    
#     else:
#         flat_list.append(element)

# print(flat_list)

#----------------------------
# def switch():
#     name = input("Enter the name: ")
#     fav_food = input("Enter the favorite food: ")
#     fav_color = input("Enter the favorite color: ")

#     print(f"""Make a selection
# 1) Create Record
# 2) Retrieve Record
# 3) Update Record
# 4) Delete Record
# 0) quit""")
        
#     option = int(input("Choose: "))

#     def create_record():
#         print("create record")
#         lines.append('{name},{fav_food},{fav_color}')
#         print(lines)


#     def quit():
#         False
#         exit()

#     def default():
#         print("Incorrect option")
    
#     # Switch map
#     switch = {
#         1: create_record,
#         0: quit
#     }
#     switch.get(option, default)()


# while True:
#     switch()

#-------------------------------------
#-------------------------------------

# Create a record: ask the user for each attribute, 
# add a new contact to your contact list with the attributes that the user entered.
# new_name = input("Enter a name: ")
# new_food = input("Enter a food: ")
# new_color = input("Enter a color: ")

# with open("contacts_list_working.csv", "a") as f:

#     f.write(new_name)
#     f.write(",")
#     f.write(new_food)
#     f.write(",")
#     f.write(new_color)
#     print(f)

# Retrieve a record: ask the user for the contact's name, 
# find the user with the given name, and display their information
# new_name = input("Enter a name: ")

# contact_list = []
# with open("contacts_list_working.csv", "r") as f:

#     f_lines = f.readlines()
#     #print(f_lines)
#     names = []
#     foods = []
#     colors = []

#     for f in f_lines:
#             split_list = f.split(",")
#             names.append(split_list[0])
#             foods.append(split_list[1])
#             colors.append(split_list[2].replace("\n",""))

#     #print(names)
#     #print(foods)
#     #print(colors)
#     index = ""
#     for n in range(len(names)):
#         #print(n, names[n])
#         if names[n] == new_name:
#             index = n
#             names_output = f"Found {names[n]}"
#             foods_output = foods[index]
#             colors_output = colors[index]
#             print(f"{names_output}, likes {foods_output} and the color {colors_output}")



# Update a record: ask the user for the contact's name, 
# then for which attribute of the user they'd like to update and 
# the value of the attribute they'd like to set.

contact_name = input("Enter a name: ")

print("Which attribute would you like to update?")

choose_option = int(input("(1) Name (2) Food (3) Color: "))

if choose_option == 1:
    
    with open("contacts_list_working.csv", "r+") as f:

        f_lines = f.readlines()
        #print(f_lines)
        names = []
        foods = []
        colors = []

        for f in f_lines:
                split_list = f.split(",")
                names.append(split_list[0])
                foods.append(split_list[1])
                colors.append(split_list[2].replace("\n",""))

        index = ""
        for n in range(len(names)):
            #print(n, names[n])
            if names[n] == contact_name:
                index = n
                names_output = f"Found {names[n]}"
                print("Enter new name")
                new_name = input("New Name: ")
                replace_string = f.replace({names[n]}, {new_name})
                f.write(replace_string)

elif choose_option == 2:
    
    with open("contacts_list_working.csv", "r+") as f:

        f_lines = f.readlines()
        #print(f_lines)
        names = []
        foods = []
        colors = []

        for f in f_lines:
                split_list = f.split(",")
                names.append(split_list[0])
                foods.append(split_list[1])
                colors.append(split_list[2].replace("\n",""))

        index = ""
        for n in range(len(names)):
            #print(n, names[n])
            if names[n] == contact_name:
                index = n
                names_output = f"Found {names[n]}"
                print("Enter new food")
                new_food = input("New food: ")
                replace_string = f.replace({foods[n]}, {new_food})
                f.write(replace_string)

elif choose_option == 3:
    
    with open("contacts_list_working.csv", "r+") as f:

        f_lines = f.readlines()
        #print(f_lines)
        names = []
        foods = []
        colors = []

        for f in f_lines:
                split_list = f.split(",")
                names.append(split_list[0])
                foods.append(split_list[1])
                colors.append(split_list[2].replace("\n",""))

        index = ""
        for n in range(len(names)):
            #print(n, names[n])
            if names[n] == contact_name:
                index = n
                names_output = f"Found {colors[n]}"
                print("Enter new Color")
                new_colors = input("New Color: ")
                replace_string = f.replace({colors[n]}, {new_colors})
                f.write(replace_string)

# Delete a record: ask the user for the contact's name, 
# remove the contact with the given name from the contact list.



# When REPL loop finishes, write the updated contact info to the CSV file to be saved.