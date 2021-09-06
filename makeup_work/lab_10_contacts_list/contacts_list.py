all_contacts = []
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    headers = lines[0]
    each_header = headers.split(",")
    all_rows = lines[1::]
    for row in all_rows:
        contact = {}
        i = 0
        for element in row.split(","):
            contact[each_header[i]] = element
            i += 1
        all_contacts.append(contact)

def Create_Record():
    contact = {}
    i = 0
    for header in each_header:
        contact[header] = input(f"Enter {header}: ")
        i += 1
    all_contacts.append(contact)
    return print(f"Added {contact} to database")

def Retrieve_Record():
    search_name = input("Enter a name to search for: ")
    result = next((x for x in all_contacts if x["name"] == search_name), print("Finished search. Results below."))
    if not result:
        print("No user found with that name")
    else:
        print(result)
    return 

def Update_Record():
    result = next((x for x in all_contacts if x[each_header[0]] == input("Enter a name to search for: ")))
    if result:
        print(result)
        update_attribute = input("Enter the attribute you'd like to update: ")
        new_value = input("Enter the new value: ")
        result[update_attribute] = new_value
    else:
        "doesnt exist"
    return

def Delete_Record():
    search_name = input("Enter a name to search for: ")
    result = next((x for x in all_contacts if x[each_header[0]] == search_name))
    if result:
        confirm = input(f"Are you sure you want to delete {result}?(y/n)")
        if confirm != "y":
            return
        else:
            all_contacts[:] = [y for y in all_contacts if y.get("name") != search_name]
    return

def Save_CSV():
    with open('contacts.csv', 'w') as file:
        file.write(headers)
        file.write("\n")
        for l in all_contacts:
            new_list = list(l.values()) 
            list_to_string = ' '.join(map(str, new_list))
            add_comma = list_to_string.replace(" ",",")
            file.write(add_comma)
            file.write("\n")
    file.close()
    return

def print_menu():      
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Show current database")
    print("2. Create new contact")
    print("3. Retrieve contact info by name")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Save CSV")
    print("q. Exit")
    print(67 * "-")
  
loop=True
while loop:
    print_menu()
    choice = input("Enter your choice [1-5]: ")
    if choice == str(1):     
        print(all_contacts)
    elif choice == str(2):
        Create_Record()
    elif choice == str(3):
        Retrieve_Record()
    elif choice == str(4):
        Update_Record()
    elif choice == str(5):
        Delete_Record()
    elif choice == str(6):
        Save_CSV()
    elif choice == "q":
        loop=False 
    else:
        print("Wrong option selection. Enter any key to try again..")