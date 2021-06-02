# Answer
# with open("contacts_list_working.csv", "r") as f:
#     data_csv = f.read()
# data_csv = [line.split(",") for line in data_csv.split("\n")]
# # csv_lines = data_csv.split("\n")
# # #print(csv_lines)
# # data_csv = []
# # for line in csv_lines:
# #     data_csv.append(line.split(","))

# keys = data_csv[0]
# #print(keys)
# data = []
# # for i, row in list(enumerate(data_csv))[1::]:
# #     row_dict = {}
# #     for j, cell in enumerate(row):
# #         row_dict[keys[j]] = cell
# #     data.append(row_dict)

# # for i, values in list(enumerate(data_csv))[1::]:
# #     print(keys)
# #     print(values)
# #     print(list(zip(keys, values)))
# #     print(dict(zip(keys, values)))
# #     data.append(dict(zip(keys, values)))

# # for i in range(1, len(data_csv)):
# #     data.append(dict(zip(keys, data_csv[i])))

# data = [dict(zip(keys, values)) for values in data_csv[1::]]

# def create_contact(data, keys):
#     # new_contact = {}
#     # for key in keys:
#     #     new_contact[key] = input(f"What is your new contacts {key}?")
#     new_contact = {key: input(f"What is your new contacts {key}?") for key in keys}
#     data.append(new_contact)
#     print(new_contact)

# def read_contact(data, keys):
#     key_string = "\n" + "\n".join(keys) + "\n"
#     key_input = input(f"What would you like to search by? Choose from {key_string}: ")
#     contact_input = input("What is your search term? ")

#     #data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))

#     data_results = []
#     for contact in data:
#         if contact[key_input] == contact_input:
#             data_results.append(contact)
#     print(data_results)

#     return data_results

#     # name = input("name? ")
#     # for contact in data:
#     #     if contact["name"] = name:
#     #         print(contact)
#     #         return contact

# def update_contact(data, keys):
#     data_results = read_contact()

#     index_to_update = int(input(f"Which contact do you want to edit? (1-{len(data_results)}) ")) - 1
#     key_to_update = input(f"Which key would you like to update? {keys} ")
#     value_to_update = input(f"What do you want to change {key_to_update} to? ")
#     data_results[index_to_update][key_to_update] = value_to_update

# def delete_contact(data, keys):
#     data_results = read_contact()
#     index_to_delete = int(input(f"Which contact do you want to delete? (1-{len(data_results)}) ")) -1
#     data.remove(data_results[index_to_delete])

# while True:
#     user_input = input("(c)reate, (r)ead, (u)pdate, (d)elete, (q)uit?")
#     if user_input == "q":
#         break
#     elif user_input == "c":
#         create_contact(data, keys)
#     elif user_input == "r":
#         read_contact(data, keys)
#     elif user_input == "u":
#         update_contact(data, keys)
#     elif user_input == "d":
#         delete_contact(data, keys)

# #print(data_csv)
# #print(data)

# data_csv_output = []
# data_csv_output.append(keys)

# for contact in data:
#     data_csv_output.append(list(contact.values()))
# data_csv_output = [",".join(line) for line in data_csv_output]
# data_csv_output = "\n".join(data_csv_output)

# #print(data_csv_output)
# with open("contacts_list_working.csv", "w") as f:
#     f.write(data_csv_output)

#-----------------------------------------------------------#
# filename = "contacts_list_working.csv"
# open_file = open(filename)

# contacts_list = []

# with open(filename) as file_obj:
#     lines = file_obj.read().strip().split("\n")
#     #print(type(lines))
#     headers = lines.pop(0)
#     #print(f"Headers: {headers}")
#     header_items = headers.split(",")
#     headers_list = [h for h in headers.split(",")]

# #print(headers_list)

# #print(lines)

# for l in lines:
#     #print(l.split(","), "line 19")
#     #print(l)
#     line_list = l.split(",")
#     contacts = dict(zip(header_items,line_list)) 
#     contacts_list.append(contacts)

