"""
Lab 23: Contact List
Manage a list of contacts with a CSV file and a CRUD REPL
"""
def load(path):
    """
    returns a list of dictionaries representating a contact list csv
    reads csv 
    """
    with open(path) as f:
        lines = f.read().split('\n')

    contacts = []
    header = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(header, row))
        contacts.append(contact)

    return header, contacts


def save(contacts, path, header):
    """
    writes contact list to a path.csv file
    """
    lines = [','.join(header)]
    for contact in contacts:
        row = ','.join(contact.values())
        lines.append(row)

    csv = '\n'.join(lines)

    with open(path, 'w') as f:
        f.write(csv)


def print_contact(contact):
    """
    pretty prints contact
    """
    if type(contact) is str:
        print(contact)
    else:
        for k, v in contact.items():
            print(f'{k}: {v}')


def print_all_contacts(contacts):
    """
    prints all contacts
    """
    for contact in contacts:
        print_contact(contact)
        print()


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
    adds contact to contacts list and returns contact
    :contact: dict
    """
    contacts.append(contact)
    return contact


def read(contacts, name):
    """
    returns contact from contacts list given a name
    """
    idx = find_contact(contacts, name)
    if idx > -1:
        return contacts[idx]
    else:
        return f'{name} not in contact list'


def update(contacts, name, updated_info):
    """
    updates existing contact given a name and dictionary of updated fields
    returns updated contact
    :name: str
    :updated_info: dict
    """
    idx = find_contact(contacts, name)
    if idx > -1:
        contacts[idx].update(updated_info)
        return contacts[idx]
    else:
        return f'{name} not in contact list'    


def delete(contacts, name):
    """
    removes contact from contacts list
    """
    idx = find_contact(contacts, name)
    if idx > -1:
        return contacts.pop(idx)
    else:
        return f'{name} not in contact list'


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
    header, contacts = load(path)
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
            save(contacts, path, header)
            break

        elif command.startswith('c'):
            contact = {}
            for key in header:
                value = input(f'{key}: ')
                contact[key] = value
            print('Creating contact...')
            create(contacts, contact)      

        elif command.startswith('r'):
            name = input('Name: ')
            print_contact(read(contacts, name))

        elif command.startswith('u'):
            contact = {}
            for key in header:
                value = input(f'{key}: ')
                contact[key] = value

            contact = {k:v for k,v in contact.items() if v}
            print('Creating contact...')
            print_contact(update(contacts, contact['name'], contact))

        elif command.startswith('d'):
            name = input('Name: ')
            print(f'Deleting {name}...')
            print_contact(delete(contacts, name))

        elif command.startswith('l'):
            print_all_contacts(contacts)

main()