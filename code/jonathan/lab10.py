with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

# create new user information
def tsukuru(a):
    # grab info for user contact
    user_name = input("\nPlease enter your name: \n").capitalize()
    user_fruit = input("Please enter your favorite fruit: \n").capitalize()
    user_color = input("and your favorite color please: \n").capitalize()
    user_list_values = []
    # insert them into list
    user_list_values.append(user_name)
    user_list_values.append(user_fruit)
    user_list_values.append(user_color)
    # convert list to dict
    user_dict = dict(zip(headers, user_list_values))
    # add to master list
    contacts.append(user_dict)
    return contacts
# find if user is in contacts
def sagasu(a, b):    
            for contact in range(len(contacts)):
                if contacts[contact]["Name"] == user_search:      
                    return True
            else: 
                return False
# finds the user and returns their data
def search(a):
    for contact in contacts:
        if contact["Name"] == user_search:
            return contact

# blank list
contacts = []

# lines into lists
headers = lines[0].split(',')
name1 = lines[1].split(',')
name2 = lines[2].split(',')
name3 = lines[3].split(',')
name4 = lines[4].split(',')
name5 = lines[5].split(',')

# list to dictionaries
person_dict1 = dict(zip(headers, name1))
person_dict2 = dict(zip(headers, name2))
person_dict3 = dict(zip(headers, name3))
person_dict4 = dict(zip(headers, name4))
person_dict5 = dict(zip(headers, name5))

# add dictionaries to list
contacts.append(person_dict1)
contacts.append(person_dict2)
contacts.append(person_dict3)
contacts.append(person_dict4)
contacts.append(person_dict5)

# crud
user_choice = input("What would you like to do today?\n[CREATE][RETRIEVE][UPDATE][DELETE][QUIT]\n").lower()

# create
if user_choice == "create":
    print(f"Updated list of contacts:\n{tsukuru(contacts)}")
# retrieve
if user_choice == "retrieve":
    user_search = input("Please enter the usersname you would like to search for:\n").capitalize()
    if sagasu(user_search, contacts) == True:
        print(search(user_search))
    else:
        print("\nThere was no user with that username.\nGoodbye")
        quit()      
# update
if user_choice == "update":
    user_search = input("Please enter the username you would like to update:\n").capitalize()
    if sagasu(user_search, contacts) == True:
        target_contact = search(user_search)
        edit_choice = input("Select what you would like to update:\n[NAME][FAVORITE FRUIT][FAVORITE COLOR]\n").lower()
        if edit_choice == "name":
            edit_answer = input("Please enter the new name:\n").capitalize()
            target_contact["Name"] = edit_answer
            print(target_contact)
        if edit_choice == "favorite fruit":
            edit_answer = input("Please enter the new favorite fruit:\n").capitalize()
            target_contact["Favorite Fruit"] = edit_answer
            print(target_contact)
        if edit_choice == "favorite color":
            edit_answer = input("Please enter the new favorite color:\n").capitalize()
            target_contact["Favorite Color"] = edit_answer
            print(target_contact)
    else:
        print("\nThere was no user with that username.\nGoodbye")
        quit()
# delete
if user_choice == "delete":
    user_search = input("Please enter the username you would like to delete:\n").capitalize()
    if sagasu(user_search, contacts) == True:
        target_contact = search(user_search)
        rusure = input(f"Are you sure you would like to delete {user_search.capitalize()} \nY/N?\n").capitalize()
        if rusure == "Y":
            target_index = contacts.index(target_contact)
            del contacts[target_index]
            print(f"Updated list of contacts:\n{contacts}")
        else:
            print("\nGoodbye")
            quit()
else:
    print("\nGoodbye")
    quit()