"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 10
Version: 1
Date: 5/26/2021

"""

import os


def parse_contacts(filename):
    # Read from the CSV to a list of lists, one list per contact.
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
    # Convert each list into a list of its own
    lines = [line.split(',') for line in lines]
    # remove header column from list
    lines.pop(0)
    # convert each list in lines to a dictionary and add to contacts
    contact_list = [{'name': i[0], 'fav_fruit': i[1], 'fav_color': i[2]} for i in lines]

    return contact_list


# define function for creating contacts
def create_contact(filename):
    print("\n" + "Add Contact ".center(24, "="))
    name = input("Contact Name: ")
    fruit = input(f"{name}'s favorite fruit: ")
    color = input(f"{name}'s favorite color: ")
    with open(filename, 'a') as file:
        file.write(f"\n{name},{fruit},{color}")

    return {'name': name, 'fav_fruit': fruit, 'fav_color': color}


def update_contact(contact_list):
    print('\n')
    print(" Update Contact ".center(24, "="))
    while True:
        try:
            contact_to_update = input("Enter name of of contact to update: ")
            for contact in contact_list:
                if contact['name'] == contact_to_update:
                    contact_index = contact_list.index(contact)
                    print(f"Update contact: {contact_to_update}")
                    print("What would you like to update?\n1) Favorite Fruit\n2) Favorite Color")
                    choice = input(": ")
                    try:
                        if int(choice) == 1:
                            contact_list[contact_index]['fav_fruit'] = input("New favorite fruit: ")
                            return contact_list
                        elif int(choice) == 2:
                            contact_list[contact_index]['fav_color'] = input("New favorite color: ")
                            return contact_list
                        else:
                            raise ValueError
                    except ValueError:
                        print("Please enter valid choice!")
        except ValueError:
            print("Name entered is not a valid contact.")


def delete_contact(contact_list):
    contact_to_delete = input("Enter name of of contact to delete: ")
    print('\n')
    for contact in contact_list:
        if contact['name'] == contact_to_delete:
            print(f"Delete contact: {contact_to_delete}")
            if input("Do you want to permanently delete this contact y/n?") in ['y', 'Y']:
                contact_list.pop(contact_list.index(contact))
                print(f"{contact_to_delete} was removed!")
            else:
                print("The operation was not completed.  No contacts were removed.")
    return contact_list


# Program runtime starts here
print(" Contact Management ".center(24, '*'))
# Get file name for contacts list.  This is only needed on initial startup.  The same file will be used until the
# program is restarted.
try:
    file = os.path.join(os.getcwd(), input("Please enter filename with extension: "))
    if file:
        contacts = parse_contacts(file)
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("File not found.")

# Loop for menu options.
while True:
    print("Please choose from the following options:\n1) Add Contact\n2) Update Contact\n3) Delete Contact\n4) Exit")
    choice = input(": ")
    try:
        if int(choice) == 1:
            contacts.append(create_contact(file))
        elif int(choice) == 2:
            contacts = update_contact(contacts)
        elif int(choice) == 3:
            contacts = delete_contact(contacts)
        elif int(choice) == 4:
            # reinsert header into list before writing CSV file
            contacts.insert(0, {'name': 'name', 'fav_fruit': 'fav_fruit', 'fav_color': 'fav_color'})
            with open(file, 'w') as outfile:
                for contact in contacts:
                    if contacts.index(contact) != len(contacts) - 1:
                        outfile.write(f"{contact['name']},{contact['fav_fruit']},{contact['fav_color']}\n")
                    else:
                        outfile.write(f"{contact['name']},{contact['fav_fruit']},{contact['fav_color']}")
            print("\nThank you for using Contact Manager")
            break
        else:
            raise ValueError
    except ValueError:
        print("\n** Please enter a valid choice! **\n")

"""
Notes:

1) There is no check for adding the same name twice...that won't throw an error but could result in unexpected logic
   errors when adding a contact.
"""
