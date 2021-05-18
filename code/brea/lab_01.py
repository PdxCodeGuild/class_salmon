conversions = { 
'ft': 0.3048,
'mi': 1609.34,
'm': 1,
'km': 1000,
'yards': 0.9144,
'inches': 0.0254,
}                              # dictionary with key value pairs 

user_input = input('Enter a number to represent a distance: ') # saving user input as a variable
key = input('Enter the type of unit: ') # saving user input as another variable
while key not in conversions: # conditions established for while loop
    key = input('Error! Enter a valid unit type! ') # allows you to redefine variable used to established condition of loop from within loop

user_output = input('What would you like to convert the unit to? ') # defining a variable, asking user what type of unit they want to output
user_input = float(user_input) # converting user input into a float
output = user_input * conversions[key] / conversions[user_output] # multiplies user input by value at key
print(f'{user_input} {key} in {user_output} is {output} {user_output}.')  # an f string printing your result  