with open("C:\\Users\\CJ\\Documents\\pdx_code_guild\\class_salmon\\code\\brea\\contact_list.csv", "r") as f:
    rows = f.read().split('\n')
    

def list_population(parameter):

    contact_list = []  
    for row in parameter:
        info = row.split(",")    
        if len(info) == 3:    
            name = info[0]
            color = info[1]
            candy = info[2]
        data = {'name': name, 'favorite color': color, 'favorite candy': candy}
        contact_list.append(data)
    return(contact_list)

contacts = list_population(rows)

def create_record():
    global contacts
    name = input('What\'s your name? ').lower()
    favorite_color = input('What\'s your favorite color? ').lower()
    favorite_candy = input('What\'s your favorite candy? ').lower()
    new_dict = {'name': name, 'favorite color': favorite_color, 'favorite candy': favorite_candy}
    return contacts.append(new_dict)

def retrieve_record():
    global contacts
    name = input('Enter contact name: ').lower()
    for i in contacts:
        if name == i['name']:
            output = f'information found for {name} was {i}:'
            return output
    return 'name not found'        

def update_record():
    global contacts
    name = input('Enter the name of the contact you\'d like to update: ')
    for i in contacts:
        if name == i['name']:
            contacts.remove(i)
            name = input('Enter name update: ')
            favorite_color = input('Enter favorite color update: ')
            favorite_candy = input('Enter favorite candy update: ')
            new_dict = {'name': name, 'favorite color': favorite_color, 'favorite candy': favorite_candy}
            contacts.append(new_dict)
            return contacts
    else:
        return

def delete_record():
    global contacts
    name = input('Enter the name of the contact you\'d like to delete: ')
    for i in contacts:
        if name == i['name']:
            contacts.remove(i)
            return contacts
    else:
        return

