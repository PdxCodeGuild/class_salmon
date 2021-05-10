with open('contacts.csv', 'r') as f:
    data_csv = f.read()
# data_csv = [line.split(',') for line in data_csv.split('\n')]
csv_lines = data_csv.split('\n')
data_csv = []
for line in csv_lines:
    data_csv.append(line.split(','))
# print(data_csv)

keys = data_csv[0]
data = []
# for i, row in list(enumerate(data_csv))[1::]:
#     line_dict = {}
#     for j, cell in enumerate(row):
#         line_dict[keys[j]] = cell
#     data.append(line_dict)

# for i, values in list(enumerate(data_csv))[1::]:
#     data.append(dict(zip(keys, values)))

# for i in range(1, len(data_csv)):
#     data.append(dict(zip(keys, data_csv[i])))
data = [dict(zip(keys, row)) for row in data_csv[1::]]
# print(data)


def create_contact(data, keys):
    new_contact = {}
    for key in keys:
        new_contact[key] = input(f"What is your new contact's {key}? ")
    # new_contact = {key: input(f"What is your new contact's {key}?") for key in keys}
    data.append(new_contact)

def read_contact(data, keys):
    key_returned_string = "\n" + "\n".join(keys) + "\n"
    key_input = input(f'What would you like to search by? Choose from{key_returned_string}: ')
    contact_input = input("What is your search term? ")
    # data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))
    # print(data_results)
    # for result in data_results:
    #     for key, value in result.items():
    #         print(f'{key}: {value}')
    #     print('')

    data_results = []
    for contact in data:
        if contact[key_input] == contact_input:
            data_results.append(contact)
    print(data_results)

    return data_results


def update_contact(data, keys):
    # key_returned_string = "\n" + "\n".join(keys) + "\n"
    # key_input = input(f'What would you like to search by? Choose from{key_returned_string}: ')
    # contact_input = input("What is your search term? ")
    # data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))
    # print(data_results)
    # for result in data_results:
    #     for key, value in result.items():
    #         print(f'{key}: {value}')
    #     print('')
    data_results = read_contact(data, keys)
    
    index_to_update = int(input(f'Which entry do you want to update? (1-{len(data_results)}) ')) - 1
    key_to_update = input(f'Which key do you want to update? {keys} ')
    value_to_update = input(f"What do you want to change {key_to_update} to? ")
    data_results[index_to_update][key_to_update] = value_to_update

def delete_contact(data, keys):
    # key_returned_string = "\n" + "\n".join(keys) + "\n"
    # key_input = input(f'What would you like to search by? Choose from{key_returned_string}: ')
    # contact_input = input("What is your search term? ")
    # data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))
    # print(data_results)
    # for result in data_results:
    #     for key, value in result.items():
    #         print(f'{key}: {value}')
    #     print('')
    data_results = read_contact(data, keys)
    index_to_delete = int(input(f'Which entry do you want to delete? (1-{len(data_results)}) ')) - 1
    data.remove(data_results[index_to_delete])

while True:
    user_input = input("(c)reate, (r)ead, (u)pdate, (d)elete, (q)uit? ")
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

data_csv_output = []
data_csv_output.append(list(data[0].keys()))
for contact in data:
    data_csv_output.append(list(contact.values()))
data_csv_output = [",".join(line) for line in data_csv_output]
data_csv_output = "\n".join(data_csv_output)
with open('contacts.csv', 'w') as f:
    f.write(data_csv_output)
