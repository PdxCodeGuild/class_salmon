with open('contacts.csv', 'r') as file:
    data_csv = file.read()
data_csv = [line.split(',') for line in data_csv.split('\n')]
keys = data_csv[0]
data = [dict(zip(keys, values)) for values in data_csv[1::]]
print(data)
def create_contact(data, keys):
    new_contact = {}
    for key in keys:
        new_contact[key] = input(f"What is your new contact's {key}? ")
    # new_contact = {key: input(f"What is your new contact's {key}? ") for key in keys}
    data.append(new_contact)
def read_contact(data, keys):
    key_string = "\n" + "\n".join(keys) + "\n"
    while True:
        key_input = input(f"What would you like to search by? Choose from{key_string}: ")
        if key_input.lower() in keys:
            continue
        else:
            print('invalid input')
    contact_input = input(f"What {key_input} do you want to search by? ")
print(read_contact(data,keys))