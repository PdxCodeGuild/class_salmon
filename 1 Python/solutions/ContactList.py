"""
ContactList.py

Class implementation of contact list
"""
class ContactList:
    def __init__(self, csv=None):
        """
        :csv: str filepath of csv to load contacts from
        """
        self.contacts = []
        self.header = ['name', 'age', 'job', 'phone', 'email', 'shoesize']
        if csv:
            self.load(csv)


    def load(self, path):
        """
        update self.contacts with parsed csv contacts
        """
        if path.endswith('.csv'):
            with open(path) as f:
                lines = f.read().split('\n')

            contacts = []
            header = lines[0].split(',')
            if header != self.header:
                if len(self.contacts) > 0:
                    return 'CSV not compatible'

            for i in range(1, len(lines)):
                row = lines[i].split(',')
                contact = dict(zip(header, row))
                contacts.append(contact)

            self.contacts += contacts
            self.header = header


    def save(self, path):
        """
        writes contact list to a path.csv file
        """
        lines = [','.join(self.header)]
        for contact in self.contacts:
            row = ','.join(contact.values())
            lines.append(row)

        csv = '\n'.join(lines)

        with open(path, 'w') as f:
            f.write(csv)


    def __find_contact(self, name):
        """
        returns contact index if name exists in contact list
        """
        for i, contact in enumerate(self.contacts):
            if contact['name'] == name:
                return i
        return -1


    def create(self, contact):
        """
        adds contact to contacts list and returns contact
        :contact: dict
        """
        self.contacts.append(contact)
        return contact


    def read(self, name):
        """
        returns contact from contacts list given a name
        """
        idx = self.__find_contact(name)
        if idx > -1:
            return self.contacts[idx]
        else:
            return f'{name} not in contact list'


    def update(self, name, updated_info):
        """
        updates existing contact given a name and dictionary of updated fields
        returns updated contact
        :name: str
        :updated_info: dict
        """
        idx = self.__find_contact(name)
        if idx > -1:
            self.contacts[idx].update(updated_info)
            return self.contacts[idx]
        else:
            return f'{name} not in contact list'    


    def delete(self, name):
        """
        removes contact from contacts list
        """
        idx = self.__find_contact(name)
        if idx > -1:
            return self.contacts.pop(idx)
        else:
            return f'{name} not in contact list'


    def print(self, contact):
        if type(contact) is str:
            print(contact)
        else:
            for field in contact:
                print(f'{field}: {contact[field]}')
            print()        


    def list(self):
        """
        prints all contacts
        """
        for contact in self.contacts:
            self.print(contact)


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


if __name__ == '__main__':
    path = 'contact_list.csv'
    contacts = ContactList(path)
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

        elif command == 'load':
            path = input('Enter filename to import: ')
            contacts.load(path)

        elif command == 'save':
            contacts.save(path)

        elif command.startswith('c'):
            contact = {}
            for key in contacts.header:
                value = input(f'{key}: ')
                contact[key] = value
            print('Creating contact...')
            contacts.create(contact)      

        elif command.startswith('r'):
            name = input('Name: ')
            contacts.print(contacts.read(name))

        elif command.startswith('u'):
            contact = {}
            for key in contacts.header:
                value = input(f'{key}: ')
                contact[key] = value

            contact = {k:v for k,v in contact.items() if v}
            print('Creating contact...')
            contacts.print(contacts.update(contact['name'], contact))

        elif command.startswith('d'):
            name = input('Name: ')
            print(f'Deleting {name}...')
            contacts.print(contacts.delete(name))

        elif command.startswith('l'):
            contacts.list()