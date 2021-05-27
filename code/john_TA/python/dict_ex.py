# with open('contacts.csv', 'r') as filename:
#     lines = filename.read().split('\n')
#     print(lines)

lines = [
    'name,favorite animal,favorite color', 
    'Sarah,dog,blue', 
    'Taylor,giraffe,green', 
    'Taylor,giraffe,green', 
    'Kyle,monkey,red']

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
list_of_dictionaries = []
headers = lines[0].split(',')
# print(headers)
for x in range(1, len(lines)):
    person = lines[x].split(',')
    # print(person)
    dict_person = dict(zip(headers, person))
    list_of_dictionaries.append(dict_person)

# print(list_of_dictionaries)

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# for x in range(len(lines)):
#     if x == 0:
#         headers = lines[0].split(',')
#         # print(headers)
#     else:
#         temp_dict = {}
#         temp_contact = lines[x].split(',')
#         # print(temp_contact)
#         temp_dict[headers[0]] = temp_contact[0]  # iterate over the whole contact
#         print(temp_dict)
#         list_of_dictionaries.append(temp_dict)

# print(list_of_dictionaries)
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

list_of_dictionaries = [{'name': 'Sarah', 'favorite animal': 'dog', 'favorite color': 'blue'}, {'name': 'Taylor', 'favorite animal': 'giraffe', 'favorite color': 'green'}, {'name': 'Taylor', 'favorite animal': 'giraffe', 'favorite color': 'green'}, {'name': 'Kyle', 'favorite animal': 'monkey', 'favorite color': 'red'}]
string_to_output = ''
for x in range(1,len(list_of_dictionaries)):
    list_new = list(list_of_dictionaries[x].values())
    # print(list_new)
    string_new = ','.join(list_new) 
    # print(string_new)
    string_to_output += string_new + '\n'

print(string_to_output)

# final_string = ''
# for dict_entry in list_of_dictionaries:
#     for a in dict_entry:
#         print(a)
#         final_string += a
#         print(final_string)





# final_string = ''
# with open('contacts_output.csv', 'w') as filename:
#     filename.write(final_string)