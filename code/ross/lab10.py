
# opens and reads the CSV file
with open('sample.csv', 'r') as file:
    lines = file.read().split('\n')
    # print("lines: ", lines)

# creates a list of contacts, including the heading
contacts = []
for line in lines:
    contacts.append(line.split(","))

# print("Contacts: ", contacts)

# print(contacts[0][0])
# print(contacts[2])


# add headings (and pops into from contacts) into a list which will be used as keys in the dictionary 
keys = contacts.pop(0)
# print("Keys: ", keys)

# print("Contacts: ", contacts)

matched_contacts = []
for i, contact in enumerate(contacts):
    user_dict = {}
    for j, data in enumerate(contacts[i]):
        user_dict[keys[j]] = contacts[i][j]
    matched_contacts.append(user_dict)
# print(matched_contacts)

# ------------------- VERSION 2 ------------------


# CREATE ------- ask user for attribute, add new contact to list
def create():
    new_contact = {}
    new_contact["name"] = input("What is the name of your new contact? ")
    new_contact["favorite fruit"] = input("What is your contact's favorite fruit? ")
    new_contact["favorite color"] = input("What is your contact's favorite color? ")
    matched_contacts.append(new_contact)
    return "User successfully added to contact list."
# print(create())

# RETRIEVE ----- ask user for contact's name, find the user, and display back to user
def retrieve():
    retrieve_contact = input("Please enter the name of the user who's information you are retrieving: ")
    for i, cont in enumerate(matched_contacts):
        if matched_contacts[i]["name"] == retrieve_contact:
            return matched_contacts[i]


# UPDATE ------- ask user for contact's name, then which attribute user would like to update, and their update input
def update():
    cont_name = input("Who's contact info would you like to update? ")
    print(f"Which attribute of {cont_name}'s would you like to update?")
    update_att = input("Enter 'n' for name, 'f' for favorite fruit, or 'c' for color: ")
    new_att = input(f"What is the updated info for {cont_name}'s attribute: ")
    print("Matched contact list = ", matched_contacts)
    for i, contact in enumerate(matched_contacts):
        if matched_contacts[i]['name'] == cont_name:
            if update_att == 'n':
                matched_contacts[i]['name'] = new_att
            elif update_att == 'f':
                matched_contacts[i]['favorite fruit'] = new_att
            elif update_att == 'c':
                matched_contacts[i]['favorite color'] = new_att
            else:
                print("There was a problem with your updated data input, please try again.")
        else:
            pass
    return f"Contact info successfully updated."

# DELETE ------- ask user for the contact's name, remove the contact with the given name from list
def delete():
    cont_name = input("Who's contact info would you like to delete from the list? ")
    for i, contact in enumerate(matched_contacts):
        if matched_contacts[i]['name'] == cont_name:
            del matched_contacts[i]
    print(matched_contacts)
    return f"You successfully deleted {cont_name}"

# Prompt user to create, retrieve, update, or delete a record
def choice():
    choice = input("What would you like to do? Enter 'c' for create, 'r' for retrieve, 'u' for update, or 'd' to delete a record: ")
    if choice == 'c':
        print(create())
    elif choice == 'r':
        print(retrieve())
    elif choice == 'u':
        print(update())
        print(matched_contacts)
    elif choice == 'd':
        print(delete())
    else:
        print("Sorry you've entered an invalid input. Please try again.")

choice()
again = input("Would you like to make further changes to the list of users? 'y' or 'n': ")
while again == 'y':
    choice()
    again = input("Would you like to make further changes to the list of users? 'y' or 'n': ")

# -------------------- VERSION 3 ---------------------
# This writes the updated into to the CSV file after running user through the REPL
with open('sample_copy.csv', 'w') as f:
    f.write(str(matched_contacts))