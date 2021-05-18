unit_converter = {
"in": 0.0254,
"ft": 0.3048, 
"yd": 0.9144,
"mi": 1609.34,
"m": 1,
"km": 1000,
}

# ask the user for distance
user_value = input("\nEnter a distance please: ")

# ask the user for the units
user_units = input("\nAnd they are which unit? (in, ft, yd, mi, m, km): ")

# ask the user for what unit to convert to
answer_units = input("\nAnd you would like the output in what unit? (in, ft, yd, mi, m, km): ")

# convert the response to a float
user_value = float(user_value)

# user input multiplied by the starting unit with values from the dictionary
user_total = user_value * unit_converter[user_units]

# take the number of meters in the user_unit and divide it by how many meters are in the answer_unit
answer = user_total / unit_converter[answer_units]

# print the answer
print(f"\n{user_value} {user_units} is {answer:.4f} {answer_units}.\n")