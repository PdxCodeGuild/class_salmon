def average(list_of_nums):
    #craete variable to store the sum
    num_sum = 0
    #loop though numbers in list
    for num in list_of_nums:
        #add numbers to sum
        num_sum += num
    # make sure list isn't empty
    if len(list_of_nums) == 0:
        return 'Error: empty list!'
    else:
        #divide sum by length of list and return the average
        average = num_sum / len(list_of_nums)
        return round(average,4)
def create_num_list():
    #empty list to store values
    user_list = []
    #emty variable for current input
    current_input = ''
    #create while loop so it wil keep aking user for input unit they type 'done'
    while current_input != 'done':
        #get input
        current_input = (input("enter a number, or 'done':  "))
        #check to see if in put is a number
        if is_number(current_input) == True:
            user_list.append(float(current_input))
        #check if input is 'done' and end loop if it is
        elif current_input.lower() == 'done':
            break
        #if not number or done let the user know the input is bad and keep it out of the list
        else:
            print(f'{current_input} is not valid input!')
    #return the average of user created list by using it as the param for average function
    return average(user_list)
def is_number(string):
    #checks if string is number by trying to covert string into float will return truf if number can be coverted into a float
    try:
        float(string)
        return True
    #if it can not be converted into a float will give ValueError which will return False
    except ValueError:
        return False
print (create_num_list())