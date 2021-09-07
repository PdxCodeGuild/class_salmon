import csv
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []
for line in lines:
    contacts.append(line.split(","))

keys = contacts.pop(0)


matched_contacts = []
for i, contact in enumerate(contacts):
    user_dict = {}
    for j, data in enumerate(contacts[i]):
        user_dict[keys[j]] = contacts[i][j]
    matched_contacts.append(user_dict)

def create():
    new_contact = {}
    new_contact["name"] = input("What is the name of your new contact? ")
    new_contact["favorite fruit"] = input("What is your contact's favorite fruit? ")
    new_contact["favorite color"] = input("What is your contact's favorite color? ")
    matched_contacts.append(new_contact)
    return "User added to contact list successfully."

def retrieve():
    retrieve_contact = input("Please enter the name of the user who's information you want to retrieve: ")
    for i, cont in enumerate(matched_contacts):
        if matched_contacts[i]["name"] == retrieve_contact:
            return matched_contacts[i]


def update():
    cont_name = input("Who's contact info would you like to update? ")
    update_att = input(f"What would you like to update for {cont_name}?\nEnter 'n' for name, 'f' for favorite fruit, or 'c' for color: ")
    
    for i, contact in enumerate(matched_contacts):
        if matched_contacts[i]['name'] == cont_name:
            if update_att == 'n':
                new_att = input(f"What is the updated name for {cont_name}: ")
                matched_contacts[i]['name'] = new_att
            elif update_att == 'f':
                new_att = input(f"What is the updated favorite fruit for {cont_name}: ")
                matched_contacts[i]['favorite fruit'] = new_att
            elif update_att == 'c':
                new_att = input(f"What is the updated favorite color for {cont_name}: ")
                matched_contacts[i]['favorite color'] = new_att
            else:
                print("There was a problem with your updated data input, please try again.")
        else:
            pass
    return f"Contact info successfully updated."

def delete():
    cont_name = input("Who's contact info would you like to delete from the list? ")
    for i, contact in enumerate(matched_contacts):
        if matched_contacts[i]['name'] == cont_name:
            del matched_contacts[i]
    # print(matched_contacts)
    return f"You successfully deleted {cont_name}"

def choice():
    choice = (input("What would you like to do? Enter 'c' for create, 'r' for retrieve, 'u' for update, or 'd' to delete a record: ")).lower()
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
cont_crud = input("Would you like to make any more changes to the list of users? 'y' or 'n': ")
while cont_crud == 'y':
    choice()
    cont_crud = input("Would you like to make any more changes to the list of users? 'y' or 'n': ")


with open('contacts.csv', 'w') as f:
    f.write(','.join(keys))
    f.write('\n')
    for key, contact in enumerate(matched_contacts):
        for k in contact:
            f.write(contact[k])
            f.write(',')
        f.write('\n')