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


# Version 2 -Implement a CRUD REPL

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
def create_record():   
    enter_name = input('Enter name: ')
    enter_fav_animal = input('Enter favorite animal: ')
    enter_fav_color = input('Enter favorite color: ')
    created_dict = {'name': enter_name, 'favorite animal': enter_fav_animal, 'favorite color': enter_fav_color}
    list_of_dicts.append(created_dict)

# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
def retrieve_record():
    results = []
    enter_name = input('Whose record would you like to retrieve? ')
    for item in list_of_dicts:
        if enter_name == item['name']:
            results.append(item)
    return results
    
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update_record():
    update_record = input('Whose record would you like to update? ')
    for index, item in enumerate(list_of_dicts):
        if update_record == item['name']:
            print('What do you want to update it to? ')
            enter_name = input('Update name to: ')
            enter_fav_animal = input('Update favorite animal to: ')
            enter_fav_color = input('Update favorite color to: ')
            created_dict = {'name': enter_name, 'favorite animal': enter_fav_animal, 'favorite color': enter_fav_color}
            list_of_dicts[index] = created_dict

# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
def delete_record():
    remove_record = input('Whose record would you like to remove? ')
    for index, item in enumerate(list_of_dicts):
        if remove_record == item['name']:
            list_of_dicts.pop(index)

def menu():
    user_options = input('What would you like to do? \n1. Create a record\n2. Retrieve a record\n3. Update a record\n4. Delete a record\n')
    if user_options == '1':
        print(create_record()) 
    elif user_options == '2':
        print(retrieve_record())
    elif user_options == '3':
        print(update_record())
    elif user_options == '4':
        print(delete_record())
    keep_going = input('Continue? Y/N ').upper()
    while keep_going == 'Y':
        print(menu())
        keep_going
        break
    else:
        print('Goodbye!')

menu()

# Version 3 - write the updated contact info to the CSV file to be saved
with open('contacts.csv', 'w') as f:
    f.write(','.join(headers))
    for contact in list_of_dicts:
        f.write('\n')
        for header in headers:
            if header != 'name':
                f.write(',')
            f.write(contact[header])