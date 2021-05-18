numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
conversion_table = {
     'mm': .001,
     'cm': .01,
     'm': 1,
     'km': 1000,
     'in': 0.0254 , 
     'inch': 0.0254, 
     'inches': 0.0254, 
     'ft': 0.3048, 
     'feet': 0.3048,
     'miles': 1609.34,
     'mi':  1609.34,
     }

UI = input('Enter number of units: ')
UI1 = UI.isnumeric()
while UI1 is False:
    UI = input('Error: Please input a number: ')
    UI1 = UI.isnumeric()
UI = float(UI)
UI2 = input('What are the input units?: ').lower()
while UI2 not in conversion_table:
    UI2 = input('Error! Please enter a valid unit type: ')
UI3 = input('What is the output units?: ')
while UI3 == UI2:
    UI3 = input('Please enter a different valid unit type than the one previously entered: ')
while UI3 not in conversion_table:
    UI3 = input('Please enter a valid unit type: ')
output = UI * conversion_table[UI2] / conversion_table[UI3]
print(f'{UI} {UI2} converted to {UI3} is {output} {UI3}! ')
