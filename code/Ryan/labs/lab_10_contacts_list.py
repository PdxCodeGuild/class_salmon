

filename = "contacts_list_working.csv"
open_file = open(filename)

with open(filename) as file_obj:
    print(type(file_obj))
    lines = file_obj.read().split("\n")
    print(type(lines))
    # Remove the headers
    headers = lines.pop(0).split(",")
    print(f"Headers: {headers}")
    #print(lines.split(","))

    
    print(lines[0].split(",", 1))


    # For each remaining line. Create a dict and append to list
    contact_list = [{key: value.split(",", 1).replace(value,"")} for key in headers for value in lines]
    print(contact_list)

# for line in open_file:
#     #print(range(len(line)))
#     line_index = line.split(',')
#     list(line_index)
#     print(type(line))
#     print(line_index)
#     contacts_list = dict.fromkeys(line_index)
#     break
#     for i in range(len(line_index)):
#         print(i, line_index[i])
#         contacts_list = dict.fromkeys(i)


#         contacts_list.insert({i}, {line_index[i]})

# print(contacts_list)

# output
# <class 'str'>
# ['name', 'favorite food', 'favorite color\n']
# {'name': None, 'favorite food': None, 'favorite color\n': None}



