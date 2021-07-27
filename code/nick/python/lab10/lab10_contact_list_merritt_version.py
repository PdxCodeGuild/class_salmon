with open('some.csv', 'r') as f:#you dont have to specify reading in the open method
    data_csv = f.read()
data_csv = [line.split(',') for line in data_csv.split('\n')]#does the same thing as below
# csv_lines = data_csv.split('\n')
# data_csv = []
# for line in csv_lines:
#     data_csv.append(line.split(","))
keys = data_csv[0]
data = []
#recipe 1
# for i, row in list(enumerate(data_csv))[1::]:#i is the row, converting this to list allows the header row to be skipped
#     row_dict = {}
#     for j, cell in enumerate(row):#j is the value in the cell
#         row_dict[keys[j]] = cell 
#     data.append(row_dict)

# for i, values in list(enumerate(data_csv))[1::]:#recipe 2
    # print(keys)
    # print(values)
    # print(list(zip(keys, values)))
    # print(dict(zip(keys, values)))
    # data.append(dict(zip(keys, values)))

# for i in range(1, len(data_csv)):#recipe 3
#     data.append(dict(zip(keys, data_csv[i])))

data = [dict(zip(keys, values)) for values in data_csv[1::1]]#recipe 4

#CRUD - REPL loop Read Evaluate Print Loop
#what we are doing with the REPL is CRUD loop
def create_contact(data, keys):
    new_contact = []
    for key in keys:
        new_contact[key] = input(f"what is your new contact's {key}?")
    # new_contact = {key: input(f"what is your new contact's {key}?") for key in keys}#dictionary comprehension
    data.append(new_contact)
    # print(new_contact)
def read_contact(data, keys):
    key_string ="\n" + "\n".join(keys) +"\n"
    key_input = input(f"what would you like to search by? Choose from {key_string}: ")#asks the user for their catalog key input
    contact_input = input('what is your search term? ')
    #filter function below looking for a test function and the thing it will loop through
    # data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))#lambda is a shorter way to put in a function

    data_results = []#will return a list of the contacts that match
    for contact in data:
        if contact[key_input] == contact_input:
            data_results.append(contact)
    print(data_results)

    return data_results

    # name = input('name?')
    # for contact in data:
    #     if contact['name'] == name:
    #         print(contact)
    #         return contact
def update_contact(data, keys):
    data_results = read_contact()
    index_to_update = int(input(f'which contact do you want to edit? (1-{len(data_results)}'))-1#subtracting makes the input suitable for python index system
    key_to_update = input(f'which key would you like to update? {keys} ')
    value_to_update = input(f'what do you want to change {key_to_update} to? ')
    data_results[index_to_update][key_to_update] = value_to_update
def delete_contact(data, keys):
    data_results = read_contact()
    index_to_delete = int(input(f'which contact do you want to delete? (1-{len(data_results)}'))-1
    data.remove(data_results[index_to_delete])#returns one of the dictionaries then removes it from data file


while True:
    user_input = input("(c)reate, (r)ead, (u)pdate, (d)elete, (q)uit?")
    if user_input == 'q':
        break
    elif user_input == 'c':
        create_contact(data, keys)
    elif user_input == 'r':
        read_contact(data, keys)
    elif user_input == 'u':
        update_contact(data, keys)
    elif user_input == 'd':
        delete_contact(data, keys)
# print(data)
#putting this into CSV
data_csv_output = []
data_csv_output.append(keys)
for contact in data:
    data_csv_output.append(list(contact.values()))
data_csv_output = [','.join(line) for line in data_csv_output]
data_csv_output = '\n'.join(data_csv_output)

with open('some.csv', 'w') as f:
    f.write(data_csv_output)

print(data_csv_output)