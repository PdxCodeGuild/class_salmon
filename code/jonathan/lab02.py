def ave(number_list):
    '''Finds the average value of a user-inputted list of floats'''
    return sum(number_list) / len(number_list)

# to give a value for my while loop
max_list_length = 9999 

# blank starting list
number_list = []

# see line 5
while len(number_list) < max_list_length: 
    
    try:
        # user is asked for a number to begin the list
        user_numbers = input("Enter a number or 'done' to quit: ")

        # typecast the string into an integer
        user_numbers = float(user_numbers)

        # adding the user given integers to the list
        number_list.append(user_numbers)

    except ValueError: # for when the user enters a non integer value 
            # when user enters done or anything not a number
            break

# average of the list the user inputted 
ave_total = ave(number_list)

# print the list of numbers given
print(f"\nYou entered {number_list}")

# prints the average of said numbers
print(f"\nThe average of the numbers is {ave_total}.\n") 