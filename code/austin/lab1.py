#create function
def convert_distance():
    #conversion table
    to_meters = {'feet': 0.3048, 'miles': 1609.34, 'meters': 1, 'kilometers': 1000, 'yards': 0.9144, 'inches':0.0254}
    #user input for distance
    distance = input('What is the distance?  ')
    #while loop that calls is_number function to see if input is a number and keeps looping until user puts in valid number
    good_input=False
    while is_number(distance) == False:
        distance = input('Error, please enter valid number for distance: \nWhat is the distance?    ')
    #show user choices for units
    for choice in to_meters:
        print(choice)
    #user inputs units of measurement to be converted
    unit = input('What are the units you want to covert?  ')
    #while loop calls valid choice function to make sure users input is in list and keeps looping to user inputs a choice that is in the list
    while valid_choice(to_meters,unit) == False:
        unit = input('Error, please enter valid unit from list above:\nWhat are the units you want to convert?  ')
    #covert distance to a float and multiple by value found at key in to_meters
    meters = float(distance) * to_meters[unit]
    #show user choices for units
    for choice in to_meters:
        print(choice)
    #user inputs units of measurement to be converted to
    convert_to_unit = input('What unit do you want to covert to?  ')
    #while loop calls valid choice function to make sure users input is in list and keeps looping to user inputs a choice that is in the list
    while valid_choice(to_meters,convert_to_unit) == False:
        convert_to_unit = input('Error, please enter valid unit from list above:\nWhat are the units you want to convert to?  ')
    #divides original distance in meters by the value at the key to get new distance and rounds to the 4th decimal place
    new_distance = round(meters / to_meters[convert_to_unit],4)
    #f string with old measurement and new measurement
    return f'\n{distance} {unit} = {new_distance} {convert_to_unit}.'

def is_number(string):
    #checks if string is number by trying to covert string into float will return truf if number can be coverted into a float
    try:
        float(string)
        return True
    #if it can not be converted into a float will give ValueError which will return False
    except ValueError:
        return False
#checks if user input is one of the options from dictionary or list
def valid_choice(options,user_input):
    if user_input in options:
        return True
    else:
        return False
print(convert_distance())