# #print(contacts_list)
# #print(type(contacts_list))
# print(contacts_list)

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

# # Create a record: ask the user for each attribute, 
# # add a new contact to your contact list with the attributes that the user entered.
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

# # Retrieve a record: ask the user for the contact's name, 
# # find the user with the given name, and display their information
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

# contact_name = input("Enter a name: ")

# print("Which attribute would you like to update?")

# choose_option = int(input("(1) Name (2) Food (3) Color: "))

# if choose_option == 1:
    
#     with open("contacts_list_working.csv", "r+") as file_obj:

#         f_lines = file_obj.readlines()
#         #print(f_lines)
#         names = []
#         foods = []
#         colors = []

#         for f in f_lines:
#                 split_list = f.split(",")
#                 names.append(split_list[0])
#                 foods.append(split_list[1])
#                 colors.append(split_list[2].replace("\n",""))

#         index = ""
#         for n in range(len(names)):
#             #print(n, names[n])
#             if names[n] == contact_name:
#                 index = n
#                 names_output = print(f"Found {names[n]}")
#                 print("Enter new name")
#                 new_name = input("New Name: ")
#                 print(type(f))
#                 replace_string = f.replace((names[n]), (new_name))
#                 file_obj.write(replace_string)

# elif choose_option == 2:
    
#     with open("contacts_list_working.csv", "r+") as file_obj:

#         f_lines = file_obj.readlines()
#         #print(f_lines)
#         names = []
#         foods = []
#         colors = []

#         for f in f_lines:
#                 split_list = f.split(",")
#                 names.append(split_list[0])
#                 foods.append(split_list[1])
#                 colors.append(split_list[2].replace("\n",""))

#         index = ""
#         for n in range(len(names)):
#             #print(n, names[n])
#             if names[n] == contact_name:
#                 index = n
#                 names_output = f"Found {names[n]}"
#                 print("Enter new food")
#                 new_food = input("New food: ")
#                 replace_string = f.replace({foods[n]}, {new_food})
#                 file_obj.write(replace_string)

# elif choose_option == 3:
    
#     with open("contacts_list_working.csv", "r+") as file_obj:

#         f_lines = file_obj.readlines()
#         #print(f_lines)
#         names = []
#         foods = []
#         colors = []

#         for f in f_lines:
#                 split_list = f.split(",")
#                 names.append(split_list[0])
#                 foods.append(split_list[1])
#                 colors.append(split_list[2].replace("\n",""))

#         index = ""
#         for n in range(len(names)):
#             #print(n, names[n])
#             if names[n] == contact_name:
#                 index = n
#                 names_output = f"Found {colors[n]}"
#                 print("Enter new Color")
#                 new_colors = input("New Color: ")
#                 replace_string = f.replace({colors[n]}, {new_colors})
#                 file_obj.write(replace_string)

#------------------
# Input
# 0_contacts_list.py
# [{'name': 'adam', 'food': 'apple', 'color': 'aqua'}, {'name': 'barney', 'food': 'banana', 'color': 'blue'}, {'name': 'charlie', 'food': 'cream', 'color': 'corriander'}, {'name': 'dan', 'food': 'durian', 'color': 'dark grey'}, {'name': 'eric', 'food': 'melon', 'color': 'purpleeric'}]
# Enter a name: adam
# Which attribute would you like to update?
# (1) Name (2) Food (3) Color: 1
# Found adam    
# Enter new name
# New Name: aaron
# <class 'str'>

# Output all messed up. 

# name,food,color
# adam,apple,aqua
# barney,banana,blue
# charlie,cream,corriander
# dan,durian,dark grey
# eric,melon,purpleeric,melon,purpleeric,melon,purpleeric,melon,purple

#------------------

# Delete a record: ask the user for the contact's name, 
# remove the contact with the given name from the contact list.



# When REPL loop finishes, write the updated contact info to the CSV file to be saved.

# ------------------------------------------------------------------------------------- #
