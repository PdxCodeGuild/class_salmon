with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
#print('lines: ', lines)


lines2 = []
for i in lines:
    lines2.append(i.split(','))

#print('Lines2 :  ', lines2)
titles = lines2.pop(0)


contacts = []
for i in lines2:
    tempo_dict = dict(zip(titles, i))
    contacts.append(tempo_dict)


def create(contacts):
    done = ''
    while done != 'n':
        temp_dict = {}
        contact_input = input('Please enter the contact name: ')
        temp_dict.update({'name': contact_input})
        fruit_input = input('Please enter the contact\'s favorite fruit: ')
        temp_dict.update({'favorite fruit': fruit_input})
        color_input = input('Please enter the contact\'s favorite color: ')
        temp_dict.update({'favorite color': color_input})
        done = input(
            'Would you like to enter another contact? \nPlease enter y or n:  ')
        contacts.append(temp_dict)


def retrieve(contacts):
    which = input(
        'Which contact would you like to retrieve? \nEnter name or "options" to see contact names: ')
    while which == 'options':
        for dict in contacts:
            print(dict.get('name'))
        which = input('Which contact would you like to retrieve?  ')
    for dict in contacts:
        if which in dict.values():
            print(f'{which}\'s favorite fruit is {dict.get("favorite fruit")} and their favorite color is {dict.get("favorite color")}.')


def update(contacts):
    while True:
        which_user = input(
            'Which contact would you like to update? Enter contact name or "options" to see contact names:  ')
        if which_user == 'options':
            for dict in contacts:
                print(dict.get('name'))
            which_user = input('Which contact would you like to update?  ')
        choose_cat = input(
            'What attribute would you like to update? \nPlease enter "name", "favorite fruit", or "favorite color":  ')
        updated_info = input(f'Please enter the new {choose_cat}:  ')
        for dict in contacts:
            if which_user in dict.values():
                dict.update({choose_cat: updated_info})

        breaker = input(
            'Would you like to update another contact? \nEnter "y" or "n" ')
        if breaker == 'options':
            for dict in contacts:
                print(dict.get('name'))
        if breaker == 'n':
            break


def delete(contacts):
    user_2_delete = input(
        'Which contact would you like to delete? \nEnter name or enter "options" to see contact names:  ')
    while user_2_delete == 'options':
        for dict in contacts:
            print(dict.get('name'))
        user_2_delete = input(
            'Which contact would you like to delete?  ')

    if user_2_delete != 'options':
        for dict in contacts:
            if user_2_delete in dict.values():
                contacts = contacts.remove(dict)


while True:
    crud = input('What would you like to do? \n Please select one of the following: \n"c" for Create a new contact \n"r" for retrieve a contact\'s information  \n"u" for update a contact\'s information \n"d" for delete a contact \n"done" to exit \n')
    if crud == 'c':
        create(contacts)
    elif crud == 'r':
        retrieve(contacts)
    elif crud == 'u':
        update(contacts)
    elif crud == 'd':
        delete(contacts)
    elif crud == 'done':
        break

# print(contacts)


newlines = ''
newlines += (','.join(titles))


for x in range(len(contacts)):
    list_new = list(contacts[x].values())
    string_new = ','.join(list_new)
    newlines += '\n' + string_new

with open('contacts.csv', 'w') as f:
    f.write(newlines)
