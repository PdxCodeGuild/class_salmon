"""
Lab 23: Contact List
Manage a list of contacts with a CSV file and a CRUD REPL
"""
def load(path):
    """
    returns a list of dictionaries representating a contact list csv
    reads csv 
    """
    contacts = []
    with open(path, 'r') as file:
        text = file.read()  # read all the text as one giant string
    lines = text.split('\n')  # split the text into multiple lines
    header = lines[0].split(',')  # the first line is the header
    for i in range(1, len(lines)):  # skip over the header, every line after represents a contact
        row = lines[i].split(',')  # attribute values of the contact
        contact = dict(zip(header, row)) # create a dictionary zipping together the header and row values
        contacts.append(contact)

    return contacts, header


def save(contacts, path, header):
    """
    writes contact list to a csv file
    """
    lines = [','.join(header)]
    for contact in contacts: # loop over contacts
        row = ','.join(contact.values()) # turn contact values into comma separated string
        lines.append(row)  # add row to lines

    csv = '\n'.join(lines) # turn lines list into string

    with open(path, 'w') as file:
        file.write(csv)


def print_contact(contact):
    """
    pretty prints contact
    """
    for key in contact:
        print(f'{key}: {contact[key]}', end='\n\n')


def find_contact(contacts, name):
    """
    returns contact index if name exists in contact list
    """
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            return i
    return -1


def create(contacts, contact):
    """
    adds contact to contacts list
    """
    contacts.append(contact)
    return contacts[-1]


def read(contacts, name):
    """
    returns contact from contacts list given a name
    """
    idx = find_contact(contacts, name)
    if idx > -1:
        return contacts[idx]


def update(contacts, name, updated_info):
    """
    updates existing contact given a name and dictionary of updated fields
    """
    idx = find_contact(contacts, name)
    if idx > -1:
        contacts[idx].update(updated_info)
        return contacts[idx]


def delete(contacts, name):
    """
    removes contact from contacts list
    """
    idx = find_contact(contacts, name)
    if idx > -1:
        return contacts.pop(idx)


def list_commands():
    print('(c)reate: create a contact')
    print('(r)ead: retrieve a contact')
    print('(u)pdate: update a contact')
    print('(d)elete: delete a contact')
    print('(l)ist: list all contacts')
    print('load: load contacts from csv')
    print('save: save contacts to csv')
    print('(h)elp/commands: display operation list')
    print('e(x)it: exit the program')    


def main():
    path = 'contact_list.csv'
    contacts, header = load(path)
    valid_inputs = ['h', 'help', 'commands', 
                    'c', 'create', 
                    'r', 'read', 
                    'u', 'update', 
                    'd', 'delete',
                    'l', 'list',
                    'load', 
                    'save',
                    'x', 'exit']

    while True:
        while True:
            command = input("What operation would you like to perform? ").strip().lower()
            if command in valid_inputs:
                break
            list_commands()

        if command in ['h', 'help', 'commands']:
            list_commands()

        elif command in ['x', 'exit']:
            break

        elif command.startswith('c') or command.startswith('u'):
            contact = {}
            for attribute_name in header:
                attribute_value = input(f"What is the contact's {attribute_name}? ")
                contact[attribute_name] = attribute_value

            if command.startswith('c'):
                create(contacts, contact)
            else:
                contact = {k:v for (k,v) in contact.items() if v}
                update(contacts, contact['name'], contact)

        elif command.startswith('r'):
            contact_name = input("What is the name of the contact you'd like to retrieve? ")
            contact = read(contacts, contact_name)
            if contact:
                print_contact(contact)
            else:
                print(f'{contact_name} not in contact list')

        elif command.startswith('d'):
            contact_name = input("What is the name of the contact you'd like to delete? ")
            delete(contacts, contact_name)

        elif command.startswith('l'):
            for contact in contacts:
                print_contact(contact)

        print()
    save(contacts, path, header)

main()