with open('c:\\Users\\Cj\\Documents\\PDX_CODE_GUILD_BOOT_CAMP\\class_salmon\\code\\Cj\\contacts.csv', 'r') as file:
    lines = file.read().split('\n')

def c_s_v(lines):
    C_S_V = []
    for line in lines:
        data = line.split(',')
        
        if len(data) == 3:
            name = data[0]
            favorite_fruit = data[1]
            favorite_color = data[2]

        value = {'name': name, 'favorite Fruit': favorite_fruit, 'favorite Color': favorite_color}
        C_S_V.append(value)    
    return C_S_V
contact_list = c_s_v(lines)

def write(contact_list):
    output = ''
    info = []
    for dictionary in contact_list:
        for k, v in dictionary.items():
            key = k
            val = v
            # info.append(k)
            info.append(v)
            output += v + ','
        output = output.strip(',')
        output += '\n'
    with open('c:\\Users\\Cj\\Documents\\PDX_CODE_GUILD_BOOT_CAMP\\class_salmon\\code\\Cj\\contacts.csv', 'w') as file:
        file.write(output)

def create():
    global contact_list
    name = input('Enter your name: ')
    favorite_fruit = input('Enter your favorite fruit: ').lower()
    favorite_color = input('Enter your favorite color: ').lower()
    val = {'name': name, 'favorite fruit': favorite_fruit, 'favorite color': favorite_color}
    contact_list.append(val)
    return contact_list

def retrieve(name):
    global contact_list
    for i in contact_list:
        if name == i['name']:
            output = i
            return output
    return "None."

def update(name):
    global contact_list
    for dict in contact_list:
        if name == dict['name']:
            contact_list.remove(dict)
            rename = input('Enter name update: ')
            new_fruit = input('Update favorite fruit: ')
            new_color = input('Update favorite color: ')
            vals = {'name': rename, 'favotire fruit': new_fruit, 'favorite color': new_color}
            contact_list.append(vals)
            return 'Contact information updated!'
    else:
        print('Error! Contact not found!')
        return 
def delete():
    global contact_list
    name = input('Enter name of contact to delete: ')
    for dict in contact_list:
        if name == dict['name']:
            contact_list.remove(dict)
            return "Contact information deleted!"
    else:
        print('Error! Contact not found!')
        return 


user_error = "Error! Please make a valid entry: "


main_menu = """
Welcome to the contact list registry.
Please make a selection:
1. Create record
2. Retrieve contact information
3. Update contact information
4. Delete contact information
5. Quit
Enter: """

return_menu = """
1. Return to main menu
2. Quit
Enter: """

search_again = """
1. Search for another contact
2. Return to main menu
3. Quit
Enter: """

update_contact_menu = """
1. Update information
2. Search for another contact
3. Return to main menu
4. Quit
Enter: """
trigger = 1

while True:              ################ Menu Naigation system
    if trigger == 0:
        trigger =1
        main_menu = main_menu.replace('Contact added to list! ', "Enter: ")
    menu_select = input(f'{main_menu}')
    if menu_select.isnumeric():
        menu_select = int(menu_select)  
    else:
        main_menu = main_menu.replace("Enter: ", user_error)
        continue
    if menu_select < 1 or menu_select > 5:
        main_menu = main_menu.replace("Enter: ", user_error)
        continue       
    if menu_select == 1:
        create()
        main_menu = main_menu.replace("Enter: ", 'Contact added to list! ')
        trigger = 0
    elif menu_select == 2:
        flag = True
        while flag is True:
            UI = input('Enter name of contact: ')
            x = retrieve(UI)
            print()
            output = f'The information found on that contact was: {x}'
            print(output)
            while x == 'None.':
                    menu_select = input(search_again)
                    if menu_select.isnumeric():
                        menu_select = int(menu_select)
                    else:
                        search_again = search_again.replace("Enter: ", user_error)
                        print(output)
                        continue
                    if menu_select > 3 or menu_select < 1:
                        print(output)
                        search_again = search_again.replace("Enter: ", user_error)
                        continue
                    elif menu_select == 1:
                        search_again = search_again.replace(user_error, "Enter: ")
                        UI = input('Enter name of contact: ')
                        x = retrieve(UI)
                        print()
                        output = f'The information found on that contact was: {x}'
                        print(output)
                    elif menu_select == 2:
                        flag = False
                        x = 1
                        continue
                    elif menu_select == 3:
                        write(contact_list)
                        exit()
            while True:
                if x == 1:
                    break
                menu_select = input(update_contact_menu)
                if menu_select.isnumeric():
                    menu_select = int(menu_select)  
                else:
                    update_contact_menu = update_contact_menu.replace("Enter: ", user_error)
                    continue
                if menu_select < 1 or menu_select > 4:
                    update_contact_menu = update_contact_menu.replace("Enter: ", user_error)
                    continue
                elif menu_select == 1:
                    output = update(UI)
                    print(output)
                    flag = False
                    break
                elif menu_select == 2:
                    break
                elif menu_select == 3:
                    flag = False
                    break
                elif menu_select == 4:
                    exit()
    elif menu_select == 3:
        UI = input('Enter name of contact: ')
        output = update(UI)
        print(output)
        while True:
            menu_select = input(return_menu)
            if menu_select.isnumeric():
                menu_select = int(menu_select)  
            else:
                return_menu = return_menu.replace("Enter: ", user_error)
                continue
            if menu_select < 1 or menu_select > 2:
                return_menu = return_menu.replace("Enter: ", user_error)
                continue
            elif menu_select == 1:
                break
            elif menu_select == 2:
                write(contact_list)
                exit()
    elif menu_select == 4:
        output = delete()
        print(output)
        while True:
            menu_select = input(return_menu)
            if menu_select.isnumeric():
                menu_select = int(menu_select)  
            else:
                return_menu = return_menu.replace("Enter: ", user_error)
                continue
            if menu_select < 1 or menu_select > 2:
                return_menu = return_menu.replace("Enter: ", user_error)
                continue
            elif menu_select == 1:
                break
            elif menu_select == 2:
                write(contact_list)
                exit()
    elif menu_select == 5:
        write(contact_list)
        exit()
        