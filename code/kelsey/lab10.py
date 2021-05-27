# Lab 10: Contact List

# Version 1 - Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. 
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

list_of_dicts = []

for i in range(len(lines)):
    if i == 0:
        headers = lines[0].split(',')
    else:
        individual_info = {}
        contact = lines[i].split(',')
        individual_info[headers[0]] = contact[0]
        individual_info[headers[1]] = contact[1]
        individual_info[headers[2]] = contact[2]
        list_of_dicts.append(individual_info)

print(list_of_dicts)

#Version 2 -Implement a CRUD REPL

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
def create_record():
    enter_name = input('Enter your name: ')
    enter_fav_animal = input('Enter your favorite animal: ')
    enter_fav_color = input('Enter your favorite color: ')
    create_dict = {}


# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
def retrieve_record():

# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update_record():

# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
def delete_record():

# Version 3 - write the updated contact info to the CSV file to be saved
with open('contacts_copy.csv', 'w') as f:
    f.write(','.join(headers))
    for i in list_of_dicts:
       f.write()

