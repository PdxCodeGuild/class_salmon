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
def created_record():
    enter_name = input('Enter your name: ')
    enter_fav_animal = input('Enter your favorite animal: ')
    enter_fav_color = input('Enter your favorite color: ')
    created_dict = {'name': enter_name, 'favorite animal': enter_fav_animal, 'favorite color': enter_fav_color}
    return list_of_dicts.append(created_dict)


# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
def retrieve_record():
    retrieve_name = input("What is the contact's name? ")
    return individual_info[]
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update_record(retrieve_record):
    retrieve_record()


# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
def delete_record(retrieve_record):
    retrieve_record()
    remove_record = input('Whose record would you like to remove? ')
    return

# Version 3 - write the updated contact info to the CSV file to be saved
with open('contacts_copy.csv', 'w') as f:
    f.write(','.join(headers))
    for contact in list_of_dicts:
        f.write('\n')
        for header in headers:
            if header != 'name':
                f.write(',')
            f.write(contact[header])
        

